import random, os.path

from copy import copy
import renpygame as pygame
import glob,re
import math
from renpygame.locals import *

import renpy.store as store
import renpy.exports
import renpy

from imageLoad import *
# from ui import *
# imuiport 
import ui
#from ui import *

if not pygame.image.get_extended():
	raise SystemExit,"sorry, extended image module required"

SCREENRECT     = Rect(0, 0, 1024, 768)


class Animation:

	def __init__(self,FilePath,Tlist,isLoop,IsAlpha = True):
		self.filePath = FilePath
		self.isAlpha = IsAlpha
		self.loadGif() # fills up images list
		self.numFrames = len(self.images)
		#self.timeList = [] 
		self.timeList = Tlist # timing informationin ms
		self.img = self.images[0]
		#self.alphaImage = blah
		self.timeElapsed = 0
		self.animationDelta = Tlist[0]
		self.totalLoopTime = 0


		if isinstance(isLoop,bool):
			self.loop = isLoop
			self.CountLoopTime = False
			self.loopTime = 0
		else: #if isLoop is an int
			self.loop = True
			self.loopTime = isLoop
			self.CountLoopTime = True

		self.currentNumLoops = 0
		self.ptr = 0
		self.stopDraw = False
		if len(Tlist) == 1:
			self.constantTime = True
		else:
			self.constantTime = False

	def reset(self):
		# Called whenever animation is forcibly reset
		self.ptr = 0
		self.timeElapsed = 0
		self.img = self.images[0]
		self.stopDraw = False
		self.totalLoopTime = 0
		
	def updateS(self,TimeElapsed):
		#self.updateTimeElapsed(TimeE)		
		self.timeElapsed += TimeElapsed
		self.totalLoopTime += TimeElapsed

		if self.constantTime == True:
			timeDelta = self.timeList[0]
		else:
			timeDelta = self.timeList[self.ptr]

		if self.timeElapsed >= timeDelta:
			self.timeElapsed = 0
			self.ptr += 1
			if self.ptr % self.numFrames == 0:
				if self.loop == False:
					self.stopDraw = True		
				self.ptr = 0
			self.img = self.images[self.ptr]
		elif self.totalLoopTime > self.loopTime and self.CountLoopTime == True:
				self.stopDraw = True
		

	def loadGif(self):
		'''This is a necessary function that will take a file path, build the gif, and set the self.images extract all images''' 
		self.images = []
		imgD = {}
		filetypes = ['.png','.gif']
		for f in filetypes:
			for fname in renpy.exports.list_files():
				if fname.startswith('data' + self.filePath):
					if fname.endswith(f):
						strSplit = fname.split("_")
						imgD[int(re.split(r'\.(?!\d)',strSplit[-1])[0])] = load_image([],fname,self.isAlpha)
						
		sorted(imgD)
		for i in imgD:
			self.images.append(imgD[i])


class SpecialEffect(pygame.sprite.Sprite):
	# A list of lists, of prespecified size. The
	EffectAnimations = []  
	offSets = [(0,0),(20,20),(0,-25),[0,50],[0,25],[0,25],[0,25],[0,25]]   
	alphas = [200,200,255,255,255,255,255,255]           # The offset is needed in order to get the positioning right

	def __init__(self,ID,Org,isLoop,Alpha,ScaleImage = False):
		pygame.sprite.Sprite.__init__(self,self.containers)
	

		
		
		if isinstance(ID,StatusEffect):
			self.se = ID
			self.Id = self.se.Id
			self.animation = self.EffectAnimations[self.Id]
			self.animation.loopTime = self.se.duration
			self.animation.CountLoopTime = True
		elif isinstance(ID,Skill): 
			self.sk = ID
			self.Id = self.sk.Id
			self.animation = self.EffectAnimations[self.sk.Id]
		elif isinstance(ID,int):
			self.animation = self.EffectAnimations[ID]
			self.Id = ID


		
		self.totalFrames = self.animation.numFrames
		self.pos = copy(Org)
	#	self.Id = ID
		
		if isinstance(ScaleImage,bool):
			self.scaleImage = ScaleImage
		else:
		
			self.scaleAmount = ScaleImage
			self.scaleImage = True

		# should put a try, except here and remove all the alpha stuff (similar to scale image)
		if Alpha:
			self.alpha = self.alphas[self.Id]
		else:
			self.alpha = 255;
		self.image = self.animation.img
		self.h = self.image.get_height()
		self.w = self.image.get_width()
		


	def updateE(self,TimeElapsed):
		self.animation.updateS(TimeElapsed)
		self.image = self.animation.img
		#self.image = self.image.convert()
		#self.image.set_colorkey([0,0,0])
		self.image.set_alpha(self.alpha)

		if self.scaleImage: self.image = pygame.transform.smoothscale(self.image,(int(round(self.w*self.scaleAmount)),int(round(self.h*self.scaleAmount))))


		self.rect = self.image.get_rect(center = (self.pos[0] + self.offSets[self.Id][0],self.pos[1] + self.offSets[self.Id][1]))


