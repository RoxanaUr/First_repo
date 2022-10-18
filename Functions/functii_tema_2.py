import random

"""
Ghicitoare de număr:
numar_secret = Generați un număr random între 1 și 30
Numar_ghicit = None
Folosind un while
User alege un număr

Programul îi spune:
● Nr secret e mai mare
● Nr secret e mai mic
● Felicitări! Ai ghicit!
"""

# Functia ai_ghicit va returna True daca s-a ghicit nr si False altfel
def ai_ghicit(nr_secret, nr_ghicit):
    if nr_secret == nr_ghicit:
        print("Felicitări! Ai ghicit!")
        return True

    if nr_ghicit > nr_secret:
        print("Nr secret e mai mic, mai incearca.")
    else:
        print("Nr secret e mai mare, mai incearca.")
    return False

numar_secret = random.randint(1, 30) # alegem un nr aleator intre 1 si 30
incercari = 0
max_incercari = 5
while incercari < max_incercari:
    incercari += 1
    numar_ghicit = int(input("Ghiceste:\n"))
    if ai_ghicit(numar_secret, numar_ghicit):
        print(f"Ai ghicit din {incercari} incercari!")
        break
else:
    # aici se va ajunge doar daca while nu a ajuns deloc la un break
    print(f"Nu ai ghicit din {max_incercari} incercari, jocul s-a terminat. Ai pierdut!")