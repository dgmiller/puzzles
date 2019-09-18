import re
def abbreviate(words):
    if type(words)!=str:
        return("input should be a string")
    else:
        words = re.sub("[-_,]", " ", words)
        print(words)
        tokens = words.split()
        acronym = [token[0] for token in tokens]
        acronym = "".join(acronym)
        acronym = acronym.upper()
        return(acronym)
