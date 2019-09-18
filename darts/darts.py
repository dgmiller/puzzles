def score(x, y):
    points = 0
    distance = (x**2 + y**2)**(1/2)
    if distance<=10:
        points += 1
    if distance<=5:
        points += 4
    if distance<=1:
        points+=5
    return(points)