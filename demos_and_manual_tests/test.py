from thelittlethings.mutable import Mutable


class A:
    def __init__(self, name):
        self.name = name

class B:
    def __init__(self, name):
        self.name = Mutable(name)

a = A("Hello")
b = B("Hello")

a_name_ref = a.name
b_name_ref = b.name

a.name += " World!"
b.name += " World!"

print(f"{a.name = }; {a_name_ref = }\n{b.name = }; {b_name_ref = }")