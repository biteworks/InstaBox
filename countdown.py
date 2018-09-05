import time, threading

counter = 10
countDownRuns = False
runFunc = "shoot"

#Countdown Funktion
def countDown():
    global countDownRuns
    global counter

    print(counter)
    counter = counter - 1

    if(counter>=1):
        startTimer(runFunc)
        return
		
    if(runFunc=="shoot"):	
        print("shoot")

    elif(runFunc=="run"):
		print("run")
		
    countDownRuns = False

#Funktion um den Timer zu starten
def startTimer(runFunc):
    global countDownRuns

    countDownRuns = True

    t = threading.Timer(1.0, countDown)
    t.start()

#Funktion um den Timer zu setzen (in Sekunden)
def setTimer(seconds):
    global counter
    counter = seconds

#Funktion um zu setzen welche Funktion am Ende des Timers aufgerufen wird
#Bisher gibt die Countdown-Funktion nach Ablauf der Zeit nur eine Konsolenausgabe aus
def setRunFunc(FuncToRun):
    global runFunc
    runFunc = FuncToRun

	
setTimer(5)
setRunFunc("shoot")
startTimer(runFunc)
