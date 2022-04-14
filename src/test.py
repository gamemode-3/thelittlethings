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