def is_isogram(string):
# tests if a word is an isogram
    
    string1 = string.replace("-", "")
    string2 = string1.replace(" ", "")
    newstring = string2.lower()
    
    maxn = 0
    
    for letter in newstring:
        newn = newstring.count(letter)
        maxn = max(newn,maxn)
        
    return((maxn < 2))
        
