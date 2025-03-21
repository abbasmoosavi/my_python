customer = {
    "name" : "Abbas Moosavi",
    "age" : 32,
    "male" : True
}
print(customer)
print(customer["name"])
# {'name': 'Abbas Moosavi', 'age': 32, 'male': True}
# Abbas Moosavi

print(customer.get('birthdate'))
# None

customer['birthdate'] = '30 Jun 1993'
print(customer.get('birthdate'))
# 30 Jun 1993

phone = input('Phone: ')
output = ''
digits_mapping = {
    "0" : "Zero",
    "1" : "One",
    "2" : "Two",
    "3" : "Three",
    "4" : "Four",
    "5" : "Five",
    "6" : "Six",
    "7" : "Seven",
    "8" : "Eight",
}

for number in phone:
    output += digits_mapping.get(number, '!') + ' '
print(output)
# Phone: 09306373499
# Zero ! Three Zero Six Three Seven Three Four ! ! 