class Enemy(pygame.sprite.Sprite):
	def __init__(self,ID,AnimSprite,AttackAnimation,CoolDown):
		# Takes an already animatedSprites images and builds and places it in game world.
		pygame.sprite.Sprite.__init__(self,self.containers)
		self.animatedSprite = AnimSprite
		self.pos = list((self.animatedSprite.point,self.animatedSprite.yOffset))
		#self.idleAnimation = Animation(self.animatedSprite.filePath,[250],True,True)
		
		self.CPos = list(copy(self.pos))
		self.idleAnimation = self.animatedSprite.animation
		self.name = self.animatedSprite.name

		if type(AttackAnimation) == bool:
			self.hasAttackAnimation = False
			self.animations = [self.idleAnimation]		
		else: 
			self.hasAttackAnimation = True
			self.attackAnimation = AttackAnimation
			self.animations = [self.idleAnimation,self.attackAnimation]
		

		self.animationID = 0
		self.image = self.idleAnimation.images[self.animatedSprite.ptr] # to make sure animation is smooth
		self.rect = self.image.get_rect(center = self.pos)
		self.Id = ID
		self.maxHealth = 100
		self.health = 100
		self.healthPercent = 1.0
		self.coolDown  = CoolDown
		self.canUseSkill = False
		self.isAlive = True
		self.timeDelta = 0
		self.specialEffect = 1
		self.isCCd = False

		''' Basic Translate Attack Animation '''

		self.translateObject = TranslateObject(12,2,[-1,0]) 

		self.direction = [-1,1]
		self.Attack = False
	
		self.GenerateUI()

		self.skill = Skill(15,0,0,10)


		self.modifers = {'RP':0,'ATK':0,'DMG':0,'CD':0,'SHIELD':0,'DEF':0,'CC':False}
		

		self.currentStatusEffects = []


	def GenerateUI(self):
		# Generates The UI using the length of the name, and its ID (which row)
		self.battleUI = ui.BattleUI(self.name,self.Id,rightSide = True) # Since not a champion
		self.chargingCircle = ui.ChargingCircle((self.pos[0],self.pos[1]-50),pygame.color.Color(255,60,9))




		
	def updateM(self,TimeElapsed):

		if self.animations[self.animationID].stopDraw == True:
			self.animations[self.animationID].stopDraw = False
			self.animationID = 0 # default back to Idle
		self.animations[self.animationID].updateS(TimeElapsed)
		self.image = self.animations[self.animationID].img

		self.updateTime(TimeElapsed)
		#self.image.convert()

		self.chargingCircle.percentComplete = float(self.timeDelta)/float(self.coolDown)
		self.chargingCircle.update()

		if self.Attack == True and self.hasAttackAnimation == False: self.defaultAttack()


		self.isCCd = self.modifers['CC']



	def updateHealth(self,Ability):
		if isinstance(Ability,Skill):
			self.health -= Ability.number

			#if self.Sound: self.soundFX[2].play()

			self.healthPercent = float(self.health)/float(self.maxHealth)
			self.battleUI.healthBar.update(self.healthPercent)
			#self.statusBar.update(self.healthPercent)

		elif isinstance(Ability,StatusEffect):
			self.currentStatusEffects.append(Ability)
			self.modifers[Ability.mod] = Ability.percentage


		if self.health <= 0:
			self.isAlive = False

	def resetTimeDelta(self):
		self.canUseSkill = False
	  #  pdb.set_trace()
		self.timeDelta = 0

	def updateTime(self,timeD):
		if not self.isCCd:
			self.timeDelta += timeD
			if self.timeDelta >= self.coolDown:
				self.canUseSkill = True
				#return self.canUseSkill
		for se in self.currentStatusEffects:
			se.update(timeD)
			if se.isDone:
				if se.mod == 'CC':
					self.isCCd = False # yeah i spelled modifier wrong..for some reason
					self.modifers['CC'] = False
				else:

					self.modifers[se.mod] = 0
				
				''' Going to need to handle processing the different status effect visual representations: auras, ColorTransforms, and basic spell animations ''' 
				if se.type == 'Aura':
					self.AuraID = 0 # 
				# elif SE.type == 'FX':
				# 	self.
				se.isDone = False

				self.currentStatusEffects.remove(se)

	def attack(self,champions,mode = 1):
		# a very basic AI that supports various modes (overrides)

			# The first mode chooses a champ at random


			# The second mode chooses a champ based on an aggro ability
				# may or may not every actually be included

			# the third mode chooses a champ by sampling from a weighted distrubtion (a combination and first and third modes)


		if mode == 1:
			return champions[random.randint(0,len(champions)-1)]
			
	def useSkill(self,Target):

		self.skill.number = self.skill.number * (1 - self.modifers['DMG'])
		self.Attack = True
		self.chargingCircle.reset = True
		Target.updateHealth(self.skill)
		self.chargingCircle.percentComplete = float(self.timeDelta) / self.coolDown
		self.chargingCircle.update()
		self.resetTimeDelta()

	def defaultAttack(self):


		self.translateObject.translate(self)
		if self.translateObject.Done == True:
			self.Attack = False





	def death(self):
		self.chargingCircle.kill()
		self.kill()

		self.specialEffect.animation.stopDraw = True


