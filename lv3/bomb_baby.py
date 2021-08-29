def solution(M, F):
    b = [int(M), int(F)]
    g = 0
    while b[0] - b[1]:
        b.sort()
        q, r = divmod(b[1] - b[0], b[0])
        t = q + (r > 0)
        g += t
        b[1] -= t * b[0]
    return str(g) if b == [1, 1] else 'impossible'
