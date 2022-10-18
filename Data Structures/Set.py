# Set - structura de date (colectie) care are doar elemente unice

set_gol = {} # NU putem face asa, asta e un dictionar
set_gol = set()

an = {'primavara', 'vara', 'toamna', 'vara'}
print(an)

an.add('primavara')
print(an)

# Set membership
anotimp = "vara"
if anotimp in an:
    print("Gasit")
else:
    print("Nu exista in set")

an.remove('vara')