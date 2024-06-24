#String concatenation means add strings together. Use the + character to add a variable to another variable

'''str1 = "Hello"
str2 = "Kiran"
result = str1 + " " + str2
print(result)'''

#The len() function returns the number of items in an object
'''text = "Python is awesome"
length = len(text)
print("Length of the string:", length)'''

#The lower() and upper() --- method returns a string where all characters are lower & upper case.
'''text = "Kiran is Awesome"
uppercase = text.upper()
lowercase = text.lower()
print(uppercase)
print("lowercase lettter are:", lowercase)'''

#Replace the text 
'''text = "Kiran is awesome"
NewText = text.replace("awesome", "Great")
print("Replaced tex is :", NewText)'''


#Split function - split words in to seperate 
'''Text = "Kiran is awesome"
splitword = Text.split()
print(splitword)'''

#The strip() method removes any leading, and trailing whitespaces.
# Leading means at the beginning of the string, trailing means at the end.

''''text = "Some spaces around   "
stripped_text = text.strip()
print("Stripped text:", stripped_text)'''

#Searh text in string
'''text = "Python is awesome"
substring = "k"
if substring in text:
    print(substring, "found in the text")
else:
    print("Not found")'''


# Float variables
'''num1 = 5.0
num2 = 2.3

# Basic Arithmetic
result1 = num1 + num2
print("Addition:", result1)

result2 = num1 - num2
print("Subtraction:", result2)

result3 = num1 * num2
print("Multiplication:", result3)

result4 = num1 / num2
print("Division:", result4)

# Rounding
result5 = round(result4, 2)  # Rounds to 2 decimal places
print("Rounded:", result5)'''

import re

text = "The quick brown fox"
pattern = "brown"

search = re.search(pattern, text)
if search:
    print("Pattern found:", search.group())
else:
    print("Pattern not found")




