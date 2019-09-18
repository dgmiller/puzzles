def abbreviate(words):
    if type(words)!=str:
        return("input should be a string")
    else:
        tokens = words.split()
        acronym = [token[0] for token in tokens]
        acronym = "".join(acronym)
        return(acronym)
