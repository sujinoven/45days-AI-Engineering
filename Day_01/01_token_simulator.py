import random

predictions ={
    "Paris":0.80,
    "London":0.10,
    "Berlin":0.07,
    "Rome":0.03
}

prompt="The capital of France is "

def predict_next_token(temperature=1.0):
    if temperature <= 0:
        return max(predictions,key=predictions.get)

    tokens=list(predictions.keys())

    weights=[
        probability ** (1/temperature)
        for probability in predictions.values()
        
    ]

    return random.choices(tokens,weights=weights,k=1)[0]

print("Prompt:",prompt)

for temperature in [0,0.5,1.0,2.0]:
    print(f"Temperature: {temperature}")

    for _ in range(5):
        print("->",predict_next_token(temperature))


#Additional Experiment

from collections import Counter

for temperature in [0, 0.5, 1.0, 2.0]:
    results = [
        predict_next_token(temperature)
        for _ in range(1000)
    ]

    counts = Counter(results)

    print(f"\nTemperature: {temperature}")

    for token, count in counts.items():
        print(f"{token}: {count / 10:.1f}%")