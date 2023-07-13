#height=float(input("Your height in m:"))
#weight=int(input("Your weight in kg:"))
def bmi(height,weight):
    res=weight/(height**2)
    return res
# print("Your BMI is:",(weight/(height**2)))