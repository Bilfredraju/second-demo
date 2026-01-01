# x - create
# r - read
# w - write
# a - append
# b - binary

#1. open a file
#2. operations
#3. close

#open('sample.txt','x')


# f=open('sample.txt','w')
# f.write('line number 1\n')
# f.write('line number 2\n')
# f.close()

# f=open('sample1.txt','w')
# f.write('line number 1\n')
# f.write('line number 2\n')
# f.close()

# f=open('sample1.txt','r')
# print(f.readlines())
# f.close()

# f=open('sample1.txt','r')
# print(f.readlines())
# f.close()


# f=open('sample.txt','r')
# val=f.readlines()#list of str aayitt
# res=[i.strip() for i in val]
# print(res)
# for i in res:
#     print(i)
# f.close()    







# f=open('sample.txt','r')
# new=f.readline(7)
# print(new)
# f.close()


# # f=open('sample.txt','a')
# # f.write('line number10\n')
# # f.write('line number20\n')
# # f.close()

# f=open('shared 2.jpg','rb')
# val=f.read()
# print(val)
# f.close()


# f1=open('shared 2.jpg','rb')#read binary
# val=f1.read()
# f2=open('ekm.jpg','wb')# write binary
# f2.write(val)
# f2.close()

# f=open('sample.txt','r')
# new=f.readline()
# print(new)
# print(f.tell())#pointerr position
# new=f.readline()
# print(new)
# print(f.tell())
# f.seek(0)
# new=f.readline()
# print(new)
# print(f.tell())
# f.close()


# # with open('sample.txt') as f:#default read mode
# #     val=f.read()
# #     print(val)


# with open('sample.txt','r') as f1, open('result1.txt','w') as f2:
#     for val in f1:
#         f2.write(val)


# with open('sample.txt','r') as f1, open('result1.txt','w') as f2:
#     val=f1.read()
#     f2.write(val)        

# with open('sample.txt','r') as f1,open('res.txt','w') as f2:
#     for val in f1:
#         a=val.strip()
#         val=a[5:]
#         f2.write(val)  


# import os
# #os.remove('sample1.txt')


# # print(os.getcwd())
# # #os.chdir('H:/cls')  'H' nammude path alla
# # print(os.getcwd())
# # print(os.listdir())
# # #os.mkdir('biluu')
# # os.makedirs('A/a/b')

# os.system('dir')
# info=os.stat('result1.txt')
# print(info.st_size)
# print(info.st_mtime)

############################################################################################

# import csv
# with open('dataone.csv','r')as csv_file:
#     csv_reader=csv.reader(csv_file)
#     print(list(csv_reader))#chumma print csv_reader kodutha generator obj kanikum,,,athukond {list} idanam

# with open('dataone.csv','r')as csv_file:
#     csv_reader=csv.reader(csv_file)
#     for line in csv_reader:
#         print(line)

# with open('dataone.csv','r')as csv_file:
#     csv_reader=csv.reader(csv_file)
#     print(next(csv_reader))#one line at a time
#     print(next(csv_reader))
#     print(next(csv_reader))


# import csv
# with open('dataone.csv','r')as csv_file:
#      csv_reader=csv.reader(csv_file)
#      for line in csv_reader:
#          for it in line:
#              if '@' in it:      
#               print(it)


# import csv
# with open('dataone.csv','r')as csv_file:
#      csv_reader=csv.reader(csv_file)
#      with open('newdataone.csv','w')as new_file:
#          csv_writer=csv.writer(new_file)
#          csv_writer.writerows(csv_reader)
     
# import csv
# with open('dataone.csv','r')as csv_file:
#      csv_reader=csv.reader(csv_file)
#      with open('newdata3.csv','w')as new_file:
#          csv_writer=csv.writer(new_file)
#          for line in csv_reader:#list aayitt varum
#              del line[1]#index 1 is lastname
#              csv_writer.writerow(line)
     
# data=[
#     ['name','age','city'],
#     ['alice',25,'new york'],
#     ['bob',30,'los angeles']
# ]

# with open('new.csv','w') as f:
#     csv_writer=csv.writer(f)
#     csv_writer.writerows(data)

# with open('dataone.csv','r')as csv_file:
#      csv_reader=csv.DictReader(csv_file)   
#      for val in csv_reader:
#          print(val) 
# ls=[]
# with open('dataone.csv','r')as csv_file:
#      csv_reader=csv.DictReader(csv_file)   
#      for val in csv_reader:
#          ls.append(val['email'])
# print(val) 

# with open('dataone.csv','r')as csv_file:
#      csv_reader=csv.DictReader(csv_file)
#      fieldname=['fname','lname','email']  
#      with open('ddd.csv','w') as new:
#          csv_writer=csv.DictWriter(new,fieldnames=fieldname)
#          csv_writer.writeheader()
#          for val in csv_reader:
#              csv_writer.writerow(val)
          
     
# with open('dataone.csv','r')as csv_file:
#      csv_reader=csv.DictReader(csv_file)
#      fieldname=['fname','lname','email']  
#      with open('ddd.csv','w') as new:
#          csv_writer=csv.DictWriter(new,fieldnames=fieldname)
#          csv_writer.writeheader()
#          for val in csv_reader:
#              del val['email']
#              csv_writer.writerow(val)

##########################################################################
#JSON

# jdata='''
# {
#     'people':[
#         {
#         'name':'bilu',
#         'phone':345696544,
#         'email':bilu@gmail.com,
#         'has_license':true
#         },
#         {
#         'name':'frd',
#         'phone':2234355444,
#         'email':frd@gmail.com,
#         'has_license':false
#         }
#     ]


