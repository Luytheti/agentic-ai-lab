import os
from dotenv import load_dotenv
from groq import Groq
from tools import calculator, weather, summarize_text
from logger import log_interaction

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

class LLMAgent:
    def select_tool(self, query):
        prompt = f"""
        You are an AI decision system.

        Available tools:

        1. calculator -> for math calculations
        2. weather -> for weather queries
        3. summarize -> for summarizing text
        4. none -> if no tool is needed

        Respond ONLY with one word:
        calculator
        weather
        summarize
        none

        Query:
        {query}
        """
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}]
        )
        tool = response.choices[0].message.content.strip().lower()
        return tool

    def run(self, query):
        tool = self.select_tool(query)
        if tool == "calculator":
            expression = query.replace("calculate", "").strip()
            output = calculator(expression)
        elif tool == "weather":
            city = query.split()[-1]
            output = weather(city)
        elif tool == "summarize":
            text = query.replace("summarize", "").strip()
            output = summarize_text(text)
        else:
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": query}]
            )
            output = response.choices[0].message.content
        log_interaction(query, tool, output)
        return output