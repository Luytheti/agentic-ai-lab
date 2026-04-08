from agent import PlanningAgent


def main():
    agent = PlanningAgent()

    print("Planning-Based AI Agent Started")
    print("Type 'exit' to quit\n")

    while True:
        query = input("User > ").strip()

        if query.lower() == "exit":
            break

        result = agent.run(query)

        print("\nFinal Output:")
        print(result)
        print("\n-------------------------\n")


if __name__ == "__main__":
    main()