print("Welcome to Tresure Island.\n\n")

print("Your mission is to find the treasure.")
print("You are at a cross road . Where you want to go? Type 'left' or 'right' ")

decision = input()

if decision == 'left':
    print("You encounter a monster. Game Over.")

elif decision == 'right':
    print(" You come to a lake. There is a island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across ")
    
    island_decision = input()

    if island_decision == 'swim':
        print("You encounter a river moster. Game Over.")
    elif island_decision == 'wait':
        print("You arrive at the island unharmed. There is a house with 3 doors. One red , one yellow, one blue. Which colour do you choice?")
        
        house_color_decision = input()

        if house_color_decision == 'red':
            print("You fell in a hole. Game Over.")
        elif house_color_decision == 'yellow':
            print("You fell in a hole. Game Over.")
        elif house_color_decision == 'blue':
            print("Congratulations! You found the treasure.")
        else:
            print("You fell in a hole. Game Over.")
       