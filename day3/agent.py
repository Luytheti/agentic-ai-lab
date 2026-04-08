import os
import re
from dotenv import load_dotenv
from groq import Groq
from tools import calculator, weather, summarize_text
from logger import log_interaction

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


class LLMAgent:

    # -------- LLM TOOL SELECTION --------
    def select_tool(self, query):
        prompt = f"""
        You are an AI tool selector.

        Tools:
        - calculator → math expressions
        - weather → weather queries
        - summarize → summarize text
        - none → general queries

        Respond with ONLY ONE word:
        calculator / weather / summarize / none

        Query: {query}
        """

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}]
        )

        return response.choices[0].message.content.strip().lower()


    # -------- HELPERS --------
    def extract_city(self, query):
        match = re.search(r"weather in ([a-zA-Z\s]+)", query.lower())
        return match.group(1).strip() if match else "mumbai"


    def extract_expression(self, query):
        return re.sub(r"calculate", "", query.lower()).strip()


    def extract_text(self, query):
        return re.sub(r"summarize|summary", "", query, flags=re.IGNORECASE).strip()


    # -------- MAIN EXECUTION --------
    def run(self, query):
        tool = self.select_tool(query)

        try:
            if tool == "calculator":
                output = calculator(self.extract_expression(query))

            elif tool == "weather":
                output = weather(self.extract_city(query))

            elif tool == "summarize":
                output = summarize_text(self.extract_text(query))

            else:
                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[{"role": "user", "content": query}]
                )
                output = response.choices[0].message.content

        except Exception as e:
            output = f"Error: {str(e)}"

        log_interaction(query, tool, output)
        return output