class Champion(pygame.sprite.Sprite):
	pathList = ['/Normal','/Red','/Blue','/Yellow','/Green']

	def __init__(self,animationPath,Org,CoolDown,SoundFX,ID,Name,RP,Skills,OrgAura,uiOffset,ATKOS = (0,0),AtkOSAura = (0,0),AtkDeltas = [150]):
		# Build Animations

		self.attackAnimations = [Animation(animationPath+'/Atk'+p,[150],False,True) for p in self.pathList]
		self.idleAnimations = [Animation(animationPath+'/Idle'+p,[150],True,True) for p in self.pathList]

		pygame.sprite.Sprite.__init__(self,self.containers)

		self.atkOffset = ATKOS
		self.atkOffsetAura = AtkOSAura
		self.currentSkill = 0

		self.animations = [self.idleAnimations,self.attackAnimations]

		#self.animations = [self.idleAnimation,self.attackAnimation] 
		self.animationID = 0 #defaults to idle animaion
		self.colorID = 0
		self.AuraID = 0

		self.posA = OrgAura
		self.pos = Org
		self.image = self.animations[0][0].img
		#self.image = load_image('data','Ahri_idle/Frame_1_(150ms).gif')
		self.rect = self.image.get_rect(center = self.pos)
		self.health = 1000
		self.maxHealth = 1000
		self.coolDown  = CoolDown
		self.canUseSkill = False
		self.isAlive = True
		self.timeDelta = 0
		self.uiOffset = uiOffset
		self.healthPercent = 1.0
		self.Id = ID
		self.name = Name
		self.rp = RP
		self.Sound = True
		self.isCCd = False
		# Sound Elements (List)
		self.soundFX = SoundFX
		if SoundFX == False:
			self.Sound = False

		self.skills = Skills
		
		self.currentStatusEffects = []

		self.modifers = {'RP':0,'ATK':0,'DMG':0,'CD':0,'SHIELD':0,'DEF':0,'HEAL':0,'CC':False}
		
		self.AuraDict = {'ATK':1,'CD':3,'HEAL':4}

	def updateC(self,TimeElapsed):
		# Update all animations and images
		#self.timeDelta += TimeElapsed

		if self.AuraID > 0:
			if self.animationID == 1:
				self.rect = self.image.get_rect(center = (self.posA[0] + self.atkOffsetAura[0],self.posA[1] + self.atkOffsetAura[1]))
			else: self.rect = self.image.get_rect(center = (self.posA[0],self.posA[1]))
		else:
			if self.animationID == 1:
				self.rect = self.image.get_rect(center = (self.pos[0] + self.atkOffset[0],self.pos[1]+self.atkOffset[1]))
			else: self.rect = self.image.get_rect(center = self.pos)

		if self.animations[self.animationID][self.AuraID].stopDraw == True:
			self.animations[self.animationID][self.AuraID].stopDraw = False
			self.animationID = 0 # default back to Idle
		self.animations[self.animationID][self.AuraID].updateS(TimeElapsed)
		self.image = self.animations[self.animationID][self.AuraID].img

		self.updateTime(TimeElapsed)
		#self.image.convert()

		''' Apply Buffs/Debuffs '''
		self.coolDown *= (1 - self.modifers['CD'])

		for s in self.skills:
			if isinstance(s,Skill):
				s.number *= (1 + self.modifers['ATK'] ) 

		self.health += (0 + self.modifers['HEAL'] )

		self.isCCd = self.modifers['CC']




		self.chargingCircle.percentComplete = float(self.timeDelta)/float(self.coolDown)
		self.chargingCircle.update()



	def updateHealth(self,Ability):
		if isinstance(Ability,Skill):
			if Ability.isEnemy == True:
				self.health -= Ability.number

				if self.Sound: self.soundFX[-1].play()

				
			else:
				self.health += Ability.number

			self.healthPercent = float(self.health)/float(self.maxHealth)
			self.battleUI.healthBar.update(self.healthPercent)
		#self.statusBar.update(self.healthPercent)

		elif isinstance(Ability,StatusEffect):
			self.currentStatusEffects.append(Ability)
			self.AuraID = self.AuraDict[Ability.mod]
			self.modifers[Ability.mod] = Ability.percentage


		if self.health <= 0:
			self.isAlive = False

	

	def updateTime(self,timeD):
		self.timeDelta += timeD
		if self.timeDelta >= self.coolDown:
			self.canUseSkill = True

		
		for SE in self.currentStatusEffects:
			SE.update(timeD)
			if SE.isDone: 
				self.modifiers[SE.mod] = 0
				SE.isDone = False
				
				if se.type == 'Aura':
					self.AuraID = 0 #
				self.currentStatusEffects.remove(SE)

	def GenerateUI(self):
		# Generates The UI using the length of the name, and its ID (which row)
		self.battleUI = ui.BattleUI(self.name,self.Id,rightSide = False) # Since not a champion
		#self.healthBarName = ui.HealthBarNameFont(self.name,(880,50))
		#self.color = pygame.color.Color(255,60,9)
		self.chargingCircle = ui.ChargingCircle((self.pos[0] + self.uiOffset[0] ,450 + self.uiOffset[1]),pygame.color.Color(57,221,240))
			#self.statusBar = ui.StatusBar((750,45*(self.Id+1)*1.2))

	
			
	def resetTimeDelta(self):
		self.canUseSkill = False
	  #  pdb.set_trace()
		self.timeDelta = 0

	def updateModifiers(self):
		pass

	def useSkill(self,Target,AbilityString):
		self.chargingCircle.reset = True
		Target.updateHealth(self.skills[self.currentSkill])
		AbilityString.append(self.skills[self.currentSkill].skillID)
		self.chargingCircle.percentComplete = float(self.timeDelta) / self.coolDown

		self.chargingCircle.update()
		self.resetTimeDelta()

		# trigger target number Effect (sword slash, fire, etc) and sound.
		self.triggerEffects()
	
	def triggerEffects(self):
		if self.Sound: self.soundFX[random.randint(0,len(self.soundFX) - 2)].play()
		# trigger champion Attack Animation
		self.animationID = 1

	def death(self):

		self.chargingCircle.kill()
		self.kill()
	#	self.battleUI.kill()

		#self.specialEffect.animation.stopDraw = True

