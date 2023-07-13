name=input("Hey, whats your name? ")
age=int(input(f"Ok,{name}, hpe old are you? "))
if age<16:
    print(f"You can't drive,{name}")
if age<18:
    print(f"You can't vote,{name}")
if age<25:
    print(f"You can't rent a car,{name}")
else:
    print("You can do anythink legal.")
