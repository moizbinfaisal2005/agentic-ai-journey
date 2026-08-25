## Exercise: The Chai Bill Calculator

# You run a chai stall. Customers order multiple cups of chai, sometimes with add-ons (extra ginger, masala, biscuits). Write a function to calculate their bill.
# Your task:
# Write a function chai_bill(cups, *addons, **discount) that:

# Charges ₹15 per cup of chai
# Adds ₹5 for each addon passed via *args (like "ginger", "masala", "biscuit")
# Applies a discount only if discount_percent is passed via **kwargs
# Returns the final bill amount

# Test it with these calls:

# print(chai_bill(2))                                              
# print(chai_bill(3, "ginger", "masala"))                          
# print(chai_bill(4, "biscuit", discount_percent=10))              
# print(chai_bill(5, "ginger", "masala", "biscuit", discount_percent=20))

# Expected output:

# * 30
# * 55
# * 58.5
# * 112.0






def chai_bill(cups,*addons,**discount):
    charges = cups * 15
    add_ons = len(addons) * 5
    bill = charges + add_ons

    if "disc_percent" in discount:
        final_price = bill - (bill * discount["disc_percent"]/100)
        return final_price
    else:
        return bill

print(chai_bill(4,"bisscut",disc_percent=10))

    
    
      

















