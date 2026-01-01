# val=10/0
# print(val)
# print('hello')

# ##########################3
# try:
#     pass
# except:
#     pass
# finally:
#     pass

# def val():

#     try:
#         a=int(input('enter the value:'))
#         b=int(input('enter the value:'))
#         res=a/b
#         print(res)
#     except:
#     #error ayalum except block handle cheyum
#         print('invalid entry')
#         val()

#     finally:
#         print('hi')    #always execute

# val()
# print('done') 



# try:
#     val1=int(input('enter the no.'))
#     val2=int(input('enter no.'))
#     print(val1/val2)
#     print(a)
# except(ZeroDivisionError,ValueError):
#     print('invalid operation')
# except:
#     print('error occur')   


# try:
#     val1 = int(input("Enter the number: "))
#     try:
#         val2 = int(input("Enter the number: "))
#         print(val1/val2)
#     except:
#         print("Cannot divided by zero")
# except:
#     print("Invalid number entered")

# try:
#     a = int(input("Enter the number1: "))
#     b = int(input("Enter the number2: "))
#     print(a/b)
#     if a>0 and b>0:
#         print(a/b)
#     else:
#         raise ValueError
# except:
#     print("Invalid entry")

# class NegativeNumberError(Exception):
#     pass

# try:
#     a = int(input("Enter the number1: "))
#     b = int(input("Enter the number2: "))
#     if a>0 and b>0:
#         print(a/b)
#     else:
#         raise NegativeNumberError("Negative numbers are not allowed")
# except NegativeNumberError as NNE:
#     print(NNE)


# try:
#     a = int(input("Enter the number1: "))
#     b = int(input("Enter the number2: "))
#     if a>0 and b>0:
#         print(a/b)
#     else:
#         raise ValueError("Invalid Entry")
# except ValueError as VE:
#     print(VE)