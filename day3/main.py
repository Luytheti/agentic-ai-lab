from agent import LLMAgent

def main():
    agent = LLMAgent()
    print("LLM-Based AI Agent Started")
    print("Type 'exit' to quit\n")
    while True:
        user_input = input("User > ").strip().lower()
        if user_input == "exit":
            break
        response = agent.run(user_input)
        print("Agent >", response)

if __name__ == "__main__":
    main()