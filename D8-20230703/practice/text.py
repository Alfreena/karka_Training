age=int(input("Enter your age:"))
text=" My name is alfee and i am "
print(text+str(age))
#startswith
print(text.startswith("M"))
#endswith
print(text.endswith("m"))
#strip
print(text.strip())
#count
print(text.count("a"))
#replace
print(text.replace(" ","."))
#title
print(text.title())
#lower
print(text.lower())
#len
print(len(text))
message="Hello python"
print(message[0])
print(message[-4])
print(message[0:5])
print(message[ :4])
print(message[6:])