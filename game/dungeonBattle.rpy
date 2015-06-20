init python:
  import pygame
  pygame.font.init()
  import renpygame
  import os
  import random
  
  renpy.music.register_channel('sounds1',"sfx",True)
  renpy.music.register_channel('sounds2',"sfx",True)
  renpy.music.register_channel('sounds3',"sfx",True)
  renpy.music.register_channel('sounds4',"sfx",True)
  config.layers = [ 'master', 'transient', 'screens', 'dungeonScene', 'overlay' ]
 
######################### BEGIN BATTLE OBJECT #########################################
 
  class Battle(renpy.Displayable):
    def __init__(self, **kwargs):
      global battleNumber
      global route
      super(Battle, self).__init__(**kwargs)
      self.width = 1024
      self.height = 768
      
      self.startScene = None
      self.endScene = 'victoryScreen'
      self.lossScene = 'gameOver'
      
      self.music = os.path.join(*['data','music','BattleStance.wav'])      
      self.victorySound = os.path.join(*['data','music','VictoryTheme2.wav'])
            
      self.scenery = []
      self.sceneryfg = []
      self.players = []
      self.enemies = []
      self.effects = []
      self.ui = []
      
      self.lastThreeAttacks = []
      self.comboTimer = 0
      self.queueCombo = ()
      self.combosDone = []      

      self.arrow = TargetArrow()
      self.ui.append(self.arrow)
      
      self.soundChannels = ['sound','sounds1','sounds2','sounds3','sounds4']
      
      if route == "Ezreal":
        self.players = [Ezreal(), Ahri(), Soraka(), Rengar()]
      else:
        self.players = [Leona(), Jayce(), Viktor(), Rumble()]
      
      self.chargingCircles = [ChargingCircle(self.players[0]),ChargingCircle(self.players[1]),ChargingCircle(self.players[2]),ChargingCircle(self.players[3])]
      self.healthBars = [HealthBar(self.players[0]),HealthBar(self.players[1]),HealthBar(self.players[2]),HealthBar(self.players[3])]
      self.ui.extend(self.healthBars)
      self.ui.extend(self.chargingCircles)
      
      self.state = 0
      self.target = 0
      self.loadBattle(battleNumber)
            
      
    def loadBattle(self, number):
      self.startScene = None
      self.endScene = 'victoryScreen'
      self.lossScene = 'gameOver'
      
      self.music = os.path.join(*['data','music','BattleStance.wav'])      
      self.victorySound = os.path.join(*['data','music','VictoryTheme2.wav'])
            
      self.scenery = []
      self.sceneryfg = []
      
      # The sky. It's in most places.
      sky = Scenery(os.path.join('data','SKY_BG.png'),(0,0))
      
      
      # The ground tiles.
      off = 0
      baseGrnd = []
      riftGrnd = []
      riverGrnd = []
      while off < 1024:
        baseGrnd.append(Scenery(os.path.join(*['data','GROUNDS','SR_GRND.gif']), (off,668)))
        riftGrnd.extend([Scenery(os.path.join(*['data','GROUNDS','SumRift_Ground_GrassMiddleLoop.png']), (off, 668)),
                         Scenery(os.path.join(*['data','GROUNDS','SumRift_Ground_GrassMiddleLoop.png']), (off+100, 668)),
                         Scenery(os.path.join(*['data','GROUNDS','SumRift_Ground_GrassMiddleLoop.png']), (off+200, 668))])
        riverGrnd.extend([Scenery(os.path.join(*['data','River','tileM.png']), (off, 668)),
                          Scenery(os.path.join(*['data','River','tileM.png']), (off+100, 668)),
                          Scenery(os.path.join(*['data','River','tileM.png']), (off+200, 668))])
                         
                         
        off += 300
        
      # Trees
      treetile = Scenery(os.path.join('data','summoner rift tree [repeatable].png'),(0,0))
      if number % 2 == 0:
        treetiles = [Scenery(os.path.join('data','summoner rift tree [repeatable].png'),(0, 668 - treetile.rect.height)),
                     Scenery(os.path.join('data','summoner rift tree [repeatable].png'),(treetile.rect.width, 668 - treetile.rect.height))]
      else:
        treetiles = [Scenery(os.path.join('data','summoner rift tree [repeatable].png'),(-88, 668 - treetile.rect.height)),
                     Scenery(os.path.join('data','summoner rift tree [repeatable].png'),(treetile.rect.width - 88, 668 - treetile.rect.height))]
      
      self.scenery.append(sky)
      self.scenery.extend(treetiles)
      

      ####### HERE IS WHERE YOU DEFINE THE BATTLES #####
      # Use this to define a scenery object
      # self.scenery.append(Scenery(os.path.join(*[<path to file seperated by commas>]), (leftmost , rightmost)))
      # If you build a list of Sceneries, use extend instead of append, and pass the list.               
      
      if number == 0:
        walls = [Scenery(os.path.join(*['data','Wall.png']),(0,668-72)),
                 Scenery(os.path.join(*['data','Wall.png']),(156,668-72)),
                 Scenery(os.path.join(*['data','Wall.png']),(312,668-72)),
                 Scenery(os.path.join(*['data','Wall.png']),(468,668-72)),
                 Scenery(os.path.join(*['data','Wall.png']),(624,668-72)),
                 Scenery(os.path.join(*['data','Wall.png']),(780,668-72)),
                 Scenery(os.path.join(*['data','Wall_w_shadow.png']),(936,668-72))]
                 
        self.scenery.extend(walls)
        self.scenery.append(Nexus((400,268)))
        self.scenery.append(Scenery(os.path.join(*['data','turret.png']),(0,0)))
        
        
        self.endScene = 'afterFirstBattle'
        self.scenery.extend(baseGrnd)
        self.enemies = [Poro()]
      elif number == 1:
        walls = [Scenery(os.path.join(*['data','Wall.png']),(0,668-72)),
                 Scenery(os.path.join(*['data','Wall.png']),(156,668-72)),
                 Scenery(os.path.join(*['data','Wall.png']),(312,668-72)),
                 Scenery(os.path.join(*['data','Wall.png']),(468,668-72)),
                 Scenery(os.path.join(*['data','Wall.png']),(624,668-72)),
                 Scenery(os.path.join(*['data','Wall.png']),(780,668-72)),
                 Scenery(os.path.join(*['data','Wall.png']),(936,668-72))]
                 
        self.scenery.extend(walls)
        self.scenery.extend(baseGrnd)
        self.enemies = [Poro(), Poro()]
      elif number == 2:
        walls = [Scenery(os.path.join(*['data','Wall.png']),(0,668-72)),
                 Scenery(os.path.join(*['data','Wall.png']),(156,668-72)),
                 Scenery(os.path.join(*['data','Wall.png']),(312,668-72)),
                 Scenery(os.path.join(*['data','Wall.png']),(468,668-72)),
                 Scenery(os.path.join(*['data','Wall.png']),(624,668-72)),
                 Scenery(os.path.join(*['data','Wall.png']),(780,668-72)),
                 Scenery(os.path.join(*['data','Wall.png']),(936,668-72))]
                 
        self.scenery.extend(walls)
        self.scenery.extend(baseGrnd)
        self.enemies = [Poro(), MrPoro(), Poro()]
      elif number == 3:
        walls = [Scenery(os.path.join(*['data','Wall.png']),(0,668-72)),
                 Scenery(os.path.join(*['data','Wall.png']),(156,668-72)),
                 Scenery(os.path.join(*['data','Wall.png']),(312,668-72)),
                 Scenery(os.path.join(*['data','Wall.png']),(468,668-72)),
                 Scenery(os.path.join(*['data','Wall.png']),(624,668-72)),
                 Scenery(os.path.join(*['data','Wall.png']),(780,668-72)),
                 Scenery(os.path.join(*['data','Wall.png']),(936,668-72))]
                 
        self.scenery.extend(walls)
        
        bushTiles = [Scenery(os.path.join(*['data','Bush','grass-tile-leftendS.png']),(724, 518)),
                     Scenery(os.path.join(*['data','Bush','grass-tile-middleS.png']),(874, 518))]
        self.scenery.extend(bushTiles)
        self.scenery.extend(baseGrnd)
        self.enemies = [MrPoro(), MeleeMinion(), MrPoro()]
      elif number == 4:
        walls = [Scenery(os.path.join(*['data','Wall.png']),(0,668-72)),
                 Scenery(os.path.join(*['data','Wall.png']),(156,668-72)),
                 Scenery(os.path.join(*['data','Wall.png']),(312,668-72)),
                 Scenery(os.path.join(*['data','Wall.png']),(468,668-72)),
                 Scenery(os.path.join(*['data','Wall.png']),(624,668-72)),
                 Scenery(os.path.join(*['data','Wall002.png']),(780,668-72))]
                 
        self.scenery.extend(walls)
        
        bushTiles = [Scenery(os.path.join(*['data','Bush','grass-tile-middleS.png']),(0, 518)),
                     Scenery(os.path.join(*['data','Bush','grass-tile-middleS.png']),(150, 518)),
                     Scenery(os.path.join(*['data','Bush','grass-tile-rightendS.png']),(300, 518))]
        groundTransitionTiles = [Scenery(os.path.join(*['data','Grounds','GroundR.png']), (724,668)),
                                 Scenery(os.path.join(*['data','Grounds','SumRift_Ground_GrassMiddleLoop.png']), (824,668)),
                                 Scenery(os.path.join(*['data','Grounds','SumRift_Ground_GrassMiddleLoop.png']), (924,668))]
        self.scenery.extend(baseGrnd)
        self.scenery.extend(bushTiles)
        self.scenery.extend(groundTransitionTiles)
        self.enemies = [Sentry()]
      elif number == 5:  #Transition into lane
        self.scenery.extend(riftGrnd)
        self.enemies = [MeleeMinion(), MeleeMinion(), MeleeMinion()]
      elif number == 6:
        bushTiles = [Scenery(os.path.join(*['data','Bush','grass-tile-leftend.png']),(424, 368)),
                     Scenery(os.path.join(*['data','Bush','grass-tile-middle.png']),(724, 368))]
        self.scenery.extend(bushTiles)
        
        self.scenery.extend(riftGrnd)
        self.enemies = [CasterMinion(), MeleeMinion(), MeleeMinion()]
      elif number == 7:
        bushTiles = [Scenery(os.path.join(*['data','Bush','grass-tile-middle.png']),(0, 368)),
                     Scenery(os.path.join(*['data','Bush','grass-tile-middle.png']),(300, 368)),
                     Scenery(os.path.join(*['data','Bush','grass-tile-rightend.png']),(600, 368)),]
        
        self.scenery.extend(bushTiles)
        self.sceneryfg.append(Scenery(os.path.join(*['data','Bush','SumRift_Bushes_FG.png']),(0,668-41)))
        self.scenery.extend(riftGrnd)
        self.enemies = [CasterMinion(), CasterMinion(), CasterMinion()]
      elif number == 8:
        self.sceneryfg.append(Scenery(os.path.join(*['data','Bush','SumRift_Bushes_FG.png']),(-129,668-41)))
        self.scenery.append(Scenery(os.path.join(*['data','Bush','SumRift_Bushes_BG.png']),(0,668-273)))
        self.scenery.extend(riftGrnd)
        self.enemies = [Sentry(), CasterMinion(), MeleeMinion()]
      elif number == 9: #Transition to Red Buff area
        self.sceneryfg.append(Scenery(os.path.join(*['data','Bush','SumRift_Bushes_FG.png']),(0,668-41)))
        self.scenery.append(Scenery(os.path.join(*['data','Bush','SumRift_Bushes_BG.png']),(-129,668-273)))
        self.scenery.extend(riftGrnd)
        self.scenery.append(Scenery(os.path.join('data','redpit.png'),(928,68)))
        self.enemies = [Cinderling(), Cinderling()]
      elif number == 10:
        self.sceneryfg.append(Scenery(os.path.join(*['data','Bush','SumRift_Bushes_FG.png']),(-129,668-41)))
        self.scenery.append(Scenery(os.path.join(*['data','Bush','SumRift_Bushes_BG.png']),(0,668-273)))
        self.music = os.path.join(*['music','dungeon.mp3'])
        self.scenery.extend(riftGrnd)
        self.scenery.append(Scenery(os.path.join('data','redpit.png'),(-96,68)))
        self.enemies = [Brambleback(), Cinderling(), Cinderling()]
      elif number == 11: #Transition into jungle
        self.sceneryfg.append(Scenery(os.path.join(*['data','Bush','SumRift_Bushes_FG.png']),(0,668-41)))
        self.scenery.append(Scenery(os.path.join(*['data','Bush','SumRift_Bushes_BG.png']),(-129,668-273)))
        self.scenery.extend(riftGrnd)
        self.enemies = [Wolf()]
      elif number == 12:
        self.sceneryfg.append(Scenery(os.path.join(*['data','Bush','SumRift_Bushes_FG.png']),(-129,668-41)))
        self.scenery.append(Scenery(os.path.join(*['data','Bush','SumRift_Bushes_BG.png']),(0,668-273)))
        
        bushTiles = [Scenery(os.path.join(*['data','Bush','grass-tile-leftend.png']),(300, 368)),
                     Scenery(os.path.join(*['data','Bush','grass-tile-middle.png']),(600, 368)),
                     Scenery(os.path.join(*['data','Bush','grass-tile-middle.png']),(900, 368)),
                     Scenery(os.path.join(*['data','Bush','grass-tile-leftendS.png']),(0, 518)),
                     Scenery(os.path.join(*['data','Bush','grass-tile-middleS.png']),(150, 518)),
                     Scenery(os.path.join(*['data','Bush','grass-tile-rightendS.png']),(300, 518)),
                     Scenery(os.path.join(*['data','Bush','grass-tile-leftendS.png']),(874, 518))]
        
        self.scenery.extend(riftGrnd)
        self.scenery.extend(bushTiles)
        self.enemies = [Wraith(), Wolf(), Wolf()]
      if number == 13:
        self.sceneryfg.append(Scenery(os.path.join(*['data','Bush','SumRift_Bushes_FG.png']),(0,668-41)))
        self.scenery.append(Scenery(os.path.join(*['data','Bush','SumRift_Bushes_BG.png']),(-129,668-273)))
        
        bushTiles = [Scenery(os.path.join(*['data','Bush','grass-tile-middle.png']),(-176, 368)),
                     Scenery(os.path.join(*['data','Bush','grass-tile-rightend.png']),(124, 368)),
                     Scenery(os.path.join(*['data','Bush','grass-tile-middleS.png']),(0, 518)),
                     Scenery(os.path.join(*['data','Bush','grass-tile-middleS.png']),(150, 368)),
                     Scenery(os.path.join(*['data','Bush','grass-tile-rightendS.png']),(300, 518))]
        
        self.scenery.extend(bushTiles)
        self.scenery.extend(riftGrnd)
        self.enemies = [Wraith(), Wraith(), Wraith()]
      if number == 14:
        self.scenery.append(Scenery(os.path.join(*['data','Bush','SumRift_Bushes_BG.png']),(-429,668-273)))
        groundTransitionTiles = [Scenery(os.path.join(*['data','River','TileL.png']), (724,668)),
                                 Scenery(os.path.join(*['data','River','TileM.png']), (824,668)),
                                 Scenery(os.path.join(*['data','River','TileM.png']), (924,668))]

        self.scenery.extend(riftGrnd)
        self.scenery.extend(groundTransitionTiles)
        self.enemies = [Wight(), Wraith(), Wraith()]
      if number == 15:
        self.scenery.append(Scenery(os.path.join(*['data','Rock004.png']),(538,668-51)))
        self.scenery.append(Scenery(os.path.join(*['data','Rock003.png']),(204,668-24)))
        self.scenery.extend(riverGrnd)
        self.enemies = [RiftScuttler(), RiftScuttler()]
      if number == 16:
        self.scenery.append(Scenery(os.path.join(*['data','pit.png']),(200,668-385)))
        
        self.scenery.append(BaronPit((748,283)))
        self.scenery.extend(riverGrnd)
        self.enemies = [Wight(), RiftScuttler(), Wolf()]
      if number == 17:
        self.music = os.path.join(*['music','dungeon.mp3'])
        self.scenery.append(BaronPit((-276,283)))
        groundTransitionTiles = [Scenery(os.path.join(*['data','River','TileR.png']), (724,668)),
                                 Scenery(os.path.join(*['data','Grounds','SumRift_Ground_GrassMiddleLoop.png']), (824,668)),
                                 Scenery(os.path.join(*['data','Grounds','SumRift_Ground_GrassMiddleLoop.png']), (924,668))]
        
        
        self.scenery.extend(riverGrnd)
        self.scenery.extend(groundTransitionTiles)
        self.enemies = [Baron()]
      if number == 18: #Transition into Twisted Treeline
        self.scenery.append(Scenery(os.path.join(*['data','transition_1.png']),(0,0)))
        self.scenery.extend(riftGrnd)
        self.enemies = [Wight(), Wight()]
      if number == 19: 
        self.scenery.append(Scenery(os.path.join(*['data','transition_2.png']),(0,0)))
        self.scenery.extend(riftGrnd)
        self.enemies = [Wight(), Sentry(), Wight()]
      if number == 20: 
        self.scenery.append(Scenery(os.path.join(*['data','transition_3.png']),(0,0)))
        self.scenery.extend(riftGrnd)
        self.enemies = [Wolf(), Wolf(), Wolf(), Wolf()]
      if number == 21: 
        self.scenery.append(Scenery(os.path.join(*['data','transition_4.png']),(0,0)))
        self.scenery.extend(riftGrnd)
        self.enemies = [RiftScuttler(), RiftScuttler(), RiftScuttler()]
      if number == 22: 
        self.scenery.append(Scenery(os.path.join(*['data','transition_5.png']),(0,0)))
        self.scenery.extend(riftGrnd)
        self.enemies = [Cinderling(), Cinderling(), Cinderling(), Cinderling()]
      if number == 23: 
        self.scenery.append(Scenery(os.path.join(*['data','transition_6.png']),(0,0)))
        self.scenery.extend(riftGrnd)
        self.enemies = [Wight(), Wight(), Wight()]
      if number == 24: #Transition into enemy base
        groundTransitionTiles = [Scenery(os.path.join(*['data','Grounds','SumRift_Ground_LeftBrickGrassTransition.png']), (624,668)),
                                 Scenery(os.path.join(*['data','Grounds','SR_GRND.gif']), (724,668))]
                                 
        self.scenery.extend(riftGrnd)
        self.scenery.extend(groundTransitionTiles)
        self.enemies = [Sentry(), Sentry(), Sentry()]
      if number == 25:
        self.music = os.path.join(*['music','dungeon.mp3'])
        self.scenery.extend(baseGrnd)
        self.scenery.append(Scenery(os.path.join(*['data','turret2.png']),(732,0)))
        self.startScene = 'beforeHacker'
        self.lossScene = 'loseFinalBattle'
        self.endScene = 'winFinalBattle'
        self.enemies = [Doran()]
        
      self.initialize()
      
    
    def initialize(self):
      for i in range(0,len(self.players)):
        self.players[i].active = False
        self.players[i].visible = False
        self.players[i].rect.left = self.players[i].centerOffset + (300 - (100*i))
        self.players[i].rect.bottom = 668
        self.players[i].battle = self
        self.players[i].currentCD = 0
        
      for i in range(0,len(self.enemies)):
        self.enemies[i].active = False
        self.enemies[i].visible = True
        self.enemies[i].rect.right = self.enemies[i].centerOffset + (1024 - (100*i))
        self.enemies[i].rect.bottom = 668
        self.enemies[i].battle = self
        
      self.target = 0
      self.arrow.rect.bottom = self.enemies[self.target].rect.centery
      self.arrow.rect.centerx = self.enemies[self.target].rect.centerx
        
      self.players[0].rect.right = 0
      self.players[0].active = True
      self.players[0].visible = True
      self.players[0].changeImage('walk')
      self.combosDone = []

      self.state = 0
      
    def deActivate(self):
      for ch in self.players:
        ch.oldActiveState = ch.active
        ch.active = False
      
      for en in self.enemies:
        en.oldActiveState = en.active
        en.active = False
        
      for ui in self.ui:
        ui.visible = False
        
    def reActivate(self):
      for ch in self.players:
        ch.active = ch.oldActiveState
        
      for en in self.enemies:
        en.active = en.oldActiveState
        
      for ui in self.ui:
        ui.visible = True
      
    def render(self, width, height, st, at):
      global battleFlag
      
      render = renpy.Render(self.width, self.height)
      for scene in self.scenery:
        child_render = scene.render(width, height, st, at)
        render.blit(child_render, scene.rect.topleft)
      
      if battleFlag == 'onward':
        self.onward()
        battleFlag = ""
      elif battleFlag == 'retreat':
        self.retreat()
        battleFlag = ""
        
      # MC walks into position
      if self.state == 0: 
        mc = self.players[0]
        mc.rect.x += 20
        
        for i in range (1, len(self.players)):
          if mc.rect.left >= (300 - (100 * i)):
            if self.players[i].alive:
              self.players[i].active = True
              self.players[i].visible = True
        
        if mc.rect.left >= 300 + mc.centerOffset:
          mc.rect.left = 300 + mc.centerOffset
          mc.changeImage('idle')
          
          for en in self.enemies: en.active = True
          
          for i in range(0,len(self.chargingCircles)):
            c = self.chargingCircles[i]
            b = self.healthBars[i]
            c.rect.centerx = (300 - (100 * i)) + 116
            c.rect.centery = 408
            b.rect.left = 64
            b.rect.top = 75 * i
          for ui in self.ui:
            ui.visible = True
          self.state = 1
          
          if self.startScene:
            self.callScene(self.startScene)
          else:
            renpy.music.play(self.music, loop=True)
            
      # The actual battle
      elif self.state == 1:
        removeList = []
        for i in range(0,len(self.enemies)):
          en = self.enemies[i]
          if en.alive and en.currentCD == 0:
            self.doEnemyAttack(i)
            en.currentCD = en.attackCD
          if not en.alive:
            removeList.append(en)
            self.effects.append(HitFlash(en,True))
        for en in removeList:
          self.enemies.remove(en)
          self.changeTarget(1)
        if not self.players[0].alive:
          if len(self.effects) == 0:
            self.state = -1
            self.callScene(self.lossScene)
        if len(self.enemies) == 0:
          for ch in self.players:
            ch.attacking = None
            ch.changeImage('idle')
          if len(self.effects) == 0:
            self.state = -1
            self.endBattle()
            
      # Onward animation
      elif self.state == 2:
        mc = self.players[0]
        mc.rect.x += 20
        if mc.rect.right >= 1024:
          self.nextBattle()
          
      elif self.state == 3:
        mc = self.players[0]
        mc.rect.x -= 15
        if mc.rect.right < 0:
          renpy.music.stop(fadeout=1)
          renpy.end_interaction("Finished")
        
        for i in range(1, len(self.players)):
          if mc.rect.left <= self.players[i].centerOffset + (300 - (100*i)):
            self.players[i].active = False
            self.players[i].visible = False
      
      elif self.state == 4: #betrayal
        if len(self.effects) == 0:
          self.state = 1
          self.callScene('betrayal')
          
      elif self.state == 5:
        if len(self.effects) == 0:
          self.state = 1
          self.callScene('hackerBeforeDuel')
        
      for ch in reversed(self.players):
        child_render = ch.render(width, height, st, at)
        render.blit(child_render, ch.rect.topleft)
      for en in self.enemies:
        child_render = en.render(width, height, st, at)
        render.blit(child_render, en.rect.topleft)
      for scene in self.sceneryfg:
        child_render = scene.render(width, height, st, at)
        render.blit(child_render, scene.rect.topleft)
      
      for ui in self.ui:
        child_render = ui.render(width, height, st, at)
        render.blit(child_render, ui.rect.topleft)
      for ef in self.effects:
        child_render = ef.render(width, height, st, at)
        render.blit(child_render, ef.rect.topleft)
        if ef.done:
          self.effects.remove(ef)
        
      self.comboTimer += 1
      if self.comboTimer == 5:
        self.lastThreeAttacks = []
        self.comboTimer = 0
        
      renpy.redraw(self, 0.1)
      return render
      
    def callScene(self,scene):
      for ch in self.players:
        ch.changeImage('idle')
        ch.attacking = False
      self.deActivate()
      renpy.call(scene)
      
    def event(self, ev, x, y, st):
      if ev.type == pygame.KEYDOWN:
        if ev.key == pygame.K_q:
          self.doPlayerAttack(3)
        elif ev.key == pygame.K_w:
          self.doPlayerAttack(2)
        elif ev.key == pygame.K_e:
          self.doPlayerAttack(1)
        elif ev.key == pygame.K_r:
          self.doPlayerAttack(0)
        elif ev.key == pygame.K_LEFT:
          self.changeTarget(1)
        elif ev.key == pygame.K_RIGHT:
          self.changeTarget(-1)
        elif ev.key == pygame.K_TAB:
          self.changeTarget(1)
        elif ev.key == pygame.K_ESCAPE:
          self.callScene("quitScreen")
      
    def endBattle(self):
      global battleNumber
      renpy.music.stop()
      renpy.music.play(self.victorySound,loop=False)
      battleNumber += 1
      for ui in self.ui:
        ui.visible = False
      self.callScene(self.endScene)
      
    def nextBattle(self):
      global battleNumber
      self.loadBattle(battleNumber)
      
    def onward(self):
      self.state = 2
      for pl in self.players:
        pl.changeImage('idle')
        pl.attacking = None
      mc = self.players[0]
      mc.changeImage('walk')
      
    def retreat(self):
      for pl in self.players:
        pl.changeImage('idle')
        pl.attacking = None
      mc = self.players[0]
      mc.changeImage('walk_left')
      self.state = 3
      
      
    def doPlayerAttack(self,i):
      global route
      if route == "Ezreal":
        global ahri_combo
        global rango_combo
        global raka_combo
      else:
        global jayce_combo
        global rumble_combo
        global vik_combo
      
      if self.state == 1:
        if len(self.enemies) > 0:
          if self.players[i].active:
            en = self.enemies[self.target]
            while not en.alive:
              self.changeTarget(1)
              en = self.enemies[self.target]
            if self.players[i].currentCD == 0:
              if len(self.lastThreeAttacks) == 3:
                self.lastThreeAttacks.pop(0)
                self.lastThreeAttacks.append(i)
                self.comboTimer = 0
              else:
                self.lastThreeAttacks.append(i)
                self.comboTimer = 0
              doCombo = False
              if not i in self.combosDone:
                if route == "Ezreal":
                  if i == 1 and ahri_combo and self.lastThreeAttacks == [0,3,1]:
                    doCombo = True
                  elif i == 2 and raka_combo and self.lastThreeAttacks == [0,1,2]:
                    doCombo = True
                  elif i == 3 and rango_combo and self.lastThreeAttacks == [0,2,3]:
                    doCombo = True
                elif route == "Leona":
                  if i == 1 and jayce_combo and self.lastThreeAttacks == [0,2,1]:
                    doCombo = True
                  elif i == 2 and vik_combo and self.lastThreeAttacks == [0,3,2]:
                    doCombo = True
                  elif i == 3 and rumble_combo and self.lastThreeAttacks == [0,1,3]:
                    doCombo = True
              if doCombo:
                self.effects = []
                self.effects.append(CharSuperAnim(self,self.players[i].superSprite))
                self.queueCombo = (self.lastThreeAttacks,en)
                self.combosDone.append(i)
              else:
                self.lastThreeAttacks == []
                self.players[i].doAttack(en)
    
    def doPlayerCombo(self):
      players = self.queueCombo[0]
      target = self.queueCombo[1]
      exCh = players.pop()
      self.players[exCh].doComboAttack(target, [self.players[players[0]], self.players[players[1]]])
      self.queueCombo = ()
      
    def doEnemyAttack(self,i):
      j = random.randint(0,3)
      while not self.players[j].alive:
        j = (j + 1) % 4
      self.enemies[i].doAttack(self.players[j])
      
    def changeTarget(self,amt):
      self.target += amt
      l = len(self.enemies)
      if l > 0:
        self.target = (l + self.target) % l
        self.arrow.rect.bottom = self.enemies[self.target].rect.centery
        self.arrow.rect.centerx = self.enemies[self.target].rect.centerx
    
    def betray(self):
        global route
        self.players[2].active = False
        self.players[2].visible = False
        self.players[2].alive = False
        if route == "Ezreal":
          betrayer = EnemyRaka()
        else:
          betrayer = EnemyViktor()
        betrayer.rect.x = self.enemies[0].rect.x - 150
        betrayer.rect.bottom = self.enemies[0].rect.bottom
        
        betrayer.active = False
        betrayer.oldActiveState = True
        betrayer.visible = True
        betrayer.alive = True
        betrayer.battle = self
        
        for hb in self.healthBars:
          if hb.parent == self.players[2]:
            self.ui.remove(hb)
            self.healthBars.remove(hb)
        poofSprite = Effect(os.path.join(*['data','Soraka','SFX', 'raka_poof.png']), (160,260),13)
        
        poofSprite.rect.bottom = betrayer.rect.bottom
        poofSprite.rect.centerx = betrayer.rect.centerx - 20
        self.effects.append(poofSprite)
        
        self.playOnNextAvailableChannel(os.path.join(*['data','EffectSFX','flash.wav']))
        self.enemies.append(betrayer)
        
        self.state = 4
        
    def oneOnOne(self):
      allies = self.players[1:]
      for hb in self.healthBars:
        if hb.parent in allies:
          self.ui.remove(hb)
      if len(self.enemies) > 1:
        en = self.enemies[1]
        en.alive = False
        en.visible = False
        en.active = False
        self.effects.append(HitFlash(en,True))
        self.enemies.remove(en)
      for a in allies:
        if a.alive:
          self.effects.append(HitFlash(a,True))
        a.alive = False
        a.visible = False
        a.active = False
      self.players[0].HP = self.players[0].maxHP
      self.players[0].currentCD = 0
      self.state = 5
    
    def getBeefy(self):
      global route
      mc = self.players[0]
      if route == "Ezreal":
        mc.animLib = AnimLib(os.path.join('data','Ezreal'), 'ezreal_buffed_', 'idle', (250,200), 0.3)
      else:
        mc.animLib = AnimLib(os.path.join('data','Leona'), 'leona_buffed_', 'idle', (275,200), 0.3)
      mc.changeImage('idle')
      mc.attackDamage = 40
      mc.maxHP = 200
      mc.HP = 200
      
    def playOnNextAvailableChannel(self,soundEffect):
      for channel in self.soundChannels:
        if not renpy.sound.is_playing(channel):
          renpy.sound.play(soundEffect,channel)
          return
      print "channel overload"
      return
          
