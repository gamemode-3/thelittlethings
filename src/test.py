from thelittlethings import *

a = Value(1.0)

b = Value(2.0)

c = a / b

Log(f"{str(a)} / {str(b)} = {str(c)}")

a += 1

Log(f"{str(a)} / {str(b)} = {str(c)}")

b -= 1

Log(f"{str(a)} / {str(b)} = {str(c)}")

c += 3

Log(f"{str(a)} / {str(b)} = {str(c)}")