data = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
data2 = []
sorted_data = []
for i in data:
    data2.append((i[1], i[0]))
    data2.sort()
print(data2)
for t in data2:
    sorted_data.append((t[1], t[0]))
print(sorted_data)
