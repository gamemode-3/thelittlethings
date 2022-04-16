all_tests = []


from src.thelittlethings import multi_test, Log
def run_tests():
    multi_test(*all_tests)
import atexit

atexit.register(run_tests)