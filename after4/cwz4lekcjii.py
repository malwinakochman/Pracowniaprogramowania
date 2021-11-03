#19

def is_within_the_given_range(a, x, y):
    is_the_given = False
    if a>x and a<y:
        is_the_given = True
    
    return is_the_given

print(is_within_the_given_range(1,2,5))