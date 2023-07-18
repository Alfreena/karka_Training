std=[{"name":"alfee","age":"21","place":"stk"},{"name":"akshaya","age":"21","place":"theroor"},{"name":"barathi","age":"21","place":"thovalai"},{"name":"sharmila","age":"20","place":"mobday market"},{"name":"sivaraj","age":"19","place":"vadasery"},{"name":"sanjai","age":"20","place":"ngl"}]
i=0
def eligible(std):
    for i in range(5):
        if (std[i]['age'])>='21':
            print(f"I'm {std[i]['name']}, I'm from {std[i]['place']}")
            i+=1   
eli=eligible(std)
