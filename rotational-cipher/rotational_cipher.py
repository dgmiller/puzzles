def rotate(text, key):
    if type(text)!=str:
        return('first input should be a string')
    else:
        text = text.lower()
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        tempList = []
        count = 0
        for letter in alphabet:
            tempList.append((letter,count))
            count += 1
        lettersDict = dict(tempList)
        newText = ""
        for letter in text:
            if letter==" ":
                newText += letter
            else:
                newKey = lettersDict.get(letter)
                if newKey + key <= 25:
                    newKey += key
                else:
                    newKey = key - (25 - newKey) - 1
                newLetter = list(lettersDict.keys())[list(lettersDict.values()).index(newKey)]
                newText += newLetter
        return(newText)

print(rotate('omg', 5))
print(rotate('c', 0))
print(rotate('Cool', 26))
print(rotate('The quick brown fox jumps over the lazy dog', 13))
print(rotate('Gur dhvpx oebja sbk whzcf bire gur ynml qbt', 13))