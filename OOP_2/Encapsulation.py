"""
Incapsulare - posibilitatea de a proteja atributele clasei
- private (atributul poate fi accesat DOAR din interiorul clasei in care a fost atribuit
- protected (atribului poate fi accesat din clasa in care a fost definit,
dar si din clasele copii
"""

class Factura:

    seria = "XYZ"
    numar = 1
    __seria = "XYZ" # atributele cu __ in fata sunt PRIVATE
    def __init__(self, nume_produs, cantitate, pret_buc):
        self.nr_fact = Factura.numar
        self.prod = nume_produs
        self.cant = cantitate
        self.pret = pret_buc
        Factura.numar += 1

f1 = Factura("Telefon", 10, 120)
print(f1.seria, f1.numar)