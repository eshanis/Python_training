import re
mystring = "This is my email ID:, Techie@shah.com"  # word @ word .word

result=re.search("\w+@\w+\.\w+", mystring)          #\w+     \w+     \w+
print(result)
print(result.group())

print("========== splitting the search ==================")
mystring2 = "This is my email ID:, Techie@shah.com"  # word @ word .word

result2=re.search("(\w+)@(\w+)\.(\w+)", mystring2)
print(result2)
print("UserName: ", result2.group(1))
print("Domain: ", result2.group(2))
print("extension: ", result2.group(3))