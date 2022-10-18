from abc import ABC

"""
2. Abstractizarea:
ca si mostenirea, dar clasa parinte este o clasa abstracta
adica nu putem face obiecte in ea si o folosim doar ca si un template
pt metodele pe care ar tr sa le implementeze copiii

"""

class FormaGeometrica(ABC):

    def aria(self):
        raise NotImplementedError

    def perimetru(self):
        raise NotImplementedError

class Cerc(FormaGeometrica):

    def __init__(self, raza):
        self.r = raza

cerc = Cerc(10)