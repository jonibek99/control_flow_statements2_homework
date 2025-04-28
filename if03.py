def main(a,b,c):
    """
    Determine the number between large and small.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """ 
    if (a<=b <=c) or (c<=b <=a):
        return b
    elif (b<=a<=c) or (c<=a<=b):
        return a
    return c
print(main(int(input()),int(input()),int(input())))


