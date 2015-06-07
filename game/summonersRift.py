import renpygame as pygame
import screenObjects
import renpy.display
import os
import random

dungeon = None

def getDungeon():
    global dungeon
    if dungeon:
        return dungeon
    else:
        dungeon = Dungeon()
        return dungeon
    
def getRetList():
    global dungeon
    return [dungeon.gifts,dungeon.bossesDefeated]
class Dungeon():
    def __init__(self):
        self.camera_rect = pygame.Rect(0,0,1024,768)
        
        self.banner = Banner() # This one's big, want to load it only once
        
        
        self.route = True
        self.currentBattle = 0
        self.battle = None
        self.bossesDefeated = 0
        
        #self.battle = None
        
        self.gameObjects = []
        
        pygame.init()
        self.eventList = []
        self.screen = renpy.display.pgrender.surface(self.camera_rect.size,True)
        
        self.callScene = ""
        self.finished = False
        
        loadScreen = screenObjects.StaticObject(screenObjects.load_image('data','Loading.png'),(0,0))
        loadScreen.draw(self.screen,(0,0))
        
        self.victorySound = pygame.mixer.Sound('data/music/VictoryTheme2.wav')
        
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
            self.battleChamps = [Ezreal(),Ahri(),Soraka(),Rengar()]
        else:    
            self.battleChamps = []
        
        self.battles = [Battle(self, self.battleChamps, [Poro(),Poro()], "afterFirstBattle"),
                        #Battle(self, self.battleChamps, [Poro(),Poro(),Poro()]    ),
                        #Battle(self, self.battleChamps, [Poro(),MrPoro(),Poro()]  ),
                        #Battle(self, self.battleChamps, [MrPoro(),Poro(),MrPoro()]),
                        FinalBattle(self, self.battleChamps),
                        Battle(self, self.battleChamps, [Baron()],music = 'data/music/bossBattle.ogg'),
                        Battle(self, self.battleChamps, [Cinderling(-150), Brambleback(), Cinderling(-100)], music = 'data/music/bossBattle.ogg'),
                        Battle(self, self.battleChamps, [MrPoro(), MrPoro(), Cinderling()])]
        
        self.gifts = pass_list[1]
        self.specialMoves = pass_list[2]
        self.sceneKeys = pass_list[3]
        self.startBattle()
        
    def startBattle(self):
        self.battle = self.battles[self.currentBattle]
        pygame.mixer.music.load(self.battle.music)
        self.battle.initialize(self.battleBG(self.currentBattle))
        
    def endBattle(self):
        pygame.mixer.music.stop()
        self.victorySound.play()
        self.currentBattle += 1
        self.callScene = self.battle.endScene
        
    def addEvent(self,event):
        if event.type == pygame.KEYDOWN:
            self.eventList.append(event.key)
    
    def getScreen(self):
        self.screen = renpy.display.pgrender.surface(self.camera_rect.size,True)
        self.screen = self.battle.updateAnimOnly(self.screen)    
        return self.screen
        
    def battleBG(self,bgNumber):
        gameObjects = []
        screen = renpy.display.pgrender.surface(self.camera_rect.size,True)
        
        print bgNumber
        if bgNumber < 10:
            # Initialization is IN ORDER. Earliest stuff on the bottom.
            sky = screenObjects.StaticObject(screenObjects.load_image('data','SKY_BG.png'),(0,0),0)
            gameObjects.append(sky)
        
            grndtileImg = screenObjects.load_image('data','Grounds/SR_GRND.gif')
            grndtile = screenObjects.InfiniteTile(grndtileImg,
                                              (0,self.camera_rect.bottom - grndtileImg.get_height()),
                                              self.camera_rect.size)
            gameObjects.append(grndtile)
        
            treeTileImg = screenObjects.load_image('data','summoner rift tree [repeatable].png')
            if bgNumber % 2 == 0:
                treetiles = [screenObjects.StaticObject(treeTileImg,(0,self.camera_rect[3] - treeTileImg.get_height() - 100)),
                             screenObjects.StaticObject(treeTileImg,(treeTileImg.get_width(),self.camera_rect[3] - treeTileImg.get_height() - 100))]
            else:
                treetiles = [screenObjects.StaticObject(treeTileImg,(-88,self.camera_rect[3] - treeTileImg.get_height() - 100)),
                             screenObjects.StaticObject(treeTileImg,(treeTileImg.get_width() - 88,self.camera_rect[3] - treeTileImg.get_height() - 100))]
            
            gameObjects.extend(treetiles)
            
            for obj in gameObjects:
                obj.draw(screen,obj.rect.topleft)
            return screen
            
    def update(self):
        self.screen = renpy.display.pgrender.surface(self.camera_rect.size,True)
        
        for event in self.eventList:
            if event == pygame.K_ESCAPE:
                self.exitStatus = 1
            elif event == pygame.K_LEFT:
                self.battle.changeTarget(1)
            elif event == pygame.K_RIGHT:
                self.battle.changeTarget(-1)
            elif event == pygame.K_q:
                self.battle.doPlayerAttack(3)
            elif event == pygame.K_w:
                self.battle.doPlayerAttack(2)
            elif event == pygame.K_e:
                self.battle.doPlayerAttack(1)
            elif event == pygame.K_r:
                self.battle.doPlayerAttack(0)
        # END EVENT LOOP #
        
        self.screen = self.battle.update(self.screen)    
        self.eventList = []
        
        return self.screen
        #pygame.display.flip()

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
                        
