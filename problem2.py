A = set()
B = set()
result = set()
c = input()
d = input()
while c != "":
    A.add(c)
    B.add(d)
    c = input()
    d = input()
else:
    pass
result.add(frozenset(A - B))
result.add(frozenset(B))
result.add(frozenset(B - A))
result.add(frozenset(A - B).union(B - A))
result.add(frozenset(A & B))
result.add(frozenset(A | B))
print(result)
