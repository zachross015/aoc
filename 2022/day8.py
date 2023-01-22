from utils import get_input

inp = get_input('day8.test')
print(inp)
for i in range(len(inp)):
    inp[i] = list(map(lambda x: int(x), inp[i]))

max_y = len(inp[0])
max_x = len(inp)

n = []
s = []
e = []
w = []

for i in len(max_x):
    n.append([])
    s.append([])
    e.append([])
    w.append([])
    for j in len(max_y):
        n[i].append(None)
        s[i].append(None)
        e[i].append(None)
        w[i].append(None)

