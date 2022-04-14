from math import isclose
from random import randrange
from thelittlethings.linked_values._link_operation import NumberOperation
from thelittlethings.variables import get_all_subclasses
from colorama import Fore, Style

def operation_str(operation):
    return f"{Style.NORMAL}{Fore.CYAN}{operation.__name__}{Style.NORMAL}{Fore.WHITE}"

PASSED = f"{Style.BRIGHT}{Fore.GREEN}PASSED{Style.NORMAL}{Fore.WHITE}"
FAILED = f"{Style.BRIGHT}{Fore.RED}FAILED{Style.NORMAL}{Fore.WHITE}"

test_amount = 20

# Get all classes that inherit from Operation
operations = get_all_subclasses(NumberOperation)

summary_string = f"\n        --- Summary ---\n\n"

for operation in operations:
    summary_string += f"Results for {operation_str(operation)}:\n"
    print(f"\n        --- {operation_str(operation)} with integers ---\n")
    fails = 0
    for _ in range(test_amount):
        a = randrange(1, 200)
        b = randrange(1, 20)

        try:
            c = operation(a, b)
        except Exception as e:
            print(f"{FAILED}: {operation_str(operation)} failed for {a} and {b} with the following exception:")
            print(e)
            fails += 1
            continue

        try:
            a_ = operation.reverse(c, b)
        except Exception as e:
            print(f"{FAILED}: Reverse for {operation_str(operation)} failed for {a} and {b} with the following exception:")
            print(e)
            fails += 1
            continue

        if not isclose(a, a_):
            print(f"{FAILED}: {operation_str(operation)} failed for {a} and {b}")
            fails += 1
        else:
            print(f"{PASSED}: {operation_str(operation)} passed for {a} and {b}")

    if fails == 0:
        summary_string += f"{PASSED}: Passed all integer tests\n"
    else:
        summary_string += f"{FAILED}: Failed {fails}/{test_amount} integer tests\n"
    
    print(f"\n        --- {operation_str(operation)} with floats ---\n")
    fails = 0
    for _ in range(test_amount):
        a = randrange(1, 20000) / 100
        b = randrange(1, 2000) / 100
        
        try:
            c = operation(a, b)
        except Exception as e:
            print(f"{FAILED}: {operation_str(operation)} failed for {a} and {b} with the following exception:")
            print(e)
            fails += 1
            continue

        try:
            a_ = operation.reverse(c, b)
        except Exception as e:
            print(f"{FAILED}: Reverse for {operation_str(operation)} failed for {a} and {b} with the following exception:")
            print(e)
            fails += 1
            continue
        
        if not isclose(a, a_):
            print(f"{FAILED}: {operation_str(operation)} failed for {a} and {b}")
            fails += 1
        else:
            print(f"{PASSED}: {operation_str(operation)} passed for {a} and {b}")
    
    if fails == 0:
        summary_string += f"{PASSED}: Passed all float tests\n"
    else:
        summary_string += f"{FAILED}: Failed {fails}/{test_amount} float tests\n"

print(summary_string)