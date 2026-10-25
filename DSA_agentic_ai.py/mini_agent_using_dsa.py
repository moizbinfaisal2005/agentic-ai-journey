# This is your final challenge.

# Build a small program that represents an AI agent's task manager.

# It should have:

# Agent memory
# Tools
# Tasks

# Program behavior
# Your program should:
# Print the agent name.
# Print available tools.
# Take the first task from the queue.
# Print: Working on: search information

# Take the next task.
# Print it.
# Continue until there are no tasks left.
# Finally print:   All tasks completed!


import collections
from collections import deque


agent_memory = {
    "name": "Research Agent",
    "status": "Working"
}

tools = [
    "search",
    "email",
    "search",
    "calculator",
    "database",
    "email",
    "browser",
    "calculator"
]

tool = set(tools)


tasks = deque([
    "search information", 
    "analyze data",
    "create report",
])

print(f"Agent Name is {agent_memory["name"]}")
print(f"Agent Status is {agent_memory["status"]}")

print("Available tools:", tool)

print("Starting tasks...")

while tasks:
    current_task = tasks.popleft()
    print("Working on:", current_task)
print("All Tasks Completed!")


    