######################### END BATTLE OBJECT #########################################

  # Things that are fighting in a battle
  class Fighter(renpy.Displayable):
    def __init__(self, animLib, position, centerOffset, attackCD, attackDamage, maxHP, **kwargs):
      self.animLib = animLib
      self.position = position
      self.centerOffset = centerOffset
      self.attackCD = attackCD
      self.currentCD = 0
      self.attackDamage = attackDamage
      self.maxHP = maxHP
      self.HP = maxHP
      
      self.rect = pygame.rect.Rect(position, animLib.framesize)
      
      self.alive = True
      self.attacking = False
      
      self.active = False
      self.oldActiveState = None
      self.visible = False
      self.battle = None
      self.target = None
      
      self.superSprite = None
      self.attackEffect = None
      self.attackEffectSize = ()
      self.attackEffectLength = 0
      
      self.attackSound = None
      self.attackVoice = None
      self.hurtSound = None
      self.hurtSprite = None
      
    def doAttack(self,target):
      if not self.attacking and self.currentCD == 0:
          self.attacking = True
          self.currentCD = self.attackCD
          self.animLib.changeImage('attack')
          self.target = target      
          if self.attackVoice:
            self.battle.playOnNextAvailableChannel(self.attackVoice)
          if self.attackEffect:
            ef = Effect(self.attackEffect,self.attackEffectSize,self.attackEffectLength)
            ef.rect.midbottom = target.rect.midbottom
            self.battle.effects.append(ef)
            
    def doComboAttack(self,target,assists):
      self.attacking = True
      self.currentCD = self.attackCD
      self.animLib.changeImage('attack')
      self.target = target
      totalDamage = self.attackDamage
      self.battle.playOnNextAvailableChannel(self.attackSound)
      ef = Effect(self.attackEffect,self.attackEffectSize,self.attackEffectLength)
      ef.rect.midbottom = target.rect.midbottom
      self.battle.effects.append(ef)
      for ch in assists:
        self.battle.playOnNextAvailableChannel(ch.attackSound)
        ch.animLib.changeImage('attack')
        ch.attacking = True
        ch.target = target
        totalDamage += ch.attackDamage
        ef = Effect(ch.attackEffect,ch.attackEffectSize,ch.attackEffectLength)
        ef.rect.bottom = target.rect.bottom
        ef.rect.center = target.rect.center
        self.battle.effects.append(ef)
      
      if hasattr(target, 'gotCombod'):
        target.gotCombod = True
      
    def getAttacked(self,damage):
      self.HP -= damage
      if self.HP <=0:
        self.alive = False
        self.active = False
        self.visible = False
      if self.attacking:
        self.attacking = False
        self.animLib.changeImage('idle')
      self.battle.effects.append(HitFlash(self,False))
      if self.hurtSound:
        self.battle.playOnNextAvailableChannel(self.hurtSound)
        
    def changeImage(self,newImage):
      self.animLib.changeImage(newImage)
      
    def render(self, width, height, st, at):
      if self.alive:
        if self.active:
          if self.currentCD > 0:
            self.currentCD -= 1
        if self.attacking:
          if self.animLib.frame == len(self.animLib.library[self.animLib.currentImage].frames) - 1:
            self.target.getAttacked(self.attackDamage)
            if self.attackSound:
              self.battle.playOnNextAvailableChannel(self.attackSound)
            self.animLib.changeImage('idle')
            self.attacking = False
            
      if self.visible:
        return self.animLib.render(width, height, st, at)
      return renpy.Render(0,0)     
  
  class Scenery(renpy.Displayable):
    def __init__(self,image,position,**kwargs):
      super(Scenery,self).__init__(**kwargs)
      self.image = image
      im = Image(image)
      rn = im.render(0,0,0,0)
      self.rect = pygame.Rect(position, rn.get_size())
      
    def render(self, width, height, st, at):
      return Image(self.image).render(width,height,st,at)
  
  class Effect(renpy.Displayable):
    def __init__(self,image, framesize, frames, **kwargs):
      super(Effect,self).__init__(**kwargs)
      self.filmStrip = FilmStrip(image, framesize, (frames,1), frames)
      self.rect = pygame.Rect((0,0), framesize)
      self.done = False
      
    def render(self, width, height, st, at):
      if self.filmStrip.index == self.filmStrip.get_length() - 1:
        self.done = True
        
      return self.filmStrip.render(width, height, st, at)
      
