# Exercise chapter 4, p.64

counting = list(range(1, 21))
print(counting)

print(max(counting))

# when one wants to create a list using the list() FUNCTION, do NOT use the
# brackets when defining the list (i.e. after 'numbers = ___').

numbers = list(range(1, 16))
print(numbers)
print(min(numbers))
print(max(numbers))
print(sum(numbers))

oddnumbers = list(range(1, 21, 2))
print(oddnumbers)

three_multiples = []
for value in range(3, 31, 3):
    three_multiples.append(value)

# Translation of above operation
# ln.21: For each value in range(3, 31, 3):
# ln.22: add each of the value to the list 'three_multiples'

print(three_multiples)

two_multiples = [value for value in range(2, 21, 2)]
print(two_multiples)

# Below: How to create and print a list of numbers in range 1-10 to the power
# of three.

# 1st method (list comprehension method)
cubes = [value**3 for value in range(1, 11)]
print(cubes)

# 2nd method
cubes2 = []
for value in range(1, 11):
    cubes2.append(value**3)

print(cubes2)

# 3rd method
cubes3 = []
for value in range(1, 11):
    value = value**3
    cubes3.append(value)

print(cubes3)
