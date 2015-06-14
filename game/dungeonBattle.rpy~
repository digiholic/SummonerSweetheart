init python:
  import pygame
  pygame.font.init()
  import renpygame
  import summonersRift
  import os
  import random
 
######################### BEGIN BATTLE OBJECT #########################################
 
  class Battle(renpy.Displayable):
    def __init__(self, **kwargs):
      global battleNumber
      global route
      super(Battle, self).__init__(**kwargs)
      self.width = 1024
      self.height = 768
      self.endScene = 'victoryScreen'
      self.music = os.path.join(*['data','music','BattleStance.wav'])      
      self.victorySound = os.path.join(*['data','music','VictoryTheme2.wav'])
            
      self.scenery = []
      self.players = []
      self.enemies = []
      self.effects = []
      self.ui = []
      
      self.arrow = TargetArrow()
      self.ui.append(self.arrow)
      
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
      sky = Scenery(os.path.join('data','SKY_BG.png'),(0,0))
      grnd = Scenery(os.path.join(*['data','GROUNDS','SR_GRND.gif']),(0,0))
      
      off = 0
      repeatGrnd = []
      while off < 1024:
        repeatGrnd.append(Scenery(os.path.join(*['data','GROUNDS','SR_GRND.gif']), (off, 768 - grnd.rect.height)))
        off += grnd.rect.width
        
      treetile = Scenery(os.path.join('data','summoner rift tree [repeatable].png'),(0,0))
      if number % 2 == 0:
        treetiles = [Scenery(os.path.join('data','summoner rift tree [repeatable].png'),(0, 668 - treetile.rect.height)),
                     Scenery(os.path.join('data','summoner rift tree [repeatable].png'),(treetile.rect.width, 668 - treetile.rect.height))]
      else:
        treetiles = [Scenery(os.path.join('data','summoner rift tree [repeatable].png'),(-88, 668 - treetile.rect.height)),
                     Scenery(os.path.join('data','summoner rift tree [repeatable].png'),(treetile.rect.width - 88, 668 - treetile.rect.height))]
                     
      if number == 0:
        self.enemies = [Poro()]
      elif number == 1:
        self.enemies = [Brambleback()]
      
      self.scenery.append(sky)
      self.scenery.extend(repeatGrnd)
      self.scenery.extend(treetiles)
      
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
        
      # Gotta find a way to do this with no rect
      # self.targetArrow...
      
      self.arrow.rect.bottom = self.enemies[self.target].rect.centery
      self.arrow.rect.centerx = self.enemies[self.target].rect.centerx
        
      self.players[0].rect.right = 0
      self.players[0].active = True
      self.players[0].visible = True
      self.players[0].changeImage('walk')
    
      self.state = 0
      self.target = 0
      
    def toggleActive(self):
      for ch in self.players:
        if ch.oldActiveState:
          ch.active = ch.oldActiveState
          ch.oldActiveState = None
        else:
          ch.oldActiveState = ch.active
          ch.active = False
      
      for en in self.enemies:
        if en.oldActiveState:
          en.active = en.oldActiveState
          en.oldActiveState = None
        else:
          en.oldActiveState = en.active
          ch.active = False
    
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
          if mc.rect.left >= self.players[i].centerOffset + (300 - (100 * i)):
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
          renpy.music.play(self.music, loop=True)
          self.state = 1
      
      # The actual battle
      elif self.state == 1:
        for i in range(0,len(self.enemies)):
          en = self.enemies[i]
          if en.alive and en.currentCD == 0:
            self.doEnemyAttack(i)
            en.currentCD = en.attackCD
          if not en.alive:
              self.enemies.remove(en)
              #self.effects.add(en.getHurtSprite())
              self.changeTarget(1)  
            
          if len(self.enemies) == 0:
            for ch in self.players:
              ch.attacking = None
              ch.changeImage('idle')
            if len(self.effects) == 0:
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
        
      for ch in self.players:
        child_render = ch.render(width, height, st, at)
        render.blit(child_render, ch.rect.topleft)
      for en in self.enemies:
        child_render = en.render(width, height, st, at)
        render.blit(child_render, en.rect.topleft)
      for ef in self.effects:
        child_render = ef.render(width, height, st, at)
        render.blit(child_render, ef.rect.topleft)
        if ef.done:
          self.effects.remove(ef)
      for ui in self.ui:
        child_render = ui.render(width, height, st, at)
        render.blit(child_render, ui.rect.topleft)
      
      renpy.redraw(self, 0.1)
      return render
      
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
        elif ev.key == pygame.K_ESCAPE:
          renpy.call("quitScreen")
      
    def endBattle(self):
      global battleNumber
      renpy.music.stop()
      renpy.music.play(self.victorySound,loop=False)
      battleNumber += 1
      for ui in self.ui:
        ui.visible = False
      
      self.toggleActive()
      renpy.call(self.endScene)
      self.toggleActive()
      
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
      if self.state == 1:
        if len(self.enemies) > 0:
          if self.players[i].active:
            en = self.enemies[self.target]
            while not en.alive:
              self.changeTarget(1)
              en = self.enemies[self.target]
            self.players[i].doAttack(en)
            
    def doEnemyAttack(self,i):
      j = random.randint(0,3)
      while not self.players[j].alive:
        j = (j + 1) % 4
      print self.enemies[i], " attacks ", self.players[j]
      self.enemies[i].doAttack(self.players[j])
      
    def changeTarget(self,amt):
      self.target += amt
      l = len(self.enemies)
      if l > 0:
        self.target = (l + self.target) % l
        self.arrow.rect.bottom = self.enemies[self.target].rect.centery
        self.arrow.rect.centerx = self.enemies[self.target].rect.centerx
      
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
      
      self.attackSound = None
      self.hurtSound = None
      self.hurtSprite = None
      
    def doAttack(self,target):
      if not self.attacking and self.currentCD == 0:
          self.attacking = True
          self.currentCD = self.attackCD
          self.animLib.changeImage('attack')
          self.target = target      
          if self.attackSound:
            renpy.sound.play(self.attackSound)
          
    def getAttacked(self,damage):
      self.HP -= damage
      if self.HP <=0:
        self.alive = False
        self.active = False
        self.visible = False
      if self.hurtSprite:
        self.battle.effects.append(self.hurtSprite)
      if self.hurtSound:
        renpy.sound.play(self.hurtSound)
        
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
######################### BEGIN CHAMPION DECLARATION #########################################
        
  class Ezreal(Fighter):
    def __init__(self):
      animLib = AnimLib(os.path.join('data','Ezreal'), 'ezreal_', 'idle', (250,200), 0.3)
      Fighter.__init__(self, animLib, position = (0,0), centerOffset = 0, attackCD = 80, attackDamage = 10, maxHP = 100)
      self.hurtSound = os.path.join(*['data','EffectSFX','EzDamage.wav'])
      self.attackSound = os.path.join(*['data','EffectSFX','EZ_Attack_1.mp3'])
      
  class Leona(Fighter):
    def __init__(self):
      animLib = AnimLib(os.path.join('data','Leona'), 'leona_', 'idle', (275,200), 0.3)
      Fighter.__init__(self, animLib, position = (0,0), centerOffset = 50, attackCD = 80, attackDamage = 10, maxHP = 120)
      self.attackSound = os.path.join(*['data','Leona','LeonaSFX','Attack1.wav'])
      self.hurtSound = os.path.join(*['data','Leona','LeonaSFX','Damage.wav'])
        
  class Ahri(Fighter):
    def __init__(self):
      animLib = AnimLib(os.path.join('data','Ahri'), 'ahri_', 'idle', (275,200), 0.3)
      Fighter.__init__(self, animLib, position = (0,0), centerOffset = 50, attackCD = 120, attackDamage = 15, maxHP = 80)
      self.attackSound = os.path.join(*['data','AhriSFX','Attack1_c.wav'])
      self.hurtSound = os.path.join(*['data','AhriSFX','AhriDamage.wav'])
        
  class Soraka(Fighter):
    def __init__(self):
      animLib = AnimLib(os.path.join('data','Soraka'), 'soraka_', 'idle', (180,250), 0.3)
      Fighter.__init__(self, animLib, position = (0,0), centerOffset = 0, attackCD = 60, attackDamage = 5, maxHP = 100)
      self.attackSound = os.path.join(*['data','EffectSFX','SorakaAttack1.wav'])
      self.hurtSound = os.path.join(*['data','EffectSFX','SorakaDamage.wav'])        
        
      
  class Rengar(Fighter):
    def __init__(self):
      animLib = AnimLib(os.path.join('data','Rengar'), 'rengar_', 'idle', (250,200), 0.3)
      Fighter.__init__(self, animLib, position = (0,0), centerOffset = 50, attackCD = 80, attackDamage = 10, maxHP = 120)
      self.attackSound = os.path.join(*['data','EffectSFX','Attack3.wav'])
      self.hurtSound = os.path.join(*['data','EffectSFX','ReceivingDamage2.wav'])
      
      
      
