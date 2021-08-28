def solution(xs, prod=1):
    if not xs:
        return '0'
    if len(xs) == 1:
        return str(xs[0])
    p, n = [i for i in xs if i > 0], [i for i in xs if i < 0]
    if len(n) == len(p + n) == 1:
        return '0'
    if len(n) % 2 == 1:
        n.remove(max(n))
    for i in p + n:
        prod *= i
    return str(prod)
