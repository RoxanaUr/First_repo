# 3. Clasa Angajat
# Atribute: nume, prenume, salariu
# Constructor pt toate atributele
# Metode:
# ● descrie()
# ● nume_complet()
# ● salariu_lunar()
# ● salariu_anual()
# ● marire_salariu(procent)

class Angajat:

    # toti parametrii constructorului(in afara de self) repr atributele
    def __init__(self, nume, prenume, salariu, cim=True):
        self.name = nume
        self.first_name = prenume
        self.salary = salariu
        self.cim = cim

    def descrie(self):
        print("-"*30)
        print(f"Nume: {self.name}")
        print(f"Prenume: {self.first_name}")
        print(f"Salariu: {self.salary}")
        if self.cim:
            print(f"Contract: CIM")
        else:
            print(f"Contract: PFA/SRL")

    def salariu_anual(self):
        return self.salary * 12

    def marire_salariu(self, procent):
        # daca facem o marire de salariu, tr sa modificam self.salary
        # altfel, imediat dupa apelarea metodei, noul salariu se pierde
        self.salary += (procent * self.salary) / 100
        return self.salary


ionel_cim = Angajat("Popescu", "Ion", 1200)
gheo_pfa = Angajat("Ionescu", "Gheorghe", 1500, cim=False)

ionel_cim.descrie()
gheo_pfa.descrie()

# daca dam print la o functie care nu returneaza nimic, ne va da none
print(f"Ionel are {ionel_cim.salariu_anual()} ron salariu anual.")
print(f" Gheo are {gheo_pfa.salariu_anual()} ron salariu anual.")

print(f"Noul salariu pentru Ionel este: {ionel_cim.marire_salariu(15)}")
print(f"Noul salariu pentru Ionel este: {gheo_pfa.marire_salariu(10)}")