#a={23,1,90,76,43,"alfee",6.54}
#b=[2,6,1,0,67,3]
#print(a)
file=open("/home/alfee/alfee.txt",'r')
#print(file)
#print(file.read(19))
#for line in file:
#    print(line)
#file=open("/home/alfee/alfee.txt",'w')
#file.write("I am a programmer")
#file.close()
#file=open("/home/alfee/alfee.txt",'r')
#print(file.read(11))
#file=open("/home/alfee/alfee.txt",'a')
#file.write("Hello! this is alfee")
#file.close()
#file=open("/home/alfee/alfee.txt",'r')
#print(file.read())
for line in file:
    print(line.split())
    