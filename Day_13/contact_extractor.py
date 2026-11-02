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
        instructions="Extract name, email, and company. Use null if missing. Never invent information.",
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


def main():

    print("=== AI Contact Extractor ===")

    text = input("\nPaste your text here:\n")

    try:
        result = extract_contact(text)

        print("\nExtracted Contact:")
        print(json.dumps(result, indent=4))

    except Exception as error:
        print("Something went wrong:", error)


if __name__ == "__main__":
    main()