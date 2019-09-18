def is_valid(isbn):
    isbn = list(isbn.replace("-","").lower())
    n = 0
    isbn_list = list()
    for i in range(10):
        if isbn[i] == "x":
            isbn[i] = 10
        else:
            try:
                isbn[i] = float(isbn[i])
            except:
                return False
        
        n += isbn[i] * (10-i)
    
    return (n % 11) == 0

for x in ["3-598-21508-8", "3-598-21507-X", "nope"]:
    print(x, is_valid(x))
