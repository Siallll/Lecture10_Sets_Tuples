d = input()
b = []
a = set()
duplicates = {}
while d != "":
    a.add(d)
    b.append(d)
    d = input()
else:
    pass

for el in b:
    if el not in duplicates:
        duplicates.setdefault(el, 0)
    else:
        duplicates[el] = duplicates[el] + 1
unique = [v for v in duplicates.values() if v == 0]
dupl = [v for v in duplicates.values() if v > 0]
print(len(unique), len(dupl))
