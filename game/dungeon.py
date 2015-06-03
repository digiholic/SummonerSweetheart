import random, os.path
import renpygame as pygame
import renpy
import renpy.display
from renpygame.locals import *
import renpy.store as store
import renpy.exports as renpy
import BattleGameEngine as BattleEngine
import screenObjects
from player import Player
from animatedSprite import *
from imageLoad import *
from tileImage import *
from ui import *
from sound import *
from Champion import *
from copy import copy
from collections import OrderedDict

dungeon = None

def getDungeon():
    global dungeon
    if dungeon:
        return dungeon
    else:
        dungeon = Dungeon()
        return dungeon
    
class Dungeon():
    def __init__(self):
        if not pygame.image.get_extended(): raise SystemExit,"sorry, extended image module required"
        self.eventList = []
        self.initialized = 0
        self.screen = renpy.display.pgrender.surface(SCREENRECT.size,True)
        self.background = renpy.display.pgrender.surface(SCREENRECT.size,True)
        
        sky = load_image('data','SKY_BG.png',True)
        self.background.blit(sky,(0,0))
        
        self.SCREENRECT = Rect(0, 0, 1024, 768)
        self.callScene = ""
        self.eventList = []
        
        self.variables = {}
        self.spriteGroups = {}
        #self.fonts = {}
        self.spellSoundEffects = {}
        self.sounds = {}
        
        self.gameObjects = []        
        self.engagements = []
        
        self.initGroupsAndContainers()
        pygame.init()
    
    def loadFromVN(self,vnInput):
        try:
            self.variables['maleRoute']           = vnInput[0]
            self.variables['gifts']               = vnInput[1]
            self.variables['comboSkillsUnlocked'] = vnInput[2]
            self.variables['sceneKeys']           = vnInput[3]
        except IndexError:
            self.variables['maleRoute']           = True
            self.variables['gifts']               = []
            self.variables['comboSkillsUnlocked'] = []
            self.variables['sceneKeys']           = []
            
    """
    Initialize all of the sprite groups and static containers for Sprites.
    """
    def initGroupsAndContainers(self):
        self.spriteGroups['updatedSprites'] = pygame.sprite.RenderUpdates()
        self.spriteGroups['uis'] = pygame.sprite.Group()
        self.spriteGroups['staticIMAGES'] = pygame.sprite.Group()
        self.spriteGroups['players'] = pygame.sprite.Group()
        self.spriteGroups['followPlayers'] = pygame.sprite.Group()
        self.spriteGroups['texts'] = pygame.sprite.Group()
        self.spriteGroups['logs'] = pygame.sprite.Group()
        self.spriteGroups['champions'] = pygame.sprite.Group()
        self.spriteGroups['poofEffect'] = pygame.sprite.Group()
        self.spriteGroups['FIRE_Effect'] = pygame.sprite.Group()
        self.spriteGroups['monsters'] = pygame.sprite.Group()
        self.spriteGroups['DB'] = pygame.sprite.Group()
        self.spriteGroups['EFFECTS'] = pygame.sprite.Group()
        self.spriteGroups['healthBarsC'] = pygame.sprite.Group()
        self.spriteGroups['battleFont'] = pygame.sprite.Group()
        self.spriteGroups['healthBars'] = pygame.sprite.Group()
    
        self.spriteGroups['SpriteGroups'] = [self.spriteGroups['uis'],self.spriteGroups['DB'],self.spriteGroups['players'],self.spriteGroups['texts'],self.spriteGroups['staticIMAGES'],self.spriteGroups['logs'],self.spriteGroups['champions'],self.spriteGroups['poofEffect'],self.spriteGroups['EFFECTS'],self.spriteGroups['FIRE_Effect'], self.spriteGroups['monsters']]
        
        #TODO: Rework these so they are objects, not static.
        ChargingCircle.containers = self.spriteGroups['uis'],self.spriteGroups['updatedSprites']
        Enemy.containers = self.spriteGroups['monsters']
        DialogueBox.containers = self.spriteGroups['DB']
        StaticImage.containers = self.spriteGroups['uis']
        SkillList.containers = self.spriteGroups['uis'],self.spriteGroups['updatedSprites']
        TileImage.containers = self.spriteGroups['staticIMAGES']
        Arrow.containers = self.spriteGroups['uis']
        Avatar.contaienrs = self.spriteGroups['uis']
        BUIBox.containers = self.spriteGroups['uis']
        StatusBarContainer.containers = self.spriteGroups['healthBarsC']
        BattleFont.containers = self.spriteGroups['battleFont']
        
        SpecialEffect.containers = self.spriteGroups['EFFECTS']
        Player.containers = self.spriteGroups['players']
        Champion.containers = self.spriteGroups['champions']
    
        AnimatedSprite.containers = self.spriteGroups['logs'],self.spriteGroups['updatedSprites']
        #SampleFont.containers = self.spriteGroups['texts'],self.spriteGroups['updatedSprites']
        StatusBar.containers = self.spriteGroups['healthBars']
    
        HealthBarNameFont.containers = self.spriteGroups['updatedSprites']
        
        self.variables['staticImage'] = StaticImage()
        
    def checkForCombo(self,AbilityString, ComboList):
        c = []
        bo = False
        for combo in ComboList:
            if len(AbilityString) >= combo.triggerLen:
                dif = len(AbilityString) - combo.triggerLen
                if AbilityString[dif::] == combo.triggerSequence:
                    c = combo
                    bo = True
                    return combo, True    
        return c,bo 

    """
    Loads all images of the rift.
    """
    def initialize(self):
        # Load the sky
        sky = screenObjects.StaticObject('data','SKY_BG.png',(0,0))
        sky.paralaxValue = 0
               
        grndtileImg = screenObjects.load_image('data','Grounds/SR_GRND.gif')
        grndtile = screenObjects.InfiniteTile(grndtileImg, (0,self.SCREENRECT.bottom - grndtileImg.get_height()), self.SCREENRECT.size)
    
        grassTileImg2 = screenObjects.load_image('data','Grounds/groundR.png')
        grassTile2 = screenObjects.StaticObject(grassTileImg2,(3500,self.SCREENRECT[3] - grndtileImg.get_height()))
        
        #TODO change repeating tile
        #grassTileImg3 = load_image('data','Grounds/SumRift_Ground_GrassMiddleLoop.png')
        #grassTile3 = TileImage(grassTileImg3,(self.SCREENRECT[2]-1,self.SCREENRECT[3] - grndtileImg.get_height()),-1,3530)
        
        treeTileImg = screenObjects.load_image('data','summoner rift tree [repeatable].png')
        treetile = screenObjects.RepeatTile(treeTileImg,(490,self.SCREENRECT[3] - treeTileImg.get_height() - 100),20)
        
        TTlineImg = screenObjects.load_image('data','TWisted Treeline Pixel2.png')
        TTline = screenObjects.RepeatTile(TTlineImg,(8322,0),10)

        TTtranImg = screenObjects.load_image('data','transitions.png')
        TTtran = screenObjects.StaticObject(TTtranImg,(6500,0))

        
        self.gameObjects = [sky,
                            grndtile
                            ]
    
    def loadImages(self):
        self.loadFromVN
        
        grndtileImg = load_image('data','Grounds/SR_GRND.gif',True)
        grndtile = TileImage(grndtileImg,(SCREENRECT[2]-1,SCREENRECT[3] - grndtileImg.get_height()),-1)
        #grndtile.isFirst = True
        
        grassTileImg2 = load_image('data','Grounds/groundR.png')
        grassTile2 = TileImage(grassTileImg2,(SCREENRECT[2]-1,SCREENRECT[3] - grndtileImg.get_height()),1,3500)
    
        grassTileImg3 = load_image('data','Grounds/SumRift_Ground_GrassMiddleLoop.png')
        grassTile3 = TileImage(grassTileImg3,(SCREENRECT[2]-1,SCREENRECT[3] - grndtileImg.get_height()),-1,3530)
    
    
        treeTilePath = 'summoner rift tree [repeatable].png'
        treeTileImg = load_image('data',treeTilePath,True)
        treetile = TileImage(treeTileImg,(SCREENRECT[2]-1,SCREENRECT[3] - treeTileImg.get_height() - 100),20)
        treetile.offSet = 470
    
        TTlineImg = load_image('data','TWisted Treeline Pixel2.png')
        TTline = TileImage(TTlineImg,(SCREENRECT[2]-1,0),10,8322)
    
        TTtranImg = load_image('data','transitions.png')
        TTtran = TileImage(TTtranImg,(SCREENRECT[2]-1,0),1,6500)
    
        skyLineImg = load_image('data','SKY_BG.png',True)
        skyLine = TileImage(skyLineImg,(SCREENRECT[2]-1,0),-1)
    
        grassTile4 = TileImage(grassTileImg3,(SCREENRECT[2]-1,SCREENRECT[3] - grndtileImg.get_height()),10,15000)
    
        treetile2 = TileImage(treeTileImg,(SCREENRECT[2]-1,SCREENRECT[3] - treeTileImg.get_height() - 100),16900)
        treetile.offSet = 470
    
        turret2Img = load_image('data','turret2.png',True)
        turret2 = TileImage(turret2Img,(SCREENRECT[2]-1,SCREENRECT[3]- 768),1,25000)
    
        #BARON RIVER
        riverLImg = load_image('data','River/tileL.png',True)
        riverMImg = load_image('data','River/tileM.png',True)
        riverRImg = load_image('data','River/tileR.png',True)
    
        riverL = TileImage(riverLImg,(SCREENRECT[2]-1,SCREENRECT[3] - grndtileImg.get_height()),1,10000)
        riverM = TileImage(riverMImg,(SCREENRECT[2]-1,SCREENRECT[3] - grndtileImg.get_height()),9,10100)
        riverR = TileImage(riverRImg,(SCREENRECT[2]-1,SCREENRECT[3] - grndtileImg.get_height()),1,11000)
    
        #CLOUDSSSS --> MAKE PATTERN
        cloudImg1 = load_image('data','Clouds/clouds1.png',True)
        cloudImg2 = load_image('data','Clouds/clouds2.png',True)
        cloudImg3 = load_image('data','Clouds/clouds3.png',True)
    
        clouds1 = TileImage(cloudImg1,(SCREENRECT[2]-1,SCREENRECT[3]- 730),1,500)
        clouds2 = TileImage(cloudImg2,(SCREENRECT[2]-1,SCREENRECT[3]- 690),1,1030)
        clouds3 = TileImage(cloudImg2,(SCREENRECT[2]-1,SCREENRECT[3]- 715),1,1435)
        clouds4 = TileImage(cloudImg1,(SCREENRECT[2]-1,SCREENRECT[3]- 743),1,2015)
        clouds5 = TileImage(cloudImg3,(SCREENRECT[2]-1,SCREENRECT[3]- 760),1,2418)
        clouds6 = TileImage(cloudImg1,(SCREENRECT[2]-1,SCREENRECT[3]- 771),1,3272)
        clouds7 = TileImage(cloudImg3,(SCREENRECT[2]-1,SCREENRECT[3]- 721),1,4699)
    
    
        ##################
        #### RED HOME ####
        ##################
    
        redPitPath = 'redPit/redpit.png'
        redPitImg = load_image('data','redPit/redpit.png',True)
        redPit = TileImage(redPitImg,(SCREENRECT[2]-1,SCREENRECT[3]- 700),1,5000)
    
    
        ###############
        #### GRASS ####
        ###############
    
        BushesFGPath = 'Bush/SumRift_Bushes_FG.png'
        BushesFGImg = load_image('data',BushesFGPath)
        BushesFG = TileImage(BushesFGImg,(SCREENRECT[2]-1,SCREENRECT[3]- 200),1,450)
        BushesFG.image.set_colorkey((255,255,255))
    
        BushesBGImg = load_image('data','Bush/SumRift_Bushes_BG.png')
        BushesBG = TileImage(BushesBGImg,(SCREENRECT[2]-1,SCREENRECT[3]- 370),1,450)
        BushesBG.image.set_colorkey((255,255,255))
    
        #BIG GRASS
        TcongBushesLImg = load_image('data','Bush/grass-tile-leftend.png',True)
        TcongBushesMImg = load_image('data','Bush/grass-tile-middle.png',True)
        TcongBushesRImg = load_image('data','Bush/grass-tile-rightend.png',True)
    
        #SMALL GRASS
        TcongBushesLImgs = load_image('data','Bush/grass-tile-leftendS.png',True)
        TcongBushesMImgs = load_image('data','Bush/grass-tile-middleS.png',True)
        TcongBushesRImgs = load_image('data','Bush/grass-tile-rightendS.png',True)
    
    
        #PURPLE BIG GRASS
        PurBushesLImg = load_image('data','BushPur/grass-tile-leftend.png',True)
        PurBushesMImg = load_image('data','BushPur/grass-tile-middle.png',True)
        PurBushesRImg = load_image('data','BushPur/grass-tile-rightend.png',True)
    
        #PURPLE SMALL GRASS
        PurBushesLImgs = load_image('data','BushPur/grass-tile-leftendS.png',True)
        PurBushesMImgs = load_image('data','BushPur/grass-tile-middleS.png',True)
        PurBushesRImgs = load_image('data','BushPur/grass-tile-rightendS.png',True)
    
    
    
        '''    USING THE GRASS    '''
    
        #BEFORE REDBUFF
        BushLred, BushMred, BushRred = buildTransitionTile([TcongBushesLImg,TcongBushesMImg,TcongBushesRImg],6,3000)
        BushL2red, BushM2red, BushR2red = buildTransitionTile([TcongBushesLImg,TcongBushesMImg,TcongBushesRImg],3,3200)
        BushLsred, BushMsred, BushRsred = buildTransitionTile([TcongBushesLImgs,TcongBushesMImgs,TcongBushesRImgs],8,2850)
    
        #IN THE JUNGLE
        BushLpur, BushMpur, BushRpur = buildTransitionTile([PurBushesLImg,PurBushesMImg,PurBushesRImg],5,14000)
        BushL2pur, BushM2pur, BushR2pur = buildTransitionTile([PurBushesLImg,PurBushesMImg,PurBushesRImg],2,14500)
        BushLspur, BushMspur, BushRspur = buildTransitionTile([PurBushesLImgs,PurBushesMImgs,PurBushesRImgs],12,13875)
    
        #BEFORE CART
        BushL, BushM, BushR = buildTransitionTile([PurBushesLImg,PurBushesMImg,PurBushesRImg],4,16755+1800)
        BushL2, BushM2, BushR2 = buildTransitionTile([PurBushesLImg,PurBushesMImg,PurBushesRImg],3,16855+1800)
        BushLs, BushMs, BushRs = buildTransitionTile([PurBushesLImgs,PurBushesMImgs,PurBushesRImgs],8,16825+1800)
    
        #AFTER CART
        BushLaf, BushMaf, BushRaf = buildTransitionTile([PurBushesLImg,PurBushesMImg,PurBushesRImg],3,19805+1800)
        BushL2af, BushM2af, BushR2af = buildTransitionTile([PurBushesLImg,PurBushesMImg,PurBushesRImg],2,20025+1800)
        BushLsaf, BushMsaf, BushRsaf = buildTransitionTile([PurBushesLImgs,PurBushesMImgs,PurBushesRImgs],12,19755+1800)
        BushLs2af, BushMs2af, BushRs2af = buildTransitionTile([PurBushesLImgs,PurBushesMImgs,PurBushesRImgs],6,20155+1800)
    
    
    
        ##############
        #### CART ####
        ##############
    
        cartImg = load_image('data','Shop/cart.png',True)
        cart = TileImage(cartImg,(SCREENRECT[2]-1,SCREENRECT[3]- 350),1,19335+1800)
    
        barImg1 = load_image('data','Shop/barblue.png',True)
        bar1 = TileImage(barImg1,(SCREENRECT[2]-1,SCREENRECT[3]- 200),1,19305+1800)
    
        barImg2 = load_image('data','Shop/barscroll.png',True)
        bar2 = TileImage(barImg2,(SCREENRECT[2]-1,SCREENRECT[3]- 200),1,19455+1800)
    
        barImg3 = load_image('data','Shop/barpur.png',True)
        bar3 = TileImage(barImg3,(SCREENRECT[2]-1,SCREENRECT[3]- 200),1,19505+1800)
    
        bushyImg = load_image('data','Bushy/bushy2.png',True)
        bushy1 = TileImage(bushyImg,(SCREENRECT[2]-1,SCREENRECT[3]- 265),1,19205+1800)
    
        bushyImg2 = load_image('data','Bushy/bushy1.png',True)
        bushy2 = TileImage(bushyImg2,(SCREENRECT[2]-1,SCREENRECT[3]- 300),1,19355+1800)
    
    
        #####################
        #### BEFORE CART ####
        #####################
    
        bushy3 = TileImage(bushyImg2,(SCREENRECT[2]-1,SCREENRECT[3]- 300),1,19005+1800)        #big
        bushy4 = TileImage(bushyImg,(SCREENRECT[2]-1,SCREENRECT[3]- 265),1,18830+1800)        #small
        bushy5 = TileImage(bushyImg,(SCREENRECT[2]-1,SCREENRECT[3]- 265),1,18655+1800)        #small
        bushy5b = TileImage(bushyImg2,(SCREENRECT[2]-1,SCREENRECT[3]- 300),1,18435+1800)        #big
        bushy5c = TileImage(bushyImg,(SCREENRECT[2]-1,SCREENRECT[3]- 265),1,18205+1800)        #small
        bushy6 = TileImage(bushyImg2,(SCREENRECT[2]-1,SCREENRECT[3]- 300),1,18075+1800)        #big
        bushy7 = TileImage(bushyImg,(SCREENRECT[2]-1,SCREENRECT[3]- 265),1,17860+1800)        #small
        bushy7b = TileImage(bushyImg,(SCREENRECT[2]-1,SCREENRECT[3]- 265),1,17550+1800)        #small
    
        barImg4 = load_image('data','Shop/bargreen.png',True)
        bar4 = TileImage(barImg4,(SCREENRECT[2]-1,SCREENRECT[3]- 200),1,18920+1800)
    
        bar4b = TileImage(barImg3,(SCREENRECT[2]-1,SCREENRECT[3]- 200),1,18970+1800)            #purple
        bar4c = TileImage(barImg1,(SCREENRECT[2]-1,SCREENRECT[3]- 200),1,18810+1800)            #blue
    
    
        ####################
        #### AFTER CART ####
        ####################
    
        bushy8 = TileImage(bushyImg2,(SCREENRECT[2]-1,SCREENRECT[3]- 300),1,19525+1800)        #big
        bushy9 = TileImage(bushyImg,(SCREENRECT[2]-1,SCREENRECT[3]- 265),1,22650+1800)        #small
        bushy10 = TileImage(bushyImg,(SCREENRECT[2]-1,SCREENRECT[3]- 265),1,19725+1800)        #small
        bushy11 = TileImage(bushyImg2,(SCREENRECT[2]-1,SCREENRECT[3]- 300),1,19885+1800)        #big
        bushy11b = TileImage(bushyImg2,(SCREENRECT[2]-1,SCREENRECT[3]- 300),1,20000+1800)        #big
        bushy12 = TileImage(bushyImg,(SCREENRECT[2]-1,SCREENRECT[3]- 265),1,20190+1800)        #small
        bushy12b = TileImage(bushyImg,(SCREENRECT[2]-1,SCREENRECT[3]- 265),1,20400+1800)        #small
        bushy13 = TileImage(bushyImg,(SCREENRECT[2]-1,SCREENRECT[3]- 265),1,20695+1800)        #small
        bar5 = TileImage(barImg4,(SCREENRECT[2]-1,SCREENRECT[3]- 200),1,19730+1800)            #green
    
    
    
        # The static images will be drawn in the order they are called in the for Loop
    
        self.staticImages = [skyLine,
                        clouds1,clouds2,clouds3,clouds4,clouds5,clouds6,clouds7,             #Clouds
                        treetile,grndtile,
                        TTline,TTtran,
                        grassTile4,grassTile3,
                        riverL,riverM,riverR,grassTile2,
                        BushLred,BushMred,BushRred,BushL2red,BushM2red,BushR2red,BushLsred,BushMsred,BushRsred, #RedPit grass
                        BushLpur,BushMpur,BushRpur,BushL2pur,BushM2pur,BushR2pur,BushLspur,BushMspur,BushRspur, #In the jungle grass
                        redPit,turret2,
                        BushL,BushM,BushR,BushL2,BushM2,BushR2,BushLs,BushMs,BushRs,                    #BG grass BEFORE
                        BushLaf,BushMaf,BushRaf,BushL2af,BushM2af,BushR2af,BushLsaf,BushMsaf,BushRsaf,BushLs2af,BushMs2af,BushRs2af,            #BG grass AFTER                    
                        bushy3,bushy7,bushy6,bushy4,bushy5,bushy5b,bushy5c,bushy7b,bar4b,bar4,bar4c,    #Before Boss 3
                        bushy13,bushy8,bushy10,bushy9,bushy11,bushy12,bushy11b,bushy12b,                #After Boss 3
                        bushy1,bushy2,bar1,bar3,cart,bar2,bar5                                             #Boss 3 - Shopkeeper
                        ]
        
        for x in range(0,SCREENRECT.width,treeTileImg.get_width()):
            self.background.blit(treeTileImg,(x,SCREENRECT[3] - treeTileImg.get_height() - 100))


        for x in range(0,SCREENRECT.width,grndtileImg.get_width()):
            self.background.blit(grndtileImg,(x,SCREENRECT[3]-grndtileImg.get_height()))
            
            
        if self.variables['maleRoute']:
            # Skills    
            plP = 'Ezreal'
            Player.walkImages = load_images(plP + '/Walk/_1.png',plP + '/Walk/_2.png',plP + '/Walk/_3.png',plP + '/Walk/_4.png',plP + '/Walk/_5.png',plP + '/Walk/_6.png')
            Player.distanceDelta = 6
            Player.idleImages = load_images(plP + '/idle/_1.png',plP + '/idle/_2.png',plP + '/idle/_3.png', plP + '/idle/_4.png')
            self.player = Player((400,SCREENRECT.height-195))
    
            champs = [Ezreal(),Ahri(),Soraka(),Rengar()]
            champsD = OrderedDict()
            for i in range(len(champs)):
                champsD[i] = champs[i] 
            self.champs = champsD
        
        else:
            # a list of combo skills that work as AOE abilities.
            plP = 'Leona'
            Player.walkImages = load_images(plP + '/Walk/Leona-walk_1.png',plP + '/Walk/Leona-walk_2.png',plP + '/Walk/Leona-walk_3.png',plP + '/Walk/Leona-walk_4.png',plP + '/Walk/Leona-walk_5.png',plP + '/Walk/Leona-walk_6.png')
            Player.distanceDelta = 6
            Player.idleImages = load_images(plP + '/idle/_1.png',plP + '/idle/_2.png',plP + '/idle/_3.png', plP + '/idle/_4.png')
            self.player = Player((400,SCREENRECT.height-195))
    
            champs = [Leona(),Jayce(),Rumble(),Viktor()]
            champsD = OrderedDict()
            for i in range(len(champs)):
                champsD[i] = champs[i] 
            self.champs = champsD
 
        """
        SampleFonts
        """
        #self.variables['sampleFont'] = SampleFont()
        #self.fonts['FPS_display'] = SampleFont()
        #self.fonts['minionPosDisplay'] = SampleFont()
        #self.fonts['channelDisplay'] = SampleFont()
        #self.fonts['playerWidth'] = SampleFont()
        #self.fonts['minionWidth'] = SampleFont()

        # Ui elements
        self.variables['skillList'] = SkillList()
        self.variables['dialoguebox'] = DialogueBox()

        
        self.spellSoundEffects[1] = pygame.mixer.Sound('data/EffectSFX/FireBall2.wav')
        self.spellSoundEffects[2] = pygame.mixer.Sound('data/EffectSFX/MagicArrow2.wav')
        self.spellSoundEffects[3] = pygame.mixer.Sound('data/EffectSFX/daggerSound2.wav')
        self.spellSoundEffects[4] = pygame.mixer.Sound('data/EffectSFX/daggerSound2.wav')

        self.variables['effectAnimations'] = [Animation('/sword_slash',[130],False,False),    #0
                                              Animation('/fire_effect',[120],False,True),   #1
                                              Animation('/Soraka/SFX',[120],False,True),   #2
                                              Animation('/ArrowAttack2',[120],False,True),   #3
                                              Animation('/smoke_puff_up',[250],False,True),  # 4
                                              Animation('/smoke_plume',[100],False,True), #5
                                              Animation('/Viktor_FX',[600,100,100,100,100,100,100,100,100,100,100,100],False,True)] #6
                                            #Animation('/Heart',[100],True,True) ]  #7
    
        SpecialEffect.EffectAnimations = self.variables['effectAnimations']
        
        #TODO Instanciate and store
        AnimatedSprite.animatedSprites = [[Animation('/Cinderling',[225],True,True), # Cinderling                                0
                                           Animation('/Minion',[225],True,True), # Melee Minion                                 1
                                           Animation('/Nexus',[100],True,True), # Shinyyyyy                                    2
                                           Animation('/Nashor', [225], True, True),    # Baron / 2nd Boss                        3
                                           Animation('/Doran', [250], True, True),    # Shopkeeper / Final Boss                    4
                                           Animation('/Redbuff', [225], True, True),    # Redbuff / 1st Boss                    5
                                           Animation('/Poro1', [175], True, True),    # Normal Poro                                 6
                                           Animation('/Poro2', [175], True, True),    # Mustache Poro                             7
                                           Animation('/Ranged', [200,150,150,150,150,150], True, True),    # Ranged Minion     8
                                           Animation('/WraithG', [250], True, True),    # Green Wraith                             9
                                           Animation('/WraithW', [200], True, True),    # White Wraith - INTENSE                10
                                           Animation('/Wolf', [175], True, True),    # Wolf                                         11
                                           Animation('/Crab', [225], True, True),    # Scuttler Crab                                12
                                           Animation('/Sentry', [225], True, True),    # Rock                                     13
                                           Animation('/pit/',[0],False,True),
                                           Animation('/BaronPit/',[100],True,True) # Baron Pit    
                                           ],
                                          [200,        #0 - Cinderling    
                                           201,        #1 - Melee minion
                                           318,        #2 - Nexus
                                           451,        #3 - Baron BOSS
                                           176,        #4 - Shopkeeper BOSS
                                           300,        #5 - Redbuff BOSS
                                           200,        #6 - Normal Poro
                                           200,        #7 - Mustache Poro
                                           201,        #8 - Ranged Minion 
                                           201,        #9 - Green Wraith
                                           201,           #10 - White Wraith (Big)
                                           200,           #11 - Wolf
                                           201,         #12 - Scuttler Crab
                                           200,        #13 - Rock
                                           200,        #14 
                                           293            #15 - Baron Pit
                                           ],
                                          ['Cinderling',
                                           'Minion',
                                           'Nexus',
                                           'Nashor',
                                           'Hacker',
                                           'Redbuff',
                                           'Poro',
                                           'Mr. Poro',
                                           'Ranged',
                                           'Wraith',
                                           'Wraith',
                                           'Wolf',
                                           'Scuttler',
                                           'Sentry',
                                           'Pit',
                                           'BaronPit'
                                           ],
                                          [True,#0 
                                           True,#1 
                                           False,#2 
                                           True,#3 
                                           True,#4 
                                           True,#5 
                                           True,#6 
                                           True,#7 
                                           True,#8 
                                           True,#9 
                                           True,#10 
                                           True,#11 
                                           True,#12 
                                           True, #13  
                                           False, #14
                                           False #15
                                           ]]
        
        self.variables['comboSkills'] = [ComboSkill(StatusEffect('ATK',False,6000, Type = 'Aura'),[0,4,2])]
        self.variables['anim']  = {1:Animation('/AttackMinion',[100],False,True)}
        
        nexus = AnimatedSprite(2,450,(0,0,0))    
        self.bgList = [nexus]
        self.minionListD = OrderedDict()
    
        self.engagements = [Engagement(450,0), Engagement(1500,1), Engagement(2300,2), Engagement(2800, 3), Engagement(3300, 4), Engagement(3800,5), Engagement(4300,6), Engagement(4750,7),
                            Engagement(5200,8), Engagement(5900,9), Engagement(6400,10), Engagement(7150,11), Engagement(7825,12), Engagement(8450,13), Engagement(9205,14),
                            Engagement(11135,15), Engagement(11895,16), Engagement(12435,17), Engagement(13115,18), Engagement(14135,19), Engagement(15005,19), Engagement(15835,20), 
                            Engagement(16775,21), Engagement(17535,22), Engagement(18935+1800,23)]
        
        j = 0
        for e in self.engagements:
            for i,mi in enumerate(e.minionList):
                j+=1
                self.minionListD[j] = mi
        
        self.clock = pygame.time.Clock()

        # Music
        #battleMusic = pygame.mixer.Sound('data/Music/Battle Stance - Zebulun Goodwin.ogg' )
        #battleMusic2 = pygame.mixer.Sound('data/house_lo.wav')
    
        pygame.mixer.music.load('data/Music/CaveSong.mp3')            #load music
        #pygame.mixer.music.load('data/Music/TTsong.mp3')        #load music
        self.sounds['victTheme'] = pygame.mixer.Sound('data/Music/VictoryTheme2.wav')
        # #renpy.audio.music.play('data/Music/Battle Stance - Zebulun Goodwin.ogg',0)
    
        # secondChannel = pygame.mixer.Channel(1)
        # thirdChannel = pygame.mixer.Channel(2)
        
        oldTime = 1
        # here all is all the sprites.
        changedDirection = False
        animationTime = .1
        i = 0
        self.variables['frameN'] = 0
        self.variables['frameCnt'] = 0
        self.variables['timeElapsed'] = 0
        self.variables['numofBM'] = 0
        self.variables['direction'] = 0
        self.variables['prev_direction'] = 0
        
        self.battleMode = False
        self.pauseGame = False
        
        #self.initialized = 2
        
    def addEvent(self,event):
        self.eventList.append(event)
    
    def getScreen(self):
        return self.screen
    
    def Pause(self,champs,SFX,Time):
        [c.updateC(Time) for c in champs.values()]

        for i,eff in enumerate(SFX):
            eff.updateE(Time)
            if eff.animation.stopDraw == True:
                eff.kill()
                eff.animation.reset()
                del SFX[i]
                #SFX = []

            if len(SFX) > 0 and len(self.spriteGroups['EFFECTS'])>0: 
                try:
                    self.spriteGroups['EFFECTS'].draw(self.screen)

                except AttributeError:
                    pass


    def update(self,screen = None):
        self.screen = renpy.display.pgrender.surface(self.SCREENRECT.size, True)
        # Step 0 - load the screen
        # Step 1 - load images (done in RenPy)
        # Step 2 - actually update things now
        if self.initialized == 0:
            loadScreen = load_image('data','Loading.png',True)
            self.screen.blit(loadScreen,(0,0))
            self.initialized = 1
            return self.screen
        elif self.initialized == 1:
            loadScreen = load_image('data','Loading.png',True)
            self.screen.blit(loadScreen,(0,0))
            self.initialized = 2
            self.loadImages()
            return self.screen
        else:
            dPressed = False
            self.variables['frameCnt'] = self.variables['frameCnt'] + 1
            if self.variables['frameCnt'] == 3:
                currentlyDrawing = True # needed to know when to start animations
    
            Time = self.clock.tick(85)
            self.variables['timeElapsed'] += Time 
    
    
            updateAnimation = False
            changedDirection = False
            TABpress = False
            vPress = False
            dPress = False
            
            for event in self.eventList:
                if event.type == QUIT or \
                (event.type == KEYDOWN and event.key == K_ESCAPE):
                    pygame.mixer.music.stop()
                    return self.variables['gifts'],self.variables['SceneKeys'][2]
                elif event.type == KEYUP and event.key == K_v:
                    vPress = True
                elif event.type == KEYUP and event.key == K_d:
                    dPress = True
                elif event.type == KEYUP and event.key == K_TAB:
                    TABpress = True
                elif event.type == KEYDOWN and event.key == K_z:
                    self.callScene = "TestTrigger"
                    print "testTrigger"
    
                [mx,my] = pygame.mouse.get_pos()
            
            self.eventList = []
            
            keystate = pygame.key.get_pressed()
    
    
            [g.clear(self.screen,self.background) for g in self.spriteGroups['SpriteGroups']]
    
            if self.battleMode == False:
                if keystate[K_d]:
                    for BGi in self.bgList:
                        BGi.checkForDraw(self.player.pos,self.background,Time,self.screen,True)
                    for AS in self.minionListD:
                        self.minionListD[AS].checkForDraw(self.player.pos,self.background,Time,self.screen,True)
            
                    self.background.scroll(-self.variables['direction'])
                    for imgi in self.staticImages:
                        imgi.updateE(self.background,self.player)
                
                    self.screen.blit(self.background,(0,0))
            
                else:
                    for BGi in self.bgList:
                        BGi.checkForDraw(self.player.pos,self.background,Time,self.screen,False)
            
                    for AS in self.minionListD:
                        self.minionListD[AS].checkForDraw(self.player.pos,self.background,Time,self.screen,False)
                
                self.variables['direction'] = keystate[K_d] - keystate[K_a]
            
                if self.variables['direction'] != self.variables['prev_direction']: changedDirection = True
                self.player.move(self.variables['direction'],changedDirection)
                if self.variables['direction'] != 0:
                    self.player.updateD(changedDirection,self.variables['direction'])
                
                
                else:
                    self.player.updateS(Time)
                self.spriteGroups['staticIMAGES'].draw(self.screen)
                self.spriteGroups['logs'].draw(self.screen)
                #self.fonts['FPS_display'].update(self.clock.get_fps(),"FPS: %0.2f",(0,0))
                #self.fonts['minionPosDisplay'].update(TTline.offSet,"PosP: %d",(400,0))
                #self.fonts['playerWidth'].update(TTline.dx,"MinionP: %0.2f",(400,200))
            
                for AS in self.minionListD:
                    if self.minionListD[AS].point <= 1000:
                        self.minionListD[AS].inRange = True 
                        if self.minionListD[AS].point <= 800:    
                            self.battleMode = True
                            
                self.variables['prev_direction'] = self.variables['direction']
            
                self.spriteGroups['players'].draw(self.screen)
                #self.spriteGroups['champions'].draw(self.screen)
            
                #self.fonts['minionWidth'].update(self.player.pos,"champsN: %s",(200,500))

            else:
                self.variables['numofBM'] += 1
                # Only initialize battleMode one time.
                if self.variables['numofBM'] == 1:
                    self.gtfoFlag = False
                    self.currentChamp = 0
                    self.comboSkillTriggered = False
                    self.abilityString = []
                    self.SFX = []
                    self.targetEnemy = 0
    
    
    
                    for c in self.champs.values():
                        c.GenerateUI()
    
                        c.battleUI.healthBar.update(c.healthPercent)
                        if c.name != 'EZREAL' or c.name != 'Leona':
                            self.SFX.append(SpecialEffect(4,c.pos,False,False,.5))
                        
    
                    #[c.GenerateUI() for c in self.spriteGroups['champions']]
                    #self.enemies = []
                    self.enemies = OrderedDict()
    
                    for i,AS in enumerate(self.minionListD):
                        if self.minionListD[AS].inRange == True:
                            try:
                                atk = self.variables['anim'][self.minionListD[AS].Id]
                            except KeyError:
                                atk = False
                            self.enemies[i] = (Enemy(i,self.minionListD[AS],atk,random.randint(4000,7000)))
                            #minionList.pop()
                            
                            #AS.point = 1000000000
                            #AS.inRange = False
                            self.minionListD[AS].kill()
                            
                    self.arrow = Arrow(self.enemies[0])        
                    # firstChannel.set_volume(.4)
                    
                    #logs.empty()
                    # if pygame.mixer and pygame.mixer.music:
                    #     #battleMusic = os_path_join('data','/Music/Battle Stance - Zebulun Goodwin2.wav')
                    #     battleMusic = 'data/house_lo.wav'
                    #     pygame.mixer.music.load(battleMusic)
                    #     pygame.mixer.music.set_volume(.7)
    
                    # build a list that represents the set of all monster IDs
                    # [g.clear(self.screen,background) for g in SpriteGroups]
    
                    moveList = []
    
    
                if self.pauseGame == False: 
                    for c in self.champs:
                        try: 
                            self.champs[c].updateTime(Time)
                            if self.champs[c].isAlive == False:
                                self.SFX.append(SpecialEffect(5,copy(self.champs[c].pos),False,False,ScaleImage = 1.2))
                                self.champs[c].death()
                                del self.champs[c]
                        except KeyError:
                            gameOver()
                                
                    for i in self.enemies:
                        self.enemies[i].updateTime(Time)
                        if self.enemies[i].isAlive == False:
                            monsterId = self.enemies[i].Id
                            self.SFX.append(SpecialEffect(5,copy(self.enemies[i].pos),False,False,ScaleImage = .5))
                            self.enemies[i].death()
                            del self.enemies[i]
                            try:
                                self.enemies[self.enemies.keys()[0]]
                                if self.targetEnemy == monsterId:
                                    self.targetEnemy = self.enemies[random.sample(self.enemies,len(self.enemies))[0]].Id
                                    #self.arrow.update(self.enemies[self.targetEnemy])
                                    self.arrow.newTarget(self.enemies[self.targetEnemy])
                                    break
                    
                
                            except IndexError:
                                # GTFO out of this else loop ASAP (I know this is terrible programming)
                                # return (JK this isn't a function)
                                self.gtfoFlag = True
    
                        if self.gtfoFlag == False:
    
                            if self.enemies[i].canUseSkill == True:
    
                                targetID = self.enemies[i].attack(self.champs.keys())
                                self.enemies[i].useSkill(self.champs[targetID])
                                specialeffect = SpecialEffect(self.enemies[i].skill.Id,self.champs[targetID].pos,False,True)
    
                                #specialeffect.animation.reset()
                                self.SFX.append(specialeffect)
                                if self.enemies[i].hasAttackAnimation == True: 
                                    self.enemies[i].animationID = 1
    
                        else:
                            pass
    
    
                    if self.gtfoFlag == True:
                        pauseGame = True
                        numPause = True
                        # call escape code
                            #chargingCircle.reset = True
                        #self.spriteGroups['uis'].empty()
                        #self.spriteGroups['EFFECTS'].empty()
                        self.spriteGroups['monsters'].empty()
                        self.arrow.kill()
                        self.spriteGroups['battleFont'].empty()
    
                        for c in self.champs.values():
                            #c.animations[c.animationID][c.AuraID].reset()
                            #c.animations[c.animationID][c.AuraID].stopDraw = True
                            #c.stopDraw = True
                            #c.resetTimeDelta()
                            c.battleUI.healthBar.kill()
                            c.chargingCircle.kill()
    
    
                    
    
                        for ASk in self.minionListD:
                            if self.minionListD[ASk].inRange == True:
                                #self.minionListD[ASk].kill()
                                del self.minionListD[ASk]
                    
                    
                    else:
                        
                        if TABpress == True:
                            keyIndex = self.enemies.keys().index(self.targetEnemy) + 1
                            if keyIndex % len(self.enemies) == 0:
                                self.targetEnemy = self.enemies.keys()[0]
                            else:
                                self.targetEnemy = self.enemies.keys()[keyIndex]
    
                            self.arrow.newTarget(self.enemies[self.targetEnemy])
                            #arrow.update(self.enemies[self.targetEnemy])
    
                        # if keystate[K_x]:
                        #     ahri.statusBar.update(0.2)
    
                        if keystate[K_d]: pass
                            #firstChannel.play(battleMusic2)
                        
                        for i in self.champs.keys():
                            #key_ = 'K_' + str(i)
                            if keystate[i+49] and self.champs[i].canUseSkill == True: self.currentChamp = i
    
                        ''' Possible refactor of keystroke code '''
    
                        # if self.champs[self.currentChamp].canUseSkill:
                        #     if keystate[K_q]:
    
                    
    
                        if keystate[K_q]:
                            if self.champs[self.currentChamp].canUseSkill == True:
                                self.champs[self.currentChamp].currentSkill = 0
                                self.champs[self.currentChamp].useSkill(self.enemies[self.targetEnemy],self.abilityString)
    
                                specialeffect = SpecialEffect(self.champs[self.currentChamp].skills[0],self.enemies[self.targetEnemy].pos,False,True)
                                self.enemies[self.targetEnemy].specialEffect = specialeffect
                                #specialeffect.animation.reset()
                                try: 
                                    self.spellSoundEffects[self.champs[self.currentChamp].skills[0].sId].play()
                                    #spellSoundEffects[self.champs[self.currentChamp].skills[0].Id].set_volume(.3)
                                except KeyError:
                                    pass
                                self.SFX.append(specialeffect)
                    
                        if keystate[K_w]:
                            if self.champs[self.currentChamp].canUseSkill == True:
                                self.champs[self.currentChamp].currentSkill = 1
                                
                                self.champs[self.currentChamp].useSkill(self.enemies[self.targetEnemy],self.abilityString)
    
                                specialeffect = SpecialEffect(self.champs[self.currentChamp].skills[1],self.enemies[self.targetEnemy].pos,False,True)
                                self.enemies[self.targetEnemy].specialEffect = specialeffect
                                #specialeffect.animation.reset()
                                try: 
                                    self.spellSoundEffects[self.champs[self.currentChamp].skills[0].sId].play()
                                    #spellSoundEffects[self.champs[self.currentChamp].skills[0].Id].set_volume(.3)
                                except KeyError:
                                    pass
                                self.SFX.append(specialeffect)
    
    
                        Combo,self.comboSkillTriggered = self.checkForCombo(self.abilityString,self.variables['comboSkills'])
                        
                        # if keystate[K_5] == True:
                        #     self.comboSkillTriggered = True
                        ''' Check if comboskill was triggered '''
                        if self.comboSkillTriggered: 
    
    
                            #for i in self.enemies:
                                #self.enemies[i].updateHealth(Combo)
                                #self.comboSkillTriggered = False
                            ri = random.randint(0,1)
                            for c in self.champs.values():
                                #c.updateHealth(Combo)
                                self.comboSkillTriggered = False
                            
                                c.AuraID = ri
    
    
                            self.abilityString = []
                            self.champs[0].triggerEffects()
    
    
                        [i.checkForDraw(self.player.pos,self.background,Time,self.screen,False) for i in self.bgList]
    
                        # Clear all rectangles
                        self.spriteGroups['players'].clear(self.screen,self.background)
                        self.spriteGroups['logs'].draw(self.screen)    
                        self.arrow.update()
                        
                        [c.updateC(Time) for c in self.champs.values()]
                        self.spriteGroups['champions'].draw(self.screen)
                    
    
                        #self.fonts['FPS_display'].update(self.clock.get_fps(),"FPS: %0.2f",(0,0))
                        
    
    
                        try: 
                            self.abilityString[0]
                            #self.variables['sampleFont'].update(self.abilityString[-1],"Player Pos: %s",(300,300) )
                        except IndexError: pass
    
                        
                        
                        self.spriteGroups['texts'].draw(self.screen)
                        self.spriteGroups['staticIMAGES'].draw(self.screen)
                        self.spriteGroups['uis'].draw(self.screen)
                        self.spriteGroups['healthBarsC'].draw(self.screen)
                        self.spriteGroups['healthBars'].draw(self.screen)
                        #self.spriteGroups['battleFont'].draw(self.screen)
                        for i in self.enemies:
                            self.enemies[i].updateM(Time)
    
                        self.spriteGroups['monsters'].draw(self.screen)
                        
            
                        for i,eff in enumerate(self.SFX):
                            eff.updateE(Time)
                            if eff.animation.stopDraw == True:
                                eff.kill()
                                eff.animation.reset()
                                del self.SFX[i]
                                #self.SFX = []
    
                        if len(self.SFX) > 0 and len(self.spriteGroups['EFFECTS'])>0: 
                            try:
                                self.spriteGroups['EFFECTS'].draw(self.screen)
    
                            except AttributeError:
                                pass
    
    
                        
                else:
                    if numPause:
                        #pygame.mixer.music.load('data/Music/VictoryTheme.wav')    
                        pygame.mixer.music.stop()
                        #pygame.mixer.music.play(1)
                        pygame.mixer.Channel(0).play(self.sounds['victTheme'])
                        #victTheme.play(1)
                        #victTheme.play()
                        numPause = False
                    #firstChannel.play(victTheme)
                    self.Pause(self.champs,self.SFX,Time)
                    [i.checkForDraw(self.player.pos,self.background,Time,self.screen,False) for i in self.bgList]
    
                    self.spriteGroups['logs'].draw(self.screen)
                    self.spriteGroups['champions'].draw(self.screen)
                    
                    if keystate[K_RETURN]: 
                        for c in self.champs.values():
                            c.animations[c.animationID][c.AuraID].reset()
                            c.animations[c.animationID][c.AuraID].stopDraw = True
                        self.battleMode = False
                        self.spriteGroups['EFFECTS'].empty()
                        pauseGame = False
                        firstWhile = True
                        self.variables['numofBM'] = 0
    
                lf = []
    
            if self.variables['frameCnt'] >= 4: 
                self.variables['frameCnt'] = 0
        
        return self.screen    


