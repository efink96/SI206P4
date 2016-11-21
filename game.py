import random
import sys

import pygame

# top-down shooter, probably
from pygame.locals import K_LEFT, K_RIGHT, K_SPACE, Rect

X_MAX = 600
Y_MAX = 600

everything = pygame.sprite.Group()