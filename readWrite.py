file = open('test.txt')
#print(file.read(3))
#print(file.readline())
#print(file.readline())

#Now need to print line  by line using readline method
#line = file.readline()
#while line!= "":
#    print(line)
#    line = file.readline()

for i in file.readlines():
    print(i)

file.close()