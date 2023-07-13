quiz=input("Are you ready for a Quiz? ")
score=0
if(quiz=="yes"):
    print("Okay, here its come!")
    q1=int(input("What is the capital of the Alaska? \n\t\t1,Melbourne\n\t\t2,Anchorage\n\t\t3,Juneau\n"))
    if(q1==3):
        print("Thats right")
        score+=1
    else:
        print("Thats Wrong")
    q2=int(input('Can you store the value "cat" in a variable of type int?\n\t\t1,Yes\n\t\t2,No\n'))
    if(q2==2):
        print("Thats right!")
        score+=1
    else:
        print("Sorry ,cat is a string. int's can only store numbers.")
    q3=int(input("What is the result of 9+6/3?\n\t\t1,5\n\t\t2,11\n\t\t3,15/3 \n"))
    if(q3==2):
        print("That right!")
        score+=1
    else:
        print("That's wrong")
    print(f"Overall,you got {score} out of 3 correct.")
    print("Thanks for playing!")
else:
    print("Exit")
    