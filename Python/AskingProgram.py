print "asking program by Benjamin Frost."

print ""
print ""

print "when you have answered a question, press enter to continue."

print ""

firstname = raw_input ("What is you frist name? ") #asks for the users first name
lastname = raw_input ("What is you last name? ") #asks for the users last name
birth = raw_input ("which year were you born? ") #aks for the year the user is born
home = raw_input ("were do you live? ") #asks the user were he or she lives
kids = raw_input ("how many kids do you have? ") #asks the user how many kids he or she have

age = 2014 - int(birth)
age2 = age - 1 # those two lines finds the age of the user

grandkids = kids
grandkids2 = int(kids) * 2 #those two lines finds the possible amout of grandkids the user will have or have

print ""

print "Hi", firstname, lastname, "you are between", age2, "and", age, "years old."
print "you live in", home, "and have", kids, "kid(s)."
print "which means you possibly is going to have", grandkids, "to", grandkids2, "grandkids."

print ""

raw_input ("press enter to exit the program.")
