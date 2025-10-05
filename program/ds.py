# val = [1,2,3,4,5]
# val.insert(2,"bilu")
# val.reverse()
# val.append(set(input("enter a number:-").split(",")))
# val.sort(reverse=True)
print()
#extend multiple values
#append only one value


# a=[1,2,'python']
# b=a.copy()
# print(id(a))
# print(id(b))
# b.append(10)
# print(b)
# print(a)
# a=['ab','123','a','ebaz']
# print(max(a,key=len))
# print()
a=[10,20,'python',1,2,3,'python',1,4]
print(a.index('python',3))
print(a.index('python',3,7))
print()

# #tuple is immutable which means values cannot be changed or added
# A=(1,2,3)
# print(A)
# a,b,c=A
# print(a)
# print(c)
# #set{} unordered, no index, no duplicate values,can store only immutable type of date, immutable or harshable(set is immutable)
# a={1,2,4,1+2j,(1,2,'bilu'),6,7,9,3,3,2,'py','bilu',frozenset({1,2,3}),[1,2,3]}#list 1 2 3 is unharshable type
# print(a)
print()
val={1,4,5,6,'python','bilu'}
val.add('hello')
print(val)
val.update([1,2,3,45,3,5])
print(val)
a=set()
print(type(a))
print()
v1={1,2,3,4,5}
v2={1,4,5,67,7}
n=v1.intersection(v2)
print(n)
print()
vall=val


ds={1:'bilu','val':25,2:[2,3,4]}
print(ds)
print(ds)
print(ds.get(2))
print(ds.get(2,'data not found'))

