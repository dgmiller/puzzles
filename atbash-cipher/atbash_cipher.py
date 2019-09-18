
master_string = "abcdefghijklmnopqrstuvwxyz"

print(master_string[3])
    
    
def encode(plain_text):
    
    word_out = ""
    
    for letter in plain_text:
        letter_index = master_string.find(letter)
        new_letter = master_string[(len(master_string)-letter_index-1)]
        word_out = word_out.join(new_letter)
    
    return(word_out)
    


def decode(ciphered_text):
    pass