class Champion(screenObjects.MultiAnimationObject):
    def __init__(self):
        screenObjects.MultiAnimationObject.__init__(self, self.directory, self.prefix, 'idleB',self.offset)
        self.attacking = False
        self.frame = 0
        self.delay = 0
        self.currentCD = 0
        self.hp = self.maxHP
        self.alive = True
        self.active = False
        
    def setBattle(self,battle):
        self.battle = battle
        
    def update(self):
        if self.currentCD > 0:
            self.currentCD -= 1
        self.updateAnim()
        
    def updateAnim(self):
        if self.delay == 2:
            self.changeSubImage(self.frame)
            self.frame += 1
            self.delay = 0
            if self.frame >= self.get_length():
                self.frame = 0
                if self.attacking != None and self.currentSheet == 'attack':
                    self.attacking.getAttacked(self.attackDamage)
                    self.attacking = None
                    self.changeImage('idleB')
        else:
            self.delay += 1
    
    def doAttack(self,target):
        if not self.attacking and self.currentCD == 0:
            self.attacking = target
            self.currentCD = self.attackCD
            self.frame = 0
            self.changeImage('attack')
            self.attackSound.play()
            #TODO animation
            
    def getAttacked(self,damage):
        self.hp -= damage
        self.hurtSound.play()
        print self.prefix, self.hp
        if self.hp <= 0: self.alive = False
        
class Enemy(screenObjects.MultiAnimationObject):
    def __init__(self, directory, prefix, offset, centerOffset, attackCD, maxHP, attackDamage):
        self.directory = directory
        self.prefix = prefix
        self.offset = offset
        self.centerOffset = centerOffset
        self.attackCD = attackCD
        self.maxHP = maxHP
        self.attackDamage = attackDamage
        
        screenObjects.MultiAnimationObject.__init__(self, self.directory, self.prefix, 'idle', self.offset)
        self.currentCD = random.randint(0,self.attackCD)
        self.hp = self.maxHP
        
        self.alive = True
        self.attacking = False
        self.active = False
        
        self.frame = 0
        self.delay = 0
        
    def setBattle(self,battle):
        self.battle = battle
        
    def update(self):
        if self.active:
            if self.currentCD > 0:
                self.currentCD -= 1
            
        self.updateAnim()
    
    def updateAnim(self):
        if self.delay == 2:
            self.changeSubImage(self.frame)
            self.frame += 1
            self.delay = 0
            if self.frame >= self.get_length():
                self.frame = 0
                if self.attacking:
                    self.attacking = False
        else:
            self.delay += 1
            
    def doAttack(self,target):
        if not self.attacking and self.currentCD == 0:
            self.attacking = True
            self.currentCD = self.attackCD
            self.frame = 0
            #self.changeImage('attack')
            #TODO Animation
            target.getAttacked(self.attackDamage)
        
    def chooseTarget(self):
        return random.randint(0,len(self.battle.players))
        
    def getAttacked(self,damage):
        self.hp -= damage
        self.battle.effects.add(self.getHurtSprite(0))
        if self.hp <= 0:
            self.alive = False
      
    def getHurtSprite(self,frameDelay = 1):
        spr = screenObjects.SheetAnimatedObject(self.directory, self.prefix+'die.png', self.offset, frameDelay)
        spr.rect = self.rect
        return spr
      
