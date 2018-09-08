import pygame, sys, os, time, threading
from picamera import PiCamera
from time import sleep
from pygame.locals import *

# Global Variables
listenToInput = True
state = 1
counter = 3
countDownRuns = False
runFunc = "shoot"

# Image Settings
imageResolution = [2592,1944]
imageFolder = '/home/pi/Desktop/Instabox/Images/'

# Event-Settings
eventName = 'Tobias-30er_'

# Assets Loading
imgStart = pygame.image.load('assets/Start.jpg')
imgHowTo = pygame.image.load('assets/Erklaerung.jpg')
imgBG = pygame.image.load('assets/Background.jpg')
imgEdit = pygame.image.load('assets/Bearbeiten.jpg')

pygame.init()
screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
pygame.mouse.set_visible(False)
camera = PiCamera()
camera.led = False

# Set Functions
def setImage(imgName):
    if(imgName == 'Start'):
        screen.blit(imgStart,(0,0))
    elif(imgName == 'HowTo'):
        screen.blit(imgHowTo,(0,0))
    elif(imgName == 'Background'):
        screen.blit(imgBG,(0,0))
    elif(imgName == 'Edit'):
        screen.blit(imgEdit,(0,0))
        
def setState(newState):
    global state
    state = newState

def setInputState(listenTo):
    global listenToInput
    listenToInput = listenTo

# Set timer value
def setTimer(seconds):
    global counter
    counter = seconds

# Choose a Function to run after countdown
def setRunFunc(FuncToRun):
    global runFunc
    runFunc = FuncToRun

# Countdown Function
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

def startTimer(runFunc):
    global countDownRuns

    countDownRuns = True

    t = threading.Timer(1.0, countDown)
    t.start()

# Capture Function
def captureProcess():
    setState(2)
    camera.resolution = (imageResolution[0], imageResolution[1])
    camera.start_preview(fullscreen=True)
    sleep(5)
    camera.awb_mode = 'auto'
    camera.exposure_mode = 'sports'

    tempTime = time.strftime('%Y-%m-%d_%H-%M-%S')
    tempImageName = imageFolder + tempTime + '.jpg'

    #camera.capture(tempImageName, use_video_port = True)
    camera.stop_preview()


def main():
    setImage('Start')
        
    while True:
        # Update Window
        pygame.display.update()
                         
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    
            if listenToInput:
                if event.type == pygame.MOUSEBUTTONDOWN:
                     captureProcess()

if __name__ == '__main__':
    main()
