import random 

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
            'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 
            'x', 'y', 'z']

numbers = ['0', '1', '2', '3', '4', '5','6','7','8','9']

symbols = ['\'', '/' ,':' ,'*', '?', '"', '<', '>', '|', '=','!',
           '@','#','$','%','^','&','(', ')']

print("Welcome to the Password Generator")

len_let = int(input("Enter the desired password length: "))

if len_let < 4:
    print("Password length should be at least 4 characters.")
    exit()
len_numb = int(input("How many numbers would you like?\n "))
len_sym = int(input("How many symbols would you like?\n "))



password = []

for i in range(1, len_let+1):   
    password += random.choice(letters)

for i in range(1, len_numb+1):
    password += random.choice(numbers)

for i in range(1, len_sym+1):
    password += random.choice(symbols)

print(password)
random.shuffle(password)
print(password)

password_order = ""
for i in password:
    password_order += i

print(password_order)


# password = ""

# for i in range(1, len_let+1):   
#     password += random.choice(letters)

# for i in range(1, len_numb+1):
#     password += random.choice(numbers)

# for i in range(1, len_sym+1):
#     password += random.choice(symbols)

# print(password)