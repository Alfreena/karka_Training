a=int(input("Enter the value a: "))
b=int(input("Enter the value b: "))
c=int(input("Enter the value c: "))
s=(a+b+c)/2
print(f"the value of s:{s}")

def tri(a,b,c,s):
    return (s*(s-a)*(s-b)*(s-c))**2
area=tri(a,b,c,s)
print(f"Area of a triangle is:{area}")

def square(a):
    return a**2
squ=square(a)
print(F"Area of a square is:{squ}")

def rectangle(a,b):
    return a*b
rect=rectangle(a,b)
print(f"Area of a rectangle is:{rect}")

def circle(a):
    return (3.14)*(a**2)
cir=circle(a)
print(f"Area of a circle is:{cir}")

def trapezium(a,b,c):
    return ((a+b)/2)*c
trap=trapezium(a,b,c)
print(f"Area of a trapezium is:{trap}")