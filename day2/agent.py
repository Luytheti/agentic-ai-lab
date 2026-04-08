import re
from tools import calculator, weather, summarize_text
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


class ToolAgent:

    # Which tool to use 
    def identify_intent(self, user_input):
        user_input = user_input.lower()

        if re.search(r"\d+\s*[\+\-\*/]\s*\d+", user_input): #\d digit \s white space 
            return "calculator"
        elif "weather" in user_input:
            return "weather"
        elif "summarize" in user_input or "summary" in user_input:
            return "summarize"
        else:
            return "llm"


    # helpers 
    def extract_city(self, user_input):
        match = re.search(r"weather in ([a-zA-Z\s]+)", user_input.lower())
        if match:
            return match.group(1).strip()
        return "nagpur"  # default


    # query handlers
    def handle_query(self, user_input):
        intent = self.identify_intent(user_input)

        try:
            if intent == "calculator":
                expression = re.sub(r"calculate", "", user_input.lower()).strip()
                return calculator(expression)

            elif intent == "weather":
                city = self.extract_city(user_input)
                return weather(city)

            elif intent == "summarize":
                text = re.sub(r"summarize|summary", "", user_input, flags=re.IGNORECASE).strip()
                return summarize_text(text)

            else:
                return self.ask_llm(user_input)

        except Exception as e:
            return f"Error: {str(e)}"


    # LLM Fallback 
    def ask_llm(self, query):
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": query}]
        )
        return response.choices[0].message.content