def group_by_length(words):
    """
    Groupe les mots par leur longueur
    
    Input: ['a', 'bb', 'ccc', 'dd', 'e']
    Output: {1: ['a', 'e'], 2: ['bb', 'dd'], 3: ['ccc']}
    
    Input: ['hello', 'world', 'hi']
    Output: {5: ['hello', 'world'], 2: ['hi']}
    
    Hint:
    - Crée un dictionnaire vide
    - Pour chaque mot, calcule sa longueur avec len(word)
    - Si la longueur n'est pas dans le dict, crée une liste vide
    - Ajoute le mot à la liste correspondante
    """
    counts = {}
    for word in words:
        len_word = len(word)
        if len_word not in counts:
            counts[len_word] = []
        counts[len_word].append(word)
    return counts

# Tests
print(group_by_length(['a', 'bb', 'ccc', 'dd', 'e']))
# {1: ['a', 'e'], 2: ['bb', 'dd'], 3: ['ccc']}

print(group_by_length(['hello', 'world', 'hi']))
# {5: ['hello', 'world'], 2: ['hi']}

print(group_by_length(['python', 'is', 'awesome']))
# {6: ['python'], 2: ['is'], 7: ['awesome']}