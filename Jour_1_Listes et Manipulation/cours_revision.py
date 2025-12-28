# 1. CRÉATION
numbers = [1, 2, 3, 4, 5]
empty = []
mixed = [1, "hello", 3.14, True]  # Peut contenir différents types

# 2. ACCÈS aux éléments
numbers = [10, 20, 30, 40, 50]

print(numbers[0])    # 10 (premier élément, index 0)
print(numbers[2])    # 30 (troisième élément)
print(numbers[-1])   # 50 (dernier élément)
print(numbers[-2])   # 40 (avant-dernier)

# 3. SLICING (découpage)
print(numbers[1:3])   # [20, 30] (index 1 à 2, le 3 est exclu)
print(numbers[:3])    # [10, 20, 30] (du début jusqu'à index 2)
print(numbers[2:])    # [30, 40, 50] (de index 2 jusqu'à la fin)
print(numbers[::2])   # [10, 30, 50] (tous les 2 éléments)

# 4. MODIFICATION
numbers.append(60)           # Ajoute à la fin → [10, 20, 30, 40, 50, 60]
numbers.insert(0, 5)         # Insère 5 à l'index 0 → [5, 10, 20, ...]
numbers.remove(30)           # Supprime la première occurrence de 30
numbers.pop()                # Supprime et retourne le dernier élément
numbers.pop(0)               # Supprime et retourne l'élément à l'index 0

# 5. MÉTHODES UTILES
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

len(numbers)         # 8 (longueur)
sum(numbers)         # 31 (somme de tous les éléments)
max(numbers)         # 9 (valeur maximum)
min(numbers)         # 1 (valeur minimum)
numbers.count(1)     # 2 (nombre d'occurrences de 1)
numbers.index(4)     # 2 (index de la première occurrence de 4)

# 6. BOUCLES sur les listes
# Méthode 1 : Parcourir les valeurs
for num in numbers:
    print(num)

# Méthode 2 : Parcourir avec les indices
for i in range(len(numbers)):
    print(f"Index {i}: {numbers[i]}")

# Méthode 3 : Parcourir valeur + index (BEST)
for index, value in enumerate(numbers):
    print(f"Index {index}: {value}")

# 7. VÉRIFICATIONS
if 5 in numbers:           # True (5 est dans la liste)
    print("5 est présent")

if 100 not in numbers:     # True (100 n'est pas dans la liste)
    print("100 est absent")



# Exemples Pratiques

# Exemple 1 : Trouver la somme des nombres pairs
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = 0
for num in numbers:
    if num % 2 == 0:  # % = modulo (reste de la division)
        total += num
print(total)  # 30 (2+4+6+8+10)

# Exemple 2 : Créer une nouvelle liste avec transformation
numbers = [1, 2, 3, 4, 5]
doubles = []
for num in numbers:
    doubles.append(num * 2)
print(doubles)  # [2, 4, 6, 8, 10]

# Exemple 3 : Compter combien de nombres sont > 5
numbers = [3, 7, 2, 9, 1, 8]
count = 0
for num in numbers:
    if num > 5:
        count += 1
print(count)  # 3 (7, 9, 8)
