name=input("Hey, what's your name?(sorry,I keep forgetting.) ")
age=int(input(f"Ok,{name}, how old are you? "))
if age<16:
    print(f"You can't drive,{name}")
elif age==16 or age==17:
    print(f"You can drive but not vote,{name}")
elif age>18 and age<24:
    print(f"You can vote but not rent a car,{name}")
else:
    print("You can do pretty much anythink.")
