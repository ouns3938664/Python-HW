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
for i, j in enumerate(a):
    if 'In stock' in j:
        where = (i, j.index("In stock"))
        print('In Stock index= '+str(where))
for i, j in enumerate(a):
    if 'Out of stock' in j:
        where = (i, j.index('Out of stock'))
        print('Out of stock index= '+str(where))

for i, j in enumerate(a):
    if 'In stock' in j:
        if 'Ruler' in j:
            a[2][1] -= 1
if a[2][1] == 0:
    del a[2][2]
    a[2].insert(2, 'Out of stock')


for i, j in enumerate(a):
    if "In stock" in j:
        if "Pencil" in j:
            a[3][1] -= 1
if a[3][1] == 0:
    del a[3][2]
    a[3].insert(2, 'Out of stock')

for i, j in enumerate(a):
    if 'In stock' in j:
        if 'Pen' in j:
            a[4][1] -= 2
if a[4][1] == 0:
    del a[4][2]
    a[4].insert(2, 'Out of stock')

for i, j in enumerate(a):
    if "In stock" in j:
        if 'Coulour pencil' in j:
            a[5][1] -= 1

if a[5][1] == 0:
    del a[5][2]
    a[5].insert(2, "Out of stock")
del a[0]
print(a)
