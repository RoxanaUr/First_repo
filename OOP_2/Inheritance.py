"""
Pilonii OOP:
iNHERITANCE (mostenire)
ABSTRACTION (abstractizare)
POLYMORPHISM (polimorfism)
ENCAPSULATION (incapsulare)

1. Mostenirea:
uneori avem clase care impartasesc atribute
Putem face o clasa de baza (parinte), apoi clase copii
care sa mosteneaza parintele, adica atributele acestuia

Mostenirea permite sa avem o ierarhie a claselor, cu oricat nivele dorim
Se pot mosteni atat atribute, cat si metodele clasei parinte
Clasa copil poate avea in plus fata de clasa parinte orice atribute sau metode.
In cazul metodelor, at cand avem in cls copil o metoda exact  ca in cea parinte,
o suprascriem, deci trebuie sa o apelam cu super().

"""
# clasa parint (de baza)
class Person:

    def __init__(self, nume, varsta, adresa):
        self.nume = nume
        self.varsta = varsta
        self.adresa = adresa

    def descrie(self):
        print(f"Nume: {self.nume}")
        print(f"Varsta: {self.varsta}")
        print(f"Adresa: {self.adresa}")

    def anul_nasterii(self):
        return 2022 - self.varsta

# clasa copil (mosteneste Person, si implicit toate atributele acestuia
class Student(Person):

    def __init__(self, nume, varsta, adresa, facultate, an_studiu):
        # super repr clasa parinte
        super().__init__(nume, varsta, adresa)
        self.facultate = facultate
        self.an_studiu = an_studiu

    def descrie(self):
        super().descrie()
        print(f"Facultate: {self.facultate}")
        print(f"An studiu: {self.an_studiu}")

class Angajat(Person):

    def __init__(self, nume, varsta, adresa, companie, salariu):
        super().__init__(nume, varsta, adresa)
        self.companie = companie
        self.salariu = salariu

    def descrie(self):
        super().descrie()
        print(f"Companie: {self.companie}")
        print(f"Salariu: {self.salariu}")

ion = Student("Ion", 21, "Cluj", "UTCN", 2)
gheo = Angajat("Gheo", 45, "Sibiu", "Continental", 2500)

ion.descrie()
gheo.descrie()

print(ion.anul_nasterii()) #chiar daca e student, mosteneste metoda anul nasterii de la cls parinte
