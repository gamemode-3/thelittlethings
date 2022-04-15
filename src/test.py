from typing import Callable
import thelittlethings.assertion as assertion

print("```\n- ```".join([
    func 
    for func 
    in dir(assertion) 
    if isinstance(getattr(assertion, func), Callable) 
    and not func.startswith("_")
]))