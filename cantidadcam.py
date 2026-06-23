def fcam(lab, f, c):
    global ops
    ops += 1
    if f == len(lab)-1 and c == len(lab[0]) - 1:
        return 0 if lab[f][c] == 0 else 1
    elif c == len(lab[0]) - 1:
        return 0 if lab[f+1][c] == 0 else fcam(lab, f+1, c)
    elif f == len(lab)-1:
        return 0 if lab[f][c+1] == 0 else fcam(lab, f, c+1)
    else:
        return (0 if lab[f+1][c] == 0 else fcam(lab, f+1, c)) + (0 if lab[f][c+1] == 0 else fcam(lab, f, c+1))


lab = [
    [1,1,1,1,1,1,1,1],
    [1,1,0,1,1,1,0,1],
    [1,1,1,1,0,1,1,1],
    [0,1,0,1,1,0,1,1],
    [1,1,0,1,1,1,1,1],
    [1,1,1,0,0,1,0,1],
    [1,0,1,1,1,0,1,1],
    [1,1,1,1,1,1,1,1]
]

ops = 0
can = fcam(lab, 0, 0)
print(f"Son {can} caminos FB y {ops} operaciones")