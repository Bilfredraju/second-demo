# ls=[1,2,3,4,5,6]
# for _ in ls:#range
#     print('hello')
# # print('done')
# ls=[1,2,3,4,5]
# new=[]
# for i in ls:
#     new.append(i+10)
# print(new)    
# ls={1:10,2:20,3:30,4:40}
# for k,v in ls.items():
#     print(k,v)
# ls=[1,2,3]
# for i in ls:
#     print(i+10)
#     for j in range(1,5):
#         print(j)
# ls=[1,2,3,4]
# for i in ls:
#     print(i,end='')
#5 4 3 2 1
#4 3 2 1
#3 2 1
#2 1
#1
# for i in range(0,6):
#     for j in range(5-i,0,-1):
#         print(j,end='')
#     print()
# i=5
# while i>=1:
#     j=i
#     while j>=1:
#         print(j,end='')
#         j=j-1
#     i=i-1
#     print()    
# for i in range(1,11):
#     if i==5:
#         continue#print('hello')
#     print(i)
# ls=[3,6,2,8,1,9,2,4]
# count=0
# while count<len(ls):
#     if ls[count]==1:
#         break
#     else:
#         print(ls[count])
#         count+=1
for i in range(1,4):
    for j in range(1,6):
        if j==3:
            print(f"breaking inner loop at i={i} j={j}")
            break
        print(f"i={i} j={j}")    