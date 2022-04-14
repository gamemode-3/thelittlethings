import os
from ._coloring import translate_color_codes
from ..values import UNDEFINED
from ..files import load_file


class Log:
    print = True
    _file = None

    _full_str = ""

    def __new__(cls, *values, sep=" ", end="\n", print_=UNDEFINED, file_path=UNDEFINED):
        file = load_file(file_path, True, default=None) or cls._file
        print_ = print_ if print_ is not UNDEFINED else cls.print


        if print_:
            value_list = list(values)
            for i in range(len(value_list)):
                if isinstance(value_list[i], str):
                    value_list[i] = translate_color_codes(value_list[i], console=True)
            print(*value_list, sep=sep, end=end)
    
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