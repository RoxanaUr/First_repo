class Patrat:

    """
    Functia init se numeste CONSTRUCTORUL clasei
    de aici se construiesc obiecte
    """

    def __init__(self, latura, culoare="alb"):
        self.lat = latura
        self.culoare = culoare

    def aria(self):
        return self.lat ** 2

patrat_alb = Patrat(12)
print(patrat_alb.lat)
print(patrat_alb.culoare)

patrat_rosu = Patrat(5, "rosu")
print(patrat_rosu.lat)
print(patrat_rosu.culoare)

def aria(latura):
    return latura ** 2

"""
Metodele sunt doar functii pe obiecte
(care primesc automat obiectul pe care le apeleaza
ca si self)
"""

print(aria(10))
print(patrat_alb.aria())
print(patrat_rosu.aria())