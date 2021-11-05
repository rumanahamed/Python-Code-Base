#create
a= [20,'hello',1.12,60,'leave','college',28]
a1 = [20,'hello',['boy',25,44.5]]  # nested List

# Read/Access - It can be done by the help of indexing
print(a[0])
print(a[1:2])
print(a[1:6:2])

#update
a[0] = 'Sunny'
print(a)
a[1:3]= [30,'marry']
print(a)
a[1:2]= ['me','december'] #in case more items are added w.r.t index then it will insert the item.
print(a)

#delete
del a[2] #delete single element corresponding to index no.
print(a)
del a[1:3] #delete multiple element corresponding to given range
print(a)
del a #delete entire list
