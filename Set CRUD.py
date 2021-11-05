#create
a = {'hello',20,1.22,'sunny','money'}
#a = set() #empty set

#read/access
for i in a:
    print(i)
#update
#we can't change its item,but we can add new items

#add method
a.add('lol')
print(a)

#update method - it take only iterable object only
a1 = {1,2}
a.update(a1)
print(a)

# delete - remove(),discared(),pop(),clear(),del




