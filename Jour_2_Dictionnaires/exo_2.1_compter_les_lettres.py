def count_letters(text):
    """
    Compte combien de fois chaque lettre apparaît dans un texte
    (Ignore les espaces et la casse)
    
    Input: "hello"
    Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    
    Input: "Hello World"
    Output: {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}
    
    Hint:
    - Crée un dictionnaire vide
    - Convertis le texte en minuscules avec text.lower()
    - Parcours chaque caractère
    - Ignore les espaces avec : if char != ' '
    - Utilise counts.get(char, 0) + 1
    """

    count_letters = {}
    for char in text.lower():
        if char != " ":
            count_letters[char] = count_letters.get(char, 0) + 1

    # for letter in text.lower():
    #     if letter in count_letters:
    #         count_letters[letter] += 1
    #     else:
    #         count_letters[letter] = 1
    return count_letters

# Tests
print(count_letters("hello"))
# {'h': 1, 'e': 1, 'l': 2, 'o': 1}

print(count_letters("Hello World"))
# {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}

print(count_letters("aaa"))
# {'a': 3}