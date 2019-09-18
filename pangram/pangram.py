def is_pangram(sentence):
    
    # ensure string is lowercase
    sentence = sentence.lower()
    
    # remove some punctuation
    for thing in ' ,.!?:;()':
        sentence = sentence.replace(thing,'')
    return set(sentence) == set("abcdefghijklmnopqrstuvwxyz")