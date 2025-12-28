# Exercice 1.3 : Somme des Positifs 
def sum_positives(numbers):
    """
    Calcule la somme UNIQUEMENT des nombres positifs (> 0)
    
    Input: [1, -4, 7, -2, 12]
    Output: 20 (car 1 + 7 + 12 = 20)
    
    Input: [-1, -2, -3]
    Output: 0 (aucun nombre positif)
    
    Input: [5, 10, -3, 8, -1]
    Output: 23 (car 5 + 10 + 8 = 23)
    
    Conseils :
    - Crée une variable total = 0
    - Parcours la liste
    - Si le nombre est > 0, ajoute-le au total
    - Retourne le total
    """
 
    total = 0
    for number in numbers:
        if number > 0:
            total += number
    return total

# Tests
print(sum_positives([1, -4, 7, -2, 12]))    # Doit afficher: 20
print(sum_positives([-1, -2, -3]))          # Doit afficher: 0
print(sum_positives([5, 10, -3, 8, -1]))    # Doit afficher: 23
print(sum_positives([0, 5, 0, 10]))         # Doit afficher: 15
