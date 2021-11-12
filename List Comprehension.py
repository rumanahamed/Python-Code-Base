x = ['hello','hi','bye']

result = [y.upper() for y in x]
print(result)

result2 = [y.upper() for y in x if y=='hi']
print(result2)
