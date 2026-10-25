# Problem 1 — Agent Tasks

# Add "Save report" to the list.
# Remove "Read results".
# Print the final list.


agent_tasks = [
    "Search web",
    "Read results",
    "Analyze data",
    "Write report",
    "Send email"
]

agent_tasks.append("Save report")
agent_tasks.remove("Read results")

print(agent_tasks)









# Problem 2 — Agent Memory

# Print the user's name.
# Print the goal.
# Change the level to "intermediate".
# Add: "current_topic": "DSA Practice" to the dictionary.



agent_memory = {
    "name": "ALI",
    "goals": "Learn Agentic AI",
    "level": "Beginner"
}

print(agent_memory["name"])

print(agent_memory.get("goals"))

agent_memory["level"] = "Intermediate"

print(agent_memory.get("level"))

agent_memory.update({"current_topic": "DSA Practice"})

print(agent_memory)






# Problem 3 — Unique Tools

# Create a new variable containing only unique tools.


tools = [
    "search",
    "email",
    "search",
    "calculator",
    "email",
    "database",
    "search"
]

unique_tools = set(tools)

print(unique_tools)






# Problem 4 — Dictionary Lookup

# 1. Prints what the "search" tool does.
# 2. Prints what the "email" tool does.
# 3. Checks whether "browser" exists.
# Don't crash the program if "browser" doesn't exist.


agent_tools = {
    "search": "Search the internet",
    "calculator": "Perform calculations",
    "email": "Send emails",
    "database": "Access database"
}

print(agent_tools.get("search"))

print(agent_tools.get("email"))

if "browser" in agent_tools:
    print(agent_tools["browser"])
else:
    print("The 'browser' tool does not exist in the agent tools.")

