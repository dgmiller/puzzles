def score(word):
    
    # ensure word is uppercase
    word = word.upper()
    
    # initialize score at zero
    score = 0
    for letter in word:
        if letter in 'AEIOULNRST':
            score += 1
        elif letter in 'DG':
            score += 2
        elif letter in 'BCMP':
            score += 3
        elif letter in 'FHVWY':
            score += 4
        elif letter in 'K':
            score += 5
        elif letter in 'JX':
            score += 8
        elif letter in 'QZ':
            score += 10
        else:
            raise ValueError("Input {0} is not a letter".format(letter))
        
    return score