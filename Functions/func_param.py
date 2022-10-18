"""
Parametrii (input-datele de intrare in functie)
sunt niste nume pe care noi le folosim pt variabilele pe care le putem
transmite functiei

"""

def say_hello_to(nume):
    print(f"Hello, eu sunt functia!")
    print(f"Tu esti {nume}")

say_hello_to("Marcela")
say_hello_to("Floarian")
say_hello_to("Mihai")

def say_goodbye(nume, varsta):
    print(f"Salut, {nume} care ai {varsta} ani!")
    print("Goodbye")

say_goodbye("Ionel", 52)
say_goodbye("Maria", 34)
"""
Parametrii sunt in general pozitionali,
adica atunci cand apelam functia
prima valoare va merge in prima variabila, a2a valoare in a2a variabila
"""
# say_goodbye(52, "Ionel")
# say_goodbye(varsta=52, nume="Ionel") #zicem ca avem parametri numiti
# say_goodbye("Honolulu") #TypeError: say_goodbye() missing 1 required positional argument: 'varsta'
# print()

"""
At cand pt anumiti parametri dorim sa avem valori prestabilite (default),
putem face asta punand o valoare direct at cand definim functie

def nume_functie(param=valoare):
   etc
   
Daca oferim o valoare prestabilita, atunci paramentrul nostru zicem ca este optional.
Adica putem apela cu:

nume_functie() SAU
nume_functie(alta valoare)

"""
def say_hi(nume, mesaj="Acesta este un mesaj standard!"):
    print(f"{mesaj}")
    print(f"I-am zis hi lui {nume}")

say_hi("Mihai")
say_hi("Mihai", "Alt mesaj!")
say_hi("Johnny")

"""
Parametrii "traiesc" doar in interiorul functiei!!
La fel si orice variabila definita in interiorul functiei
"""

"""
IMPORTANT: desi putem avea oricati parametri vrem noi la o functie,
NU este recomandat sa avem mai mult de 6!
"""

