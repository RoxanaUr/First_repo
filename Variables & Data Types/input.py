# Input este functia cu care preluam date de la utilizator (de la tastatura)
nume = input("Introdu numele:\n")

# \n - newline, adica ducem cursorul pe urmatoarea linie, ca sa arate frumos

print(f"Salut, {nume}")

# By default, ce primim noi de la input este INTOTDEAUNA string

varsta = input("Cati ani ai?\n")
print(type(varsta))

# Daca dorim alte tipuri de date, trebuie sa facem type casting
varsta = int(varsta)
print(type(varsta))

# Exercitiu cu assert si input : cod captcha
rezultat_captcha = int(input("Cat este 12 + 21?\n"))
assert rezultat_captcha == 33, "Nu esti om, esti robot"

x,y = 5, 17
rezultat_captcha2 = int(input(f"Cat este {x} + {y}?\n"))
assert rezultat_captcha2 == x + y, "Nu esti pregatit destul"