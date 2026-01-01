class employee:
    val='HDFC'
    def __init__(self,first,last,mail):#constructor
        self.first=first
        self.last=last
        self.mail=mail
    def fullname(self):
        return f"{self.first}{self.last}"
    def call_mail(self):
        return self.mail  
    def info(self):
        return f"{self.first}{self.last}\n{self.mail}" 

emp1=employee('bilu','raju','bilu@gmail.com')
emp2=employee('alfy','raj','alfy@gmail.com')

#print(emp1.first)
#print(emp2.first)

# print(emp1.fullname())
# print(emp2.fullname())
# print(emp1.call_mail())
# print(emp2.call_mail())

print(emp1.info())
print(emp2.info())