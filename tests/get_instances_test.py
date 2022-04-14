from thelittlethings.variables import get_instances, get_names

class Letter:
    def __init__(self, name) -> None:
        self.name = name

a = Letter("a")
b = Letter("b")
c = Letter("c")
d = Letter("d")
e = Letter("e")
f = Letter("f")
g = Letter("g")
h = Letter("h")
i = Letter("i")
j = Letter("j")
k = Letter("k")
l = Letter("l")
m = Letter("m")
n = Letter("n")
o = Letter("o")
p = Letter("p")
q = Letter("q")
r = Letter("r")
s = Letter("s")
t = Letter("t")
u = Letter("u")
v = Letter("v")
w = Letter("w")
x = Letter("x")
y = Letter("y")
z = Letter("z")


print((*(
    [
        name for name 
        in get_names(instance) 
        if name != "instance"
    ]
    for instance 
    in get_instances(Letter)),)
)