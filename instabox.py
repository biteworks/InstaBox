#Anzeige des Bildes nach der Aufnahme funktioniert noch nicht
#Loop bei Bildaufnahme inklusive Anzeige der Nummer
#Startbildschirm
#Druckoption??

import random, pygame, sys, os
from pygame.locals import *
import picamera
import time
import ConfigParser

# Frames und Aufloesung
FPS = 25
WINDOWWIDTH = 800
WINDOWHEIGHT = 480
EVENTNAME = 'wedding'
IMAGEFOLDER = '/home/pi/Desktop/InstaBox-Images/'

# Pygame und Kamera initialisieren
cam = picamera.PiCamera()
pygame.init()

# Fenster erstellen
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('InstaBox')
pygame.mouse.set_visible(False)

# Kamera-Vorschau starten
def startCam():
    cam.start_preview(fullscreen=False,window=(0,0,800,480))
    cam.vflip = True
    cam.hflip = True

# Kamera-Vorschau beenden
def endCam():
    cam.stop_preview()

# Bild aufnehmen in maximaler Aufloesung
def captureImg(imgName):
    cam.exposure_mode = 'sports'
    cam.resolution = (2592, 1944)
    cam.capture(IMAGEFOLDER + imgName + '.jpg');
    
# Bild anzeigen
def displayImg(imgName):
    img = pygame.image.load(IMAGEFOLDER + imgName + '.jpg')
    pygame.display.blit(img, (0, 0))
    
# Countdown und Aufnahme
def captureProcess():
    startCam()
    time.sleep(3)
    endCam()

    # Starte den Aufnahmeprozess
    #(soll noch in Loop um das Ganze drei mal zu machen)
    print("3")
    pygame.time.delay(1000)
    print("2")
    pygame.time.delay(1000)
    print("1")
    pygame.time.delay(1000)  
    print("Bitte lachen!")
    tempTime = time.strftime('%Y-%m-%d_%H-%M-%S')
    tempImgName = tempTime + '_' + EVENTNAME
    print (tempImgName)

    # Bild aufnehmen
    captureImg(tempImgName)
    pygame.time.delay(1000)

    #Bild anzeigen
    #displayImg(tempImgName)
    

def main():
    while True:
        # Update des Renderfensters 
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    captureProcess()

if __name__ == '__main__':
    main()
