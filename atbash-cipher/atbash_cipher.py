
master_string = "abcdefghijklmnopqrstuvwxyz"
    
def encode(plain_text):
    
    plain_text_out = plain_text.lower()
    
    word_out = ""
    
    for letter in plain_text_out:
        try:
            letter_index = master_string.find(letter)
            new_letter = master_string[(len(master_string)-letter_index-1)]
            word_out = word_out + new_letter
        except:
            pass
        
    format_word_out = " ".join([word_out[i:i+5] for i in range(0, len(word_out), 5)])
        
    return(format_word_out)
    


def decode(ciphered_text):
    
    word_out = ""
    
    ciphered_edit = ciphered_text.replace(" ","")
    
    for letter in ciphered_edit:
        try:
            letter_index = master_string.find(letter)
            new_letter = master_string[(len(master_string)-letter_index-1)]
            word_out = word_out + new_letter
        except:
            pass
        
    return(word_out)
    
    