def leap_year(year):
    is_leap = 0
    if year%4==0:
        if year%100!=0:
            is_leap = 1
        else:
            if year%400==0:
                is_leap = 1
    if is_leap == 1:
        return(True)
    else:
        return(False)


