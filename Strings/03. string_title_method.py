#suppose a user fills name in website  in small letters
first_name = 'ram'
last_name = 'pathak'

#to capitalize the first letter we do following
print(first_name.title())

#this (.title()) is called a "method" in python. A method is an action that python can perform in a piece of data. 
# Every method is followed by a set of brackets. More info can be inserted inside the brackets.
# Here we used .title() method to manipulate variables.
# More eg.
print(first_name.title() + " " + last_name.title())
print(last_name.title())