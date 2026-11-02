from openai import OpenAI
from dotenv import load_dotenv
import os
import json

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

contact_schema = {
    "type": "object",
    "properties": {
        "name": {"type": ["string", "null"]},
        "email": {"type": ["string", "null"]},
        "company": {"type": ["string", "null"]}
    },
    "required": ["name", "email", "company"],
    "additionalProperties": False
}

def extract_contact(text):

    response = client.responses.create(
        model="gpt-4.1-mini",
        instructions="""
        Extract the name, email, and company.
        If information is missing, return null.
        Never invent information.
        """,
        input=text,
        text={
            "format": {
                "type": "json_schema",
                "name": "contact_extraction",
                "strict": True,
                "schema": contact_schema
            }
        }
    )

    return json.loads(response.output_text)

def count_words(text):
    return len(text.split())

tools = [
    {
        "type": "function",
        "name": "count_words",
        "description": "Count the words in the provided text.",
        "parameters": {
            "type": "object",
            "properties": {
                "text": {
                    "type": "string"
                }
            },
            "required": ["text"],
            "additionalProperties": False
        },
        "strict": True
    }
]

def get_word_count(text):

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=f"Use the count_words tool to count the words in this text:\n{text}",
        tools=tools,
        tool_choice="required"
    )

    for item in response.output:

        if item.type == "function_call":

            if item.name != "count_words":
                raise ValueError("Unexpected tool requested")

            arguments = json.loads(item.arguments)

            result = count_words(**arguments)

            tool_response = client.responses.create(
                model="gpt-4.1-mini",
                previous_response_id=response.id,
                input=[
                    {
                        "type": "function_call_output",
                        "call_id": item.call_id,
                        "output": str(result)
                    }
                ]
            )

            return result

    raise RuntimeError("The model did not request the expected tool.")
def process_text(text):

    # Extract contact details
    contact = extract_contact(text)

    # Count words using our Python tool
    word_count = get_word_count(text)

    # Combine both results
    result = {
        "contact": contact,
        "word_count": word_count
    }

    return result

def main():

    print("=== Week 2 AI Contact Extractor ===")
    print("Paste your text below.")
    print("Type END on a new line when finished.\n")

    lines = []

    while True:

        line = input()

        if line.strip().upper() == "END":
            break

        lines.append(line)

    text = "\n".join(lines)

    if not text.strip():
        print("No text was provided.")
        return

    try:

        result = process_text(text)

        print("\n=== Extracted Information ===")
        print(json.dumps(result, indent=4))

    except Exception as error:

        print("\nThe application encountered an error.")
        print(error)


if __name__ == "__main__":
    main()