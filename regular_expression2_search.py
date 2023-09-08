# SEARCH FUNCTION IN REGEX
#search()
import re

var3 = "Today I reached work at 10:00am , tomorrow I will reach AT 11:00 am"

res= re.search("\s", var3)   # first occurrence of "blank space"
print("first occurrence of white space: ", res.start())

res= re.search("\d", var3)   # first occurrence of "digit"
print("first occurrence of digit: ", res.start())

res= re.search("I", var3)   # all occurance of "I"
print("first occurrence of I: ", res.start())

res= re.search("at", var3, re.I)   # first occurance of at
print("case insensitive search for 'at': ", res.start())
print(res.end())
print(res.span())

res= re.search("AT", var3, re.I)   # first occurance of at even though upper case search
print("case insensitive search for 'AT': ", res.start())
print(res.end())
print(res.span())

res= re.search("AT", var3)   # first occurance of at
print("case sensitive search for 'AT': ", res.start())
print(res.end())
print(res.span())

res2= re.findall("at", var3, re.I)   # all occurance of at
print("using findall: ", res2)