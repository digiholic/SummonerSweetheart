import renpygame as pygame
import screenObjects
import renpy.display

dungeon = None

def getDungeon():
    global dungeon
    if dungeon:
        return dungeon
    else:
        dungeon = Dungeon()
        return dungeon
    
class Dungeon():
    def __init__(self,debug=False):
        self.camera_rect = pygame.Rect(0,0,1024,768)
        """
        if debug == True:
            self.mscreen = pygame.display.set_mode(self.camera_rect.size)
        """
        
        self.gameObjects = []
        
        pygame.init()
        self.eventList = []
        self.screen = renpy.display.pgrender.surface(self.camera_rect.size,True)
        
        self.callScene = ""
        loadScreen = screenObjects.StaticObject(screenObjects.load_image('data','Loading.png'),(0,0))
        loadScreen.draw(self.screen,(0,0))
        
        #TODO: INITIALIZATION GOES HERE
        # Initialization is IN ORDER. Earliest stuff on the bottom.
        sky = screenObjects.StaticObject(screenObjects.load_image('data','SKY_BG.png'),(0,0))
        sky.paralaxValue = 0
        self.gameObjects.append(sky)
        
        grndtileImg = screenObjects.load_image('data','Grounds/SR_GRND.gif')
        grndtile = screenObjects.InfiniteTile(grndtileImg,
                                              (0,self.camera_rect.bottom - grndtileImg.get_height()),
                                              self.camera_rect.size)
        self.gameObjects.append(grndtile)
        
        clouds1 = screenObjects.load_image('data','Clouds/clouds1.png')
        clouds2 = screenObjects.load_image('data','Clouds/clouds2.png')
        clouds3 = screenObjects.load_image('data','Clouds/clouds3.png')
        clouds = [screenObjects.StaticObject(clouds1,( 500,self.camera_rect.bottom - 730), paralaxValue = 0.7),
                  screenObjects.StaticObject(clouds2,(1030,self.camera_rect.bottom - 690), paralaxValue = 0.5),
                  screenObjects.StaticObject(clouds2,(1435,self.camera_rect.bottom - 715), paralaxValue = 0.9),
                  screenObjects.StaticObject(clouds1,(2015,self.camera_rect.bottom - 743), paralaxValue = 0.3),
                  screenObjects.StaticObject(clouds3,(2418,self.camera_rect.bottom - 760), paralaxValue = 0.5),
                  screenObjects.StaticObject(clouds1,(3272,self.camera_rect.bottom - 771), paralaxValue = 0.8),   
                  screenObjects.StaticObject(clouds3,(4699,self.camera_rect.bottom - 721), paralaxValue = 0.7)]
        
        self.cloudsGroup = pygame.sprite.Group(clouds)
        
        treeTileImg = screenObjects.load_image('data','summoner rift tree [repeatable].png')
        treetile = screenObjects.RepeatTile(treeTileImg,(490,self.camera_rect[3] - treeTileImg.get_height() - 100),20)
        self.gameObjects.append(treetile)
        
    """
    def run(self):
        self.clock = pygame.time.Clock()
        self.exitStatus = 0
        while self.exitStatus == 0:
            for event in pygame.event.get():
                self.addEvent(event)
            self.mscreen.blit(self.update(),(0,0))
            self.clock.tick(60)
            pygame.display.flip()
        return [None,None]
    """

    def addEvent(self,event):
        self.eventList.append(event)
    
    def getScreen(self):
        return self.screen
    
    def update(self):
        self.screen = renpy.display.pgrender.surface(self.camera_rect.size,True)
        for event in self.eventList:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.exitStatus = 1
                elif event.key == pygame.K_LEFT:
                    self.camera_rect.x -= 25
                elif event.key == pygame.K_RIGHT:
                    self.camera_rect.x += 25
                elif event.key == pygame.K_UP:
                    self.camera_rect.y -= 25
                elif event.key == pygame.K_DOWN:
                    self.camera_rect.y += 25
                elif event.key == pygame.K_z:
                    self.callScene = 'TestTrigger'
                    #renpy.exports.say("test","test text")
                
            elif event.type == pygame.KEYUP:
                pass
            elif event.type == pygame.MOUSEMOTION:
                pass
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pass
            elif event.type == pygame.MOUSEBUTTONUP:
                pass
            elif event.type == pygame.QUIT:
                self.exitStatus = 1
        # END EVENT LOOP #
        
        # BEGIN UPDATES #
        for obj in self.gameObjects:
            if obj.inScreen(self.camera_rect):
                obj.update()
        # END UPDATES #
        
        # BEGIN DRAWING #
        for obj in self.gameObjects:
            if obj.inScreen(self.camera_rect):
                offset = obj.stageToScreen(self.camera_rect)
                obj.draw(self.screen,offset)
        self.cloudsGroup.draw(self.screen)
        # END DRAWING #
        self.eventList = []
        return self.screen
        #pygame.display.flip()
            
if __name__ == '__main__':
    
    Dungeon(True).run()