from agent import ToolAgent

def main():
    agent = ToolAgent()

    print("Tool-Using AI Agent Started")
    print("Type 'exit' to quit\n")

    while True:
        user_input = input("User > ").strip()

        if user_input.lower() == "exit":
            break

        response = agent.handle_query(user_input)
        print("Agent >", response)


if __name__ == "__main__":
    main()