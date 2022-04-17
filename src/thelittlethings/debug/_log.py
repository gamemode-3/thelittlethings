import sys
from ._coloring import translate_color_codes
from ..constants import UNDEFINED
from ..files import load_file


class Log:
    """
    a class for logging information to the console and / or a file.

    looking for the logarithm operator? use ```Ln```, ```LogB``` or ```RLogB```.
    """
    print = True
    _file = None
    sep = " "
    end = "\n"

    _full_str = ""

    def __new__(cls, *values, sep=UNDEFINED, end=UNDEFINED, print_=UNDEFINED, file_path=UNDEFINED):
        file = load_file(file_path, True, default=None) or cls._file
        print_ = cls.print if print_ is UNDEFINED else print_
        sep = cls.sep if sep is UNDEFINED else sep
        end = cls.end if end is UNDEFINED else end

        if print_:
            value_list = list(values)
            for i in range(len(value_list)):
                if isinstance(value_list[i], str):
                    value_list[i] = translate_color_codes(value_list[i], console=True)
            sys.stdout.flush()
            sys.stdout.write(sep.join(str(value) for value in value_list) + end)
    
        value_list = list(values)
        for i in range(len(value_list)):
            if isinstance(value_list[i], str):
                value_list[i] = translate_color_codes(value_list[i], console=False)
        write_string = sep.join(str(value) for value in value_list) + end

        cls._full_str += write_string

        if file is not None:
            file.write(write_string)
    
    @classmethod
    def load_file(cls, file_path, create_if_nonexistant=True):
        cls.close_file()
        cls._file = load_file(file_path, create_if_nonexistant)
    
    @classmethod
    def close_file(cls):
        if cls._file is not None:
            cls._file.close()
            cls._file = None