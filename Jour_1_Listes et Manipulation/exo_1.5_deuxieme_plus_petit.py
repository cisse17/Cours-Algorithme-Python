# EXERCICE 
def second_smallest(numbers):
    """
    Trouve le DEUXIÈME plus petit nombre
    
    Input: [5, 2, 8, 1, 9]
    Output: 2 (le plus petit est 1, le deuxième plus petit est 2)
    
    Input: [10, 3, 7, 3, 15]
    Output: 3 (attention aux doublons!)
    
    Hint:
    - Trouve d'abord le plus petit
    - Ensuite, trouve le plus petit parmi ceux qui sont > au plus petit
    - OU trie la liste et prends le 2ème élément
    """
    
    set_numbers = set(numbers)
    # second_smallest_number = sorted(set_numbers, key=abs)
    second_smallest_number = sorted(set_numbers, reverse=False)
    return second_smallest_number[1]
    


# Tests
print(second_smallest([5, 2, 8, 1, 9]))     # Doit afficher: 2
print(second_smallest([10, 3, 7, 15]))      # Doit afficher: 7
print(second_smallest([1, 1, 2, 3]))        # Doit afficher: 2""

