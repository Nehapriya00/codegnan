#Error Handling:
#try block: the try block test block of code for error
#except block: the except block let handif the code contain errors.
#else block: this will be excuted, if the try block has no errors in the code.

try:
    print(10/0)
except:
    print("This will handle ZeroDivisionError")

#-------
try:
    a=10+"str"
    print(a)    
except:
    print("This will handle TypeError")

#------
try:
    print("Any")
except:
    print("This will handle NameError")
else:
    print("No error")

#--------
try:
    print(r)
except TypeError:
    print("It will handle TypeError")

#--------
try:
    print(9+"h")
except NameError:
    print("It will handle NameError")


#it will only handle the error with the flow of try block code
try:
    print(a)
    print(9+"e")
except TypeError:
    print("It will handle TypeError")
except NameError:
    print("It will handle NameError")


#finally block: this will be excuted either try block contain error or not.
try:
    print(a)
except:
    print("Error")
else:
    print("No Error")
finally:
    print("The End")



