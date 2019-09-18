def find_anagrams(word, candidates):
    is_anagram = []
    for c in candidates:
        if c.lower() == word.lower():
            continue
        if len(c) == len(word):
            list_c = []
            list_w = []
            for w in range(len(word)):
                list_c.append(c[w].lower())
                list_w.append(word[w].lower())
            if sorted(list_c) == sorted(list_w):
                is_anagram.append(c)
    return(is_anagram)
