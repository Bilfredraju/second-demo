# val = "Awesome"   #Global Variable

# def callme():
#     val = "Nice"    #Local
#     print("Python is",val)

# callme()
# print(val)



val = "Awesome"   #Global Variable

def callme():
    global val   #to convert local to global
    val = "Nice"    #Local
    print("Python is",val)

callme()
print(val)