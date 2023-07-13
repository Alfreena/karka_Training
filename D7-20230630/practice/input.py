passed_out_year=input("Which year you passed out from college:")
print(passed_out_year)
#type_of_passed_out_year=type(passed_out_year)
#print(type_of_passed_out_year)
int_passed_out_year=int(passed_out_year)
print(type(int_passed_out_year))
is_eligible = (int_passed_out_year==2022 and int_passed_out_year>=2023)
if is_eligible:
    print("You are eligible")
else:
    print("You are not eligible")
    