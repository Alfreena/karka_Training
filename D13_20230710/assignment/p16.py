gender=input("What is your gender(M or F): ")
f_name=input("First name: ")
l_name=input("Last name: ")
age=int(input("Age: "))
print("\n")
marr=input(f"Are you married, {f_name}(yes or no)? ")
print("\n")
if gender=="F" and marr=="yes":
    print(f"Then i shall call you Mrs.{l_name}")
if gender=="F" and marr=="no":
    print(f"Then i shall call you Ms.{l_name}")
if gender=="M" and marr=="yes":
    print(f"Then i shall call you Mr.{l_name}")
if gender=="M" and marr=="no":
    print(f"Then i shall call you {f_name}{l_name}")
    