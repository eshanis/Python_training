"""
REGULAR EXPRESSIONS:
=> pattern matching
#META CHARACTERS
\ Used to drop special meaning of characters following it

[] matched the characters given within the []

[^] matches characters except which is give within the []

^ Matches beginning of string

$ matches end of string

. matches any character except newline

? matches zero or one occurrence

| mean OR (matches any of the characters separated by pipe symbol)

* any number of occurrences

+ One or more occurrence

{} indicates the number of occurrences of a preceding RE to match

{n} exact n number

{n,m} n - min  m-max  (range)

() Enclose a group of regular expressions

\d matches any decimal digits, this is equivalent to the set class [0-9]

\D matches any non-digit character

\s  matches any whitespace character

\S matches any non-white space character

\w matches any alphanumeric character thi sis equivalent to the class [a-zA-Z0-9]

\W matches any non alpha numeric character

\b matches any word with the boundary (space before or it's the starting)

\B matches any word without boundary

[0-9]  matches any number

[^0-9] matches any other than number between 0-9

[a-z] matches any lower case character

[A-Z] matches any upper case alphabet

"""

# match()   #used only for one word not a string

import re

mystr = "Python"

# compile pattern on top of string then use match() function
# compile()
# match()

pattern = re.compile(
	"P\w*")  # starts with P then an alphanumeric value but * indicates any number of alphanumeric values
res = pattern.match(mystr)

print(res)
print(res.group())

print("============ alternate way to match pattern =========================")
mystr2 = "Python2"

res2=re.match("P\w*" ,mystr2)

print(res2)
print(res2.group())

#will not work of you give a middle character to macth like "t" since this starts looking from the beginning
#res2=re.match("t\w*" ,mystr2)

# will not work for a string either
#mystr2 = "I love Python2"

print("=========== SPLIT METHOD split() ====================")

mystr3 = "This is my 4 Python2 class3"
print(re.split("\s",mystr3)) #gives list as output ,splits on white space
print(re.split("\d",mystr3)) #gives list as output splits on digit

print("========= findall() ================")
mystr4 = "This is my Python class. All the best! Thank you for attending!!"

print(re.findall("th", mystr4)) # find all occurrences of "th"
print(re.findall("th" , mystr4, re.I))  # ignores case

var = "hello 123 !@#$%^"
print(re.findall("\w", var))  # 3 to find only alphanumeric character
print(re.findall("[a-zA-Z0-9]", var)) # same results as above
print(re.findall("\w+", var)) # the + helps find the whole word instead of each character
print(re.findall("\w*", var)) # doesn't work
print(re.findall("\W", var)) # non alphanumeric characaters
print(re.findall("\D", var))  # non digit characters

print("++++++++++++++++++++")
var2 = "Today I reached work at 10:00am , tomorrow I will reach at 11:00 am"
print(re.findall("\d", var2))
print(re.findall("[0-9]", var2))
print(re.findall("\d+", var2)) # the + helps find the whole word instead of each character

print("======================================")