import re
def rotate(text, key):
    if type(text)!=str:
        return('first input should be a string')
    else:
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        ALPHABET = alphabet.upper()
        lowDict = []
        uppDict = []
        for ind in range(len(alphabet)):
            lowDict.append((alphabet[ind],ind))
            uppDict.append((ALPHABET[ind],ind))
        lowDict = dict(lowDict)
        uppDict = dict(uppDict)
        newText = ""
        for letter in text:
            if re.match('(?![a-zA-Z])',letter):
                newText += letter
            else:
                if letter.isupper():
                    lettersDict = uppDict
                else:
                    lettersDict = lowDict
                newKey = lettersDict.get(letter)
                if newKey + key <= 25:
                    newKey += key
                else:
                    newKey = key - (25 - newKey) - 1
                newLetter = list(lettersDict.keys())[list(lettersDict.values()).index(newKey)]
                newText += newLetter
        return(newText)