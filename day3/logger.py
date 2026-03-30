from datetime import datetime

LOG_FILE = "logs.txt"

def log_interaction(user_input, tool, output):
    with open(LOG_FILE, "a") as f:
        f.write("\n--------------------------\n")
        f.write(f"Time: {datetime.now()}\n")
        f.write(f"User Input: {user_input}\n")
        f.write(f"Selected Tool: {tool}\n")
        f.write(f"Output: {output}\n")