import re
# substitute / replace something sub()

mystr = "Today I reached work at 10:00am , tomorrow I will reach at 11:00 am"
print(mystr)
res = re.sub("\s","***", mystr)
print("after substitution: ", res)

res = re.sub("\s","***", mystr, 2)  # only for first two blank spaces
print("only first two blank spaces: ", res)