#Declare a list of your friend's name [5 names]
names = ['John', 'Matt', 'Chris', 'Nelson', 'Jack']
print(names)
#add a new name to the end of the list
names.append('Lee')
print(names)
#add a new name to the beginning of the list
names.insert(0, 'Lerena')
print(names)
#display all names in Descending order
names.sort(reverse=True)
print(names)
#list with hyphen
print('-'.join(names))
#Find an itme in list
print(names.index('John'))
if 'John' in names:
    print('John is in the list')
else:
    print('John is not in the list')
