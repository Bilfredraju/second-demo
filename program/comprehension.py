ls=[]
# for i in range(1,11):
#     ls.append(i*i)
# print(ls)
# print([i*i for i in range(1,11)])

# ls=[]
# for i in range(1,21):
#     if i%2==0:
#         ls.append(i)
# print(ls)

# print([i for i in range(1,21)if i%2==0])

# import math as m
# print([m.sqrt(i) for i in range(1,21)])

# a=['bilu','ramu','gijo']
# b=['py','cyber','analyst']
# ls=[]
# # for i in a:
# #     for j in b:
# #         ls.append((i,j))
# # print(ls)
# print([(i,j) for i in a for j in b])        
#print([(i,'even')if i%2==0 else (i,'odd') for i in range(1,21)])
# ls=[1,0,-2,4,0,3,-5]
# print([(i,'negative')if i<0 else (i,'zero')if i==0 else(i,'positive') for i in ls])
# ls=[]
# count=int(input('enter the count:-'))
# for _ in range(count):
#     ls.append(int(input('enter a value:-')))
# print(ls)
#print([int(input('enter the values:-'))for _ in range(int(input('enter the count:-)))])
# ds={}
# # for i in range(1,11):
# #     ds[i]=i*i
# # print(ds)
# print({i:i*i for i in range(1,11)})
# tp=((i,'even')if i%2==0 else(i,'odd')for i in range(1,21))
# print(tp)
# for i in tp:
#     print(i)
# #print(next(tp))  
# ls=[1,0,-2,4,0,3,-5]
# tp=((i,'negative') if i<0 else(i,'zero') if i==0 else(i,'positive')for i in ls)  
               
#swap keys and values in a dictionary
data={'a':1,'b':2,'c':3}
print({v:k for k,v in data.items()})
#create a dictionary where keys are numbers (1-10) and values are 'even' or 'odd'

print({i:'even' if i%2==0 else 'odd' for i in range(1,11)})  #print({i:k for i in range(1,11) for k in range(1,11) if k%2==0})  

text='dictionary'
print({i:text.count(i) for i in text})

