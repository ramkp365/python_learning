# The find method in Python is a string method that is used to locate a particular sub-string within a given string. 
# Its purpose is to return the position of the first occurrence of the sub-string in the string. 
# If the sub-string is not found, the find method returns -1.
# python starts counting from 0
What_is_your_name = "My name is Ram".find('Ram')
print(What_is_your_name)

#Here, python returned number 11 and not "My name is Ram" because .find() string method is being used.
#Starting  position of R in Ram is 11, if we start from M with 0. So, 11 is returned.
# More eg
What_is_your_name = "My name is Ram".find('name')
print(What_is_your_name)