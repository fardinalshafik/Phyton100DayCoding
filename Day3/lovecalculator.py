print("Welcome to the Love Calculator!")

name1 = input("Enter the first name: ")

name2 = input("Enter the second name: ")

name = name1.lower() + name2.lower()


t = name.count("t")
r = name.count("r")
u = name.count("u")
e = name.count("e")

true = t + r + u + e 

l = name.count("l")
o = name.count("o")
v = name.count("v")
e = name.count("e")

love = l + o + v + e

score = str(true) + str(love)
print("Score: " + score + "%")