#This archive will be used to put introducion conceptions from python development

print(int(1), type(int('1')))
print(type(float('1') + 1))
print(float('1') + 1)
print(bool(''))

complete_name = 'Felipe Milk Leche'
age = 25
weight = 79.5

print("{} tem {} anos e pesa {}kg".format(complete_name, age, weight)) #A way to print that informations above

a_ten_times = 'A' * 10
print(a_ten_times)

#Using the function input to collect datas from the user

name = input('What is your name? ')
print('Your name is {}'.format(name))

#Understanding IF, ELIF and ELSE

age = input("Scan your age: ")

if int(age) >= 18 and name != '':
    print('You are an Adault')
else :
    print('You are not an Adault')

#Using operators In and Not In

print('P' in name or 'p' in name)
print('W' not in name)


try:
    print('Testing try ', name)
    name_to_int = int(name)
    print(name_to_int)
    ...
except:
    print('name can not be converted to a number')
    ...

CONSTANT_VARIABLE = 1 #This is how to create a constant on python