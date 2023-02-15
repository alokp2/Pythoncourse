#Finding the greater number among three values
n1=int(input("Enter value of A:"))
n2=int(input("Enter value of B:"))
n3=int(input("Enter value of C:"))

if(n1>n3):
    if(n1>n2):
        print(n1,"is greater")
    else:
        print(n2,"is greater")
else:
    if(n2>n3):
        print(n2,"is greater")
    else:
        print(n3,"is greater")








#WAP to find odd or even and whether n is positive or negative.
n=int(input("Enter Number:"))
n1=int(input("Enter Number:"))

if n>0:
    print("\nIt is +ve")
else:
    print("\nIt is -ve")

if(n%2==0):
    print("It is even")

else:
    print("It is odd")

#finding max number between two number
if(n>n1):
    print("n:",n," is the max value")

else:
    print("n1:",n1," is max value");
