import traceback
from ._log import Log
from ..variables import get_instances, get_names
from time import perf_counter
from colorama import Fore, Style


class Timer:
    timers = {}
    auto_log = True
    logging_accuracy = 3

    def __new__(cls, name=None):
        return TimerObject(name)

    @classmethod
    def start(cls, name):
        cls.timers[name] = {}
        cls.timers[name]["start"] = perf_counter()
    
    @classmethod
    def stop(cls, name, auto_log=None):
        if name not in cls.timers:
            raise Exception(f"Timer {name} not started")

        cls.timers[name]["stop"] = perf_counter()
        cls.timers[name]["time"] = cls.timers[name]["stop"] - cls.timers[name]["start"]

        if auto_log is None:
            auto_log = cls.auto_log
        
        if auto_log:
            cls.log(name)
    
    @classmethod
    def log(cls, name):
        if name not in cls.timers:
            raise Exception(f"Timer {name} not started")
        
        if "time" not in cls.timers[name]:
            raise Exception(f"Timer {name} not stopped")

        name_string = f"[Fore: cyan, Style: bright]{name}[Style: reset_all]"

        time_string = f"[Fore: white, Style: bright]{cls.timers[name]['time']:.{cls.logging_accuracy}f}[Style: reset_all]"        

        Log(f"[Style: reset_all]Timer {name_string} took {time_string} seconds")

    @classmethod
    def get(cls, name):
        if name not in cls.timers:
            raise Exception(f"Timer {name} not started")

        if "time" not in cls.timers[name]:
            raise Exception(f"Timer {name} not stopped")

        return cls.timers[name]["time"]

    @classmethod
    def delete(cls, name):
        if name not in cls.timers:
            raise Exception(f"Timer {name} does not exist")
        
        cls.timers.pop(name)

        for object in get_instances(TimerObject):
            if object.name == name:
                object.delete()
    
    @classmethod
    def clear(cls):
        cls.timers = {}


class TimerObject:
    def __init__(self, name):
        if name == None:
            (_,_,_,text)=traceback.extract_stack()[-3]
            name = text[:text.find('=')].strip()
        if name == "Timer(":
            raise Exception("Timer requires a name. Use Timer(name), Timer.start(name) or name = Timer().")
        self.name = name
        self.start()
    
    def start(self):
        Timer.start(self.name)
        return self
    
    def stop(self, auto_log=None):
        Timer.stop(self.name, auto_log)
        return self
    
    def log(self):
        Timer.log(self.name)
        return self
    
    def get(self):
        return Timer.get(self.name)
    
    def delete(self):
        if self.name in Timer.timers:
            Timer.timers.pop(self.name)
        del self