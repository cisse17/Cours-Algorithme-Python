
# Exercice 1.4 : Inverser une Liste 
def reverse_list(numbers):
    """
    Inverse l'ordre des éléments d'une liste
    SANS utiliser reverse() ou [::-1]
    
    Input: [1, 2, 3, 4]
    Output: [4, 3, 2, 1]
    
    Input: [10, 20]
    Output: [20, 10]
    
    Hint 1 (Méthode facile):
    - Crée une liste vide
    - Parcours la liste ORIGINALE de la fin vers le début
    - Utilise range(len(numbers)-1, -1, -1) pour parcourir à l'envers
    
    Hint 2 (Méthode alternative):
    - Crée une liste vide
    - Parcours la liste normalement
    - Utilise insert(0, element) pour insérer au début
    """
 
    # reverse_liste = sorted(numbers, reverse=True)
    reverse_liste = []
    for number in numbers:
        reverse_liste.insert(0, number)
    return reverse_liste


# Tests
print(reverse_list([1, 2, 3, 4]))       # Doit afficher: [4, 3, 2, 1]
print(reverse_list([10, 20]))           # Doit afficher: [20, 10]
print(reverse_list([5]))                # Doit afficher: [5]
print(reverse_list([1, 2, 3, 4, 5]))    # Doit afficher: [5, 4, 3, 2, 1]
