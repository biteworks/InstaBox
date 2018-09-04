import time, threading

counter = 3

def countDown():
    global counter
    print(counter)
    counter = counter - 1

    if(counter>=1):
        startTimer()
        return

    counter = 3

def startTimer():
    t = threading.Timer(1.0, countDown)
    t.start()  # after 30 seconds, "hello, world" will be printed

startTimer()
