def make_negative( number ):

    if number > 0:
        return -number
    elif number < 0:
        return number
    elif number == 0:
        return 0

    return -abs(number)
    return -number if number > 0 else number

print(make_negative(1))  # return -1
print(make_negative(-5)) # return -5
print(make_negative(0) ) # return 0