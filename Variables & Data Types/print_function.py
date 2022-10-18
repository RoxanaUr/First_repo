age = 34
surname = "Roxana"
name = "Ursache"

# Print este o functie care "scrie" in consola, dar asteapta stringuri
print("Eu ma numesc " + surname + name)
print("Eu am " + str(age) + " ani") # Nu putem concatena varsta(int) cu str, deci trebuie sa facem type casting

# F-strings (formatted strings)
print(f"Pe mine ma cheama {surname} {name} si am {age} ani.") # este varianta recomandata

print(f"Am mai crescut un an, acum am {age + 1} ani")

var_str = f"Aici voi scrie mult text... fdfd Autor: {surname} {nume}"
var_str += f"Am scris si voi mai scrie fdsghdfg {age}"