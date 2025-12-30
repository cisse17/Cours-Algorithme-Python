# Exemple 1 : Grouper par catégorie
fruits = ["apple", "banana", "apricot", "blueberry", "cherry"]

groupes = {}
for fruit in fruits:
    first_letter = fruit[0]
    if first_letter not in groupes:
        groupes[first_letter] = []
    groupes[first_letter].append(fruit)

print(groupes)
