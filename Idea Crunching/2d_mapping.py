# program should use the output of a Ultra-Sonic sensor and create a 2d map get a simple program to display an
# object informant of the sensor and how far it is( colour the object depending on distance eg; red=close, green=far)
from dis import dis
from math import dist
import pygame
import random

#Libraries
import RPi.GPIO as GPIO
import time
 
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#set GPIO Pins
GPIO_TRIGGER = 23
GPIO_ECHO = 24
 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
 
def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance
 


pygame.init()
pygame.display.set_caption('2d Map')
screen = pygame.display.set_mode((700,700))

def display_quit(): # closes the display
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        
    return True

def redraw(): # update's the display frames
    pygame.time.delay(10)
    screen.fill((255,255,255))
    screen.fill((0,0,0),(0,0,200,700))
    screen.fill((0,0,0),(500,0,200,700))
    


    #x=random.randrange(650)
    #detect(x)
    dist=distance()
    ultra_sonic_visual.senosr(dist)
    pygame.display.update()


class Detect():
    def senosr(self, distance=0):
        if distance==0:
            pass
        else:
            self.detect_display(distance) # Todo create ratio between display size and real world 
        

    def detect_display(self,dist):
        if dist <= 700//3: # colours object depending on distance
            colour=(255,0,0)
            print(dist, colour)
        elif dist >=700//3 and dist<=700//2:
            colour=(255,255, 0)
            print(dist, colour)
        else:
            colour=(0,255,0)
            print(dist, colour)

        pygame.draw.rect(screen, colour, (330,dist,50,50))
    

ultra_sonic_visual = Detect()


def main():
    display_run = True
    while display_run:
        display_run = display_quit()
        redraw()
if __name__ == '__main__':
    try:
        while True:
            main()
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()

print('exceuted')