class Battle():
    def __init__(self,dungeon,players,enemies,endScene = "victoryScreen", music='data/music/BattleStance.wav'):
        self.players = players
        self.enemies = enemies
        self.endScene = endScene
        
        self.dungeon = dungeon
        self.music = music
        
        self.effects = pygame.sprite.Group()
        #self.effects.add(self.dungeon.banner)
        
        self.ui = pygame.sprite.Group()
        self.targetArrow = Arrow()
        
        self.currentTarget = 0
        self.state = 0 # state 0, start animation, state 1, actual battle, state 2, going onward, state 3, going backward
        
        self.bg = None
        
    def initialize(self,bg):
        self.bg = bg
        
        for i in range(0,len(self.players)):
            self.players[i].active = False
            self.players[i].rect.left = self.players[i].centerOffset + (300 - (100*i))
            self.players[i].rect.bottom = 668
            self.players[i].setBattle(self)
            
        for i in range(0,len(self.enemies)):
            self.enemies[i].active = False
            self.enemies[i].rect.right = self.enemies[i].centerOffset + (1024 - (100*i))
            self.enemies[i].rect.bottom = 668
            self.enemies[i].setBattle(self)
        
        self.targetArrow.rect.bottom = self.enemies[self.currentTarget].rect.centery
        self.targetArrow.rect.centerx = self.enemies[self.currentTarget].rect.centerx
        
        self.players[0].rect.right = 0
        self.players[0].changeImage('walkB')
        self.players[0].active = True
    
    def updateAnimOnly(self,screen):
        screen.blit(self.bg, (0,0))
        
        for ch in self.players:
            ch.updateAnim()
        
        for en in self.enemies:
            en.updateAnim()
            
        for ef in self.effects:
            ef.update()
        
        for ui in self.ui:
            ui.update()        
        
        # DRAW
        for ch in reversed(self.players):
            if ch.alive and ch.active:
                ch.draw(screen,ch.rect.topleft)
        
        for en in self.enemies:
            if en.alive:
                en.draw(screen,en.rect.topleft)
        
        self.effects.draw(screen)
        self.ui.draw(screen)
            
        return screen
        
    def update(self,screen):
        screen.blit(self.bg,(0,0))
        
        if self.state == 0:
            # Make the main character walk into position
            mc = self.players[0]
            mc.rect.x += 15
            
            for i in range(1,len(self.players)):
                if mc.rect.left >= self.players[i].centerOffset + (300 - (100*i)):
                    self.players[i].active = True
            
            if mc.rect.left >= 300 + mc.centerOffset:
                mc.rect.left = 300 + mc.centerOffset
                mc.changeImage('idleB')
                for en in self.enemies: en.active = True
                
                self.ui.add(self.targetArrow)
                pygame.mixer.music.play(-1)
                
                self.state = 1
                    
        elif self.state == 1:
            
            for i in range(0,len(self.enemies)):
                en = self.enemies[i]
                if en.alive and en.currentCD == 0:
                    self.doEnemyAttack(i)
                    en.currentCD = en.attackCD
            
            for en in self.enemies:
                if not en.alive:
                    self.enemies.remove(en)
                    self.effects.add(en.getHurtSprite())
                    self.changeTarget(1)
            
            if len(self.enemies) == 0:
                for ch in self.players:
                    ch.attacking = None
                    ch.changeImage('idleB')
                if len(self.effects) == 0:
                    self.dungeon.endBattle()
                  
        # Onward Animation
        elif self.state == 2:
            mc = self.players[0]
            mc.rect.x += 15
            if mc.rect.left >= 1024:
                self.dungeon.startBattle()
            
        # Exit Animation
        elif self.state == 3:
            mc = self.players[0]
            mc.rect.x -= 15
            if mc.rect.right < 0:
                mc.flipX()
                self.dungeon.finished = True
                pygame.mixer.music.fadeout(1000)
                
            for i in range(1,len(self.players)):
                if mc.rect.left <= self.players[i].centerOffset + (300 - (100*i)):
                    self.players[i].active = False
                
        for ch in self.players:
            ch.update()
        
        for en in self.enemies:
            en.update()
            
        for ef in self.effects:
            ef.update()
        
        for ui in self.ui:
            ui.update()        
        
        # DRAW
        for ch in reversed(self.players):
            if ch.alive and ch.active:
                ch.draw(screen,ch.rect.topleft)
        
        for en in self.enemies:
            if en.alive:
                en.draw(screen,en.rect.topleft)
            
        self.effects.draw(screen)
        self.ui.draw(screen)
        
        return screen
    
    def onward(self):
        self.state = 2
        for pl in self.players:
                pl.changeImage('idleB',0)
                pl.attacking = None
        mc = self.players[0]
        mc.changeImage('walkB',0)
        
    def retreat(self):
        self.state = 3
        for pl in self.players:
                pl.changeImage('idleB',0)
        mc = self.players[0]
        mc.flipX()
        mc.changeImage('walkB',0)
    
    def doPlayerAttack(self,i):
        if self.state == 1:
            if len(self.enemies) > 0:
                en = self.enemies[self.currentTarget]
                while not en.alive:
                    self.changeTarget(1)
                    en = self.enemies[self.currentTarget]
                try:
                    self.players[i].doAttack(en)
                except:
                    pass
            
    def doEnemyAttack(self,i):
        if self.state == 1:
            j = self.enemies[i].chooseTarget()
            while not self.players[j].alive:
                j = self.enemies[i].chooseTarget()
            
            self.enemies[i].doAttack(self.players[j])
        
    def changeTarget(self,amt):
        self.currentTarget += amt
        l = len(self.enemies)
        if l > 0:
            self.currentTarget = (l + self.currentTarget) % l
            self.targetArrow.rect.bottom = self.enemies[self.currentTarget].rect.centery
            self.targetArrow.rect.centerx = self.enemies[self.currentTarget].rect.centerx
        else:
            self.targetArrow.kill()

