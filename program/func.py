# def val():
#     print('hello')
    
# val()    
# val()
# val()
# def add_val():
#     a=int(input('enter value:'))
#     b=int(input('enter value:'))
#     c=int(input('enter value:'))
#     res=a+b+c
#     print(res)
# add_val()    


# a,b,c=[10,20,30]
# def add_val(a,b,c):
#     res=a+b+c
#     print(res)
# add_val(a,b,c)
# add_val(11,22,33)


# a,b,c=[10,20,30]
# def add_val(a,b,c):
#     res=a+b+c
#     return res
# re=add_val(a,b,c)


# def vals(num):
#     print(num*2)
# vals(re)   
# 
# 
#  
#position argument passing
# def add_val(a,b,c):
#     return a+b+c
# print(add_val(1,2,3))

#arbitary argument passing
# def add_val(*a):
#     print(a)
#     for i in a:
#         print(i*i)
# add_val(1,2,3,4,5)    


# def add_val(**a):
#     print(a)
#     for i in a:
#         print(i)
# add_val(a=2,b=4,c=3,d=2,e=7)        

# def s(a):
#     s=0
#     while a>0:
#         s=s+a%10
#         a=a//10
#     print(s)
# num=int(input('enter a  number:'))
# print(s(num))

# def fact(a):
#     f=1
#     if a<0:
#         return 'no fact'
#     elif a==0:
#         return a
#     else:
#         for i in range(1,a+1):
#             f*=i #1=1*1  2*3   3*4   4*5   5*6  
#         return f


# print(fact(int(input('enter a number:'))))
    
# x=lambda a:a+10
# print(x(5))

# # x=lambda a,b:a*b
# # print(x(5,6))

# # for i in range(10,0,-1):
# #     print(i)

# str='hello'
# for i in range(len(str)-1,-1,-1):
#      print(str[i])

# def func1(*mylist):
#     for num in mylist:
#         print(num)
#     return
# func1(1,2,3,4)
# func1(1,2)


# def myFun(*args,**kwargs):
#     print("args:",args)
#     print("kwargs:",kwargs)
# myFun('geeks','for','geeks'first='geeks'mid='for'last='geeks')    



# color=['red','blue','green']
# for i in enumerate(color):
#     print(i)

# a=int(input("enter the value:"))
# b=int(input('enter the value:'))
# c=int(input('enter the value:'))
# val=lambda a,b,c:a if a>b &a>c else b if b>c else c
# print(val(a,b,c))

# def sqr(a):
#     return a*a
# print(list(map(sqr,[1,2,3,4])))#map fn sequenceinn  oro elmts pick cheyth fn neet kodukum


data=[0,1,'',None,'python',False,[],[1,2,3]]
print(list(filter(None,data)))#none default false ann ath vech each and every elmt nokum

data=[2,5,8,10,16,3,14]
print(list(filter(lambda x:x>10 and x%2==0,data)))

#reduce fn : elmts cummulative akum oru single elmt int reduce fn akum
from functools import reduce
a=[2,3,4]
print(reduce(lambda x,y:x+y,a))#5+4=9
print(reduce(lambda x,y:x+y,a,1))
ls=[2,55,1,17,10,8,20]
print(reduce(lambda x,y:x if x>y else y,ls))



