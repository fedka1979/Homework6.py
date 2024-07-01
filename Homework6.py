my_dict = {'Andrey': 1979, 'Kate': 1986, 'Sofya': 2005, 'Polina': 2013}
print(my_dict)
print(my_dict['Andrey'])
print(my_dict.get('Kolya'))
my_dict.update({'Kolya': 2005,
                'Darya': 2013})
print(my_dict)
a = my_dict.pop('Darya')
print(my_dict)
print(a)
my_set = {1979, 1986, 2005, 2013, 2005, 2013}
print(my_set)
my_set.add('Kolya')
my_set.add(5)
print(my_set)
my_set.discard('Kolya')
print(my_set)
