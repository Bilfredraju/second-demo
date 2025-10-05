#import time as t
# print(dir(t))
# print(help(dir))

# print(t.asctime())
# print(t.time())
#print(t.localtime(t.time()))

# val=(1990,9,29,0,0,0,0,0,0,)
# print(t.localtime(t.mktime(val)))

# from time import sleep
# sleep(5)
# print('hello')

# import calendar as cl
# print(cl.calendar(2026))
# print(cl.month(2025,9,2,3))
# print(cl.leapdays(2020,2029))

# print(dir(cl))

# import datetime as dt
# print(dt.date(2025,9,29))
# print(dt.date.today())

# d=dt.date.today()
# print(d.weekday())
# print(d.isoweekday())

# di=dt.date.today()
# print(d)
# dt=dt.timedelta(days=5)
# print(di+dt)
# print(di-dt)

# import random as rd
# # print(rd.random())
# # print(rd.uniform(1,10))
# # print(rd.randint(1,10))

# vals=['err','rttt','eere']
# print(f'{rd.choice(vals)}Bilu')#sample completly unique

# vals=['err','rttt','eere']
# print(f'{rd.choice(vals)}Bilu')

# #choices



# 3##############
# import random
# from time import sleep
# lottery_tickets=[]
# print('creating 100 tickets')
# sleep(2)
# for i in range(100):
#     lottery_tickets.append(random.randrange(100000,9999999))

# v=random.sample(lottery_tickets,k=2)
# print('finding winners! please wait')
# sleep(5)
# print(f'winners are:{v}')

###################################
x=isinstance(5,int)#5=obj class=int
print(x)
class employee:
    pass
emp=employee()
print(isinstance(emp,employee))

a=[False,False,False]
b=[True,False,False]
print(any(a))
print(all(b))
#########################
print(abs(-11))
print(abs(-1.34))#abs   convert to absolute values(positive values)
#####################33
import math
print(math.sqrt(5))
print(math.pi)
print(math.sin(5))

from math import ceil,floor

print(ceil(5.6))
print(floor(5.6))
#########################
import statistics as st
print(st.mean(1,2,3,4,5))
print(st.median([1,2,3,3,4,5,55,7]))