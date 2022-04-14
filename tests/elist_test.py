from thelittlethings import EList, Log


builtin_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
e_list = EList(builtin_list.copy())

Log("Builtin List")
for index, element in enumerate(builtin_list):
    Log(index, element)
    if element % 3 != 0:
        builtin_list.remove(element)

Log("Extended List")
# The EList adjusts the iterator index as it goes to iterate over all objects
# instead of all indices every time.
for index, element in e_list.enumerate():
    Log(index, element)
    if element % 3 != 0:
        e_list.remove(element)

Log(f"{builtin_list=}, {e_list=}")

a = EList([1, 2, 3, 4])
b = EList([3, 4, 5, 6])

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

Log(set_a - set_b)
Log(a - b)

Log(set_a | set_b)
Log(a | b)

Log(set_a & set_b)
Log(a & b)

Log(set_a ^ set_b)
Log(a ^ b)