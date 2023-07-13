year=input("Enter a year:")
int_year=int(year)
print(type(int_year))
is_leapyear=(int_year%400==0)or(int_year%100!=0)and(int_year%4==0)
if is_leapyear:
    print(year,"is a leap year")
else:
    print(year,"is not a leap year")