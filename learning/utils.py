def find_max(numbers):
    max=0
    for number in numbers:
        if(number>max):
            max = number
    print(f'Max is = {max}')