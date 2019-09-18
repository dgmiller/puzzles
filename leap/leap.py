def leap_year(year):
    is_leap = 0
    if year%4==0:
        if year%100!=0:
            is_leap = 1
        else:
            if year%400==0:
                is_leap = 1
    if is_leap == 1:
        print(year,"is a leap year")
    else:
        print(year,"is not a leap year")



