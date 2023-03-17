def is_leap(year): #Write a function
    leap = False
    
    # Write your logic here
    if (year % 4 == 0 and not year % 100 == 0) or year % 400 == 0:
        leap = True 
    return leap