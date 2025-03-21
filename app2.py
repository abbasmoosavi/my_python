import math

print(10//3)
# 3

print(round(2.9))
# 3

print(math.ceil(4.6))
# 5

print(math.floor(4.6))
# 4

is_hot = False
is_cold = True
if is_hot:
    print("It's a hot day")
elif is_cold:
    print("It's a cold day")
else:
    print("It's a undefined day")
    
weight = int(input('Weight: '))
unit= input('(L)bs or (K)g: ')
if(unit.upper() == 'L'):
    converted = weight * 0.45
    print(f'You are {converted} kilos')
else:
    converted = weight / 0.45
    print(f'You are {converted} pounds')
# Weight: 82
# (L)bs or (K)g: k
# You are 182.22222222222223 pounds

i = 1
while i<=5:
    i+=1
    print(i)
print('done')
# 2
# 3
# 4
# 5
# 6
# done

i = 1
while i<=5:
    print('*' * i)
    i+=1
# *
# **
# ***
# ****
# *****

secret_number = 5
i=0
while i<= 3:
    guess = int(input('Guess: '))
    if guess == secret_number:
        print('You Win!')
        break
    else:
        i += 1