## Exercise: Codebasics Chai Stall — Resilient Bill Calculator

# Remember the chai bill calculator from lesson 2? Customers (and bugs) don't always behave. Make it bulletproof.

# Write a function `safe_chai_bill(cups, price_per_cup)` that:
# 1. Converts `cups` and `price_per_cup` to numbers using `int()` / `float()` (they may arrive as text from a form).
# 2. Uses `try/except` to catch a `ValueError` if someone passes `"two"` instead of `2` → return the message `"Please enter numbers only."`
# 3. If `cups` is less than 1, return the message `"Cups must be at least 1"`.
# 4. Otherwise return the total bill (`cups * price_per_cup`).

# Test it with these calls:
# ```python
# print(safe_chai_bill("3", "15"))     # normal text input from a form
# print(safe_chai_bill(2, 15))          # normal numbers
# print(safe_chai_bill("two", 15))      # bad input -> caught
# print(safe_chai_bill(0, 15))          # too few cups
# ```

# Expected (roughly):
# ```
# 45
# 30
# Please enter numbers only.
# Cups must be at least 1
# ```

# **Bonus:** wrap the call in lesson 3's Streamlit app so a bad recipe request shows `st.error(...)` instead of crashing.



def safe_chai_bill(cups, price_per_cup = 15):
   
  

   try:
      cups = int(cups)
   except ValueError:
      return "Please Enter Only Numbers not TEXT"
   if cups < 1:
      return("Cups Should At Least 1 Not 0")
   total = cups * price_per_cup
   return total
    
  

print(safe_chai_bill("3"))

print(safe_chai_bill(2))

print(safe_chai_bill("four"))

print(safe_chai_bill("0"))

print(safe_chai_bill(0))

