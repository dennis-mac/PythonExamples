
import array
import numpy

my_array = array.array('i', [1,3,5,7,9,2,4,6,8,10])
print(my_array)
print(type(my_array))

# sort array using numpy
my_array= numpy.sort(my_array)
print(type(my_array))


# convert back to regular array
my_array = array.array('i',my_array.tolist())

print(my_array)
print(type(my_array))