######################### BEGIN UI DECLARATION #########################################

  class TargetArrow(renpy.Displayable):
    def __init__(self, **kwargs):
      super(TargetArrow,self).__init__(**kwargs)
      self.image = os.path.join(*['data','icons','arrow2.png'])
      im = Image(self.image)
      rn = im.render(0,0,0,0)
      self.rect = pygame.Rect((0,0), rn.get_size())
      
      self.bounce = -5
      self.bounceDir = 1
      self.visible = False
      
    def render(self,width, height, st, at):
      self.rect.y += self.bounce
      self.bounce += self.bounceDir
      if self.bounce == 5: self.bounceDir = -1
      if self.bounce == -5: self.bounceDir = 1
      if self.visible:
        return Image(self.image).render(width, height, st, at)
      else:
        return renpy.Render(0,0)

  
  class ChargingCircle(renpy.Displayable):
    def __init__(self, parent, **kwargs):
      super(ChargingCircle,self).__init__(**kwargs)
      self.parent = parent
      self.rect = pygame.Rect((0,0), (64,64))
      self.filmstrip = FilmStrip(os.path.join(*['data','icons','chargingCircle.png']), (64,64), (10,1),10,False)
      
      self.visible = False
      
    def render(self, width, height, st, at):
      if not self.parent.alive:
        self.visible = False
      if self.visible:
        percentage = float(self.parent.currentCD) / float(self.parent.attackCD) * 100
        
        if percentage == 0:
          self.filmstrip.index = 0
        elif percentage > 0 and percentage <= 10:
          self.filmstrip.index = 1
        elif percentage > 10 and percentage <= 20:
          self.filmstrip.index = 2
        elif percentage > 20 and percentage <= 30:
          self.filmstrip.index = 3
        elif percentage > 30 and percentage <= 40:
          self.filmstrip.index = 4
        elif percentage > 40 and percentage <= 50:
          self.filmstrip.index = 5
        elif percentage > 50 and percentage <= 60:
          self.filmstrip.index = 6
        elif percentage > 60 and percentage <= 70:
          self.filmstrip.index = 7
        elif percentage > 70 and percentage <= 90:
          self.filmstrip.index = 8
        elif percentage > 90:
          self.filmstrip.index = 9
        return self.filmstrip.render(width,height,st,at)
      else:
        return renpy.Render(0,0)
    
  class HealthBar(renpy.Displayable):
    def __init__(self, parent, **kwargs):
      super(HealthBar, self).__init__(**kwargs)
      self.parent = parent
      
      self.barimage = os.path.join(*['data','icons','healthBar.png'])
      self.barrect = pygame.Rect((41,35),(168,29))
      
      self.image = os.path.join(*['data','icons','battleuiBOX.png'])
      self.rect = pygame.Rect((0,0),(219,73))
      
      self.visible = False
    
    def render(self, width, height, st, at):
      percentage = float(self.parent.HP) / float(self.parent.maxHP)
      
      bar = Transform(self.barimage, crop=(0, 0, percentage * self.barrect.width, self.barrect.height))
      barrender = bar.render(width,height,st,at)
      
      render = Image(self.image).render(width,height,st,at)
      render.blit(barrender, self.barrect.topleft)
      if self.visible:
        return render
      else:
        return renpy.Render(0,0)
        
  class HitFlash(renpy.Displayable):
    def __init__(self, parent, death, **kwargs):
      super(HitFlash, self).__init__(**kwargs)
      self.parent = parent
      if death:
        self.filmstrip = self.parent.animLib.library['die']
      else:
        self.filmstrip = self.parent.animLib.library['damage']
      
      self.frame = 0
      self.lastFrame = self.filmstrip.get_length()
      self.done = False
      self.rect = self.parent.rect
      
    def render(self, width, height, st, at):
      t = self.filmstrip.frames[self.frame]
      self.frame += 1
      if self.frame == self.lastFrame:
        self.done = True
        return renpy.Render(0,0)
      else:
        render = t.render(width, height, st, at)
        return render
    
  class CharSuperAnim(renpy.Displayable):
    def __init__(self, battle, image, **kwargs):
      super(CharSuperAnim, self).__init__(**kwargs)
      self.battle = battle
      self.image = image
      self.holdTime = 0
      self.done = False
      
      im = Image(self.image)
      rn = im.render(0,0,0,0)
      self.rect = pygame.Rect((0,0), rn.get_size())
      
      self.rect.right = 0
      self.rect.bottom = 768
      
    def render(self, width, height, st, at):
      if self.rect.right == 0:
        self.battle.playOnNextAvailableChannel(os.path.join(*['data','effectSFX','tpStart.wav']))
      
      if self.rect.centerx < 300:
        self.rect.x += 150
      else:
        self.holdTime += 1
      if self.holdTime == 14:
        self.battle.playOnNextAvailableChannel(os.path.join(*['data','effectSFX','tpFinish.wav']))
      if self.holdTime >= 15:
        self.rect.x += 200
        if self.rect.left > 1024:
          self.battle.doPlayerCombo()
          self.done = True
      return Image(self.image).render(width, height, st, at)
