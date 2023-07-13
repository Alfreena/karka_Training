day=int(input("weekday: "))
def days(day):
    if day==0 or day==7:
        print("Today is a Saterday!")
    elif day==1:
        print("Today is a Sunday!")
    elif day==2:
        print("Today is a Monday!")
    elif day==3:
        print("Today is a Tuesday!")
    elif day==4:
        print("Today is a Wednesday!")
    elif day==5:
        print("Today is a Thursday!")
    elif day==6:
        print("Today is a Friday!")
    else:
        print("error")
cal=days(day)
