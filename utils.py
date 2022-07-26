import pygame as pg
from pygame import *

def shaded_image(image, color):
    m = pg.mask.from_surface(image, 0)
    shader = pg.Surface((image.get_size()), masks=m).convert_alpha()
    shader.fill(color)
    copied = image.copy()
    copied.blit(shader, (0,0), special_flags=pg.BLEND_RGBA_MULT)
    return copied

def rot_center(image, angle, pos_center):

    rotated_image = pg.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(center = pos_center).center)

    return rotated_image, new_rect
