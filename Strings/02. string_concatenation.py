#concatenation means combining things
# Suppose I write: name = "ram Krishan pathak"
# But in email that say "Mr. first_name" wouldn't know what is first name
# So we must break down
first_name = "Ram"
middle_name = "Krishan"
last_name = "Pathak"

#now if email says "Hello first_name", then first name is known aand this is where concatenation comes in:
print("Hello " + first_name)

#Or (leave space after Hi or Dear)
print("Dear " + last_name)

# if i write the following, I will face space problem
print(first_name + middle_name + last_name)

#to avoid this spacing problem, use a blank quote
print(first_name + " " + middle_name + " "+ last_name)