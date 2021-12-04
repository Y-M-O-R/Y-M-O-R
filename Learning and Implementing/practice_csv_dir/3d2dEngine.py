# engine that projects 3d to 2d
import pygame
import math

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600

fps           = 60;                      # how many 'update' frames per second
step          = 1/fps;                   # how long is each frame (in seconds)
width         = 1024;                    # logical canvas width
height        = 768;                     # logical canvas height
segments      = [];                      # array of road segments
canvas        = Dom.get('canvas');       # our canvas...
ctx           = canvas.getContext('2d'); # ...and its drawing context
background    = null;                    # our background image (loaded below)
sprites       = null;                    # our spritesheet (loaded below)
resolution    = null;                    # scaling factor to provide resolution independence (computed)
roadWidth     = 2000;                    # actually half the roads width, easier math if the road spans from -roadWidth to +roadWidth
segmentLength = 200;                     # length of a single segment
rumbleLength  = 3;                       # number of segments per red/white rumble strip
trackLength   = null;                    # z length of entire track (computed)
lanes         = 3;                       # number of lanes
fieldOfView   = 100;                     # angle (degrees) for field of view
cameraHeight  = 1000;                    # z height of camera
cameraDepth   = null;                    # z distance camera is from screen (computed)
drawDistance  = 300;                     # number of segments to draw
playerX       = 0;                       # player x offset from center of road (-1 to 1 to stay independent of roadWidth)
playerZ       = null;                    # player relative z distance from camera (computed)
fogDensity    = 5;                       # exponential fog density
position      = 0;                       # current camera Z position (add playerZ to get player's absolute Z position)
speed         = 0;                       # current speed
maxSpeed      = segmentLength/step;      # top speed (ensure we can't move more than 1 segment in a single frame to make collision detection easier)
accel         =  maxSpeed/5;             # acceleration rate - tuned until it 'felt' right
breaking      = -maxSpeed;               # deceleration rate when braking
decel         = -maxSpeed/5;             # 'natural' deceleration rate when neither accelerating, nor braking
offRoadDecel  = -maxSpeed/2;             # off road deceleration is somewhere in between
offRoadLimit  =  maxSpeed/4;

def resetRoad():
    segments= []
    for roadLength in range(500):
        screen_point1 =   {'world':{'z': roadLength *segmentLength,'x': 0, 'y': 0},'camera':{'x': 0, 'y': 0}, 'screen':{'x': 0, 'y': 0}}
        screen_point1 =   {'world':{'z':(roadLength+1)*segmentLength,'x': 0, 'y': 0},'camera':{'x': 0, 'y': 0}, 'screen':{'x': 0, 'y': 0}}
        colour = math.floor(roadLength/rumbleLength%2)
        segments.append({roadLength, screen_point1, screen_point2})

class Util:  # general purpose  maths
    def project(self, point, x_camera, y_camera, z_camera, z, distance):  # camera translated to 2d plane
        # translate from world coordinate to camera coordinate (3d coordinates to 2d coordinates)
        point['camera']['x'] = (point['world']['x'] or 0)- x_camera
        point['camera']['y'] = (point['world']['y'] or 0)- y_camera
        point['camera']['z'] = (point['world']['z'] or 0)- z_camera
        # project and scale cordinates for 2d plane
        point['scree']
class Camera:
    def __init__(self):
        self.fov = 90  # degree # todo tweak later
        self.distance = 1 / math.tan(self.fov / 2)


class Segment:
    def __init__(self):
        pass