def great_user():
    print('Hello there')
    print('Welcome to my repo')
    
great_user()
# Hello there
# Welcome to my repo


def argument(first_name, last_name):
    print(f'Hello {first_name} {last_name}')
    
argument('Abbas', 'Moosavi')
# Hello Abbas Moosavi

def keyword_argument(first_name, last_name):
    print(f'Hello {first_name} {last_name}')
    
keyword_argument(last_name='Moosavi',first_name='Abbas')
# Hello Abbas Moosavi

try:    
    age = int(input('Age: '))
    print(age)
except ValueError:
    print('Invalid Error')
