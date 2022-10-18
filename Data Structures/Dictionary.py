
dict_gol = {}

# dict1 = {
#     "s": 12,
#     3: 45,
#     3.14: "un alt string",
#     True: 5,
#     "x": False
# }

tren = ["grau", "orz", "orez", "hrisca", "quinoa", "porumb"]
tren_colorat = {
    "rosu": "grau",
    "verde": "orz",
    "albastru": ["orez", ""],
    "galben": "hrisca",
    "alb": "quinoa",
    "negru": "porumb",
    "rosu": "amaranth"
}

# Cheile di dictionar trebuie sa fie unice
print(f"In vagonul rosu avem {tren_colorat['rosu']}")
print(f"In vagonul rosu avem {tren_colorat['rosu']}")

# Exemplu: vreau sa vad de cate ori apare o litera anume intr-un text
cuvant = "abracadabra"

# daca facem asa, vom avea nevoie de 26 variabile, prea multe
litera_a_cnt = cuvant.count("a")
litera_b_cnt = cuvant.count("b")

# Facem un dictionar in care key este litera cautata, iar value este de cate ori apare in text
dict_litere_cnt = {
    "a": cuvant.count("a"),
    "b": cuvant.count("b"),
    "r": cuvant.count("r")
}

# Exemplu: grupare date in mod logic
student_name = "Popescu"
student_firstname = "Ion"
student_age = 21
student_weight = 76.5

student = {
    "name": "Popescu",
    "firstname": "Ion",
    "age": 21,
    "weight": 76.5
}

print(f"Ma cheama {student['name']} {student['firstname']}."
      f"Am {student['weight']}")

# Operatii pe dictionare
tren_colorat = {
    "rosu": "grau",
    "verde": "orz",
    "albastru": "amaranth",
    "galben": "hrisca",
    "alb": "quinoa",
    "negru": "porumb",
}
# Adaugare element
tren_colorat['roz'] = "naut"

# Stergere element
del tren_colorat['roz'] # sterge elementul unde gaseste cheia roz

# Modificare
tren_colorat['rosu'] = "pietre"

print()