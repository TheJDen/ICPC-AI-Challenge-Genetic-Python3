import math
from collections import namedtuple

dflt_width = 7600
dflt_height = 4200

Vector2D = namedtuple("Vector2D", ['x', 'y'])

class Artifact:
    def __init__(self, coords):
        self.pos = coords

    @property
    def pos(self):
        return self._pos

    @pos.setter
    def pos(self, coords):
        self._pos = Vector2D(*coords)

class Ship:

    def __init__(self, coords=(0,0), bearing=90.0):
        self._pos = Vector2D(*coords)
        self.bearing = bearing
        # self.vel = Vector2D(0,0)

    @property
    def pos(self):
        return self._pos

    @pos.setter
    def pos(self, coords):
        new_pos = Vector2D(*coords)
        # self.vel = Vector2D(new_pos.x - self._pos.x, new_pos.y - self._pos.y)
        self._pos = new_pos

class Player:
    def __init__(self, perceptron=lambda x:(1,1,0,0,0,1)):
        self.perceptron = perceptron
        self.ship = Ship()

class World:
    
    def __init__(self, player, width=dflt_width, height=dflt_height):
        self.player = player
        self.width = width
        self.height = height
        self.artifact = None

    def update(self, state):
        try: self.artifact.pos = state["artfPos"]
        except: self.artifact = Artifact(state["artfPos"])
        self.player.ship.pos = state["shipPos"]
        self.player.ship.bearing = state["shipR"]

    def min_displacements_to(self, world_obj): # toroidal
        dx = world_obj.pos.x - self.player.ship.pos.x
        dy = world_obj.pos.y - self.player.ship.pos.y
        dx = (dx + self.width/2) % self.width - self.width/2 # black magic
        dy = (dy + self.height/2) % self.height - self.height/2
        return Vector2D(dx,dy)