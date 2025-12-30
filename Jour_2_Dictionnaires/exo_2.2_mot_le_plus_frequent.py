def most_frequent_word(text):
    """
    Trouve le mot qui apparaît le plus souvent
    
    Input: "hello world hello python world world"
    Output: "world" (apparaît 3 fois)
    
    Input: "a b c a b a"
    Output: "a" (apparaît 3 fois)
    
    Hint:
    - Sépare le texte en mots avec text.split()
    - Compte les occurrences de chaque mot dans un dict
    - Trouve le mot avec le count maximum
    - Utilise max() ou une boucle
    """

    text_split = text.split()
    
    frequent_word = []
    total = 0
   
    for text in text_split:
        frequent_word.append(text)
        total += 1
     
      
    return frequent_word
    # frequent_word = {}
   
    # for text in text_split:
    #     if text in frequent_word:
    #         frequent_word[text] += 1
    #         # frequent_word[text] = frequent_word.get(text, 0) + 1
    #     else:
    #         frequent_word[text] = 1
    # return frequent_word

# Tests
print(most_frequent_word("hello world hello python world world"))


# print(most_frequent_word("a b c a b a"))
# "a"

# print(most_frequent_word("python"))
# "python"