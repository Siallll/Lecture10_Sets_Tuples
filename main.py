set1 = set([1, 2, 3, 4])  # set is the unique values(example in list)
set2 = {1, 2, 3, 5}
# .add adds value to set
set1.add(6)
print(set1)

# .update updates multiple values at same time
set1.update([7, 8, 9])  # using [] in syntax
print(set1)

# .remove removes value in set but can raise error
set1.remove(6)  # using try: except: stops raise error
print(set1)

# .discard removes value in set without raising error
set1.discard(4)
print(set1)

# .pop removes last value in set but cant trust because set is not in order

# .clear removes all values in set
set1.clear()
print(set1)

set1 = {1, 2, 3, 4}
set2 = {5, 6, 7, 8}
## operations with sets
## (|) or .union the sum of 2 sets
print(set1 | set2)
print(set1.union(set2))
# (&) or .intersection the same values in the sets
set1.update([5, 6, 7, 8])
print(set1 & set2)

# (-) or .difference() gets difference only from first set wich are not in second
days1 = {"Monday", "Tuesday", "Wednesday", "Thursday"}
days2 = {"Monday", "Tuesday", "Sunday"}
print(days1 - days2)  # {"Wednesday", "Thursday" will be printed}
print(days1.difference(days2))  # Doesn't print difference in second from first set

### checking sets with check operators <, >, <=, >=, ==
days1 = {"Monday", "Tuesday", "Wednesday", "Thursday"}
days2 = {"Monday", "Tuesday"}
days3 = {"Monday", "Tuesday", "Sunday"}
# days1 is the superset of days2 hence it will print true.
print(days1 > days2)    # True
# prints false since days1 is not the subset of days2
print(days1 < days2)    # False
# prints false since days2 and days3 are not equivalent
print(days1 == days2)    # False
