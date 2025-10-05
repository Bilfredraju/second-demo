# assert 6>3
# print('hello')

# def val():
#     age=int(input('enter your age'))
#     assert age>=0,'invalid data'
#     print(f'age is :{age}')
# val() 

def avg(val):
    assert len(val)!=0,'invalid data'
    print(sum(val)/len(val))
avg([1,2,3,4,5])    