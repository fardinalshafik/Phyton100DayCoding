Rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

Paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

Scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

print ("Welcome to the Rock Paper Scissors GAME!\n")

import random
choice = [ Rock , Paper ,Scissors]

print("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors. ")

user_choice = int(input())
if user_choice > 2 & user_choice < 0:
    print("Invalid input. You loss.")
    exit()
print(choice[user_choice])

computer_choice = random.randint(0,2)

print("Computer chose:\n")
print(choice[computer_choice])

if user_choice == 0 and computer_choice == 2:
    print("You win!")
elif user_choice == 1 and computer_choice == 0:
    print("You win!")
elif user_choice == 2 and computer_choice == 1:
    print("You win!")
elif user_choice == 0 and computer_choice == 1:
    print("You loss!")
elif user_choice == 1 and computer_choice == 2:
    print("You loss!")
elif user_choice == 2 and computer_choice == 1:
    print("You loss!")
elif user_choice == computer_choice :
    print("It's a tie!")




# if user_choice not in range(3):
#     print("Invalid input. Please try again.")
#     exit()
# elif user_choice == 0:
#     user_choice_word = "Rock"
#     print(rock)
#     print("Computer chose:\n")
#     computer_choice = random.choice(choice)
#     print(computer_choice)
#     if computer_choice == user_choice_word:
#         print("It's a tie!")
#     elif(computer_choice == "Paper"):
#         print("Computer wins!")
#     elif(computer_choice == "Scissors"):
#         print("You win!")
# elif user_choice == 1:
#     user_choice_word = "Paper"
#     print(Paper)
#     print("Computer chose:\n")
#     computer_choice = random.choice(choice)
#     print(computer_choice)
#     if computer_choice == user_choice_word:
#         print("It's a tie!")
#     elif(computer_choice == "Rock"):
#         print("You win!")
#     elif(computer_choice == "Scissors"):
#         print("Computer wins!")
# elif user_choice == 2:
#      user_choice_word = "Scissors"
#      print(Scissors)
#      print("Computer chose:\n")
#      computer_choice = random.choice(choice)
#      print(computer_choice)
#      if computer_choice == user_choice_word:
#         print("It's a tie!")
#      elif(computer_choice == "Rock"):
#         print("Computer wins!")
#      elif(computer_choice == "Paper"):
#       print("You win!")
