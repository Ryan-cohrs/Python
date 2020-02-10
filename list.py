info = input("Please enter your name, age, and job title:  ")
data = info.split()
name = data[0]
age = data[1]
job = data[2]
print("You're name is " + name + " and you are " + age + " years old and you work as an " + job + ".")