from typing import Any, Callable, Dict, Iterable, Tuple, Type

import inspect
from ..debug import Log
from .. import to_string, get_first_shared_inheritance, get_types


Log.load_file("testing.log")


PASSED = f"[style: bright, color: green]PASSED[style: reset_all]"
FAILED =   f"[style: bright, color: red]!!! FAILED[style: reset_all]"
SUM_PASSED = f"[style: bright, color: green]PASSED[style: reset_all]"
SUM_FAILED =   f"[style: bright, color: red]FAILED[style: reset_all]"


def _format_function(string):
    return f"[style: bright, color: magenta]{string}[style: reset_all]"

def _format_object(string):
    return f"[style: bright, color: cyan]{string}[style: reset_all]"


class TestSummary:
    def __init__(self, object_type: type, functions: Iterable[Callable], total_fails: int, total_tests: int):
        self.object_type = object_type
        self.functions = functions
        self.total_fails = total_fails
        self.total_tests = total_tests
    
    @property
    def function_name_string(self) -> Iterable[str]:
        return to_string.list(
            [_format_function(function.__name__.replace("_", " ")) for function in self.functions]
        )
    
    @property
    def object_name_string(self) -> str:
        return _format_object(self.object_type.__name__)
    
    @property
    def raw_function_name_string(self) -> Iterable[str]:
        return to_string.list(
            [function.__name__.replace("_", " ") for function in self.functions]
        )
    
    @property
    def raw_object_name_string(self) -> str:
        return self.object_type.__name__



def test(objects, *assert_functions, iterations=1):
    """
    test a list of objects with one or more given assert functions
    """

    if isinstance(objects, Callable):
        assert_functions = (*assert_functions, 
        objects)

    for func in assert_functions:
        func.takes_index = func.__code__.co_argcount > 1
        func.takes_object = func.__code__.co_argcount > 0


    assert_function_strings = []

    max_raw_function_string_length = 0

    for func in assert_functions:
        assert_function_strings.append(
            _format_function(func.__name__.replace('_', ' '))
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
            object_string = repr(object_)
        
        max_raw_object_string_length = max(len(object_string), max_raw_object_string_length)
        
        object_string = _format_object(object_string)
        
        object_strings.append(object_string)

    max_object_string_length = max(len(object_string) for object_string in object_strings)

    max_function_string_length = max(len(string) for string in assert_function_strings)
    
    summary_string = f"\n\n\n{' ' * int((max_raw_object_string_length + max_raw_function_string_length + 15) / 2)}--- summary ---\n\n"

    total_fails = 0

    for object_, object_string in zip(objects, object_strings):

        print("")
        
        for assert_function, assert_function_string in zip(assert_functions, assert_function_strings):
            fails = 0
            for i in range(iterations):
                return_string = ""
                try:
                    if assert_function.takes_index:
                        return_string = assert_function(object_, i)
                    elif assert_function.takes_object:
                        return_string = assert_function(object_)
                    else:
                        return_string = assert_function()
                except AssertionError as e:
                    Log(f"{FAILED}: {object_string} - {assert_function_string} - assertion failed: {e}")
                    fails += 1
                    total_fails += 1
                    continue
                except Exception as e:
                    Log(f"{FAILED}: {object_string} - {assert_function_string} - exception thrown: {e}")
                    fails += 1
                    total_fails += 1
                    continue
                if not isinstance(return_string, str):
                    return_string = ""
                else:
                    return_string = f" with message: {return_string}"
                Log(f"{PASSED}: {object_string} - {assert_function_string} - passed{return_string}")
            if fails == 0:
                summary_string += f"{SUM_PASSED}: {object_string: <{max_object_string_length}} - {assert_function_string: <{max_function_string_length}} - passed all tests\n"
            else:
                summary_string += f"{SUM_FAILED}: {object_string: <{max_object_string_length}} - {assert_function_string: <{max_function_string_length}} - failed {fails}/{iterations} tests\n"
    
    Log(summary_string)

    return TestSummary(get_first_shared_inheritance(get_types(*objects)), assert_functions, total_fails, iterations * len(objects) * len(assert_functions))


def multi_test(*arguments: Tuple[Tuple[Iterable[Any], Callable, Callable, Dict[str, Any]]]):
    """
    run multiple tests and recieve a summary of the results.
    syntax: 
    ```python
    multi_test(
        (objects_1, function_1, function_2, {'iterations': iterations}),
        (objects_2, function_1, function_2, {'iterations': iterations}),
    )
    ```
    """

    summaries: list[TestSummary] = []

    for arguments_ in arguments:
        args = arguments_ if not isinstance(arguments_[-1], dict) else arguments_[:-1]
        kwargs = arguments_[-1] if isinstance(arguments_[-1], dict) else {}
        summaries.append(test(*args, **kwargs))

    longest_object_string = max(len(summary.object_name_string) for summary in summaries)

    longest_raw_object_string = max(len(summary.raw_object_name_string) for summary in summaries)
    longest_raw_function_string = max(len(summary.raw_function_name_string) for summary in summaries)

    summary_strings = []

    for summary in summaries:
        if summary.total_fails == 0:
            summary_strings.append(
                f"{SUM_PASSED}: {summary.object_name_string: <{longest_object_string}}"
                f" - {summary.function_name_string}"
                f"{' ' * (longest_raw_function_string - len(summary.raw_function_name_string))}"
                f" - passed all tests")
        else:
            summary_strings.append(
                f"{SUM_FAILED}: {summary.object_name_string: <{longest_object_string}}"
                f" - {summary.function_name_string}"
                f"{' ' * (longest_raw_function_string - len(summary.raw_function_name_string))}"
                f" - failed {summary.total_fails}/{summary.total_tests} tests")

    summary = f"\n\n\n{' ' * int((longest_raw_object_string + longest_raw_function_string + 15) / 2)}--- summary ---\n\n"
    summary += "\n".join(summary_strings)

    Log(summary)

    return summaries


def test_from_class(cls: Type[Any], iterations=1) -> TestSummary:
    """
    run a test with all functions in a class that start with `test_`
    """

    return test([None], *(func for name, func in inspect.getmembers(cls, predicate=inspect.isfunction) if name.startswith("test_")))