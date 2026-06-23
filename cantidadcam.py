def imprime(mat):
    for x in mat:
        print(x)
    print        

def fcamFB(lab, f, c):
    global ops
    ops += 1
    if f == len(lab)-1 and c == len(lab[0]) - 1:
        return 0 if lab[f][c] == 0 else 1
    elif c == len(lab[0]) - 1:
        return 0 if lab[f+1][c] == 0 else fcamFB(lab, f+1, c)
    elif f == len(lab)-1:
        return 0 if lab[f][c+1] == 0 else fcamFB(lab, f, c+1)
    else:
        return (0 if lab[f+1][c] == 0 else fcamFB(lab, f+1, c)) + (0 if lab[f][c+1] == 0 else fcamFB(lab, f, c+1))

def fcamPD(lab, f, c):
    n = len(lab)
    mem = [[-1 for _ in range(n)] for _ in range(n)]
    z = fcamPDUtl(lab, mem, f, c)
    return z

def fcamPDUtl(lab, mem, f, c):
    global ops
    ops += 1
    if mem[f][c] != -1:
        return mem[f][c]
    elif f == len(lab)-1 and c == len(lab[0]) - 1:
        mem[f][c] = (0 if lab[f][c] == 0 else 1)
        return mem[f][c]
    elif c == len(lab[0]) - 1:
        mem[f][c] = (0 if lab[f+1][c] == 0 else fcamPDUtl(lab, mem, f+1, c))
        return mem[f][c]
    elif f == len(lab)-1:
        mem[f][c] = (0 if lab[f][c+1] == 0 else fcamPDUtl(lab, mem, f, c+1))
        return mem[f][c]
    else:
        mem[f][c] = ((0 if lab[f+1][c] == 0 else fcamPDUtl(lab, mem, f+1, c)) + (0 if lab[f][c+1] == 0 else fcamPDUtl(lab, mem, f, c+1)))
        return mem[f][c]



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
imprime(lab)
ops = 0
can = fcamFB(lab, 0, 0)
print(f"Son {can} caminos FB y {ops} operaciones")

ops = 0
can = fcamPD(lab, 0, 0)
print(f"Son {can} caminos PD y {ops} operaciones")
