# var1 = 1
# var2 = 2
# var3 = int(input())
# if var3 > var2:
#     print("Greater")
# elif var3 == var2:
#     print("Equal")
# else:
#     print("Smaller")

# list1 = [1,2,3,4]
# print(1 not in list1)
# if 12 not in list1:
#     print("No")

print("enter the age")
var1 = int(input())
if var1 > 18 and var1 < 60:
    print("You can drive")
elif var1 == 18:
    print("you have to come and see")
else:
    print("you cant drive")