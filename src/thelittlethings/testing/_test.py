from typing import Callable
from colorama import Fore, Style
from ..debug import Log


def test(objects, *assert_functions, iterations=10):
    """
    test a list of objects with one or more given assert functions
    """

    PASSED = f"[Style: Bright, Color: Green]    PASSED[Style: Reset_All]"
    FAILED =   f"[Style: Bright, Color: Red]!!! FAILED[Style: Reset_All]"
    SUM_PASSED = f"[Style: Bright, Color: Green]PASSED[Style: Reset_All]"
    SUM_FAILED =   f"[Style: Bright, Color: Red]FAILED[Style: Reset_All]"

    if isinstance(objects, Callable):
        assert_functions = (*assert_functions, 
        objects)

    for func in assert_functions:
        func.takes_index = func.__code__.co_argcount > 1


    assert_function_strings = []

    max_raw_function_string_length = 0

    for func in assert_functions:
        assert_function_strings.append(
            f"[Style: Bright, Color: Magenta]{func.__name__.replace('_', ' ').title()}[Style: Reset_All]"
        )
        max_raw_function_string_length = max(max_raw_function_string_length, len(func.__name__))

    object_strings = []

    max_raw_object_string_length = 0

    for object_ in objects:
        if hasattr(object_, "name"):
            object_string = object_.name
        elif hasattr(object_, "__name__"):
            object_string = object_.__name__
        else:
            object_string = str(object_)
        
        max_raw_object_string_length = max(len(object_string), max_raw_object_string_length)
        
        object_string = f"[Style: Bright, Color: LightCyan_EX]{object_string}[Style: Reset_All]"
        
        object_strings.append(object_string)

    max_object_string_length = max(len(object_string) for object_string in object_strings)

    max_function_string_length = max(len(string) for string in assert_function_strings)
    
    summary_string = f"\n\n\n{' ' * int((max_raw_object_string_length + max_raw_function_string_length + 15) / 2)}--- Summary ---\n\n"

    for object_, object_string in zip(objects, object_strings):

        print("")
        
        for assert_function, assert_function_string in zip(assert_functions, assert_function_strings):
            fails = 0
            for i in range(iterations):
                return_string = ""
                try:
                    if assert_function.takes_index:
                        return_string = assert_function(object_, i)
                    else:
                        return_string = assert_function(object_)
                except AssertionError as e:
                    Log(f"{FAILED}: {object_string} - {assert_function_string} - Assertion failed: {e}")
                    fails += 1
                    continue
                except Exception as e:
                    Log(f"{FAILED}: {object_string} - {assert_function_string} - Exception thrown: {e}")
                    fails += 1
                    continue
                if not isinstance(return_string, str):
                    return_string = ""
                else:
                    return_string = f" with message: {return_string}"
                Log(f"{PASSED}: {object_string} - {assert_function_string} - Passed{return_string}")
            if fails == 0:
                summary_string += f"{SUM_PASSED}: {object_string: <{max_object_string_length}} - {assert_function_string: <{max_function_string_length}} - Passed all tests\n"
            else:
                summary_string += f"{SUM_FAILED}: {object_string: <{max_object_string_length}} - {assert_function_string: <{max_function_string_length}} - Failed {fails}/{iterations} tests\n"
    
    Log(summary_string)