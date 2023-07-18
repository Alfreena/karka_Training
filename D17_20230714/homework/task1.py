std=[{"name":"alfee","age":"21","place":"stk"},{"name":"akshaya","age":"20","place":"theroor"},{"name":"barathi","age":"20","place":"thovalai"},{"name":"sharmila","age":"20","place":"mobday market"},{"name":"sivaraj","age":"19","place":"vadasery"},{"name":"sanjai","age":"20","place":"ngl"}]
i=0
name=std[1]["name"]
age=std[1]["age"]
place=std[1]["place"]
def detail(std):
     print(f"I am {name} ,I'm {age} years old, and i'm from {place}")
det=detail(std)
print("\n")
#
for i in range(5):
     print(f"I am {std[i]['name']},)I'm {std[i]['age']}, and i'm from {std[i]['place']}")
     i+=1
#
