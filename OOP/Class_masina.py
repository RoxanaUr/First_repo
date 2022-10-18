class Hamburger:

    def __init__(self, ingrediente, vegetarian=False):
        self.ingrediente = ingrediente
        self.vegetarian = vegetarian

    def reteta(self):
        print("Prajiti chifla")
        print("Puneti partea de jos a chiflei pe o farfurie")
        if self.vegetarian:
            print("Adaugati halloumi")
        else:
            print("Adaugati vita Angus")
        for ingredient in self.ingrediente:
            print(f"Adaugati {ingredient}")
        print("Puneti partea de sus a chiflei peste ingrediente")
        print("Serviti cald!")


