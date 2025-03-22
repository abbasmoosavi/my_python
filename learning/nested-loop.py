for x in range(4):
    for y in range(3):
        print(f'({x},{y})')
# (0,0)
# (0,1)
# (0,2)
# (1,0)
# (1,1)
# (1,2)
# (2,0)
# (2,1)
# (2,2)
# (3,0)
# (3,1)
# (3,2)

numbers = [5,2,5,2,2]
for x in numbers:
    print('*'*x)
# *****
# **
# *****
# **
# **
for x_count in numbers:
    output= ''
    for count in range(x_count):
        output += 'X'
    print(output)
# XXXXX
# XX
# XXXXX
# XX
# XX