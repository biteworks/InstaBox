import time, threading

counter = 10
countDownRuns = False

def countDown():
    global countDownRuns
    global counter

    print(counter)
    counter = counter - 1

    if(counter>=1):
        startTimer()
        return

    countDownRuns = False

def startTimer():
    global countDownRuns

    countDownRuns = True

    t = threading.Timer(1.0, countDown)
    t.start()  # after 30 seconds, "hello, world" will be printed

def setTimer(seconds):
    global counter
    counter = seconds

	
setTimer(5)
startTimer()
