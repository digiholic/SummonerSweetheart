import random, os.path
from copy import deepcopy,copy
from math import sin,cos,radians,degrees
import renpygame as pygame
from renpygame.locals import *
import renpy.store as store
import renpy.exports as renpy

import BattleGameEngine as BattleEngine

if not pygame.image.get_extended():
	raise SystemExit,"sorry, extended image module required"

from tileImage import TileImage
#from player import Player
from animatedSprite import AnimatedSprite
from imageLoad import *
from sound import *
from Champion import *
#from champion import Animation

# 1024*768
# size of screen
SCREENRECT     = Rect(0, 0, 1024, 768)



class Component:
		# is essentially an image oject that needs methods for highlighting the image. Useful for menus and 
		#def __init__(self,AlphaImage,Image,Pos,Rotate):
		def __init__(self):
			# 

			self.image = load_image('data','icons/alpha39_38.gif')
			self.default = load_image('data','icons/triangleC.gif')
			self.highlightVersion = load_image('data','/icons/traingleHL.gif')
			#self.pos = Pos
			self.rect = self.image.get_rect()
			self.width = self.image.get_width()
			self.height = self.image.get_height()
			self.isHighlight = False

		def update(self):
			if self.isHighlight == True:
				self.image = self.highlightVersion
			else:
				self.image = self.default
			
			self.rect = self.image.get_rect()

class SkillList(pygame.sprite.Sprite):
	# Is made of 8 triangular(trapazoid) components orinented in a certain way and blipped on the main surface skillList(sprite)
		def __init__(self):
			pygame.sprite.Sprite.__init__(self,self.containers)
			self.image = load_image('data','icons/alpha140_140.gif')
			self.image0 = copy(self.image)
			self.rect = self.image.get_rect(center  = (700,700))
			self.triangleTL = Component()	
			self.isHighlight = False	


		def update(self,isHL=False):
			self.triangleTL.isHighlight = isHL
			self.triangleTL.update()
			self.image = self.image0
			self.image.blit(self.triangleTL.image,pygame.Rect((0,0),(self.triangleTL.width,self.triangleTL.height)))


class ChargingCircle(pygame.sprite.Sprite):

	def __init__(self,Pos,Color):
		pygame.sprite.Sprite.__init__(self, self.containers)
		self.image = load_image('data','icons/alpha50_50.gif')
		self.image0 = load_image('data','icons/alpha50_50.gif')
		self.originalImage = copy(self.image)
		self.pos = Pos
		self.rect = self.image.get_rect(center = Pos)
		self.radius_width = 16
		self.readyCircle = load_image('data','icons/FinalGlowing.png',True)
		self.readyCircle.set_colorkey((0,0,0))
		self.percentComplete = 0
		self.reset = False
		self.color = Color

	def update(self):
		if self.percentComplete >= 1:
			#self.reset = False
			#self.image = self.originalImage
			if self.reset == True:
				#self.reset = False
				self.image = load_image('data','icons/alpha50_50.gif')
				#self.image.set_colorkey((0,0,0))
				#self.reset = True
				#self.image =load_image('data','icons/alpha50_50.gif')
				#self.percentComplete = 0
				#self.rect = self.image.get_rect(center = (self.pos[0]+1,self.pos[1]-13))
				self.rect = self.image.get_rect(center = self.pos)
				self.reset = False
				#self.image = self.image0
			elif self.reset == False:
				self.image = load_image('data','icons/FinalGlowing.png',True)
				self.image.set_colorkey((0,0,0))
				self.rect = self.image.get_rect(center = (self.pos[0]-1,self.pos[1]-03))
		else:
		
				i = self.percentComplete * 360
		
			
				p2 = [round(25 + 13 * cos(radians(i))), round(25 - 13 * sin(radians(i)))]
				
				#p2 = [(25 + 12 * cos(radians(i))), (25 - 12 * sin(radians(i)))] 
				pygame.draw.aaline(self.image, self.color, [25, 25],p2, 2)
				#if self.percentComplete == 1:
					# draw the ready sp
				#self.rect = self.image.get_rect(center = (self.pos[0]+1,self.pos[1]-13))
				#self.rect = self.image.get_rect(center = self.pos)


class StatusBarContainer(pygame.sprite.Sprite):
	def __init__(self,Org,rightSide = False ):
			pygame.sprite.Sprite.__init__(self, self.containers)
			offSetX = 45
			offSetX2 = 100
			self.image = load_image('data','icons/Whitebar.png',True)
			if rightSide == False:
			#	self.image = pygame.transform.flip(self.image,True,False)
				Org = ((Org[0]+offSetX),Org[1])
			else:
				self.image = pygame.transform.flip(self.image,True,False)
				Org = ((Org[0]+offSetX2),Org[1])
			#self.image = load_image('data','icons/alpha145_30.gif')
			self.rect = self.image.get_rect().move(Org)