######################### BEGIN ENEMY DECLARATION #########################################
  class Poro(Fighter):
    def __init__(self):
      animLib = AnimLib(os.path.join('data','Poro1'), 'poro_', 'idle', (200,200), 0.3)
      Fighter.__init__(self, animLib, position = (0,0), centerOffset = 0, attackCD = 120, attackDamage = 10, maxHP = 40)
      self.currentCD = random.randint(0,self.attackCD)
        
  class Brambleback(Fighter):
    def __init__(self):
        animLib = AnimLib(os.path.join('data','Brambleback'), 'brambleback_', 'idle', (400,400), 0.3)
        Fighter.__init__(self, animLib, position = (0,0), centerOffset = 0, attackCD = 120, attackDamage = 20, maxHP = 200)
        self.currentCD = 120
        self.zonya = False
        self.zTimer = 0
        #self.sound1 = pygame.mixer.Sound('data/EffectSFX/zonya1.wav')
        self.sound = (os.path.join(*['data','EffectSFX','zonya2.wav']))
    
    def render(self, height, width, st, at):
      render = Fighter.render(self, height, width, st, at)
      if self.zonya:
        self.zTimer += 1
        if self.zTimer == 40:
          self.zonya = False
          self.changeImage('idle')
          self.zTimer = 0
          self.HP = 100
          renpy.call("redBattle")
      return render
        
    def getAttacked(self,damage):
        self.HP -= damage
        if self.HP <= 0:
            #self.sound1.play()
            renpy.sound.play(self.sound)
            self.changeImage('zonya')
            self.zonya = True
            
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
  
