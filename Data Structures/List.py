"""
Listele sunt structuri de date (colectii in Python prin care poti tine mai multe valori
Valorile se pot accesa prin INDICE (adica pozitia valorii in lista)
"""
list1 = [5, 7, 12, -3, 8]
list2 = ["Ana", "are", "mere"]
list3 = [True, False, False, True, False, False, False]

#          0      1       2        3          4        5
tren = ["grau", "orz", "orez", "hrisca", "quinoa", "porumb"]
print(f"In vagonul 1 avem {tren[1]}")
print(tren[1:4]) # slicing functioneaza pe liste exact ca si la stringuri
print(f"In ultimul vagon avem {tren[-1]}") # indexare negativa
print(f"Trenul are in total {len(tren)} vagoane!") # lungimea listei se det cu functia len

# Pentru a adauga elemente noi in lista folosim o functie numita append
tren.append("ovaz")
print(tren)
print(tren, len(tren))

# Listele nu trebuie obligatoriu sa aiba elemente cu acelasi tip
lista_complexa = ["un string", True, 12, "alt string", 3.14]

lista_complexa.remove() # stergere un element din lista bazat pe valoare
lista_complexa.pop()
lista_complexa.clear() # sterge toate elementele din liste

del lista_complexa # sterge VARIABILA lista_complexa
# va da eroare la print, deoarece am sters lista complet

#       0     1    2    3    4    5    6    7
l = ["a", "b", "c", "a", "b", "x", "z", "b"]
index_primul_b = l.index("b") # returneaza indexul la care gasim valoarea din paranteza
print(index_primul_b)
# ca sa gasim al doilea b, trebuie sa facem slicing si sa incepem cautarea de la pozitia primului
index_al_doilea_b = l[index_primul_b + 1:].index("b") + index_primul_b + 1

# Deoarece putem sa adaugam/stergem/modificam elemente din lista, zicem ca lista e MUTABILA
l[0] = l[0].upper()
l[1] = l[1].upper()


# Functii pe liste: max, min, sum

lx = [5, 7, 12, -3, 8, 2, 3, 21]
print(max(lx)) # gaseste nr maxim
print(min(lx)) # gaseste nr minim
print(sum(lx)) # face suma

# list membership: verificare daca o valoare se gaseste intr-o lista
print(7 in lx) # afiseaza True
print(6 in lx) # afiseaza False


vocale = ['a', 'e', 'i', 'o', 'u']

if litera == 'a' or litera == 'e' or litera = 'u':
    print("Litera este vocala")

litera = input("Litera:\n")
if litera in vocale:
    print("Litera este vocala")

# Concatenarea (adunarea) a doua liste
ly = [70, 33, 14, 51]
lz = lx + ly
print(lz) # se alatura cele 2 liste
print(f"LX: {lx}\nLY: {ly}")
print(lz)