class StatusBar(pygame.sprite.Sprite):

	def __init__(self,Org,rightSide = False):
		pygame.sprite.Sprite.__init__(self, self.containers)
		self.offSetX = 43
		self.offSetX2 = 98
		self.org0 = copy(Org)
		self.rs = rightSide

		self.image = load_image('data','icons/alpha145_30.gif')
		self.h = 10

		self.bar = pygame.Rect([6,12],[120,self.h])
		pygame.draw.rect(self.image,pygame.color.Color(255,60,9),self.bar)
		if rightSide:
		 	self.image = pygame.transform.flip(self.image,True,False)


		 	Org = ((Org[0]+self.offSetX2),Org[1]-6)
		else:
			Org = ((Org[0]+self.offSetX),Org[1]-6)

		self.org = Org
		self.image0 = copy(self.image)
		self.rect = self.image.get_rect().move(Org)
		self.maxX = 120
		#self.bar = pygame.Rect([6,12],[120,12])
		#pygame.draw.rect(self.image,pygame.color.Color(255,60,9),self.bar)
		self.color = pygame.color.Color(255,60,self.h)

		#self.update()


	def update(self,percentBar):
		# percentBar is percentage of bar to render
		#self.image = load_image('data','icons/alpha145_30.gif')
		#pygame.draw.rect(self.image0,pygame.color.Color(255,60,9),pygame.Rect([6,12],[round(percentBar * self.maxX),12]))
		self.image0 = load_image('data','icons/alpha145_30.gif')
		if self.rs:
			#self.image2 = pygame.Surface((120,6))
			#self.image2.fill(self.color,pygame.Rect([6,12],[round(percentBar * self.maxX),12]))
			#self.image2 = pygame.transform.flip(self.image2,True,False)
			pygame.draw.rect(self.image0,self.color,pygame.Rect([6,12],[round(percentBar * self.maxX),self.h]))
			self.image0 = pygame.transform.flip(self.image0,True,False)
			#self.org  = (self.org0[0] + round(self.maxX *percentBar),self.org[1])
			#self.org  = (self.org0[0] + 300,self.org[1])

			self.image = self.image0
			#self.rect = self.image.get_rect().move(self.org)
		else:
			pygame.draw.rect(self.image0,self.color,pygame.Rect([6,12],[round(percentBar * self.maxX),self.h]))
			self.image = self.image0
	

class HealthBarNameFont(pygame.sprite.Sprite):
	def __init__(self,NameString,Org):
		pygame.sprite.Sprite.__init__(self,self.containers)
		
		self.font = pygame.font.Font('Futura.ttc',18)
		#self.color = pygame.color.Color(255,60,9)
		self.color = Color('black')
		self.image = self.font.render(NameString,0,self.color)
		self.rect = self.image.get_rect().move(Org) 


class Banner(pygame.sprite.Sprite):

	def __init__(self):
		pygame.sprite.Sprite.__init__(self,self.containers)
		#self.image = load_image('data','icons/Top_ui.gif')
		#self.image0 = copy(self.image)
		#self.rect = self.image.get_rect()
		self.pos = (0,0)
		self.animation = Animation('/UITop',[20],False,True)
		#self.image = animation.images[0]


	def update(self,TimeElapsed):
		self.animation.updateS(TimeElapsed)
		if self.animation.stopDraw == True:
			self.image = self.animation.images[-1]
		else:
			self.image = self.animation.img
		#self.image.set_colorkey((30,157,27))
		self.rect = self.image.get_rect(topleft = self.pos)

class movingText(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self,self.containers)
		
		self.font = pygame.font.Font('Futura.ttc',14)
		self.color = Color('black')
		self.rect = self.image.get_rect()

class Arrow(pygame.sprite.Sprite):
	def __init__(self,Enemy):
		Pos = Enemy.pos
		self.tobject = TranslateObject(6,.2,[0,1])
		self.H = Enemy.image.get_height()
		pygame.sprite.Sprite.__init__(self,self.containers)
		self.image = load_image('data','icons/Arrow2.png',True)
		self.image.set_alpha(100)
		self.rect = self.image.get_rect(center = (Pos[0],Pos[1] + self.H/SCREENRECT[3] * 60  ))
		self.pos = Pos
		self.targetEnemy = Enemy
		self.enemyChanged = False

	def newTarget(self,Enemy):
		self.targetEnemy = Enemy
		self.enemyChanged = True


	def update(self):
		if self.enemyChanged:
			self.tobject.translate(self)
			self.pos = self.targetEnemy.pos
			self.H = self.targetEnemy.image.get_height()
			self.rect = self.image.get_rect(center = (self.pos[0],self.pos[1] + self.H/SCREENRECT[3] * 60 ))
			self.enemyChanged = False
			
		else:
			self.tobject.translate(self)
			