class FinalBattle(Battle):
    def __init__(self, dungeon, players):
        enemies = [Doran()]
        
        Battle.__init__(self, dungeon, players, enemies)
        self.players = players
        self.enemies = enemies
        self.endScene = ""
        
        self.dungeon = dungeon
        self.music = ""
        
        self.effects = pygame.sprite.Group()
        #self.effects.add(self.dungeon.banner)
        
        self.currentTarget = 0
        self.state = 0 # state 0, start animation, state 1, actual battle, state 2, going onward, state 3, going backward
        
        self.bg = None
    
    def update(self,screen):
        screen.blit(self.bg,(0,0))
        
        if self.state == 0:
            # Make the main character walk into position
            mc = self.players[0]
            mc.rect.x += 15
            
            for i in range(1,len(self.players)):
                if mc.rect.left >= self.players[i].centerOffset + (300 - (100*i)):
                    self.players[i].active = True
            
            if mc.rect.left >= 300 + mc.centerOffset:
                mc.rect.left = 300 + mc.centerOffset
                mc.changeImage('idleB')
                for en in self.enemies: en.active = True
                
                self.ui.add(self.targetArrow)
                
                self.state = 4
                self.dungeon.callScene = 'beforeHacker'
                
        elif self.state == 1:
            
            for i in range(0,len(self.enemies)):
                en = self.enemies[i]
                if en.alive and en.currentCD == 0:
                    self.doEnemyAttack(i)
                    en.currentCD = en.attackCD
            
            for en in self.enemies:
                if not en.alive:
                    self.enemies.remove(en)
                    self.effects.add(en.getHurtSprite())
                    self.changeTarget(1)
            
            if len(self.enemies) == 0:
                for ch in self.players:
                    ch.attacking = None
                    ch.changeImage('idleB')
                if len(self.effects) == 0:
                    self.dungeon.endBattle()
                  
        # Onward Animation
        elif self.state == 2:
            mc = self.players[0]
            mc.rect.x += 15
            if mc.rect.left >= 1024:
                self.dungeon.startBattle()
            
        # Exit Animation
        elif self.state == 3:
            mc = self.players[0]
            mc.rect.x -= 15
            if mc.rect.right < 0:
                mc.flipX()
                self.dungeon.finished = True
                pygame.mixer.music.fadeout(1000)
                
            for i in range(1,len(self.players)):
                if mc.rect.left <= self.players[i].centerOffset + (300 - (100*i)):
                    self.players[i].active = False
                
        elif self.state == 4: #betrayal
            if len(self.effects) == 0:
                self.state = 1
                self.dungeon.callScene = 'betrayal'
            
        for ch in self.players:
            ch.update()
        
        for en in self.enemies:
            en.update()
            
        for ef in self.effects:
            ef.update()
        
        for ui in self.ui:
            ui.update()        
        
        # DRAW
        for ch in reversed(self.players):
            if ch.alive and ch.active:
                ch.draw(screen,ch.rect.topleft)
        
        for en in self.enemies:
            if en.alive:
                en.draw(screen,en.rect.topleft)
            
        self.effects.draw(screen)
        self.ui.draw(screen)
        
        return screen
    
    def betray(self):
        self.players.remove(self.players[2])
        betrayer = EnemyRaka()
        betrayer.rect.x = self.enemies[0].rect.x - 150
        betrayer.rect.bottom = self.enemies[0].rect.bottom
        
        betrayer.flipX()
        
        poofSprite = screenObjects.SheetAnimatedObject('data/Soraka/SFX', 'raka_poof.png', 160, 0)
        
        poofSprite.rect.bottom = betrayer.rect.bottom
        poofSprite.rect.centerx = betrayer.rect.centerx
        self.effects.add(poofSprite)
        
        pygame.mixer.Sound('data/EffectSFX/flash.wav').play()
        self.enemies.append(betrayer)
          
