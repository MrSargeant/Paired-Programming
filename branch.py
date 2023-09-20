#create a program that creates and @elizabethan email from the first name, last name and year they joined

firstname = input("What is your firstname?")
lastname = input("What is your lastname?")
year = input("What year did you join?")


email = year[2:5]+lastname+firstname[0:1]+"@elizabethan.notts.sch.uk"

print("your email is:" email)

print("This is going to be a conflict!")