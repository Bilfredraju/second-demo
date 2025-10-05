# v1="it's sunday"
# v2='have a great day'
# #it's a great day 
# #great sunday
# print()
# print(v1.strip("sunday"))
# print(v2.strip('have'))

# a=v2.strip("have a great day")
# b=v1.strip("it's")
# c=print(a+b)

# print(v1[:5]+v2[5:])
# print(v2[7:-3]+v1[5:])
# print()
# print(v1[0:4]+v2[4:])

# sub=['I','you']  #i play hocky,i play football,i love hocky,i love football,you play hocky,you play football,you love hocky,you love football
# ver=['play','love']
# obj=['hockey','football']


# for i in sub:
#     for j in ver:
#         for k in obj:
#             print(i,j,k)
# for i in range(len(sub)):
#     for j in range(len(ver)):
#         for k in range(len(obj)):
#             print(sub[i],ver[j],obj[k])
# ls=[12,24,35,24,88,120,155,88,120,155]
# new=[]
# for i in ls:
#     if i not in new:
#         new.append(i)
# print(new)        
# # n=input('enter a sentence')#Ab A
# # d={'uppercase':0,"lowercase":0}#uc=0,lc=0
# # for i in n:
# #     if i.isupper():
# #         d["uppercase"]+=1 #u+=1,l+=1
# #     elif i.islower():
# #         d["lowercase"]+=1
# # print(d)            
# ls=['bbb','fff','ddd']
# ls1=[123,23,45]
# print([(i,j) for i in ls for j in ls1])
# # c1=int(input('enter the count'))
# ls=[]
# # for i in range(c1):
# #     ls.append(input('enter the name:-'))
# # print(ls)
#print([input('enter the name:-') for i in range(int(input('enter the count')))])




#values=[[1,2,3],[4,,5,6],['a','b']]      o/p=[1,4,'a']-using list comprehension

# val=[[1,2,3],[4,5,6],['a','b','c']]

# print([i[2]for i in val])

# a=[1,2,3,4]   #o/p=[2,4,6,8]
# b=[1,2,3,4]
# print([a[i]+b[i] for i in range(len(a))])#print([i+j for i in a for j in b if a.index(i)==b.index(j)])

# mat=[[1,2],[3,4],[5,6],[7,8]]#o/p=[[1,3,5,7],[2,4,6,8]]
# print([[j[i] for j in mat] for i in range(len(mat[0]))])




# for i in range(len(mat[0])):
#     for j in mat:
#         print(join j[i])






# #ls=['x','xx','xxx','xxxx','xxxxx']
# print(['x' *i for i in range(1,6)])

# # val='comprehension'
# # print(''.join([i for i in val if i.lower() not in 'aeiou']))

# mar=[[1,2,3,4],[4,5],[6,7,8,9]]
# print([j  for i in mar for j in i])




# # for i in mar:
# #     for j in i:
#         print(j)

# words=['apple','banana','orange','grapes','elephant','mango']#extract starting from vowels
# print([words[i] for i in range(len(words))if words[i][0] in 'aeiou'])#print([i for i in words if i[0].lower() in 'aeiou'])


#create a dict mapping words to their lenghts
# words=['python','dict','comprehension','exercise']
# print({i:len(i)for i in words})
#nested dictionary using comprehension

#{1:{1:1,2:4,3:9},2:{1:1,2:4,3:9},3:{1:1,2:4,3:9}}
#print({i:{j:j**2 for j in range(1,4)}for i in range(1,4)})

#declare a funtion to find factorial of a number

# def factorial(n):
#     f=1
#     if n<0:
#         return "no fact"
#     elif n==0:
#         return f
#     else:
#         for i in range(1,n+1):
#             f*=i
#         return f    #print(f)    
        
# print(factorial(int(input('enter a number:'))))


#wa fn that takes a number and returns the sum of its digits

# def summ(a):                             #def summ(a)
#     s=0                                     # print(int(i) for i in str(a))
#     while a>0:   #123                            #return sum(int(i) for i in str(num))
#         s=s+a%10    # 0+123%10(3)   12%10 (2)      1%10  (1)          #print(summ(1234))
#         a=a//10      #123//10 (12)
#     print(s) 
# num= int(input('enter a number:'))
# summ(num)       

# #count vowels in a str

# # def count_vowels(s):
# #     c=0
# #     for ch in s:
# #         if ch in 'aeiou':
# #             c+=1
# #     return c        
# print(count_vowels('aeiouhhu'))

# def count_vowels(str):
#     return sum(1 if ch in 'aeiou' else 0 for ch in str)
# print(count_vowels('alfredraj'))

#find max in a list
# ls=[10,20,40,35,85,65]
# def find_max(numbers):
#     max=numbers[0]
#     for i in numbers:
#         if i>max:
#             max=i
#     return max
# print(find_max(ls))        
#def find_max(numbers):
#     numbers.sort()
#     return numbers[-1]
# print(find_max(ls))

#########################################
#factorial using recursive fn
# def find_fact(num):
#     if num<0:
#         return 'no fact'
#     elif num==0 or num==1:
#         return 1
#     else:
#         return num*find_fact(num-1)
# print(find_fact(5))    

# ls=[2,3,4,5]
# def ls_sum(num):
#     if len(num)==1:
#         return num[0]
#     else:
#         return num[0]+ls_sum(num[1:])
# print(ls_sum(ls))    

# ls=[1,2,[3,4],5,[6,7]]
# def ls_sum(data):
#     total=0
#     for val in data:
#         if type(val)==type([]):
#             total=total+ls_sum(val)
#         else:
#             total=total+val    #0+1 1+2=3 3+3=6 6+4=7 7+3=10 10=5=15 6+7=13 13+15=28
#     return total
# print(ls_sum(ls))      

# #reverse a str using recursive fumction


# val='hello'
# def rev(str):
#     if str=="":
#         return str
#     else:
#         return rev(str[1:]) +str[0]
# print(rev(val)) 

# def add(x):
#     return x+2
# def mul(x):
#     return x*2
# result=add(mul(2))
# print(result)



# def compose(a,b):
#     def composed(x):
#         return a(b(x))
#     return composed





# def double(x):
#     return x*2    
# def increment(x):
#     return x+1
# val=compose(double,increment)
# print(val(5))



str="a cit"        

