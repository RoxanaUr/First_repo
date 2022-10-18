from Class import Person

class CursProgramare:

    def __init__(self, compania, nume, durata, data_inceput):
        self.compania = compania
        self.nume = nume
        self.durata = durata
        self.data_inceput = data_inceput
        self.studenti = []

    def inscriere_student(self, student):
        # Aici am putea sa verificam daca a trecut data de inceput si daca nu, sa inscriem studentul
        self.studenti.append(student)
    def descriere_curs(self):
        print(f"{self.nume} [{self.compania}] - {self.durata} zile")
        print("-"*80)
        for student in self.studenti:
            print(f"{student.nume} {student.prenume} ({student.varsta})")

        curs_python = CursProgramare("IT Factory", "Introducere in Python", 120, "2023")

