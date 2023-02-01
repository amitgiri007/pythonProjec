# While loop

# i = 0
# while(i<45):
#     print(i)
#     i = i + 5

# print("enter your day=")
# i=int(input())
# while(i<30):
#     i=i+1
#     total=30-i
#     print("Day=",i)
#     print("Total days left for month end=",total)
#
# Same using if condition
# print("enter your day=")
# i=int(input())
# if i < 30:
#     # i = i+1
#     total = 30 - i
#     print("Total :",total)

# # Factor calculation
print("factor of ----")
n1 = int(input())
factor = 1
# print(factor)
while factor<=n1:
    result = (n1 / factor)
    if result in range(1,n1)  :
        print(factor)
    factor = factor + 1