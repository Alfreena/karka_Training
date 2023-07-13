marks=[56,78,85,73]
tot=0
for i in marks:
    print("Befor:",tot)
    tot+=i
    print("After:",tot)
enum_mark=enumerate(marks)
print(type(enum_mark))
for i,mark in enum_mark:
    print("Entering iteration process for items:"+str(i))
    print("Befor:",tot)
    tot=tot+mark
    print("After:",tot)
    print("Exiting iteration process for items:"+str(i))
    print("\n")
