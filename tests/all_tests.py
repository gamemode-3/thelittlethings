all_tests = []


from src.thelittlethings import multi_test, Log
def run_tests():
    multi_test(*all_tests)
    Log.print = False
    Log("\nuse the search function (ctrl+f) to find failed tests and summaries")
import atexit

atexit.register(run_tests)