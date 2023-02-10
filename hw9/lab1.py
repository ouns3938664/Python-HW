data = [7, 10, 12, 14, 16, 20, 29, 37]
i = 0
ip = [14, 29]
for j in range(len(ip)):
    for i in range(len(data)+1):
        if i > len(data)-1:
            print('Hmmm Its doesnt seem here.')
        elif ip[j] == data[i]:
            print('Oh! num '+str(ip[j])+' its there at Index : '+str(i))
            break
