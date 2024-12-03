print("Welcome to the tip calculator : ")

bills = input("What was the total bill? ")

percentage = input("What percentage tip would you like to give? (e.g. 20, 18, 15, etc.) ")

tip = (float(percentage) / 100) * float(bills)

totalbill =float(bills) + float(tip)

person = input ("How many people to split the bill? ")

splitbill = totalbill / int(person)

print("Each person should pay: " + str(round(splitbill,2)))