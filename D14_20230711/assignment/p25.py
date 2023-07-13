num=int(input("Enter the number:"))
def month(num):
    if num==1:
        print(f"Number\tMonth\n{num}\t January")
    elif num==2:
        print(f"Number\tMonth\n{num}\t February")
    elif num==3:
        print(f"Number\tMonth\n{num}\t March")
    elif num==4:
        print(f"Number\tMonth\n{num}\t April")
    elif num==5:
        print(f"Number\tMonth\n{num}\t May")
    elif num==6:
        print(f"Number\tMonth\n{num}\t June")
    elif num==7:
        print(f"Number\tMonth\n{num}\t July")
    elif num==8:
        print(f"Number\tMonth\n{num}\t August")
    elif num==9:
        print(f"Number\tMonth\n{num}\t September")
    elif num==10:
        print(f"Number\tMonth\n{num}\t October")
    elif num==11:
        print(f"Number\tMonth\n{num}\t November")
    elif num==12:
        print(f"Number\tMonth\n{num}\t December")
    else :
        print("error")
months=month(num)
      