######################
# ADDITIONAL CLASSES #
######################

class Engagement:
    clusterMins = [[6,6],         #1
    [7,1,6],                     #2
    [1,1],                         #3
    [6,8,13],                     #4
    [13,0],                     #5
    [0,1,13],                     #6
    [0,0],                         #7 Red Buff
    [5],                         #8
    [8,11,13],                     #9
    [9,7], #                    10
    [12,1], #                    11
    [13,6,9], #                    12
    [10,12], #                    13
    [13,10,13], #                14
    [3], #                        15 Nashor
    [6,7,6], #                    16
    [9,10,9], #                    17
    [0,12,8], #                    18
    [1,11], #                    19
    [11,10], #                    20
    [7,0,11], #                    21
    [12,12,12], #                22
    [9,1,8], #                    23
    [4]] #                        24

    clusterPos =[[400,480],     #1
    [400,500,600],                 #2
    [400,530],                     #3
    [400,475,560],                 #4
    [400,460],                     #5
    [400,530,600],                 #6
    [400,550],                     #7
    [400],                         #8
    [400,530,600],                 #9
    [400,510],                     #10
    [400,550],                     #11
    [400,450,510],                 #12
    [400,530],                     #13
    [400,495,580],                 #14
    [400],                         #15 Nashor
    [400,470,500],                 #16
    [400,480,560],                 #17
    [400,510,580],                 #18
    [400,550],                     #19
    [400,510],                     #20
    [400,460,600],                 #21
    [400,480,560],                 #22
    [400,515,600],                 #23
    [400]                         #24
    ]

    ''' A cluster of minions for an engagement '''
    def __init__(self,Pos,ID):
        self.posX = Pos 
        self.minionList = []
        for i,p in zip(self.clusterMins[ID],self.clusterPos[ID]):
            self.minionList.append(AnimatedSprite(i,p + self.posX))

class StaticImage(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self,self.containers)
        self.image = renpy.display.pgrender.surface((40,40),True)
        self.color = pygame.color.Color(124,21,30)
        self.image.fill(self.color)
        self.image.set_colorkey(self.color)
        #self.newImage = alphaImage.set_alpha(30)
        #self.image.convert_alpha()
        self.rect = self.image.get_rect(center = (300,200))

    def update(self):
    #    self.rect = self.image.get_rect(center = (100,200))
        self.rect = self.rect.clamp(SCREENRECT)