class Ezreal(Champion):
	def __init__(self):
		EzSkills  = [Skill(Num = 10,aID = 3,sID = 2, SKILLID = 0),Skill(Num = 10,aID = 3,sID = 2, SKILLID = 0)]
		ezreal_SFX = [pygame.mixer.Sound('data/EffectSFX/EZ_Attack_1.mp3'), pygame.mixer.Sound('data/EffectSFX/EzDamage.wav')]
		Champion.__init__(self,'/Ezreal',(430,573),6000,ezreal_SFX,0,'EZREAL',2,EzSkills,(429,572),(-8,0),ATKOS = (23,-3),AtkOSAura = (23,-11))

class Ahri(Champion):
	def __init__(self):
		AhriSkills = [Skill(10,1,1,2),StatusEffect('CC',False,5000,aID = 7)]
		ahri_SFX = [pygame.mixer.Sound('data/AhriSFX/Attack1_c.wav'),pygame.mixer.Sound('data/AhriSFX/Attack2.ogg'),pygame.mixer.Sound('data/AhriSFX/AhriDamage.wav')]
		Champion.__init__(self,'/Ahri',(301,570),12000,ahri_SFX,1,'AHRI',0,AhriSkills,(299,565),(0,0),ATKOS = (65,1),AtkOSAura = (66,5))
		
