#!/usr/bin/python
# -*- coding: UTF-8 -*-

from multiprocessing import Manager
import multiprocessing
import sys
from time import sleep, time
from datetime import datetime

class ProgressBar:
    """
    class for easily creating a progress bar
    """
    def __init__(
        self,
        max_value=100,
        width=20,
        log_interval=0.1,
        display_percentage=True,
        display_time_passed=True,
        display_time_remaining=True,
        draw_function=None,
    ):
        self._progress = Manager().Value("progress", 0)
        self._cancel = Manager().Value("cancel", False)

        self.max_value = max_value

        if draw_function is None:
            draw_function = ProgressBar.draw_bar

        self.process = multiprocessing.Process(
            target=ProgressBar.run,
            args=(
                self._progress,
                self._cancel,
                width,
                max_value,
                log_interval,
                display_percentage,
                display_time_passed,
                display_time_remaining,
                draw_function,
            ),
        )

        self.process.start()

    @staticmethod
    def run(
        progress,
        cancel,
        width,
        max_value,
        log_interval,
        display_percentage,
        display_time_passed,
        display_time_remaining,
        draw_function,
    ):
        start_time = datetime.now()
        while not cancel.value:
            if progress.value >= max_value:
                cancel.value = True

            bar_string = draw_function(progress.value, width, max_value)
            if display_percentage:
                bar_string += (
                    " {:.2f}%".format(progress.value / max_value * 100)
                )
            time_delta = datetime.now() - start_time
            if display_time_passed:
                bar_string += " | Time passed: " + str(time_delta)
            if display_time_remaining:
                remaining_time_estimate = (
                    time_delta * (max_value / (progress.value if progress.value != 0 else 0.001) - 1)
                ) 
                bar_string += " | Time remaining: " + str(remaining_time_estimate)            
            while len(bar_string) < width + 20:
                bar_string += " "
            sys.stdout.flush()
            sys.stdout.write("\r" + bar_string)
            sleep(log_interval)
        sys.stdout.write("\n")
    
    def update(self, value):
        self._progress.value = value

    def cancel(self):
        self._cancel.value = True
        self.process.join()
    
    def finish(self):
        self._progress.value = self.max_value
        self.process.join()

    def await_done(self):
        self.process.join()

    @staticmethod
    def draw_bar(progress, width, max_value):
        return_str = "】"
        progress_width = progress / max_value * width
        return_str += "█" * int(progress_width)#
        rest = progress_width - int(progress_width)
        if 0 == rest and progress_width < width:
            return_str += " "
        elif 0 < rest < 0.125:
            return_str += "▏"
        elif 0.125 <= rest < 0.25:
            return_str += "▎"
        elif 0.25 <= rest < 0.375:
            return_str += "▍"
        elif 0.375 <= rest < 0.5:
            return_str += "▌"
        elif 0.5 <= rest < 0.625:
            return_str += "▋"
        elif 0.625 <= rest < 0.75:
            return_str += "▊"
        elif 0.75 <= rest < 0.875:
            return_str += "▉"
        elif 0.875 <= rest < 1:
            return_str += "█"
            
        return_str += " " * int(width - progress_width)
        return_str += "【"
        return return_str

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is None:
            self.finish()
        else:
            self.cancel()

    @property
    def progress(self):
        return self._progress.value

    @progress.setter
    def progress(self, value):
        self._progress.value = value