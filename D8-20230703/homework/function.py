n1=int(input("Enter the first number:"))
n2=input("Enter the operator:")
n3=int(input("Enter the third number:"))
def add(n1,n2,n3):
    if n2=="+":
        result= n1+n3
    if n2=="-":
        result =n1-n3
    if n2=="*":
        result= n1*n3
    if n2=="/":
        result = n1/n3
    if n2=="%":
        result = n1%n3
    if n2=="**":
        result = n1**n3
    return result
tot=add(n1,n2,n3)
print(tot)