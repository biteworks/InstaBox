#Composition in der Groesse anpassen
#Eventuell effekte
#Counter in Textdatei packen
#Bild fuer die Bearbeitung
#Startbildschirm
#Druckoption??

import random, pygame, sys, os
from pygame.locals import *
import picamera
import time
#import ConfigParser

# Variablen
FPS = 25
WINDOWWIDTH = 800
WINDOWHEIGHT = 480
EVENTNAME = 'hochzeit'
RAWIMAGEFOLDER = '/home/pi/Desktop/InstaBox-Images/Single/'
COMPIMAGEFOLDER = '/home/pi/Desktop/InstaBox-Images/Comp/'
listenToInput = True

# Screens

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
    cam.capture(imgName);
    
# Bild anzeigen
def displayImg(imgName):
    global listenToInput
    img = pygame.image.load(imgName)
    DISPLAYSURF.blit(img, (0, 0))
    listenToInput = True

def displayProcess(comp):
    print('Hier soll angezeigt werden, dass die Bilder verarbeitet werden')
    # 10 Sekunden Delay
    pygame.time.delay(10000)
    displayImg(comp)

def compositeImgs(imgNames):
    comp = COMPIMAGEFOLDER + time.strftime('%Y-%m-%d_%H-%M-%S') + '_' + EVENTNAME + '_comp.jpg'
    command = "montage " + imgNames[0] + ' ' + imgNames[1] + ' ' + imgNames[2] + ' ' + imgNames[3] + ' -geometry 1296x972+2+2 ' + comp + '&'
    os.system(command)
    displayProcess(comp)
    
# Countdown und Aufnahme
def captureProcess():
    global listenToInput
    listenToInput = False
    
    # Liste mit Bildnahmen loeschen
    imgNames = []
    
    # Kamerabild Anzeigen
    startCam()

    # Delay von 3 Sekunden
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
        tempImgName = RAWIMAGEFOLDER + tempTime + '.jpg'
        
        # Bild aufnehmen und Bildnahme an das Array anhaengen
        cam.annotate_text = ""
        captureImg(tempImgName)
        
        imgNames.append(tempImgName)
        cam.resolution = (800, 480)
        
        if i == 1:
            pygame.time.delay(1000)

        else:
            pygame.time.delay(500)

    # Kamera Bild beenden
    endCam()
    
    print imgNames
    compositeImgs(imgNames)
    
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
            if listenToInput:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        captureProcess()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    (mouseX, mouseY) = pygame.mouse.get_pos()
                    print mouseX, mouseY
                    captureProcess()

if __name__ == '__main__':
    main()
