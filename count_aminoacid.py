with open('faa.faa', mode='r') as f:
    s = ''
    for line in f:
        x = line.strip()
        if x[0] != '>':
            s = s + x
y = list(set(s))
for i in y:
    n = s.count(i)
    z = n*100/len(s)
    print(f'{i}\t{z}')
