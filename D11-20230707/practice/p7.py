height=float(input("Your height in m:"))
weight=int(input("Your weight in kg:"))
def bmi(height,weight):
    return weight/height**2
print("Your BMI is:",weight/(height**2))