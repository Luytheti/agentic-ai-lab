import os
from datetime import datetime
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY") # for accessing the LLM
client = Groq(api_key=GROQ_API_KEY)

def get_user_input():
    return input("User > ").strip().lower()

def identify_intent(user_input):

    if "hello" in user_input or "hi" in user_input:
        return "greeting"

    elif "date" in user_input:
        return "date"

    elif "calculate" in user_input:
        return "calculation"

    elif any(op in user_input for op in ["+", "-", "*", "/"]):
        return "calculation"

    else:
        return "llm_fallback"

def greet():
    return "Hello! I am your AI Agent."

def get_date():
    return str(datetime.now().date())

def calculate(expression):

    try:
        result = eval(expression)
        return f"Result: {result}"
    except:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "user", "content": expression}
            ]
        )

        return response.choices[0].message.content

def ask_llm(query):

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": query}
        ]
    )

    return response.choices[0].message.content

def agent(user_input):

    intent = identify_intent(user_input)

    if intent == "greeting":
        return greet()

    elif intent == "date":
        return get_date()

    elif intent == "calculation":

        expression = user_input.replace("calculate", "").strip()
        return calculate(expression)

    else:
        return ask_llm(user_input)

def main():

    print("AI Rule-Based Agent Started")
    print("Type 'exit' to quit\n")

    while True:

        user_input = get_user_input()

        if user_input == "exit":
            break

        response = agent(user_input)

        print("Agent >", response)


if __name__ == "__main__":
    main()