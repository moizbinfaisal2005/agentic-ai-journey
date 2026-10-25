# Problem 10 — Agent Task Queue

# Imagine your agent receives:
# Search PSX stocks
# Analyze FFC
# Analyze OGDC
# Create report
# Send email

# The agent must process them in exactly the order received.
# Your job:
# Create a queue and add all 5 tasks.

# Then remove the tasks one by one.

# Use:
# deque
# append()
# popleft()



import collections
from collections import deque


queue = deque(["Search PSX stocks",
               "Analyze FFC",
                "Analyze OGDC",
                "Create report"
])


print(f"{queue} Original Queue")

queue.append("Send email")

print(f"{queue} After adding 'Send email'")

print(f"{queue.popleft()} remove from queue")

print(queue)

print(f"{queue.popleft()} remove from queue")

print(f"{queue} Queue after 2 tasks removed")

print(f"{queue.popleft()} remove from queue")
print(f"{queue.popleft()} remove from queue")
print(f"{queue.popleft()} remove from queue")

print(f"{queue} Final Queue after all tasks removed")







# Problem 11 — Agent Memory


# Create an agent memory dictionary:
# user_name
# investment_amount
# risk_level
# current_task
# completed_tasks

# Use these values:
# Ali
# 5000
# medium
# analyze stocks
# []

# Then imagine the agent finishes the task.

# Change:
# current_task → create recommendation

# and add "analyze stocks" to completed_tasks.




agent_memory = {
    "user_name": "Ali",
    "investment_amount": 5000,
    "risk_level": "medium",
    "current_task": "analyze stocks",
    "completed_tasks": []
}

print(agent_memory)

agent_memory["current_task"] = "create recommendation"

print(agent_memory)

agent_memory["completed_tasks"].append("analyze stocks")

print(agent_memory)






# Problem 12 — Duplicate Tools


# Your agent receives tools from several developers:

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

print(tool)


