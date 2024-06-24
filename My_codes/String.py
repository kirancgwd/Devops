

#String example
'''
my_str="python"
my_str1="example"
my_str2 = my_str+" "+my_str1
print(my_str2)
'''

#Case converion operations on string
#print(dir(my_str2))   #gives possible operations for string

'''
my_str2="Python Example"
print(my_str2.upper())
print(my_str2.lower())
print(my_str2.title())
'''

#Boolean string operations- which give true or false

'''
my_str="kiran tutorial"
print(my_str.islower()) #Gives True bcs all are in lowercase
print(my_str.isupper()) #Give Fals bcs all string nit in uppercase
print(my_str.isspace()) #Gives False bcs along with space strings are there
'''

#Join , Center and Zfull(padding) String operations

y  = '+'.join('helll')
z = "testing_python"
print(y)
print("\n".join(y))
print("\t".join(y)) #Join
print(f"{y.center(20)}\n{z.center(20)}") #center
print(z.zfill(20))  #padding


