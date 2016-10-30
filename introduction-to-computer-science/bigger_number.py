def bigger(a, b):
    if a > b:
        return a
    else:
        return b

#print bigger(1, 2)

# Second method
def biggest(a, b, c):
    if a >= b and a >= c:
        return a
    else:
        if b >= c and b >= a:
            return b
        else:
            return c

#Third method
def biggest(a, b, c)
    return bigger(bigger(a,b),c)

print biggest(1, 2, 3)
print biggest(30, 20, 10)
print bigger(20, bigger(40,10))