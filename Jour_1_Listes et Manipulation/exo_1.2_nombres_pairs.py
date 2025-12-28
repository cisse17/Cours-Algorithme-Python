
# Exercice 1.2 : Nombres Pairs ⭐
"""
    Retourne une liste contenant SEULEMENT les nombres pairs
    
    Input: [1, 2, 3, 4, 5, 6]
    Output: [2, 4, 6]
    
    Input: [1, 3, 5, 7]
    Output: []
    
    conseils :
    - Crée une liste vide pour stocker les résultats
    - Parcours la liste d'entrée
    - Si un nombre est pair (nombre % 2 == 0), ajoute-le à ta liste
    - Retourne la liste
"""

def get_evens(numbers):
   
    nombres_pairs = []
    for number in numbers:
        if number % 2 == 0:
            nombres_pairs.append(number)
    return nombres_pairs

# Tests
print(get_evens([1, 2, 3, 4, 5, 6]))    # Doit afficher: [2, 4, 6]
print(get_evens([1, 3, 5, 7]))          # Doit afficher: []
print(get_evens([0, 2, 4]))             # Doit afficher: [0, 2, 4]
print(get_evens([10, 15, 20, 25]))      # Doit afficher: [10, 20]
