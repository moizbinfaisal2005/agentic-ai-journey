                                # While Loop Questions For Practice

  
#Quest 1

# i = 100
# while i >= 1:
#     print(i)
#     i -= 1



#Quest 2

# a = int(input("Enter Your Number Here: "))
# i = 1

# while i <= 10:
#     print (f" {a} x {i} = {a * i}")
#     i += 1
    


#Quest 3


# l = [1,4,9,16,25,36,49,65,81,100]

# idx = 0

# while idx <= len(l)-1:
#     print(l[idx])
#     idx += 1


#Quest 4


# l = (1,4,9,16,25,36,49,65,81,100)

# i =  0

# user = int(input("Search Number Here: "))

# while i < len(l):
#     if (l[i] == user):
#         print("Found")
       
#     i += 1 
     

user = input("Do You want Ascending Or Decending Order of Numbers A Or B: ")

if user.lower() == "a":
    a = int(input("Enter Start Number: "))
    b = int(input("Enter End Number: "))

    if a >= b:
      print("Your Start Number  should larger than End Number")
    else:
     for i in range(a,b):
      print(i)


elif user.lower() == "b":
    a = int(input("Enter End Number: "))
    b = int(input("Enter Start Number: "))

    if a <= b:
      print("Your End Number should larger than Start Number")
    else:
     for i in range(a,b,-1):
      print(i)
      

else:
  "Enter Correct Option Please"
