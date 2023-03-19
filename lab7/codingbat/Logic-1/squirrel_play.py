def squirrel_play(temp, is_summer):
    if is_summer and 60 <= temp <= 100 or 60 <= temp <= 90 and not is_summer:
        return True
    else:
        return False
