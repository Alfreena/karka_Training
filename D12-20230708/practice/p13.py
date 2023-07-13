print("TWO QUESTIONS!\nThink of an object, and I'll try to guess it.")
q1=input("Question 1, Is it animal,vegetable,or mineral? \n")
q2=input("Question 2, Is it's is bigger than a breadbox? \n")
def question(q1,q2):
    if q1=="animal" and q2=="yes":
        print("My guess is that you are thinking of a mouse.\nI would ask you if i'm right ,but i don't actually care")
    if q1=="animal" and q2=="no":
        print("My guess is that you are thinking of a squirrel.\nI would ask you if i'm right ,but i don't actually care")
    if q1=="vegetable" and q2=="yes":
        print("My guess is that you are thinking of a watermelon.\nI would ask you if i'm right ,but i don't actually care")
    if q1=="vegetable" and q2=="no":
        print("My guess is that you are thinking of a carrot.\nI would ask you if i'm right ,but i don't actually care")
    if q1=="mineral" and q2=="yes":
        print("My guess is that you are thinking of a camaro.\nI would ask you if i'm right ,but i don't actually care")
    if q1=="mineral" and q2=="no":
        print("My guess is that you are thinking of a paper clip.\nI would ask you if i'm right ,but i don't actually care")
qu=question(q1,q2)