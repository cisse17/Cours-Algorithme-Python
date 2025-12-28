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