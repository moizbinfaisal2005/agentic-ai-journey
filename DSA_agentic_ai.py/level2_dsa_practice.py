# Problem 5 — Stack

# Create a stack:
# Add these in order:
# Then remove one item using pop().



stack = ["Open website",
        "Search product",
        "Read product"
]


print(stack.pop())

print(stack)

stack.append("Add to cart")

print(stack)








# Problem 6 — Queue


# Create a queue using deque
# Then remove two tasks using popleft()


import collections
from collections import deque

queue = deque(["Task A",
               "Task B",
               "Task C",
               "Task D" 
])


queue.popleft()
queue.popleft()

print(queue)










