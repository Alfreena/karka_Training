weight=int(input("Enter your current earth weight: "))
print("I have information for the following planets:\n \t1.Venus \t2.Mars  \t3.Jupiter\n \t4.Saturn \t5.Uranus \t6.Neptune")
planet=int(input("Which planet are you visiting? "))
def wei(planet,weight):
    if planet==1:
        return weight*0.78
    elif planet==2:
        return weight*0.39
    elif planet==3:
        return weight*2.65
    elif planet==4:
        return weight*1.17
    elif planet==5:
        return weight*1.05
    elif planet==6:
        return weight*1.23
pl=wei(planet,weight)
print(f"your weight would be {pl} pounds on the planet ")