class Soraka(Champion):
	def __init__(self):
		SorakaSkills = [Skill(10,2,0,6),Skill(10,2,0,6)]
		soraka_SFX = [pygame.mixer.Sound('data/EffectSFX/SorakaAttack1.wav'),pygame.mixer.Sound('data/EffectSFX/SorakaDamage.wav')]
		Champion.__init__(self,'/Soraka',(152,538),8000,soraka_SFX,2,'SORAKA',1,SorakaSkills,(180,573),(27,0),ATKOS = (0,1),AtkOSAura = (-24,-29))

class Rengar(Champion):
	def __init__(self):
		RengarSkills = [Skill(10,0,3,4),Skill(10,0,3,4)]
		rengar_SFX = [pygame.mixer.Sound('data/EffectSFX/Attack3.wav'),pygame.mixer.Sound('data/EffectSFX/ReceivingDamage2.wav')]
		Champion.__init__(self,'/Rengar',(120,570),10000,rengar_SFX,3,'RENGAR',3,RengarSkills,(65,570),(-55,0),ATKOS = (0,-2),AtkOSAura = (48,2))

class Leona(Champion):
	def __init__(self):
		LeoSkills = [Skill(10,0,0,0)]
		leona_SFX = [pygame.mixer.Sound('data/Leona/LeonaSFX/Attack1.wav'),pygame.mixer.Sound('data/Leona/LeonaSFX/Attack2.wav'),pygame.mixer.Sound('data/Leona/LeonaSFX/Damage.wav')]
		Champion.__init__(self,'/Leona',(400,568),6000,leona_SFX,0,'Leona',3,LeoSkills,(400,560),(0,-25),ATKOS = (65,0),AtkOSAura = (65,5))
		
class Jayce(Champion):
	def __init__(self):
		JayceSkills = [Skill(10,0,0,2)]
		jayce_SFX = [pygame.mixer.Sound('data/EffectSFX/JayceAttack.wav'),pygame.mixer.Sound('data/EffectSFX/JayceDamage.wav')]
		Champion.__init__(self,'/Jayce',(293,556),12000,jayce_SFX,1,'Jayce',2,JayceSkills,(264,562),(-10,-25),ATKOS = (-55,-23),AtkOSAura = (-3,-9))
		
