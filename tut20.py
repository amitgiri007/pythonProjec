
# write a prog which takes input from user and tell him
# no of guesses 9
# print the number of guesses left
# no of guesses he took to finish
# game over


# while(True):
#     n = int(input("Enter the number :"))
#     print("Total number of guesses 9")
#     if n = 100:

# n = 18
i = 0
while i < 5:
    print("no of guesses left", 5 - i)
    print("enter the number")
    x = int(input())
    if x > 18:
        print("guess a smaller no")
    elif x < 18:
        print("guess a bigger no")
    else:
        print("your guess is correct")
        print("no of guesses required", i + 1)
        break
    i = i + 1
if i > 4:
    print("game over")





