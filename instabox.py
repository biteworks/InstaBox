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
EVENTNAME = 'hochzeit'
IMAGEFOLDER = '/home/pi/Desktop/InstaBox-Images/'

# Pygame und Kamera initialisieren
cam = picamera.PiCamera()
cam.led = False
pygame.init()
    
# Fenster erstellen
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('InstaBox')
pygame.mouse.set_visible(False)

# Kamera-Vorschau starten
def startCam():
    cam.start_preview(fullscreen=False,window=(0,0,800,480))
    #cam.annotate_text = 'hello world'
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
    DISPLAYSURF.blit(img, (0, 0))

def compositeImgs(imgNames):
    command = "sdnsd"
    
# Countdown und Aufnahme
def captureProcess():
    startCam()
    pygame.time.delay(3000)

    # Starte den Aufnahmeprozess (4 Bilder)
    for i in range(4):
        cam.annotate_text_size = 60
        cam.annotate_text = "3"
        
        pygame.time.delay(1000)
        cam.annotate_text = "2"
        
        pygame.time.delay(1000)
        cam.annotate_text = "1"
        
        pygame.time.delay(1000)
        cam.annotate_text = "Bitte lachen!"
        
        pygame.time.delay(1500)
        
        # Zeitstempel fuer das Bild setzen
        tempTime = time.strftime('%Y-%m-%d_%H-%M-%S')
        tempImgName = tempTime + '_' + EVENTNAME
        
        # Bild aufnehmen
        cam.annotate_text = ""
        captureImg(tempImgName)
        cam.resolution = (800, 480)
        
        if i == 1:
            pygame.time.delay(1000)

        else:
            pygame.time.delay(500)

    # Kamera Bild beenden
    endCam()
    
    #Fertiges Bild anzeigen
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
            if event.type == pygame.MOUSEBUTTONDOWN:
                (mouseX, mouseY) = pygame.mouse.get_pos()
                print mouseX, mouseY
                captureProcess()

if __name__ == '__main__':
    main()
