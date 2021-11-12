x = {1:'hello',2:'hi',3:'bye'}
print(x,type(x))
result = {z:y.upper() for z,y in x.items()}
print(result)