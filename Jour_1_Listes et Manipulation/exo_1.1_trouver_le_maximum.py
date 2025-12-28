
def find_max(numbers):
    """
    Trouve le plus grand nombre dans une liste
    SANS utiliser la fonction max()
    
    Input: [3, 7, 2, 9, 1]
    Output: 9
    
    Input: [-5, -2, -10, -1]
    Output: -1
    
    Conseils : 
    - Commence par supposer que le premier élément est le max
    - Parcours la liste et compare chaque élément avec ton max actuel
    - Si tu trouves un élément plus grand, il devient le nouveau max
    """

    max_element = numbers[0]

    for number in numbers:
        if number > max_element:
            max_element = number
    return max_element

# Tests
print(find_max([3, 7, 2, 9, 1]))        # Doit afficher: 9
print(find_max([-5, -2, -10, -1]))      # Doit afficher: -1
print(find_max([42]))                   # Doit afficher: 42
print(find_max([5, 5, 5, 5]))           # Doit afficher: 5








