def main(a,b,c):
    """
    Find the largest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
#     if a>b and a>c:
#         return a
#     elif b>a and b>c:
#         return b
#     return c
# print(main(int(input()),int(input()),int(input())))
    return  max(a,b,c)
print(main(int(input()),int(input()),int(input())))

