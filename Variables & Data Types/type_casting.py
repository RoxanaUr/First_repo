# Aceste 2 variabile sunt de tipul string
row1 = "42"
row2 = "True"

print(type(row1)) # va afisa <class 'str'>, adica row1 este string
print(type(row2))

# Type Casting - fortam conversia unei variabile de la un tip la altul
# row1 - il convertim de la str la int (se poate si la float)

my_int = int(row1)
# my_int este creat din valoarea pe care o avea row1, DAR row1 nu se modifica si nici nu isi modifica tipul
print(row1, type(row1))  # 42 <class 'str'>
print(my_int, type(my_int))  # 42 <class 'int'>

row1 = int(row1) # Acum am modificat row1, prin suprascriere (este acum int)

my_bool = bool(row2)
print(row2, type(row2))
print(my_bool, type(my_bool))

# Str -> float
row3 = "42"
my_float = float(row3)
print(row3, type(row3))
print(my_float, type(my_float))

# Int -> float
another_float = float(my_int)
print(another_float, type(another_float))

# Toate variabilele se pot converti in string
my_string = str(another_float)
print(my_string, type(my_string))

# Int -> bool
real = bool(5) # orice val dif de 0 este considerata adevarata
not_real = bool(0)
print(real, type(real))
print(not_real, type (not_real))

#-------------------------
# If you want to specify the data type of a variable, this can be done with casting.
# Example
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

# Get the Type
# You can get the data type of a variable with the type() function.
# Example
x = 5
y = "John"
print(type(x))
print(type(y))
