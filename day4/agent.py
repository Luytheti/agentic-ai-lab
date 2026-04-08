from planner import generate_plan
from tools import extract_numbers, compute_average, summarize_result


class PlanningAgent:

    def run(self, query):
        print("\n--- Generating Plan ---\n")
        plan = generate_plan(query)

        if not plan:
            print("No valid plan generated.\n")
            return "Failed to generate plan."

        print("Plan:")
        for step in plan:
            print("→", step)

        print("\n--- Executing ---\n")

        data = None

        for step in plan:

            if step == "extract_numbers":
                data = extract_numbers(query)
                print("Extracted Numbers:", data, "\n")

            elif step == "compute_average":
                data = compute_average(data)
                print("Computed Average:", data, "\n")

            elif step == "summarize_result":
                summary = summarize_result(data)
                print("Summary:", summary, "\n")
                return summary

        return data