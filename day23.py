#File Handling: file handler is an object of file to maintain several function of file like, creating,reading,updating and deleting the file.
#open a file: 1.open() 2.with open()
'''
name=open("filename","mode") 
-----
-----
name.close()
#modes :
"r": it is used to reading the file,error if file does not exist.
"a":it is used to add the text into file,error if file does not exist.
"w": is used to add the txtx into file but it will override of all txt inside file.if the file does not exist it will create with that name.
"x":used to create the file. but will throw error if we used "r" mode to create.
method:
-------
write()
read(): this method can read entire file line by line where we can specify the side
readline():can read only one line at a time in a file.
readlines(): it will read entire file and gives in a list where each line is each index in the lis
'''
#example program

so=open("demo1.txt", "r")
print(so.read())
so.close()
#program

with open('demo.txt','w') as any_:
    any_.write('hello')


#program
any_=open("demo1.txt","r")
print(any_.read())
any_.close()


#program
any_=open("demo1.txt","r")
print(any_.readlines())

