l=[1,100,300,4,5,6]
x=int(input("Enter the element to find the index:"))
for i,l in enumerate(l):
    if (x==l):
       print("Index of the element",x ,"is",i)
