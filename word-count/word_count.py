import re
def count_words(sentence):
    #[\s,.:;!?\']?
    list_w = [item.group(1).lower() for item in re.finditer(r'(([A-Za-z]+(\'[A-Za-z]+)?|[0-9]+))',sentence)]
    dictCount = {}
    for item in list_w:
        if item in dictCount:
            dictCount[item] += 1
        else:
            dictCount[item] = 1
    return(dictCount)