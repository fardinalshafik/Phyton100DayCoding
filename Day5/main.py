# heights = input("Enter the list of heights :").split()

# print(heights)

# total_heights = 0
# for i in heights:
#     total_heights += int(i)

# students = 0
# for j in heights:
#     students +=1

# average_height = round(total_heights / students)

# print("Average height is : ", average_height)

# score = input("Enter the score: ").split()

# print(score)

# highest_score = 0
# for i in score:
#     if int(i) > highest_score:
#         highest_score = int(i)

# print("Highest score is : ", highest_score)

# total = 0
# for i in range(1,11):
#     total += i
#     print(i)
# print("Total score is : ", total)

for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
