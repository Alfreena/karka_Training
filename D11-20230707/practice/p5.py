name=input("Hello! what is your name? ")
age=int(input(f"Hi,{name}! How old are you? "))
def cal_age(age):
    befor=age+5
    after=age-5
    return(f"Did you know that in five years you will be {befor} years old ?\nAnd five years ago you were {after}! Imagine that! ")
cl=cal_age(age)
print(cl)