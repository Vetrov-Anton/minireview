f = open('table.txt')
c = f.readlines()
s = []
for line in c:
    x = line.split('\t')
    s.append(x)
s_ch_plus = []
for line in s:
    if line[4] == 'chromosome' and line[9] == '+' and line[0]=='CDS':
        s_ch_plus.append(line)
operons1 = []
for i in range(1,len(s_ch_plus)):
    if int(s_ch_plus[i][7]) - int(s_ch_plus[i-1][8]) <= 5:
        operons1.append([s_ch_plus[i-1][8],s_ch_plus[i][7],s_ch_plus[i-1][13], s_ch_plus[i][13]])
with open("operons_1", "w") as file:
    for line in operons1:
        file.writelines(line[0]+'\t'+line[1]+'\t'+line[2]+'\t'+line[3]+'\n')


print(operons1)








