"""
Exceptii:
clase speciale Python folosite at cand ceva nu merge bine in cod
Folosim mecanismul try-except pt a gestiona posibilele exceptii aparute
in cod, astfel incat programul sa NU se opreasca.

try:
    incercam ceva aici
    care s-ar putea sa dea exceptie
excepti NumeExceptie as e:
    aici gestionam exceptia cum consideram noi
"""

l = [1, 2, 3, 4]
print(l[0])
# daca as decomenta codul de mai jos, codul s ar opri cu eroare
# print(l[220])
try:
    print(l[5])
except IndexError as e:
    print("Am dat de o eroare de tipul IndexError")

"""
Unde am putea folosi try-except:
- input de la utilizator
(verificam daca am primit ce asteptam noi)
"""
# try:
#     varsta = int(input("Introduceti varsta:\n"))
#     print(f"Ati introdus {varsta}")
# except ValueError as e:
#     print("Nu ati introdus un numar.")
#
# print("La revedere")

"""
Reguli pt prinderea exceptiilor:
- avem mereu un singur try, dar putem avea mai multe exept
- daca avem mai multe exceptii posibile, trebuie sa le punem de la
cea mai specifica la cea mai generica
- la final, putem avea inclusiv un except "gol", care sa
prinda un except la care nu ne-am gandit noi
"""
try:
    nr_par = int(input(f"Introduceti un numar par:\n"))
    assert nr_par % 2 == 0
except ValueError as e: # as e, ii dam un nume variabilei
    print("Nu ati introdus un numar.")
except AssertionError as e:
    print("Numarul nu este par!")
except:
    # in general nu vrem sa facem asa, sa nu specificam exceptia pe care o prindem
    print("A aparut alta exceptie, nu stim care..")

print("Am terminat.")