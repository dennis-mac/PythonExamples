import array

# remove duplicates from an array and preserve order
myarray = array.array('i', [5, 1, 2, 3, 1, 4, 5, 3])
print(type(myarray))

unique = list(dict.fromkeys(myarray))
print(unique)  

myarray = array.array('i', unique)

print(type(myarray))