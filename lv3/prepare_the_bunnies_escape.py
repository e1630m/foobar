def walker(m, w, h):
    m[0][0] = 1
    nxt = [(0, 0)]
    while nxt:
        x, y = nxt.pop(0)
        for i, j in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + i, y + j
            if 0 <= nx < w and 0 <= ny < h:
                if not m[ny][nx]:
                    lowest = float('inf')
                    for k, l in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        tx, ty = nx + k, ny + l
                        if 0 <= tx < w and 0 <= ty < h:
                            if m[ty][tx]:
                                lowest = min(lowest, m[ty][tx])
                    m[ny][nx] = lowest + 1
                    nxt.append((nx, ny))
    return m[-1][-1]


def solution(m):
    w, h = len(m[0]), len(m)
    if walker([[1000 if i else 0 for i in l] for l in m], w, h) == w + h - 1:
        return w + h - 1
    shortest = float('inf')
    for x, y in [(x, y) for x in range(w) for y in range(h) if m[y][x]]:
        tmap = [[1000 if i else 0 for i in l] for l in m]
        tmap[y][x] = 0
        result = walker(tmap, w, h)
        if result:
            shortest = min(shortest, result)
            if shortest == w + h - 1:
                break
    return shortest
