print("TWO MORE QUESTION \nThink of something and I'll try to guess it!")
q1=input("Question1, Does it stay 'inside' or 'oudside' or 'both'?\n")
q2=input("Question2, Is it a living thing?\n")
def question(q1,q2):
    if q1=="inside" and q2=="yes":
        print("Then what else could you be thinking of besides a houseplant")
    if q1=="inside" and q2=="no":
        print("Then what else could you be thinking of besides a shower chair")
    if q1=="outside" and q2=="yes":
        print("Then what else could you be thinking of besides a python")
    if q1=="outside" and q2=="no":
        print("Then what else could you be thinking of besides a billboard")
    if q1=="both" and q2=="yes":
        print("Then what else could you be thinking of besides a dog")
    if q1=="both" and q2=="no":
        print("Then what else could you be thinking of besides a cell phone")
qu=question(q1,q2)
    
    