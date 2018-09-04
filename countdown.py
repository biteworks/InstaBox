import time, threading

counter = 10
countDownRuns = False

def countDown():
    global countDownRuns
    global counter

    print(counter)
    counter = counter - 1

    if(counter>=1):
        startTimer(counter)
        return

    countDownRuns = False

def startTimer(countDownTime):
    global countDownRuns
    global counter

    countDownRuns = True

    if not countDownRuns:
        counter = countDownTime

    t = threading.Timer(1.0, countDown)
    t.start()  # after 30 seconds, "hello, world" will be printed

startTimer(counter)
