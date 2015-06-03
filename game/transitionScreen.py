import renpygame as pygame
import renpy.display
from animatedSprite import *
from Champion import *
import screenObjects
import os


class TransitionScreen():
    def __init__(self,bgList,animations):
        self.SCREENRECT = pygame.Rect(0, 0, 1024, 768)
        self.screen = renpy.display.pgrender.Surface(self.SCREENRECT.size,True)
        self.gameObjects = []
        self.buildTestScreen()
        self.clock = pygame.time.Clock()
        
        
    def buildTestScreen(self):
        # Build the BGSurface
        sky = screenObjects.StaticObject(screenObjects.load_image('data','SKY_BG.png'),(0,0))
        self.gameObjects.append(sky)
        
        grndtileImg = screenObjects.load_image('data','Grounds/SR_GRND.gif')
        grndtile = screenObjects.RepeatTile(grndtileImg,
                                              (0,self.SCREENRECT.bottom - grndtileImg.get_height()),
                                              20)
        self.gameObjects.append(grndtile)
        
        treeTileImg = screenObjects.load_image('data','summoner rift tree [repeatable].png')
        treetile1 = screenObjects.StaticObject(treeTileImg,
                                              (0,self.SCREENRECT[3] - treeTileImg.get_height() - 100))
        treetile2 = screenObjects.StaticObject(treeTileImg,
                                              (treeTileImg.get_width(),self.SCREENRECT[3] - treeTileImg.get_height() - 100))
        treetile3 = screenObjects.StaticObject(treeTileImg,
                                              (treeTileImg.get_width() * 2,self.SCREENRECT[3] - treeTileImg.get_height() - 100))
        
        
        self.gameObjects.extend([treetile1,treetile2,treetile3])
        
        # Build animated sprites
        poro = screenObjects.AnimatedObject((640,320),4, os.path.join(os.path.dirname(__file__),'data/Poro1'),['_1','_2','_3','_4'],5)
        self.gameObjects.append(poro)
        
        ez = screenObjects.AnimatedObject((64,320),4, os.path.join(os.path.dirname(__file__),'data/Ezreal/Idle'),
                                          ['_1','_2','_3','_4'],6)
        self.gameObjects.append(ez)
        
    def update(self):
        self.screen = renpy.display.pgrender.surface(self.SCREENRECT.size,True)
        self.clock.tick(85)
        
        for obj in self.gameObjects:
            obj.update()
        for obj in self.gameObjects:
            obj.draw(self.screen,obj.rect.topleft)
            
        return self.screen