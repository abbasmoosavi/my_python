print("Abbas Moosavi")

price = 10
print(price)

name= input('Please enter your name:')
print('Hi, '+name)

birth_year = input('Enter your birthdate year:')

age = 2025 - int(birth_year)
print('You are '+str(age)+ ' years old.')

course = 'Python for Begginers'
print(course[2:])
# thon for Begginers

course = 'Python for Begginers'
print(course[:5])
# Pytho

another = course[:]
print(another)
# Python for Begginers

print(another[1:-1])
# ython for Begginer

message= f'{name} [{price}] is {age} old!'
print(message)
# Abbas [10] is 32 old!

print(len(course))
# 20

print(course.upper())
# PYTHON FOR BEGGINERS

print('Python' in course)
# True