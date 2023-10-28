
# n = int(input("A number to check is prime or not :"))
# count = True
# for i in range(2,n):
#     if n % i == 0:
#         count = False
# if count == True:
#     print("Your Number is Prime")
# else:
#     print("Your Number is not Prime")

def prime(n):
    count=1
    for i in range(2,n):
     if n % i == 0:
        count=0
    if count == 1:
        print("Your Number is Prime")
    else:
        print("not Prime")
num=int(input("Enter number to check prime :"))
prime(num)
