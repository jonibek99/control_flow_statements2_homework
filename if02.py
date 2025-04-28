def main(a,b,c):
    """
    Find the smallest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
#     return min(a,b,c)
# print(main(int(input()),int(input()),int(input())))
    if a<b or  a<c:
        return a
    elif b<a or b<c:
        return b
    return c
print(main(int(input()),int(input()),int(input())))