class Effect(screenObjects.AnimatedObject):
    def __init__(self,topleft,length,directory,order,delay,prefix,loop):
        screenObjects.AnimatedObject.__init__(self, topleft, length, directory, order, delay, prefix, loop)
            
class Banner(Effect):
    def __init__(self):
        order = ['01','02','03','04','05','06','07','08','09','10',
                 '11','12','13','14','15','16','17','18','19','20',
                 '21','22','23','24','25','26','27','28','29','30']
        Effect.__init__(self,(0,0),30,'data/UITop',order,0,'layout_UI_2_000',False)


class Arrow(screenObjects.StaticObject):
    def __init__(self):
        img = screenObjects.load_image('data/icons', 'arrow2.png')
        screenObjects.StaticObject.__init__(self, img, (0,0))
        
        self.bounce = -5
        self.bounceDir = 1
        
    def update(self):
        self.rect.y += self.bounce
        self.bounce += self.bounceDir
        if self.bounce == 5: self.bounceDir = -1
        if self.bounce == -5: self.bounceDir = 1
        
class Ezreal(Champion):
    def __init__(self):
        self.directory = 'data/Ezreal'
        self.prefix = 'ezreal_'
        self.offset = 250
        self.attackCD = 120
        self.attackDamage = 10
        self.centerOffset = 0
        self.maxHP = 100
        self.attackSound = pygame.mixer.Sound('data/EffectSFX/EZ_Attack_1.mp3')
        self.hurtSound = pygame.mixer.Sound('data/EffectSFX/EzDamage.wav')
        Champion.__init__(self)