######################### BEGIN CHAMPION DECLARATION #########################################
        
  class Ezreal(Fighter):
    def __init__(self):
      global ahri_rp
      global raka_rp
      global rango_rp
      
      total_rp = ahri_rp + raka_rp + rango_rp
      
      maxHP = 100
      attackDamage = 15
      attackCD = 80
      
      if total_rp >= 50:
        maxHP = 110
      
      if total_rp >= 100:
        maxHP = 120
        attackDamage = 20
        attackCD = 75
        
      if total_rp >= 150:
        maxHP = 130
        
      if total_rp >= 200:
        maxHP = 140
        attackCD = 70
        attackDamage = 25
        
      if total_rp >= 250:
        maxHP = 150
        attackCD = 60
        attackDamage = 30
        
      if total_rp >= 300:
        maxHP = 200
        attackCD = 40
        attackDamage = 40
      
      animLib = AnimLib(os.path.join('data','Ezreal'), 'ezreal_', 'idle', (250,200), 0.3)
      Fighter.__init__(self, animLib, (0,0), 0, attackCD, attackDamage, maxHP)
      self.attackVoice = os.path.join(*['data','EffectSFX','EZ_Attack_1.mp3'])
      self.attackSound = os.path.join(*['data','EffectSFX','ezBolt.wav'])
      
      self.hurtSound = os.path.join(*['data','EffectSFX','EzDamage.wav'])
      
      self.attackEffect = os.path.join(*['data','ArrowAttack2','effect_arrow.png'])
      self.attackEffectSize = (250,150)
      self.attackEffectLength = 6
      
  class Leona(Fighter):
    def __init__(self):
      global jayce_rp
      global vik_rp
      global rumble_rp
      
      total_rp = jayce_rp, vik_rp, rumble_rp
      
      maxHP = 120
      attackDamage = 10
      attackCD = 80
      
      if total_rp >= 50:
        maxHP = 110
      
      if total_rp >= 100:
        maxHP = 120
        attackDamage = 15
        attackCD = 75
        
      if total_rp >= 150:
        maxHP = 130
        
      if total_rp >= 200:
        maxHP = 140
        attackCD = 70
        attackDamage = 20
        
      if total_rp >= 250:
        maxHP = 150
        attackCD = 60
        attackDamage = 25
        
      if total_rp >= 300:
        maxHP = 200
        attackCD = 40
        attackDamage = 40
      
      animLib = AnimLib(os.path.join('data','Leona'), 'leona_', 'idle', (275,200), 0.3)
      Fighter.__init__(self, animLib, (0,0), 50, attackCD, attackDamage, maxHP)
      self.attackVoice = os.path.join(*['data','Leona','LeonaSFX','Attack1.wav'])
      self.attackSound = os.path.join(*['data','EffectSFX','daggerSound2.wav'])
      
      self.hurtSound = os.path.join(*['data','Leona','LeonaSFX','Damage.wav'])
      
      self.attackEffect = os.path.join(*['data','sword_slash','effect_sword.png'])
      self.attackEffectSize = (150,150)
      self.attackEffectLength = 5
      
        
  class Ahri(Fighter):
    def __init__(self):
      global ahri_rp
      maxHP = 80
      attackDamage = 15
      attackCD = 100
      
      if ahri_rp >= 25:
        maxHP = 100
      
      if ahri_rp >= 50:
        attackDamage = 20
      
      if ahri_rp >= 75:
        maxHP = 120
        attackCD = 90
      
      if ahri_rp >= 100:
        maxHP = 140
        attackDamage = 25
        attackCD = 80
      
      animLib = AnimLib(os.path.join('data','Ahri'), 'ahri_', 'idle', (275,200), 0.3)
      Fighter.__init__(self, animLib,  (0,0), 50, attackCD, attackDamage, maxHP)
      self.attackVoice = os.path.join(*['data','AhriSFX','Attack1_c.wav'])
      self.attackSound = os.path.join(*['data','EffectSFX','FireBall.wav'])
      
      self.hurtSound = os.path.join(*['data','AhriSFX','AhriDamage.wav'])
      self.superSprite = os.path.join(*['ahri','vr','ahriwink.png'])  
  
      self.attackEffect = os.path.join(*['data','fire_effect','effect_fire.png'])
      self.attackEffectSize = (150,150)
      self.attackEffectLength = 18
      
  class Jayce(Fighter):
    def __init__(self):
      global jayce_rp
      maxHP = 80
      attackDamage = 15
      attackCD = 100
      
      if jayce_rp >= 25:
        maxHP = 100
      
      if jayce_rp >= 50:
        attackDamage = 20
      
      if jayce_rp >= 75:
        maxHP = 120
        attackCD = 90
      
      if jayce_rp >= 100:
        maxHP = 140
        attackDamage = 25
        attackCD = 80
      
      animLib = AnimLib(os.path.join('data','Jayce'), 'jayce_', 'idle', (400,250), 0.3)
      Fighter.__init__(self, animLib,  (0,0), -50, attackCD, attackDamage, maxHP)
      self.attackVoice = os.path.join(*['data','EffectSFX','JayceAttack.wav'])
      self.attackSound = os.path.join(*['data','EffectSFX','hammertime.wav'])
      
      self.hurtSound = os.path.join(*['data','EffectSFX','JayceDamage.wav'])
      self.superSprite = os.path.join(*['jayce','vr','happy.png'])
      
      self.attackEffect = os.path.join(*['data','sword_slash','effect_sword_gold.png'])
      self.attackEffectSize = (150,150)
      self.attackEffectLength = 5
      
  
  class Soraka(Fighter):
    def __init__(self):
      global raka_rp
      maxHP = 100
      attackDamage = 5
      attackCD = 60
      
      if raka_rp >= 25:
        maxHP = 120
      
      if raka_rp >= 50:
        attackCD = 40
      
      if raka_rp >= 75:
        maxHP = 140
        attackDamage = 10
      
      if raka_rp >= 100:
        maxHP = 150
        attackDamage = 15
        attackCD = 25
      
      animLib = AnimLib(os.path.join('data','Soraka'), 'soraka_', 'idle', (180,250), 0.3)
      Fighter.__init__(self, animLib,  (0,0),  0, attackCD, attackDamage, maxHP)
      self.attackVoice = os.path.join(*['data','EffectSFX','SorakaAttack1.wav'])
      self.attackSound = os.path.join(*['data','EffectSFX','rakaBolt.wav'])
      self.hurtSound = os.path.join(*['data','EffectSFX','SorakaDamage.wav'])        
      self.superSprite = os.path.join(*['raka','vr','angry.png'])
      
      self.attackEffect = os.path.join(*['data','Soraka','SFX', 'raka_poof.png'])
      self.attackEffectSize = (160,260)
      self.attackEffectLength = 13
      
  class Viktor(Fighter):
    def __init__(self):
      global vik_rp
      maxHP = 100
      attackDamage = 5
      attackCD = 60
      
      if vik_rp >= 25:
        maxHP = 120
      
      if vik_rp >= 50:
        attackCD = 40
      
      if vik_rp >= 75:
        maxHP = 140
        attackDamage = 10
      
      if vik_rp >= 100:
        maxHP = 150
        attackDamage = 15
        attackCD = 25
      
      animLib = AnimLib(os.path.join('data','Viktor'), 'viktor_', 'idle', (150,300), 0.3)
      Fighter.__init__(self, animLib,  (0,0),  30, attackCD, attackDamage, maxHP)
      self.attackVoice = os.path.join(*['data','EffectSFX','viktor_Attack.wav'])
      self.attackSound = os.path.join(*['data','EffectSFX','vikBolt.wav'])
      
      self.hurtSound = os.path.join(*['data','EffectSFX','viktor_ReceiveDamage.wav'])
      self.superSprite = os.path.join(*['vik','vr','happy.png'])
      
      self.attackEffect = os.path.join(*['data','Viktor_FX', 'pink_explosion.png'])
      self.attackEffectSize = (550,400)
      self.attackEffectLength = 13
      
  class Rengar(Fighter):
    def __init__(self):
      global rango_rp
      maxHP = 120
      attackDamage = 10
      attackCD = 80
      
      if rango_rp >= 25:
        attackDamage = 15
      
      if rango_rp >= 50:
        maxHP = 140
      
      if rango_rp >= 75:
        attackCD = 70
        attackDamage = 20
      
      if rango_rp >= 100:
        maxHP = 180
        attackCD = 60
      
      
      animLib = AnimLib(os.path.join('data','Rengar'), 'rengar_', 'idle', (250,200), 0.3)
      Fighter.__init__(self, animLib,  (0,0),  50, attackCD, attackDamage, maxHP)
      self.attackVoice = os.path.join(*['data','EffectSFX','Attack3.wav'])
      self.attackSound = os.path.join(*['data','EffectSFX','daggerSound.wav'])
      self.hurtSound = os.path.join(*['data','EffectSFX','ReceivingDamage2.wav'])
      self.superSprite = os.path.join(*['rango','vr','confident.png'])
      
      self.attackEffect = os.path.join(*['data','sword_slash','effect_sword.png'])
      self.attackEffectSize = (150,150)
      self.attackEffectLength = 5
      
      
  class Rumble(Fighter):
    def __init__(self):
      global rumble_rp
      maxHP = 120
      attackDamage = 10
      attackCD = 80
      
      if rumble_rp >= 25:
        attackDamage = 15
      
      if rumble_rp >= 50:
        maxHP = 140
      
      if rumble_rp >= 75:
        attackCD = 70
        attackDamage = 20
      
      if rumble_rp >= 100:
        maxHP = 180
        attackCD = 60
      
      animLib = AnimLib(os.path.join('data','Rumble'), 'rumble_', 'idle', (300,200), 0.3)
      Fighter.__init__(self, animLib,  (0,0),  0, attackCD, attackDamage, maxHP)
      self.attackVoice = os.path.join(*['data','EffectSFX','RumbleAttack1.wav'])
      self.attackSound = os.path.join(*['data','EffectSFX','rumbleHit.wav'])
      
      self.hurtSound = os.path.join(*['data','EffectSFX','RumbleDamage1.wav'])
      self.superSprite = os.path.join(*['rumble','vr','flat.png'])  
      
      self.attackEffect = os.path.join(*['data','smoke_puff_up','smoke_puff.png'])
      self.attackEffectSize = (500,500)
      self.attackEffectLength = 13
        
      
