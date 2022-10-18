# for imbricat -> for in for
hotel = [
    ["Birou management", "Toaleta", 10, 11, 12, 13, 13], # etaj parter
    [20, 21, 22, 23, 24, 25, 26], # etaj 1
    [30, 31, 32, 33, 34, 35, 36], # etaj 2
    [40, 41, 42] # ultimul etaj
]

for etaj in hotel:
    print(f"Etaj nou: {etaj}")
    for camera in etaj:
        print(f"   camera {camera}")

# Tabla inmultirii
for i in range(1, 10): # 0, 1, 2, 3, 4
    for j in range(1, 10):
        print(f"{i}x{j}={i*j}")
    print()