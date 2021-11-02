#Creat
a = {'name':'Ruman','Age':25,'Address':'Delhi'}

#Access/Read
print(a['name'])
print(a['Address'])

#accessing by get() method
print(a.get('name'))

#accessing all the key by using key
print(a.keys())

#accessing all the values by using value
print(a.values())

#accessing all the items by using item function
b = a.items()
print(b)

#Update - the value of specific item can be changed by referring to its key name.

a['name'] = 'Kamran'
print(a)

a['location'] = 'UP' #if key will not present, then it will add the key along with its value.
print(a)

#update method - will update existing list
a.update({'name':'sajan'})
print(a)

#remove/delete

#1.popitem method - it removes last inserted item
a.popitem()
print(a)
del a['Address']  #del method
print(a)

# #clear method - it will delete all item
# a.clear()
# print(a)

#copy
a.copy()
print(a)

#fromkeys() - method
a.fromkeys('name')
print(a)




