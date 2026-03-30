# Assignment 4 – Planning Based AI Agent

## Overview

This assignment implements a **planning-based AI agent** capable of solving tasks that require multiple sequential steps.

Unlike previous assignments where the agent directly selected a tool, this agent first **creates a plan** and then executes each step sequentially.

This demonstrates the concept of **task decomposition and planning**, which is an important capability in advanced **Agentic AI systems**.

---

# Objective

The objectives of this assignment are:

* Implement **task decomposition**
* Design a **multi-step planning agent**
* Execute tasks sequentially
* Display **intermediate outputs**

---

# Features

The agent can:

* Break down a complex task into steps
* Execute steps sequentially
* Use external tools
* Show intermediate outputs
* Generate summaries using an LLM

Example task:

User query:

Find the average of 5, 10, 15 and summarize the result

Steps performed:

1. Extract numbers
2. Compute average
3. Generate summary

---

# Technologies Used

* Python 3.9+
* Groq API
* Llama-3.3-70B-Versatile model
* python-dotenv

---

# Project Structure

```
agentic-ai-lab/
│
├── assignment4_planning_agent/
│   ├── agent.py
│   ├── planner.py
│   ├── tools.py
│   ├── main.py
│
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

# Installation

Clone the repository

```
git clone <repo-url>
cd agentic-ai-lab
```

Create virtual environment

```
python -m venv venv
```

Activate environment

Linux / Mac

```
source venv/bin/activate
```

Windows

```
venv\Scripts\activate
```

Install dependencies

```
pip install -r requirements.txt
```

---

# Configure API Key

Create a `.env` file:

```
GROQ_API_KEY=your_api_key_here
```

---

# Running the Agent

```
python assignment4_planning_agent/main.py
```

---

# Example Usage

```
User > Find the average of 5, 10, 15 and summarize the result
```

Output:

```
Plan Steps:
extract_numbers
compute_average
summarize_result
```

Intermediate outputs are displayed before the final answer.

---

# Code Explanation

## planner.py

Generates a step-by-step plan using the LLM.

Example plan:

```
1. extract_numbers
2. compute_average
3. summarize_result
```

---

## tools.py

Contains helper functions:

* `extract_numbers()` – extracts numbers from text
* `compute_average()` – calculates average
* `summarize_result()` – generates summary using LLM

---

## agent.py

Responsible for:

1. Getting plan from planner
2. Executing each step
3. Displaying intermediate outputs
4. Returning final result

---

## main.py

Runs the interactive terminal interface.

---

# Learning Outcomes

Through this assignment we learn:

* Task decomposition
* Sequential reasoning
* Planning-based AI agents
* Integration of LLM planning with tools

---

# Future Improvements

Possible extensions include:

* Multi-agent planning systems
* Dynamic tool generation
* Memory-enabled agents
* Autonomous workflow agents
