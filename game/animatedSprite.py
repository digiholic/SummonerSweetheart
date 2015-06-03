import renpygame as pygame
import renpy.display

if not pygame.image.get_extended():
    raise SystemExit,"sorry, extended image module required"

SCREENRECT     = pygame.Rect(0, 0, 1024, 768)

class AnimatedSprite(pygame.sprite.Sprite):
    defaultImage = renpy.display.pgrender.surface((1,1),True)
    animatedSprites = []
    numberFrames = 5
    
    def __init__(self,ID,PosX,ColorKey = False):
        pygame.sprite.Sprite.__init__(self, self.containers)
        #super(Player,self).__init__(self, self.containers)
        self.Id = ID
        self.animation = self.animatedSprites[0][self.Id]
        self.images = self.animation.images
        self.image = self.defaultImage
        self.numFrames = len(self.images)
        #self.animationDelta = AD
        self.inRange = False
        self.colorKey = ColorKey
        self.name = self.animatedSprites[2][self.Id]
        
        self.timeList = self.animation.timeList

        self.img = self.images[0]
 
        self.width = self.img.get_width()
        
        if len(self.timeList) == 1:
            self.constantTime = True
        else:
            self.constantTime = False
                    
        #self.image = self.newImage
        #self.image = self.images[0]
        self.facing = -1
        self.distance = 0
        self.timeElapsed = 0
        self.ptr = 0
        self.posX = PosX
        #201
        self.yOffset = SCREENRECT.height - self.animatedSprites[1][self.Id]
        self.offset = 0
        self.srcArea = pygame.Rect((0,0),(0,0))
        
        # checks to see if the sprite is active, beginning, or ending
        self.Active = False
        self.Begin = False
        self.End = False
        #self.origin = [SCREENRECT.width-100,SCREENRECT.height - 300]
        #self.rect = self.image.get_rect(center = self.origin)
        self.rect = self.image.get_rect()
        self.point = SCREENRECT.width + self.img.get_width()
        self.cnt = 0

    def checkForDraw(self,x,background,timeE,screen,shouldOffset):
        if self.Active == False:
        #if self.posX - self.image.get_width() == x: 
            if self.posX == x:
                # Triggered when Player position is in range of sprite
                self.image = self.images[0]
                self.Active = True # Active until player =
                self.drawSprite(background,timeE,screen,shouldOffset)
            else:
                pass
        # If sprite is Active
        else: self.drawSprite(background,timeE,screen,shouldOffset)
        
    def drawSprite(self,background,timeE,screen,shouldOffset):
        if shouldOffset == True:
            self.point -= 1
            self.updateTimeElapsed(timeE)

            self.offset += 1
            self.rect = self.image.get_rect(center = (self.point,self.yOffset))
            #self.rect.move(self.point,200)
            #self.image.get_rect()

            self.updateS()
            #self.image = self.newImage.convert_alpha(self.newImage)
            #self.image.blit(self.img,(0,0))
            #self.image.set_colorkey((0,0,0))
            self.image = self.img
        
    def updateTimeElapsed(self,TimeE):
        self.timeElapsed += TimeE


    def updateS(self):
        if self.constantTime == True:
            timeDelta = self.timeList[0]
        else:
            timeDelta = self.timeList[self.ptr]

        if self.timeElapsed >= timeDelta:
            self.timeElapsed = 0
            self.ptr += 1
        if self.ptr % self.numFrames == 0:
            self.ptr = 0
            self.img = self.images[self.ptr]
        # if self.timeElapsed >= self.animationDelta:
            #  self.timeElapsed = 0
            #  self.ptr += 1
        #  if self.ptr % self.numFrames == 0:
            #   self.ptr = 0
            #  self.img = self.images[self.ptr]

        #  if self.colorKey == False:
            #   pass
        #  else:
            #   self.img.set_colorkey((0,0,0))

# Needs to draw with offset