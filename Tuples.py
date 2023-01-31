tuple1 = (1, 2, "hello")  # if 1 element will not be tuple
## to make it tuple with 1 element (1,) , needs to be put in end of element
tuple2 = True, 1
### print elements in tuple with for and while
print(tuple1)
for i in tuple1:
    print(i, end=" ")
# (*) (+) (in) for and len operators for tuples
print(tuple1 * 2)  # Prints tuple elements 2 times
print(tuple1 + tuple2)  # prints single tuple with elements from tuple1 and 2
# in is to search value in tuple
print(2 in tuple1)
# for to cycle values in tuple
for i in tuple1:
    print(i, end=" ")
print()
# frozenset
fset = frozenset([1, 2, 3, 4])
print(fset)
