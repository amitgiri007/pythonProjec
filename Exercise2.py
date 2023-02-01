# Exercise 2 - Faulty Calculator
# Design a calculator which will correctly solve all the problems except the following ones:
# 45*3 =555, 56+9 = 77 , 56/6 = 4
# Answer

var1 = input("Enter the Operator :")
var2 = int(input("Enter the Number :"))
var3 = int(input("Enter the Number :"))

if var1 == "*":
    if var2 == 45 and var3 == 3:
        print("The output is :",555)
    else:
        print("The output is :",var2 * var3)

elif var1 == "+":

    if var2 == 56 and var3 == 9:
        print("The output is :",77)
    else:
        print("The output is :",var2 + var3)

elif var1 == "/":
    if var2 == 56 and var3 == 6:
        print("The output is :", 4)
    else:
        print("The output is :", var2 / var3)

if var1 == "-":
        print("The output is :",var2 - var3)
else:
        print("Enter the correct operator")





