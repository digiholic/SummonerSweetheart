import renpygame as pygame
import screenObjects
import renpy.display
import os

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
        
        self.route = True
        self.battle = Battle([Ezreal(),Ahri(),Soraka(),Rengar()],[])
        #self.battle = None
        
        self.gameObjects = []
        
        
        pygame.init()
        self.eventList = []
        self.screen = renpy.display.pgrender.surface(self.camera_rect.size,True)
        
        self.callScene = ""
        
        loadScreen = screenObjects.StaticObject(screenObjects.load_image('data','Loading.png'),(0,0))
        loadScreen.draw(self.screen,(0,0))
        
        
        
        
        
        
        # Initialization is IN ORDER. Earliest stuff on the bottom.
        sky = screenObjects.StaticObject(screenObjects.load_image('data','SKY_BG.png'),(0,0),0)
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
        
        #treeTileImg = screenObjects.load_image('data','summoner rift tree [repeatable].png')
        #treetile = screenObjects.InfiniteTile(treeTileImg,(490,self.camera_rect[3] - treeTileImg.get_height() - 100),self.camera_rect.size)
        #self.gameObjects.append(treetile)
        
        self.player = Player(self,True)
        self.player.update()
        
        self.clock = pygame.time.Clock()
        
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

    def loadFromVN(self,pass_list):
        if pass_list[0]: #Route == True means Ezreal
            self.battleChamps = [Ezreal(),Ahri()]
        else:    
            self.battleChamps = []
            
    def addEvent(self,event):
        self.eventList.append(event)
    
    def getScreen(self):
        return self.screen
    
    def update(self):
        self.clock.tick(60)
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
                elif event.key == pygame.K_d:
                    if self.player.currentSheet == 'idle': self.player.changeImage('walk', 0)
                elif event.key == pygame.K_q:
                    if self.battle:
                        self.battle.doAttack(3)
                elif event.key == pygame.K_w:
                    if self.battle:
                        self.battle.doAttack(2)
                elif event.key == pygame.K_e:
                    if self.battle:
                        self.battle.doAttack(1)
                elif event.key == pygame.K_r:
                    if self.battle:
                        self.battle.doAttack(0)
                                                
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    self.player.changeImage('idle', 0)
            
            elif event.type == pygame.MOUSEMOTION:
                pass
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pass
            elif event.type == pygame.MOUSEBUTTONUP:
                pass
            elif event.type == pygame.QUIT:
                self.exitStatus = 1
        # END EVENT LOOP #
        
        # BEGIN BACKGROUNDS
        for obj in self.gameObjects:
            obj.update()
        for obj in self.gameObjects:
            obj.draw(self.screen,obj.rect.topleft)
        
        self.cloudsGroup.draw(self.screen)    
        # END BACKGROUNDS
        
        # BEGIN UPDATES #
        if self.battle:
            self.screen = self.battle.update(self.screen)
            
        else:
            # BEGIN UPDATE #
            self.player.update()
            # END UPDATE #
            
            # BEGIN DRAWING #
            self.player.draw(self.screen, self.player.rect.topleft)    
            # END DRAWING #
            
        self.eventList = []
        return self.screen
        #pygame.display.flip()
            
class Champion(screenObjects.MultiAnimationObject):
    def __init__(self):
        screenObjects.MultiAnimationObject.__init__(self, self.directory, self.prefix, 'idleB',self.offset)
        self.attacking = False
        self.frame = 0
        self.delay = 0
        self.currentCD = 0
        self.hp = 100
        
    def update(self):
        if self.currentCD > 0:
            self.currentCD -= 1
        if self.delay == 2:
            self.changeSubImage(self.frame)
            self.frame += 1
            self.delay = 0
            if self.frame >= self.get_length():
                self.frame = 0
                if self.attacking and self.currentSheet == 'attack':
                    self.attacking = False
                    self.changeImage('idleB')
        else:
            self.delay += 1
        
    def doAttack(self):
        print "attacking", self.currentCD
        if not self.attacking and self.currentCD == 0:
            self.attacking = True
            self.currentCD = self.attackCD
            self.frame = 0
            self.changeImage('attack')
        
class Ezreal(Champion):
    def __init__(self):
        self.directory = 'data/Ezreal'
        self.prefix = 'ezreal_'
        self.offset = 250
        self.attackCD = 120
        self.centerOffset = 0
        
        Champion.__init__(self)
        
class Ahri(Champion):
    def __init__(self):
        self.directory = 'data/Ahri'
        self.prefix = 'ahri_'
        self.offset = 275
        self.attackCD = 120
        self.centerOffset = 50
        
        Champion.__init__(self)
        
class Soraka(Champion):
    def __init__(self):
        self.directory = 'data/Soraka'
        self.prefix = 'soraka_'
        self.offset = 180
        self.attackCD = 120
        self.centerOffset = 0
        
        Champion.__init__(self)

class Rengar(Champion):
    def __init__(self):
        self.directory = 'data/Rengar'
        self.prefix = 'rengar_'
        self.offset = 250
        self.attackCD = 120
        self.centerOffset = 50
        
        Champion.__init__(self)


class Enemy(screenObjects.MultiAnimationObject):
    def __init__(self):
        pass
    
    

class Player(screenObjects.MultiAnimationObject):
    def __init__(self,dungeon,route):
        self.dungeon = dungeon
        self.frame = 0
        self.delay = 0
        
        if route == True:
            self.directory = 'data/Ezreal'
            self.prefix = 'ezreal_'
            self.startingImage = 'idle'
            self.offset = 150
        else:
            self.directory = 'data/Ezreal'
            self.prefix = 'ezreal_'
            self.startingImage = 'idle'
            self.offset = 150
        
        screenObjects.MultiAnimationObject.__init__(self, self.directory, self.prefix, self.startingImage, self.offset)
        self.rect.topleft = (200,self.dungeon.camera_rect.height - 300)
        
    def update(self):
        if self.delay == 2:
            self.changeSubImage(self.frame)
            self.frame += 1
            self.delay = 0
            if self.frame >= self.get_length():
                self.frame = 0
        else:
            self.delay += 1
            
class Battle():
    def __init__(self,players,enemies):
        self.players = players
        self.enemies = enemies
        for i in range(0,len(self.players)):
            self.players[i].rect.left = self.players[i].centerOffset + (450 - (150*i))
            self.players[i].rect.bottom = 668
        
    def update(self,screen):
        # UPDATE
        for ch in self.players:
            ch.update()
        for en in self.enemies:
            en.update()
            
        # DRAW
        for ch in self.players:
            ch.draw(screen,ch.rect.topleft)
        for en in self.enemies:
            en.draw(screen,en.rect.topleft)
            
        return screen
    
    def doAttack(self,i):
        self.players[i].doAttack()