a = ['Number ID', 'Name', 'Count'], []
a = list(a)
al = len(a)
print(al)
v = ['Rubber', 0, 'Out of stock'], [
    'Ruler', 5, 'In stock'], ['Pencil', 1, 'In stock']
v = list(v)
for i in range(0, len(v)):
    a[(len(a)-1)] = v[i].copy()
    a.append([])
