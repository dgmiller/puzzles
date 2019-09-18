def is_pangram(sentence):
    """
    Tests to see if input sentence is a pangram (a sentence containing all letters of the alphabet).
    INPUT
        sentence (str)
    RETURNS
        (bool) indicating whether the sentence is a pangram
    
    """
    
    # ensure string is lowercase
    sentence = sentence.lower()
    
    return set("abcdefghijklmnopqrstuvwxyz") in set(sentence)