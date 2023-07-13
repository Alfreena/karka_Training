year=int(input("Enter the year:"))
def eligible(a):
    if a>=2020 and a<=2023:
        return ("you are eligible")
    else:
        return ("you are not eligible")
b=eligible(year)
print(eligible(year))