class Ahri(Champion):
    def __init__(self):
        self.directory = 'data/Ahri'
        self.prefix = 'ahri_'
        self.offset = 275
        self.attackCD = 180
        self.attackDamage = 15
        self.centerOffset = 50
        self.maxHP = 80
        self.attackSound = pygame.mixer.Sound('data/AhriSFX/Attack1_c.wav')
        self.hurtSound = pygame.mixer.Sound('data/AhriSFX/AhriDamage.wav')        
        Champion.__init__(self)
class Soraka(Champion):
    def __init__(self):
        self.directory = 'data/Soraka'
        self.prefix = 'soraka_'
        self.offset = 180
        self.attackCD = 80
        self.attackDamage = 5
        self.centerOffset = 0
        self.maxHP = 100
        self.attackSound = pygame.mixer.Sound('data/EffectSFX/SorakaAttack1.wav')
        self.hurtSound = pygame.mixer.Sound('data/EffectSFX/SorakaDamage.wav')        
        Champion.__init__(self)
class Rengar(Champion):
    def __init__(self):
        self.directory = 'data/Rengar'
        self.prefix = 'rengar_'
        self.offset = 250
        self.attackCD = 100
        self.attackDamage = 10
        self.centerOffset = 50
        self.maxHP = 120
        self.attackSound = pygame.mixer.Sound('data/EffectSFX/Attack3.wav')
        self.hurtSound = pygame.mixer.Sound('data/EffectSFX/ReceivingDamage2.wav')
        Champion.__init__(self)
class Poro(Enemy):
    def __init__(self):
        Enemy.__init__(self, 'data/Poro1', 'poro_', 200, 0, 160, 40, 10)
class MrPoro(Enemy):
    def __init__(self):
        Enemy.__init__(self, 'data/Poro2', 'mrporo_', 200, 0, 160, 100, 15)
class Cinderling(Enemy):
    def __init__(self,offset = 0):
        Enemy.__init__(self, 'data/Cinderling', 'cinderling_', 200, offset, 60, 60, 5)
class Brambleback(Enemy):
    def __init__(self):
        Enemy.__init__(self, 'data/Brambleback', 'brambleback_', 400, 200, 160, 200, 20)
        self.zonya = False
        self.zTimer = 0
        self.sound1 = pygame.mixer.Sound('data/EffectSFX/zonya1.wav')
        self.sound2 = pygame.mixer.Sound('data/EffectSFX/zonya2.wav')
    
    def update(self):
        Enemy.update(self)
        if self.zonya:
            self.zTimer += 1
            if self.zTimer == 80:
                self.sound1.play()
                self.sound2.play()
                self.battle.dungeon.callScene = "redBattle"
        
    def getAttacked(self,damage):
        self.hp -= damage
        if self.hp <= 0:
            self.sound1.play()
            self.sound2.play()
            self.changeImage('zonya')
            self.zonya = True
            
            
class Baron(Enemy):
    def __init__(self):
        Enemy.__init__(self, 'data/Nashor', 'baron_', 800, 100, 160, 800, 20)
        self.eventTimer = 0
        self.eventTrigger = False
        
    def update(self):
        Enemy.update(self)
        if self.eventTrigger:
            self.eventTimer += 1
            if self.eventTimer >= 240:
                getDungeon().callScene = "waitBaron"
                
    def getAttacked(self,damage):
        self.hp -= damage
        if self.hp <= self.maxHP / 2:
            print "half health"
            self.eventTrigger = True
            self.eventTimer = 0
            
        if self.hp <= 0:
            self.alive = False
            getDungeon().callScene = "killBaron"

class Doran(Enemy):
    def __init__(self):
        Enemy.__init__(self, 'data/Doran', 'doran_', 100, 0, 60, 600, 20)
        
    def getAttacked(self,damage):
        self.hp -= damage
        if self.hp <= 0:
            self.alive = False
            
class EnemyRaka(Enemy):
    def __init__(self):
        Enemy.__init__(self, 'data/Soraka', 'soraka_', 180, 0, 80, 100, 5)
        
    def getAttacked(self,damage):
        self.hp -= damage
        if self.hp <= 0:
            self.alive = False