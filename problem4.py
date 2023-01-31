dict1 = {}
user_input_a = input()
user_input_b = input()
a = set()
b = set()
while user_input_a and user_input_b != "":
    a.update(user_input_a)
    b.update(user_input_b)
    user_input_a = input()
    user_input_b = input()
else:
    pass

dict1["|"] = (a | b)
dict1["&"] = (a & b)
dict1["-"] = (a - b)
print(dict1)
