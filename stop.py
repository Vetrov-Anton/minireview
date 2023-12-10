with open('sdc.fna', mode='r') as f:
    s = ''
    for line in f:
        s = s + line.strip()
a = s.split('>')
a = a[1:]
c = []
for i in a:
    c.append(i[-3]+i[-2]+i[-1])
u = sorted(list(set(c)))
for i in u:
    print(f'{i}\t{c.count(i)} ')
print(a[c.index('AAA')],)



