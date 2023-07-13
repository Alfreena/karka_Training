print("WELCOME TO MITCHELL'S TINY ADVENTURE!")
q1=input("You are in an creepy house! Would you like to go 'Upstaits' or into the 'kitchen'?\n")
if q1=="kitchen":
    k1=input("There is a long countertop with a dirty dishes everywhere.Off to one side there is ,as you'd expect,a refrigeraror. You may open the 'refrigerator' or look in a 'cabinet'. \n")
    if k1=="refrigerator":
        r1=input("Inside the refrigerator you see food and stuff.It preety nasty.Would you like to eat some of the food?('yes'or 'no')\n")
        if r1=="yes":
            print("You are saved.")
        if r1=="no":
            print("You die of starvation")
    if k1=="cabinet":
        r2=input("Inside the cabinet you see vessel and stuff.Would you like to get some of the stuff?('yes'or 'no')\n")
        if r2=="yes":
            print("You are saved.")
        if r2=="no":
            print("You die ")
if q1=="upstairs":
    k2=input("In upstairs there is a 'room' and 'balcony' you may choose any of them.\n")
    if k2=="room":
        a1=input("Inside the room you see soom 'cloths' and 'book' .Would you like to get some of the stuff?('yes','no')\n")
        if a1=="yes":
            print("you got some cloths and book")
        if a1=="no":
           print("Exit")
    if k2=="balcony":
        a2=input("In the balcony you soom 'chairs' and 'plants'\n")
        if a2=="chairs":
            print("take a rest")
        if a2=="plants":
            print("take a snap")