# }

# '''
#print(type(jdata))


import json as js  
# data=js.loads(jdata)
# print(data)
# print()


# for i in data['people']:
#     print(i['name'])

# data=js.loads(jdata)
# for i in data['people']:  
#     del val['email']
# newdata=js.dumps(data)
# print(newdata)

# with open('states.json','r')as f:
#     data=js.load(f)
#     print(data)
#     print(type(data))

# with open('states.json','r')as f:
#     data=js.load(f)
#     for i in data['states']:
#         print(i)

# with open('states.json','r')as f:
#     data=js.load(f)
#     with open('new_states.json','w') as new_file:
#         json_writer = js.dump(data,new_file,indent=5)

# with open('states.json','r')as f:
#     data=js.load(f)
#     for val in data['states']:
#         if val["name"] == "American Samoa":
#             val["name"] = "American Sam"
#     with open('new_states1.json','w') as new_file:
#         json_writer = js.dump(data,new_file,indent=2)

# with open('states.json','r')as f:
#     data=js.load(f)
#     for val in data['states']:
#         if val["name"] == "American Samoa":
#             data ['states'].remove(val)
#             break
#     with open('new_states2.json','w') as new_file:
#         json_writer = js.dump(data,new_file,indent=2)

# with open('states.json','r')as f:
#     data=js.load(f)
#     for val in data['states']:
#         del val['areacode']
#     with open('new_states3.json','w') as new_file:
#         json_writer = js.dump(data,new_file,indent=2)


import requests as rs

# data = rs.get("data=js.loads(jdata)
# for i in data['people']:  
#     del val['email']
# newdata=js.dumps(data)
# print(newdata)

# with open('states.json','r')as f:
#     data=js.load(f)
#     print(data)
#     print(type(data))

# with open('states.json','r')as f:
#     data=js.load(f)
#     for i in data['states']:
#         print(i)

# with open('states.json','r')as f:
#     data=js.load(f)
#     with open('new_states.json','w') as new_file:
#         json_writer = js.dump(data,new_file,indent=5)

# with open('states.json','r')as f:
#     data=js.load(f)
#     for val in data['states']:
#         if val["name"] == "American Samoa":
#             val["name"] = "American Sam"
#     with open('new_states1.json','w') as new_file:
#         json_writer = js.dump(data,new_file,indent=2)

# with open('states.json','r')as f:
#     data=js.load(f)
#     for val in data['states']:
#         if val["name"] == "American Samoa":
#             data ['states'].remove(val)
#             break
#     with open('new_states2.json','w') as new_file:
#         json_writer = js.dump(data,new_file,indent=2)

# with open('states.json','r')as f:
#     data=js.load(f)
#     for val in data['states']:
#         del val['areacode']
#     with open('new_states3.json','w') as new_file:
#         json_writer = js.dump(data,new_file,indent=2)


# import requests as rs

# data = rs.get("https://jsonplaceholder.typecode.com/todos")
# print(data.text)
# val = js.loads(data.text)
# with open('new_data.json','w') as f:
#     js.dump(val,f,indent=2)

###############################################################################################################

# XML OPERATIONS


import xml.etree.ElementTree as ET
# data='''<?xml version="1.0" encoding="UTF-8"?>
# <metadata>
# <food>
#     <item name="breafast">idily</item>
#     <price>$2.5</price>
#     <description>
#     two idyly's with chatney
#     </description>
#     <calories>553</calories> I
# </food>
# <food>
#     <item name="breafast">Dosha</item>
#     <price>$1.5</price>
#     <description>
#     Dosha with vada
#     </description>
#     <calories>700</calories>
# </food>
# </metadata>'''

# myroot =ET.fromstring(data)
# print(myroot.tag)
# # path location    in forward slash/

tree=ET.parse('C:/Users/alfre/OneDrive/Documents/pyy/eg2.xml')#file edukan
ET.dump(tree)#file read cheyam xml content read cheyn
root=tree.getroot()#roottag kittan vendi
# print(root)
# print(root.tag)
# print(root[0].tag)
# print(root[0][0].tag)

# for x in root[0]:
#     print(x.tag,x.attrib)
#     print(x.text)


# for x in root.findall('food'):
#     item=x.find('item').text
#     price=x.find('price').text
#     print(item,price)




# for x in root.iter('description'):
#     a=str(x.text)+'new description has been added'
#     x.text=str(a)
#     x.set('updated','yes')
# tree.write('new6.xml')  




# for x in root[0].iter('description'):
#     a=str(x.text)+'new description has been added'
#     x.text=str(a)
#     x.set('updated','yes')
# tree.write('new6.xml')  

# for x in root[0].iter('description'):
#     a=str(x.text)+'new description has been added'
#     x.text=str(a)
#     x.set('updated','yes')
# tree.write('new6.xml')  





# ET.SubElement(root,'speciality')#root[0]
# for x in root.iter('speciality'):
#     a='south indiam speciality'
#     x.text=a
# tree.write('new2.xml')


# root[0][0].attrib.pop('name')
# tree.write('new3.xml')

# root[0].remove(root[0][0])
# tree.write('new4.xml')

# root[0].clear()
# tree.write('news.xml')

for val in root.iter('food'):#subrootinn  akathtt
    ET.SubElement(val,'speciality')#root[0]
    for x in root.iter('speciality'):
        a='south indian speciality'
        x.text=a
tree.write('abc.xml')