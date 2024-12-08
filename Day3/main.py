# print("Welcome to the rollercoaster!")
# height = int(input("Height in cm: "))

# if height > 120:
#     print("Congratulations! You are allowed to ride the rollercoaster.")
# else:
#     print("Sorry, you are not allowed to ride the rollercoaster. You are too short.")


# num = int (input("Enter the number "))

# if num % 2 == 0:
#     print("The number is even")
# else:
#     print("The number is odd")

# print("The BMI Calculator")

# weight = float(input("Enter your weight in kg: "))
# height = float(input("Enter your height in m: "))

# bmi = round(weight / (height ** 2),2)
# print(f"Weight is {weight} , Height is {height}, BMI is {bmi}")

# if bmi < 18.5:
#     print("Underweight")
# elif bmi < 25:
#     print("Normal weight")
# elif bmi < 30 :
#     print("Overweight")
# elif bmi < 35:
#     print("Obese Class I")
# else :
#     print("Obese Class II")


# year = int(input("Year: "))

# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print(f"{year} is a leap year.")
# else:
#     print(f"{year} is not a leap year.")


# print("Welcome to Python Pizza Deliveries!")

# size = input("What size pizza do you want? (small, medium, large): ")
# if(size == "small"):
#     price = 15
# elif(size == "medium"):
#     price = 20
# elif(size == "large"):
#     price = 25
# else:
#     print("Invalid size. Please choose from small, medium, or large.")
#     exit()

# pepperoni = input("Do you want pepperoni? (yes/no): ")
# if(pepperoni == "yes"):
#     if(size == "small"):
#         price += 2
#     elif(size == "medium" or size == "large"):
#         price += 3
#     else:
#         print("Invalid size. Pepperoni is only available for small, medium, and large sizes.")
#         exit()

# cheese = input("Do you want cheese? (yes/no): ")

# if(cheese == "yes"):
#     price += 1

# print(f"Your total cost is ${price}.")