######################### BEGIN ENEMY DECLARATION #########################################
  class Poro(Fighter):
    def __init__(self):
      animLib = AnimLib(os.path.join('data','Poro1'), 'poro_', 'idle', (200,200), 0.3)
      Fighter.__init__(self, animLib, position = (0,0), centerOffset = 0, attackCD = 100, attackDamage = 10, maxHP = 40)
      self.currentCD = random.randint(0,self.attackCD)
      self.hurtSprite = True
  
  class MrPoro(Fighter):
    def __init__(self):
      animLib = AnimLib(os.path.join('data','Poro2'), 'mrporo_', 'idle', (200,200), 0.3)
      Fighter.__init__(self, animLib, position = (0,0), centerOffset = 0, attackCD = 100, attackDamage = 12, maxHP = 80)
      self.currentCD = random.randint(0,self.attackCD)
      self.hurtSprite = True


  class Cinderling(Fighter):
    def __init__(self):
      animLib = AnimLib(os.path.join('data','Cinderling'), 'cinderling_', 'idle', (200,200), 0.3)
      Fighter.__init__(self, animLib, position = (0,0), centerOffset = 0, attackCD = 40, attackDamage = 5, maxHP = 40)
      self.currentCD = random.randint(0,self.attackCD)
      self.hurtSprite = True
     
  class MeleeMinion(Fighter):
    def __init__(self):
      animLib = AnimLib(os.path.join('data','Minion'), 'minion_', 'idle', (200,200), 0.3)
      Fighter.__init__(self, animLib, position = (0,0), centerOffset = 0, attackCD = 90, attackDamage = 15, maxHP = 80)
      self.currentCD = random.randint(0,self.attackCD)
      self.hurtSprite = True
  
  class CasterMinion(Fighter):
    def __init__(self):
      animLib = AnimLib(os.path.join('data','Ranged'), 'caster_', 'idle', (200,200), 0.3)
      Fighter.__init__(self, animLib, position = (0,0), centerOffset = 0, attackCD = 130, attackDamage = 25, maxHP = 50)
      self.currentCD = random.randint(0,self.attackCD)
      self.hurtSprite = True
  
  class RiftScuttler(Fighter):
    def __init__(self):
      animLib = AnimLib(os.path.join('data','Crab'), 'crab_', 'idle', (200,200), 0.3)
      Fighter.__init__(self, animLib, position = (0,0), centerOffset = 0, attackCD = 100, attackDamage = 10, maxHP = 100)
      self.currentCD = random.randint(0,self.attackCD)
      self.hurtSprite = True
  
  class Sentry(Fighter):
    def __init__(self):
      animLib = AnimLib(os.path.join('data','Sentry'), 'sentry_', 'idle', (200,200), 0.3)
      Fighter.__init__(self, animLib, position = (0,0), centerOffset = 0, attackCD = 120, attackDamage = 35, maxHP = 80)
      self.currentCD = random.randint(0,self.attackCD)
      self.hurtSprite = True
  
  class Wolf(Fighter):
    def __init__(self):
      animLib = AnimLib(os.path.join('data','Wolf'), 'wolf_', 'idle', (200,200), 0.3)
      Fighter.__init__(self, animLib, position = (0,0), centerOffset = 0, attackCD = 60, attackDamage = 15, maxHP = 50)
      self.currentCD = random.randint(0,self.attackCD)
      self.hurtSprite = True
  
  class Wraith(Fighter):
    def __init__(self):
      animLib = AnimLib(os.path.join('data','WraithG'), 'wraith_', 'idle', (200,200), 0.3)
      Fighter.__init__(self, animLib, position = (0,0), centerOffset = 0, attackCD = 60, attackDamage = 10, maxHP = 40)
      self.currentCD = random.randint(0,self.attackCD)
      self.hurtSprite = True
  
  class Wight(Fighter):
    def __init__(self):
      animLib = AnimLib(os.path.join('data','WraithW'), 'wight_', 'idle', (200,200), 0.3)
      Fighter.__init__(self, animLib, position = (0,0), centerOffset = 0, attackCD = 60, attackDamage = 15, maxHP = 90)
      self.currentCD = random.randint(0,self.attackCD)
      self.hurtSprite = True
  
  class Brambleback(Fighter):
    def __init__(self):
        animLib = AnimLib(os.path.join('data','Brambleback'), 'brambleback_', 'idle', (400,400), 0.3)
        Fighter.__init__(self, animLib, position = (0,0), centerOffset = 0, attackCD = 120, attackDamage = 20, maxHP = 200)
        self.currentCD = 120
        self.zonya = False
        self.zTimer = 0
        self.gotCombod = False
        self.zReady = True
        self.sound1 = os.path.join(*['data','EffectSFX','zonya1.wav'])
        self.sound2 = os.path.join(*['data','EffectSFX','zonya2.wav'])
        self.hurtSprite = True
    
    def render(self, height, width, st, at):
      render = Fighter.render(self, height, width, st, at)
      if self.zReady:
        self.battle.combosDone = [1,2,3]
      else:
        self.battle.combosDone = []
      if self.zonya:
        self.attackCD = 120
        self.active = False
        self.zTimer += 1
        if self.zTimer == 80:
          self.zonya = False
          self.changeImage('idle')
          self.zTimer = 0
          self.HP = 50
          self.active = True
          self.battle.callScene("redBattle")
      return render
        
    def getAttacked(self,damage):
        self.HP -= damage
        
        if self.HP <=0 and self.gotCombod:
          self.active = False
          self.zonya = False
          self.attackCD = 120
          self.attacking = False
          self.changeImage('idle')
          self.battle.callScene("killRed")    
        
        if not self.zonya:
          self.battle.effects.append(HitFlash(self,False))
          if self.HP <= 0:
            self.battle.playOnNextAvailableChannel(self.sound1)
            self.battle.playOnNextAvailableChannel(self.sound2)
            self.changeImage('zonya')
            self.zonya = True
            self.zReady = False
    
    def die(self):
      self.visible = False
      self.active = False
      self.alive = False
  
  class Baron(Fighter):
      def __init__(self):
        animLib = AnimLib(os.path.join('data','Nashor'), 'baron_', 'idle', (800,800), 0.3)
        Fighter.__init__(self, animLib, position = (0,0), centerOffset = 100, attackCD = 160, attackDamage = 30, maxHP = 600)
        self.eventTimer = 0
        self.currentCD = random.randint(0,self.attackCD)
        self.eventTrigger = False
        
      def render(self, height, width, st, at):
        render = Fighter.render(self, height, width, st, at)
        if self.eventTrigger:
          self.eventTimer += 1
          if self.eventTimer == 150:
            self.battle.callScene("waitBaron")
        return render
        
      def getAttacked(self,damage):
        self.HP -= damage
        #self.battle.effects.append(HitFlash(self,False))
          
        if self.HP <= self.maxHP / 2:
            if not self.eventTrigger:
              self.battle.playOnNextAvailableChannel(os.path.join(*['data','EffectSFX','baronspissed.wav']))
              self.attackCD = 20
              self.attackDamage = 5
            self.eventTrigger = True
            self.eventTimer = 0
            
        if self.HP <= 0:
            self.eventTrigger = False
            self.active = False
            self.attackCD = 20
            self.attacking = False
            self.changeImage('idle')
            self.battle.callScene("killBaron")
     
      def die(self):
        self.visible = False
        self.active = False
        self.alive = False
  
  class Doran(Fighter):
    def __init__(self):
      animLib = AnimLib(os.path.join('data','Doran'), 'doran_', 'idle', (100,150), 0.3)
      Fighter.__init__(self, animLib, position = (0,0), centerOffset = 0, attackCD = 80, attackDamage = 15, maxHP = 800)
      self.currentCD = self.attackCD
      self.halfHealthScene = False
      
    def getAttacked(self,damage):
        self.HP -= damage
        self.battle.effects.append(HitFlash(self,False))
        if self.HP <= self.maxHP / 2 and self.halfHealthScene == False:
          if len(self.battle.effects) == 0:
            self.halfHealthScene = True
            self.battle.callScene('hackerHalfHealth')
        if self.HP <= 0:
            self.alive = False
    
  class EnemyRaka(Fighter):
    def __init__(self):
      animLib = AnimLib(os.path.join('data','Soraka'), 'soraka_enemy_', 'idle', (180,250), 0.3)
      Fighter.__init__(self, animLib, position = (0,0), centerOffset = 0, attackCD = 60, attackDamage = 5, maxHP = 100)
      self.attackVoice = os.path.join(*['data','EffectSFX','SorakaAttack1.wav'])
      self.attackSound = os.path.join(*['data','EffectSFX','rakaBolt.wav'])
      self.hurtSound = os.path.join(*['data','EffectSFX','SorakaDamage.wav'])        
      self.superSprite = os.path.join(*['raka','vr','angry.png'])
      
      self.attackEffect = os.path.join(*['data','Soraka','SFX', 'raka_poof.png'])
      self.attackEffectSize = (160,260)
      self.attackEffectLength = 13
      
      self.currentCD = self.attackCD
    
    def render(self,width,height,st,at):
      render = Fighter.render(self,width,height,st,at)
      return render   
  
  class EnemyViktor(Fighter):
    def __init__(self):
      animLib = AnimLib(os.path.join('data','Viktor'), 'viktor_enemy_', 'idle', (150,300), 0.3)
      Fighter.__init__(self, animLib, position = (0,0), centerOffset = 30, attackCD = 60, attackDamage = 5, maxHP = 100)
      self.attackVoice = os.path.join(*['data','EffectSFX','viktor_Attack.wav'])
      self.attackSound = os.path.join(*['data','EffectSFX','vikBolt.wav'])
      
      self.hurtSound = os.path.join(*['data','EffectSFX','viktor_ReceiveDamage.wav'])
      self.superSprite = os.path.join(*['vik','vr','happy.png'])
      
      self.attackEffect = os.path.join(*['data','Viktor_FX', 'pink_explosion.png'])
      self.attackEffectSize = (550,400)
      self.attackEffectLength = 13
      
      self.currentCD = self.attackCD
      
