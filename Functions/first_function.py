"""
Functii - bucati de cod reutilizabile pe care oricine le poate folosi
Adica noi definim o functie o data si apoi o putem folosi in mai multe locuri

Sintaxa

def nume_functie (optional, aici putem avea parametri):
  aici, indentat
  va fi
  corpul functiei
  adica tot ceea ce se executa
  in functie

Cat timp doar definim o functie, nimic nu se intampla.
Trebuie sa o APELAM pt ca codul din interior sa se execute.
"""

def say_hello():
    print("Hello")
    print("Aceasta este prima mea functie!")

print("Aici vom invata despre functii")
say_hello()
say_hello()
say_hello()
say_hello() # CTRL + D