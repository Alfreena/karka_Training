import p7
height=float(input("Enter height in m: "))
weight=int(input("Enter weight in kg: "))
val=p7.bmi(height,weight)
print(f"Your bmi is {val}")
if val<18.5:
    print("BMI category: underweight")
elif val>18.5 and val<24.9 :
    print("BMI category: Normal weight")
elif val>25.0 and val<29.9 :
    print("BMI category: overweight")
elif val>30.0:
    print("BMI category: Normal obese")
