import os
import sys
import multiprocessing
from multiprocessing.managers import ValueProxy
import time


def run(file_path: str, refresh_interval: float = 0.1):
    # create a shared value to close the execution
    file_closed = multiprocessing.Manager().Value("closed", False)

    # open the first system argument as a file

    if not os.path.isfile(file_path):
        base_path = os.path.dirname(sys.argv[0])
        if os.path.isfile(base_path + file_path):
            file_path = base_path + file_path
        elif os.path.isfile(base_path + os.sep + file_path):
            file_path = base_path + os.sep + file_path
        else:
            raise FileNotFoundError(
                "File not found: \n  " + file_path 
                + "\n| " + base_path + file_path 
                + "\n| " + base_path + os.sep + file_path
            )
    
    with open(file_path, "r") as f:
        # read the file
        code = f.read()

    # create a new process to execute the code
    p = multiprocessing.Process(target=_run, args=(code, file_closed))
    # start the process
    p.start()

    # Loop and check if the file has been modified
    while not file_closed.value:
        # get the current state of the code
        with open(file_path, "r") as f:
            current_code = f.read()
        # check if the code has changed
        if code != current_code:
            print("Reloading code...")
            code = current_code
            # if it has, reload the code
            p.terminate()
            p = multiprocessing.Process(target=_run, args=(code, file_closed))
            p.start()
        # sleep for the refresh interval
        time.sleep(refresh_interval)


def _run(code, close: "ValueProxy[bool]"):
    new_globals = globals()
    new_globals["__name__"] = "__main__"
    exec(code, new_globals)
    # exit execution
    close.value = True


if __name__ == "__main__":
    print("Name is main")
    run(sys.argv[1], *({"refresh_interval": sys.argv[2]}) if len(sys.argv) > 2 else {})