# O variabila este o un container din memorie care stocheaza valori

""" EN:
Variables are containers for storing data values.

A variable is a symbolic name that is a reference or pointer to an object.
Once an object is assigned to a variable, you can refer to the object by that name.
But the data itself is still contained within the object.
"""


# snake_case - stilul in care se denumesc variabilele in Python (litere mici si underscore)
first_variable = 1

# Numele de variabile pot contine doar litere mari, mici, numere si underscore
# Numele trebuie sa fie unice, valorile se pot repeta
var1 = 5
var_1 = 100
VAR_ = 10
_var = "x"

# Numele de variabile nu pot incepe cu cifra

# Atribuire multipla
x, y, z = 10, 12, 15   # echivalent cu x = 10; y = 12; z = 15
a = b = c = 10

# Numele de variabile trebuie sa aiba SENS
a = 31
age = 31

# Variabile sunt case sensitive (myvar=3 e diferita de myVar=5)
# Var pot sa isi schimbe valoarea pe parcurs (suprascriere); si chiar si tipul de date



# ---------------------------------------------
# Unpack a Collection
# If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.
# Example
# Unpack a list:

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#--------------------------------------------

# SLICING SI INDEXARE PE STRINGURI


nume = "Adela"
print(len(nume))
print(nume[2]) # va afisa "e", al 3lea caracter din sir
# A d e l a
# 0 1 2 3 4
print(nume[1:3]) # va printa "de"
# str[star:stop:pas] pas e in mod implicit 1

# len(nume) va fi 5, deci slincing-ul nostru va lua in cons si ultimul char
print(nume[0:len(nume):2]) # va printa Aea
print(nume[_:len(nume:2)])
print(nume[0: :2])
print(nume[ : :2])
# Cele 4 instructiuni sunt echivalente, deoarece in slicing pute omite capetele

# Putem avea si valori negative la indexare/ slicing
print(nume[-1]) # nume[len(nume)-1] -> a
print(nume[-2]) # l
print(nume[-3]) # e

print(nume[::-1]) # stringul inversat

#--------------------------------------------

# METODE PE STRING

s = "Coral is either the stupidest animal or the smartest rock. How are you?"
d = "1234"
print(s.isdigit()) # False
print(d.isdigit()) # True

print(s.split("the")) # scoate the din text de 3 ori, si imparte ce e st si dr in stringuri separate
print(s.split(".")) # scoate ce urmeaza dupa punct

s.count(s)
print(f"Cuvantul 'the' apare de {s.count(' the ')}")

print(s.index('the')) # va afisa indexul la care gaseste prima data substringul the

print(s.upper()) # uppercase
print(s.lower()) # lowercase

print(s.replace("the", "***""))
# va inlocui the cu *** peste tot in stringul s

print(s.partition(".")) # spre deosebire de split, va returna si caracterul lipsa