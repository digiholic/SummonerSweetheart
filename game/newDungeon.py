import pygame
pygame.font.init()
import renpygame
import summonersRift
import os

class Battle(renpy.Displayable):
    def __init__(self, **kwargs):
        global battleNumber
        super(Battle, self).__init__(**kwargs)
        self.width = 1024
        self.height = 768
        self.loadBattle(battleNumber)
    
    def loadBattle(self, number):
        pass
    
    def render(self, width, height, st, at):
          pass
    
    def event(self, ev, x, y, st):
        pass
    
class AnimatedObject(renpy.Displayable):
    def __init__(self, directory, prefix, defaultImage, offset, **kwargs):
        super(AnimatedObject, self).__init__(**kwargs)
        self.directory = directory
        self.prefix = prefix
        self.startingImage = defaultImage
        self.width = offset
        
        self.subImage = 0
        self.location = (0,0)
        self.imageLibrary = self.buildImageLibrary(directory, prefix)
    
    def render(self, width, height, st, at):
        pass
  
    def buildImageLibrary(self,directory, prefix):
        imageDict = {}
        fullPath = os.path.join(renpy.config.gamedir,directory)
        for f in os.listdir(fullPath):
            fname, ext = os.path.splitext(f)
            if fname.startswith(prefix):
                spriteName = fname[len(prefix):]
                fp = os.path.join(fullPath,f)
                imageDict[spriteName] = fp
                return imageDict
           
class Fighter(AnimatedObject):
    def __init__(self, **kwargs):
        pass