#create
a=(5,10.2,'hello')
print(a)
a=(20,)# tuple with single element.
print(a)
a=()
print(a)

#access/read - with the help of indexing
a=(5,10.2,'hello')
print(a[2])
print(a[0:2]) # range

#Update- We can't update tuple as it is immutable, however, updation can be done with the help of concatination & typecasting
#delete
a=(5,10.2,'hello')
del a # removing an item or deleting an item is not possible, we can only delete entire tuple.