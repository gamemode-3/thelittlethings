# thelittlethings

a library full of small utilities for you to use in your code

## contents
• [installation](#installation)\
• [auto_reload](#auto_reload)\
&emsp;➜ [usage](#-usage)\
&emsp;⛭ [technical details](#-technical-details)\
• [debug.Log](#debug.Log)\
&emsp;➜ [usage](#-usage-1)\
&emsp;⛭ [technical details](#-technical-details-1)\
• [debug.Timer](#debug.Timer)\
&emsp;➜ [usage](#-usage-2)\
&emsp;⛭ [technical details](#-technical-details-2)

## installation
thelittlethings is not yet available for installation. you can clone the repository and add the src directory to your PATH or project.

## auto_reload

### ➜ usage

in ```run.py```:
```python
from thelittlethings import auto_reload

auto_reload.run("file_to_auto_reload.py", refresh_interval=0.1)
```

in ```file_to_auto_reload.py```:
```python
while True:
    print("Hello World")
    time.sleep(1)
```

now, when you run ```run.py```, ```"Hello World"``` will be printed every second. if you modify ```file_to_auto_reload.py``` and save it, you will see the changes reflected in the output.


### ⛭ technical details
the script checks for changes in the file in set intervals. you can change the interval by modifying the ```refresh_interval``` variable. The refresh interval is in seconds and defaults to ```0.1```.

if an error occurs, auto reload will not terminate.

if your script (```file_to_auto_reload.py```) stops without errors, auto reload will terminate.

taking inputs currently doesn't work as multiprocessing throws an ```end of file``` error.


## debug.Log

### ➜ usage
```Log``` is used to both print to the console and log to a file:
```python
from thelittlethings import Log

Log("Hello World")
```

By default it will only print to the console. To load a file, do:
```python
Log.load_file("log.txt")
```

from now on, all ```Log``` statements will be printed to the console and also to the file.

only one file can be loaded at a time.

to close the file, do:
```python
Log.close_file()
```

to use a different file for one statement, do:
```python
Log("Hello World", file_path="other_log.txt")
```

to disable printing to the console, do:
```python
Log.print = False
```

or, to disable it for only one statement, do:
```python
Log("Hello World", print=False)
```

```Log``` uses custom formatting for color and style. To change the text color, do:
```python
Log("[Text: Red]Hello World")
```

to change the background color, do:
```python
Log("[Background: Red]Hello World")
```

to change the text style, do:
```python
Log("[Style: Bright]Hello World")
```

color, background and style can be combined:
```python
Log("[Text: Red, Background: Green, Style: Bright]Hello World")
```

to access the color code parser, do:
```python
from thelittlethings import translate_color_codes


translate_color_codes("your_text_here", console=True)
```
where the console argument says whether to apply the codes or ignore them.


### ⛭ technical details
when the script exits, the file is closed automatically and all styles are reset.

To make the parser ignore an opening square bracket, follow it with a backslash.


## debug.Timer

### ➜ usage
```Timer``` is used to time the execution of a block of code:
```python
from thelittlethings import Timer

Timer.start("timer 1")
# do something
Timer.stop("timer 1")

Timer("timer 2")
# do something
Timer.stop("timer 2")

timer_3 = Timer()
# do something
timer_3.stop()

timer_4 = Timer()
# do something
Timer.stop("timer_4")
```

when a timer is stopped, the elapsed time is logged:

<img src="https://raw.githubusercontent.com/dots-git/thelittlethings/master/docs/assets/Timer_output.png" width="260" height="70" />

\
to manually log the elapsed time, do:
```python
Timer.log("timer 1")
```

to get the elapsed time, do:
```python
Timer.get("timer 1")
```

### ⛭ technical details
a timer is not automatically restarted after it is stopped. 

```Timer``` uses ```Log``` for logging. color codes in timer names will therefore be applied.

