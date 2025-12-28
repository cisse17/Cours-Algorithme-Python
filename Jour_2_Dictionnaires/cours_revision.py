# Qu'est-ce qu'un Dictionnaire ?
# Un dictionnaire (dict) est une structure de données qui stocke des paires clé-valeur.

# Dictionnaire Python
user = {
    "name": "Alice",      # clé: "name",  valeur: "Alice"
    "age": 25,            # clé: "age",   valeur: 25
    "city": "Paris"       # clé: "city",  valeur: "Paris"
}


# 1. CRÉATION de Dictionnaires
# Méthode 1 : Avec {}
empty_dict = {}
user = {"name": "Alice", "age": 25}

# Méthode 2 : Avec dict()
user = dict(name="Alice", age=25)

# Méthode 3 : À partir de listes
keys = ["name", "age"]
values = ["Alice", 25]
user = dict(zip(keys, values))  # {'name': 'Alice', 'age': 25}

# Différents types de valeurs
data = {
    "name": "Alice",           # string
    "age": 25,                 # int
    "scores": [10, 15, 20],    # list
    "address": {               # dict dans dict !
        "city": "Paris",
        "zip": "75001"
    }
}

# 2. ACCÉDER aux Valeurs
user = {"name": "Alice", "age": 25, "city": "Paris"}

# Méthode 1 : Avec [] (attention aux erreurs !)
print(user["name"])    # "Alice" ok
print(user["email"])   # KeyError: 'email' n'existe pas !

# Méthode 2 : Avec .get() (PLUS SÛR)
print(user.get("name"))           # "Alice" ok
print(user.get("email"))          # None (pas d'erreur) 
print(user.get("email", "N/A"))   # "N/A" (valeur par défaut) 

# Exemple pratique
email = user.get("email", "pas d'email")
print(f"Email: {email}")  # Email: pas d'email


# 3. AJOUTER / MODIFIER des Valeurs

user = {"name": "Alice", "age": 25}

# Ajouter une nouvelle clé
user["email"] = "alice@mail.com"
# user = {"name": "Alice", "age": 25, "email": "alice@mail.com"}

# Modifier une valeur existante
user["age"] = 26
# user = {"name": "Alice", "age": 26, "email": "alice@mail.com"}

# Ajouter plusieurs clés d'un coup avec .update()
user.update({"city": "Paris", "country": "France"})
# user = {"name": "Alice", "age": 26, "email": "...", "city": "Paris", "country": "France"}

# Incrémenter une valeur
scores = {"math": 10}
scores["math"] += 5       # scores = {"math": 15}

# Ajouter à une liste dans un dict
data = {"tags": []}
data["tags"].append("python")
data["tags"].append("django")
# data = {"tags": ["python", "django"]}


# 4. SUPPRIMER des Éléments

user = {"name": "Alice", "age": 25, "email": "alice@mail.com"}

# Méthode 1 : del
del user["email"]
# user = {"name": "Alice", "age": 25}

# Méthode 2 : .pop() (retourne la valeur supprimée)
age = user.pop("age")
print(age)  # 25
# user = {"name": "Alice"}

# Méthode 3 : .pop() avec valeur par défaut
email = user.pop("email", "pas d'email")
print(email)  # "pas d'email" (pas d'erreur si clé absente)

# Méthode 4 : .clear() (vide tout)
user.clear()
# user = {}


# 5. VÉRIFIER si une Clé Existe
user = {"name": "Alice", "age": 25}

# Méthode 1 : Avec 'in' (RECOMMANDÉ)
if "name" in user:
    print(f"Nom: {user['name']}")

if "email" not in user:
    print("Pas d'email")

# Méthode 2 : Avec .get()
if user.get("email"):
    print(user["email"])
else:
    print("Pas d'email")



# 6. PARCOURIR un Dictionnaire
user = {"name": "Alice", "age": 25, "city": "Paris"}

# Méthode 1 : Parcourir les CLÉS
for key in user:
    print(key)
# Output:
# name
# age
# city

# Méthode 2 : Parcourir les CLÉS (explicite)
for key in user.keys():
    print(f"{key}: {user[key]}")
# Output:
# name: Alice
# age: 25
# city: Paris

# Méthode 3 : Parcourir les VALEURS
for value in user.values():
    print(value)
# Output:
# Alice
# 25
# Paris

# Méthode 4 : Parcourir CLÉ + VALEUR (MEILLEURE MÉTHODE)
for key, value in user.items():
    print(f"{key} = {value}")
# Output:
# name = Alice
# age = 25
# city = Paris

# 7. MÉTHODES Utiles
user = {"name": "Alice", "age": 25, "city": "Paris"}

# .keys() - Toutes les clés
print(user.keys())    # dict_keys(['name', 'age', 'city'])
print(list(user.keys()))  # ['name', 'age', 'city']

# .values() - Toutes les valeurs
print(user.values())  # dict_values(['Alice', 25, 'Paris'])
print(list(user.values()))  # ['Alice', 25, 'Paris']

# .items() - Tous les couples (clé, valeur)
print(user.items())
# dict_items([('name', 'Alice'), ('age', 25), ('city', 'Paris')])

# len() - Nombre de clés
print(len(user))  # 3

# .copy() - Copier un dictionnaire
user_copy = user.copy()


# 8. COMPTER avec les Dictionnaires (IMPORTANT !)
# Exemple : Compter les lettres dans un texte
text = "hello"

# Méthode classique
counts = {}
for letter in text:
    if letter in counts:
        counts[letter] += 1
    else:
        counts[letter] = 1

print(counts)  # {'h': 1, 'e': 1, 'l': 2, 'o': 1}

# Méthode avec .get() (plus court)
counts = {}
for letter in text:
    counts[letter] = counts.get(letter, 0) + 1

print(counts)  # {'h': 1, 'e': 1, 'l': 2, 'o': 1}