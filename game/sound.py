
import renpygame as pygame

from renpygame.locals import *

import renpy.store as store
import renpy.exports as renpy

import BattleGameEngine as BattleEngine

if not pygame.image.get_extended():
    raise SystemExit,"sorry, extended image module required"


def load_sound(file):
    if not pygame.mixer: return dummysound()
    file = os.path.join('data', file)
    try:
        sound = pygame.mixer.Sound(file)
        return sound
    except pygame.error:
        print 'Warning, unable to load,', file
    return dummysound()






