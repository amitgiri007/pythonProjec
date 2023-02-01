# Break and continue statement

# i = 0
# while(True):
#     print(i, end= " ")
#     if (i == 44):
#         break #stop the loop
#     i = i + 2

# i = 0
# while(True):
#     if i + 1 < 5:
#         i = i + 1
#         continue
#     print(i + 1, end=" ")
#     if (i == 44):
#         break #stop the loop
#     i = i + 1

# Study Break n continue again

while(True):
    n1 = int(input("Enter the number \n"))
    if n1 > 100:
        print("Congrats")
        break
    else:
        print("Try Again")
        continue

