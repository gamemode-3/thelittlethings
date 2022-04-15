import os
import sys
import multiprocessing
from multiprocessing.managers import ValueProxy
import time


def run(file_path: str, refresh_interval: float = 0.1):
    """
    run a python file and reload it whenever it is modified
    """

    file_closed = multiprocessing.Manager().Value("closed", False)

    if not os.path.isfile(file_path):
        base_path = os.path.dirname(sys.argv[0])
        if os.path.isfile(base_path + file_path):
            file_path = base_path + file_path
        elif os.path.isfile(base_path + os.sep + file_path):
            file_path = base_path + os.sep + file_path
        else:
            raise FileNotFoundError(
                "File not found: \n  "
                + file_path
                + "\n| "
                + base_path
                + file_path
                + "\n| "
                + base_path
                + os.sep
                + file_path
            )

    with open(file_path, "r") as f:
        code = f.read()

    p = multiprocessing.Process(target=_run, args=(code, file_closed))
    p.start()

    while not file_closed.value:
        with open(file_path, "r") as f:
            current_code = f.read()

        if code != current_code:
            print("Reloading code...")
            code = current_code

            p.terminate()
            p = multiprocessing.Process(target=_run, args=(code, file_closed))
            p.start()

        time.sleep(refresh_interval)


def _run(code, close: "ValueProxy[bool]"):
    new_globals = globals()
    new_globals["__name__"] = "__main__"
    exec(code, new_globals)

    close.value = True


if __name__ == "__main__":
    print("Name is main")
    run(sys.argv[1], *({"refresh_interval": sys.argv[2]}) if len(sys.argv) > 2 else {})
