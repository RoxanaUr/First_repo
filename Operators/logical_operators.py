# Avem 3 operatori logici (functioneaza doar pe variabila boolean): and, or, not
# And - conditie de SI: x and y -> atat x, cat si y trebuie sa fie adevarat
are_permis = True
e_major = True

# AND - ambele conditii tr sa fie adevarate pt ca rezultatul sa fie adevarat
assert are_permis and e_major, "Nu ai voie sa conduci o masina"

nota1, nota2, nota3 = 7, 3, 8
assert nota1 > 4 and nota2 > 4 and nota3 > 4, "Ai picat"


# OR - x sau y: adevarat daca cel putin una dintre conditiile x sau y este adevarata
assert nota1 > 4 or nota2 > 4 or nota3 < 4, "Nu ai trecut la nici un examen"


# NOT - operatorul de negare: transforma True in False si viceversa
major = varsta > 18
print(major)
print(not major)