######################### END ENEMY DECLARATION #########################################

# A way to manage multiple sprite sheets.
  class AnimLib(renpy.Displayable):
    def __init__(self, directory, prefix, defaultImage, framesize, delay, loop = True, **kwargs):
      super(AnimLib, self).__init__(**kwargs)
      self.library = {}
      supportedFileTypes = [".jpg",".png",".gif",".bmp",".pcx",".tga",".tif",".lbm",".pbm",".xpm"]
      self.framesize = framesize
      
      self.defaultImage = defaultImage
      self.currentImage = defaultImage
      self.frame = 0
      
      fullPath = os.path.join(renpy.config.gamedir, directory)
      for f in os.listdir(fullPath):
        fname, ext = os.path.splitext(f)
        if fname.startswith(prefix) and ext in supportedFileTypes:
          spriteName= fname[len(prefix):]
          fp = os.path.join(fullPath,f)
          #x, y, w, h = renpy.get_image_bounds(fp)
          #length = w / framesize[0]
          #TODO
          im = Image(fp)
          rn = im.render(0,0,0,0)
          w, h = rn.get_size()
          l = w / framesize[0]
          
          self.library[spriteName] = FilmStrip(fp, framesize, (10,10), delay, l, loop)
          
      
    def changeImage(self, newImage):
      self.currentImage = newImage
      try:
        self.library[self.currentImage].index = 0
        self.frame = 0
      except:
        self.currentImage = self.defaultImage
        self.library[self.currentImage].index = 0
        self.frame = 0
        
    def render(self, width, height, st, at):
      render = self.library[self.currentImage].render(width, height, st, at)
      self.frame = self.library[self.currentImage].index
      return render
      
    def visit(self):
      return [self.library[self.currentImage]]
      
  # This takes a sprite sheet and animates it. Created by xela from the RenPy forums
  class FilmStrip(renpy.Displayable):
        def __init__(self, image, framesize, gridsize, delay, frames=None, loop=True, reverse=False, **kwargs):
            super(FilmStrip, self).__init__(**kwargs)
            width, height = framesize
            self.image = Image(image)
            cols, rows = gridsize
          
            self.done = False
            
            if frames is None:
                frames = cols * rows
        
            i = 0
        
            # Arguments to Animation
            args = [ ]
        
            for r in range(0, rows):
                for c in range(0, cols):
        
                    x = c * width
                    y = r * height
        
                    args.append(Transform(self.image, crop=(x, y, width, height)))
        
                    i += 1
                    if i == frames:
                        break
        
                if i == frames:
                    break
                    
            # Reverse the list:
            if reverse:
                args.reverse()
                
                
            self.width, self.height = width, height
            self.frames = args
            self.delay = delay
            self.index = 0
            self.loop = loop
        
        def render(self, width, height, st, at):
            if not st:
                self.index = 0
            
            t = self.frames[self.index]
            
            if self.index == len(self.frames) - 1:
                if self.loop:
                    self.index = 0
                else:
                    self.done = True
                    return renpy.Render(0, 0)
            else:
                self.index = self.index + 1
            
            child_render = renpy.render(t, width, height, st, at)
            render = renpy.Render(self.width, self.height)
            render.blit(child_render, (0, 0))
            #renpy.redraw(self, self.delay)
            return render
        
        def get_length(self):
            return len(self.frames)
                
        def visit(self):
            return [self.image]
  
  
  class Torch(FilmStrip):
    def __init__(self,position,**kwargs):
      FilmStrip.__init__(self, os.path.join(*['data','Anim_Fire','anim_fire.png']), (100,125), (3,1), 0.3, 3, True, **kwargs)
      self.rect = pygame.Rect(position, (100,125))
      
  class Nexus(FilmStrip):
    def __init__(self,position,**kwargs):
      FilmStrip.__init__(self, os.path.join(*['data','Nexus','nexus.png']), (525,400), (14,1), 0.3, 14, True, **kwargs)
      self.rect = pygame.Rect(position, (525,400))
      
  class BaronPit(FilmStrip):
    def __init__(self,position,**kwargs):
      FilmStrip.__init__(self, os.path.join(*['data','BaronPit','baronPit.png']), (1300,385), (4,1), 0.3, 4, True, **kwargs)
      self.rect = pygame.Rect(position, (1300,385))
      
  
