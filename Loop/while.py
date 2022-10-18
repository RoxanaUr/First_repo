# WHILE - ciclu repetitiv in care nu stim exact nr de pasi, DAR stim ca avem o conditie de indeplinit
# while - cat timp
# while conditie:
#    fa ceva

i = 0
while i < 5:
    print(i)
    i += 1 # daca nu incrementam noi i-ul, programul va crash-ui pt ca bucla se va tot repeta

"""
In viata reala, vom folosi while atunci cand nu stim exact cat timp trebuie sa executam un cod,
dar avem o conditie de oprire. Exemple:
 - validarea unui input de la utilizator
 - validare user/parola
 - pentru a forta un nr maxim de incercari pt o anumita actiune
"""

age_is_correct = False
while not age_is_correct:
    age = int(input("Varsta dvs.:"))
    if 1 < age < 99:
        age_is_correct = True
    else:
        print("Varsta nu este corecta")


user, parola = "adela", "helloworld"
print("Nu sunteti logat, trebuie sa va logati")
nr_incercari = 0
nr_max_incercari = 3
while True:
    my_user = input("Introduceti username-ul dvs: \n")
    if user == my_user:
        my_password = input("Introduceti parola dvs:\n")
        if parola == my_password:
            print("Sunteti logat cu succes")
            break
        else:
            print("Parola gresita, incercati din nou")
    else:
        print("User inexistent")
    nr_incercari +=1
    print(f"Ai incercat sa te loghezi de {nr_incercari} ori")
