def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print("factorial :",fact)
num=int(input("enter the number :"))
factorial(num)
#recursion.
def recursion(n):
    if n==0 or n==1:
        return 1
    else:
        return n*recursion(n-1)
print("factorial with the help of recursion :",recursion(5))
