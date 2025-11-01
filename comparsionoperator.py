#nested if-else statement
def find_maximum(a,b,c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
print(find_maximum(10, 20, 15)) 