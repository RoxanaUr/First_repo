# if conditie1:
#     fa ceva daca conditie1 este adevarat
# elif conditie2:
#     fa ceva daca conditie2 este adevarat
# elif conditie3:
#     fa ceva daca conditie3 este adevarat
# else:
#     fa ceva daca nici o conditie de pana acum nu a fost adevarata

varsta = int(input("Varsta:\n"))
if varsta <= 2:
    print("Esti bebelus")
elif varsta <= 12:
    print("Esti copil")
elif varsta <= 18:
    print("Esti adolescent")
elif varsta <= 65:
    print("Esti adult")
else:
    print("Esti pensionar")