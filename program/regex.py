text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
cat
pat
mat
bat
'''




# import re
# pattern=re.compile(r'abc')
# matches=pattern.finditer(text_to_search)
# for i in matches:
#     print(i)


# import re
# pattern=re.compile(r'\.') #dot
# matches=pattern.finditer(text_to_search)
# for i in matches:
#     print(i)    

# import re
# pattern=re.compile(r'coreyms.com')
# matches=pattern.finditer(text_to_search)
# for i in matches:
#     print(i) 

# # - Any Character Except New Line
# #   \d      - Digit (0-9)
# #   \D      - Not a Digit (0-9)
# #   \w      - Word Character (a-z, A-Z, 0-9, _)
# #   \W      - Not a Word Character
# #   \s      - Whitespace (space, tab, newline)
# #   \S      - Not Whitespace (space, tab, newline)
   
# #   Anchors:
# # \b      - Word Boundary
# # \B      - Not a Word Boundary
# # ^       - Beginning of a String
# # $       - End of a String

 
# # character set
# #   []      - Matches Characters in brackets
# #   [^ ]    - Matches Characters NOT in brackets
# #    |       - Either Or
# #   ( )     - Group

# #   Quantifiers:
# #   *       - 0 or More
# #   +       - 1 or More
# #   ?       - 0 or One
# #   {3}     - Exact Number
# #   {3,4}   - Range of Numbers (Minimum, Maximum)


# # #  ### Sample Regexs ####

# # #   [a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+       

# import re
# pattern=re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
# matches=pattern.finditer(text_to_search)
# for i in matches:
#     print(i) 

# import re
# pattern=re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d')
# matches=pattern.finditer(text_to_search)
# for i in matches:
#     print(i) 

import re
pattern=re.compile(r'[89]00 -\d{3} -\d{3} -\d{4}')
matches=pattern.finditer(text_to_search)
for i in matches:
    print(i) 

# # import re
# # pattern=re.compile(r'[^b]at')
# # matches=pattern.finditer(text_to_search)
# # for i in matches:
# #     print(i) 

# import re
# pattern=re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')
# matches=pattern.finditer(text_to_search)
# for i in matches:
#     print(i) 

# emails='''
# miketyson@gmail.com
# henry.cavill@university.edu
# jason-321-statham@my-work.net
# '''
# import re
# pattern=re.compile(r'[@]$.com$.edu$.net')
# matches=pattern.finditer(emails)
# for i in matches:
#     print(i)

['x','xx','xxx','xxxx']
print(list(map(lambda x:x*'x',range(1,6))))

from functools import reduce
ls=['hello','python','is','nice']#hello python is nice
print(reduce(lambda x,y:x+' '+y,ls))

num=[1,2,3,4,5,6,7,8,9]
result=list(map(lambda x:x*2,filter(lambda x:x%2 !=0,num)))
print(result)

lst=[[1,2],[3,4],[5,6]]#[1,2,3,4,5,6]
print((reduce(lambda x,y:x+y,lst)))

print(','.join([str(i) for i in range(2000,3201)if i%7==0 and i%5!=0]))