class Rumble(Champion):
	def __init__(self):
		RumbleSkills = [Skill(10,0,0,3)]
		rumble_SFX = [pygame.mixer.Sound('data/EffectSFX/RumbleAttack1.wav'),pygame.mixer.Sound('data/EffectSFX/RumbleAttack2.wav'),pygame.mixer.Sound('data/EffectSFX/RumbleDamage1.wav')]
		Champion.__init__(self,'/Rumble',(197,558),8000,rumble_SFX,2,'Rumble',1,RumbleSkills,(162,577),(-40,-25),ATKOS = (0,0),AtkOSAura = (35,-3))
		
class Viktor(Champion):
	def __init__(self):
		VikSkills = [Skill(10,6,0,4)]
		Champion.__init__(self,'/Viktor',(43,546),10000,False,3,'Viktor',0,VikSkills,(42,558),(-2,-25),ATKOS = (-4,-27),AtkOSAura = (-4,-35))
		
class Skill():
	comboSkillIDs = [16,17,18,19,20,21]
	def __init__(self,Num,aID,sID,SKILLID,IsEnemy = True):
		# aID = animationID
		# sID = soundID

		self.isEnemy = IsEnemy
		self.Id = aID
		self.number = Num
		self.sId = sID
		self.skillID = SKILLID
	
	

class ComboSkill():
	def __init__(self,Ability,TriggerSequence):
		self.ability = Ability
		self.triggerSequence = TriggerSequence
		self.triggerLen = len(self.triggerSequence)


class TranslateObject():
	'''Translates any pygame Rect (Sprite) as a function of position'''
	''' Built in support for predefined Paths, Polar and Cart Coordiantes '''
	def __init__(self,distT,Speed,Vector2D,Axis='xyz',Path = None):
		self.distTranslate = distT # maximum distance to translate
		self.speed = Speed
		self.axis = Axis
		self.currentLoop = 0
		#self.axisTypes = ['x','y','both','polar']

		self.direction = [1,-1] # Used to reverse vector for looping
		#self.Attack = False
		#self.unitVector = self.getUnitVector(Vector2D)
		self.unitVector = Vector2D
		self.Done = False
		self.distanceTraveled = 0
		self.loop = 0

	def translate(self,Sprite):
		self.Done = False
	 	if self.distanceTraveled < self.distTranslate:
	 		self.distanceTraveled += 1 * self.speed
	 		Sprite.pos[0] += self.unitVector[0] * self.direction[self.loop] * self.speed
	 		#self.CPos[0] = round(self.CPos)
	 		Sprite.pos[1] += self.unitVector[1] * self.direction[self.loop] * self.speed
	 		self.distnaceTraveled = round(self.distanceTraveled)
			Sprite.rect = Sprite.image.get_rect(center = Sprite.pos)
		else:
			self.distanceTraveled = 0
			self.loop += 1
			if self.loop > 1:
				self.loop = 0
				#self.Attack = False
				self.Done = True

	def getUnitVector(self,V2D):
		if self.axis == 'polar':
			return [math.cos(V2D[0]),math.sin(V2D[1])]
		else:
			mag = math.sqrt(V2D[0]**2 + V2D[1]**2)
			if mag==1: 
				return V2D
			else:
				return [V2D[0]/mag,V2D[1]/mag]



class StatusEffect():

	types = [0,1,2,3]
	# 0 = Slow
	# 1 = 

	def __init__(self,Mod,IsEnemy,Duration,Percentage = 0.10,aID=0,ID = 0,Type= None):
		self.mod = Mod
		self.isEnemy = IsEnemy #buff,debuff
		self.duration = Duration
		self.percentage = Percentage
		self.timeElapsed = 0
		self.Id = aID #animation ID
		self.skillID = ID
		self.isDone = False
		self.type = Type  # type refers to "Aura","Color","FX", None assumes no visual representation



	def update(self,TimeD):
		self.timeElapsed += TimeD
		if self.timeElapsed >= self.duration:
			self.isDone = True
			self.timeElapsed = 0




def useSkill(Champion,Target,Skill):
	Target.updateHealth(Skill)
	Champion.chargingCircle.percentComplete = float(Champion.timeDelta) / Champion.coolDown
	Champion.chargingCircle.update()
	Champion.resetTimeDelta()



