a=3
print(a ** 3)
#presidence of operators
print(5+8-2)
print(5-8+2)
#String manipulation
str1="welcome"
print(len(str1)) # to find the length of string
print(str1[2]) # to print the index value of string
a=1234
c=str(a) # to store the value of a is int to string
print(type(c)) # to print the type of c( int or string or boolen)
#operations in string #find
print(str1.find("l")) # to find the index of "l"
print(str1.find("a"))
print(str1.upper()) # it will print the string in uppercase
print(str1)
print(str1.count("e")) # to count how many of "e" is there
print(str1.isupper()) # to check the srting is uppercase if yes it will print true else false
str2=" hello "
print(str2)
print(str2.strip()) #removing space
x=" coimbatore "
print(x.replace("o","a").upper()) #replace and uppercase - 2 operations in same line
print(x.lstrip()) #left side space remove
print(x.rstrip()) #right side space remove
#split operation
x1="You can use multiple programming languages like Java, C#, Python, etc to create Selenium Test Scripts"
print(x1.split())
print(x1.split("etc"))
x2="sathish\" kumar" #\" escape character (escape the logic)
print(x2)
x3='''
Selenium Software is not just a single tool
'''
print(x3)
print('not' in x3)
print(x3[::-1])
print(x3.capitalize())