from src.thelittlethings import RSub, Var, Log


a = Var(1)

b = Var(2)

c = RSub(a, b)

Log(f"{repr(c)} = {c}")

c.value = 6.5

Log(f"{repr(c)} = {c}")