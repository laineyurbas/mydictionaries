import random

# dicts have curly brackets and key value pairs. key on left (string)
# value on left, value is on the right
# python = objected oriented language - attributes and methods
# json file = way for ppl to exhange info online
""""""
phonebook = {}  # creates an empty dic

phonebook = {'Chris': '555−1111',
             'Katie': '555−2222',
             'Joanne': '555−3333'}
""""""
""""""
# creates a dic w hard coded values
# key = names, value = phone numbers, so 3 key value pairs

'''''
print()
print('*****  start section 1 - print dictionary ********')
print()

mydictionary = dict(m=8, n=9)
print(mydictionary)
# print number of elements in dic use len function
print(len(phonebook))
print(type(phonebook))  # type tells you what type it is - this is a Dict


print()
print('*****  end section 1 ********')
print()
'''
'''
phone = (phonebook['Chris'])
print(phone)  # value is returned #key error = didnt find a match

 ###idk where to add the quotes
print()
print('*****  start section 2 - search dictionary ********')
print()
name = 'Chris'
if name in phonebook:
    print(phonebook[name])
else:
    print(f"{name} is not in the phonebook")







print()
print('*****  end section 2 ********')
'''''
''''''
# print()
''''''


''''


print()
'''''
'''''
print('*****  start section 3 - edit/append dictionary ********')
print()

print(phonebook)
phonebook['Chris'] = '555-0123'
phonebook['Joe'] = '555-4444'  # keys in dicts have to be unique

print(phonebook)


print()
print('*****  end section 3 ********')
print()


print()
'''''
'''''
print('*****  start section 4 - delete/remove from dictionary ********')
print()
print(phonebook)
del phonebook['Chris']
print(phonebook)

print()
print('*****  end section 4 ********')
'''''
'''''
print()


print()
'''''
'''''
print('*****  start section 5 - iterate through keys, values, items ********')
print()

for key in phonebook: ##key = list, it does not matter what you use for list as long as youre consistent
    print(f"the key is {key} and the value is {phonebook[key]}")

for value in phonebook.values():
    print(value)

for k,v in phonebook.items():
    print(f"the key is {key} and the value is {value}")

for ph_tuple in phonebook.items():
    print(ph_tuple)


print()
print('*****  end section 5 ********')
print()
for key in phonebook:
    print(key)
'''
# print()
'''''
print('*****  start section 6 - using get and clear ********')
print()

# looking for chris, if no match is found it print 999
phone = phonebook.get('Chris', '999')
print(phone)

phonebook.clear
print(phonebook)

print()
print('*****  end section 6 ********')
'''''


"""""
print()
print('*****  start section 7 - using pop method ********')
print()
remove = phonebook.pop("Chris", "not found")
print(remove)
print(phonebook)

"""""
# print()
# print('*****  end section 7 ********')

""
"""""
print()
print('*****  start section 8 - using popitem ********')
print()

a = phonebook.popitem
print(a)
print(phonebook)

print()
print('*****  end section 8 ********')
print()
"""""

print()
print('*****  start section 9 - using random and converting to list ********')
print()

phonebook_list = list(phonebook)
print(phonebook_list)
random_key = random.choice(phonebook_list)  # works only w lists
print(random_key)
print(phonebook[random_key])

# how you can print that w not defining a ton of vars
print(phonebook[random.choice(list(phonebook))])

print()
print('*****  end section 9 ********')
print()