class DialogueBox(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self,self.containers)
		self.image = load_image('data','icons/TextBox2.png',True)
		self.image.set_alpha(100)
		#self.image.covert_alpha()
		self.rect = self.image.get_rect(topleft = (0,0))


class Avatar(pygame.sprite.Sprite):
	#heads = []
	def __init__(self,headID,Pos):
		#pygame.sprite.Sprite.__init__(self,self.containers)
		#self.image = self.heads[headPic]
		self.image = load_image('data','icons/heads/ahrihead.png')
		self.pos = Pos
		self.rect = self.image.get_rect(center = (0,self.pos[1]))

class BUIBox(pygame.sprite.Sprite):
	def __init__(self,Pos,RightSide):
		pygame.sprite.Sprite.__init__(self,self.containers)
		self.pos = Pos
		self.image = load_image('data','icons/batlleuiBOX.png',True)
		if RightSide:
			self.image = pygame.transform.flip(self.image,True,False)
			self.rect = self.image.get_rect(midright = (self.pos[0]+300,self.pos[1]))
		else:
			self.rect = self.image.get_rect(midleft = self.pos)

class BattleUI:

	Pos = [[(0,60 + 80*i) for i in range(4)],[(SCREENRECT[2]-300,60 + 80*i) for  i in range(4)]]
	
	def __init__(self,Name,ID,rightSide = False):
		

		self.nameFont = BattleFont()
		self.pos = self.Pos[int(rightSide)][ID]
		self.name = Name
		self.buiBox = BUIBox(self.Pos[int(rightSide)][ID],rightSide)
		self.statusBarContainer = StatusBarContainer(self.pos,rightSide)

		if rightSide:
			self.nameFont.update(self.name,'%s',self.pos)

			pass
		else:
			self.nameFont.update(self.name,'%s',self.pos)

			self.avatar = Avatar(Name,self.pos)

		self.nameFont = HealthBarNameFont(Name,self.pos)
		self.healthBar = StatusBar(self.pos,rightSide)

	def update(self,Percent):
		self.healthBar.update(Percent)

	def kill(self):
		self.healthBar.kill()


class BattleFont(pygame.sprite.Sprite):
	def __init__(self,size=30,font = 'Achafont.ttf',):
		pygame.sprite.Sprite.__init__(self,self.containers)
		
		self.font = pygame.font.Font(font,size)
		#self.font.set_italic(1)
		self.color = Color('black')
		self.image = self.font.render('',0,self.color)
		self.rect = self.image.get_rect().move(10,300)

	def update(self,pos,mg,org):
		msg = mg % pos
		self.image = self.font.render(msg,0,self.color)
		self.rect = self.image.get_rect().move(org)

class SampleFont(pygame.sprite.Sprite):
	# An example of rendering font. From what I can tell this is best to handle with globals
	def __init__(self,size=30,font = 'Achafont.ttf',):
		pygame.sprite.Sprite.__init__(self,self.containers)
		
		self.font = pygame.font.Font(font,size)
		#self.font.set_italic(1)
		self.color = Color('black')
		self.image = self.font.render('',0,self.color)
		self.rect = self.image.get_rect().move(10,300)

	def update(self,pos,mg,org):
		msg = mg % pos
		self.image = self.font.render(msg,0,self.color)
		self.rect = self.image.get_rect().move(org)

class VictoryImage(pygame.sprite.Sprite):

	def __init__(self,pos):
		pygame.sprite.Sprite.__init__(self,self.containers)
		self.image = load_image()
		self.rect = self.image.get_rect(center = pos)

class Scene:
	''' Scenes are composed of lines(dialogues), and include any other "scripted" events for example moving characters, etc. '''
	''' Every Scene is connected to a specific encounter and will pause the game until completed '''

	def __init__(self):
		self.triggerEnd = True # trigger at end of encounter, or beginning
		self.encounter = 0 # encounter ID to trigger the scene




class Dialogue:
	''' Dialogee's are simply all the text that transpires on a text box until it closes. '''
	def __init__(self):
		self.db = DialogueBox()
		self.font = SampleFont()
	#	self.lines = 












