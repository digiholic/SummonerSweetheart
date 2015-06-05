import renpygame as pygame
import renpy.display
import renpy.config
import os

def load_image(path,fname):
    fp = path + '/' + fname
    #sprite = pygame.image.load(fp)
    sprite = renpy.display.pgrender.load_image(renpy.loader.load(fp), fp)
    return sprite

"""
A ScreenObject is anything drawn on the screen.
If it's animated, it'll have an update method that is called every frame.
Otherwise, it's just there to be blitted on the screen.

If defining a static ScreenObject, pass in an image for it to render
and a position to render to.
"""
class ScreenObject(pygame.sprite.Sprite):
    def __init__(self,paralaxValue = 1.0):
        pygame.sprite.Sprite.__init__(self)
        self.image = renpy.display.pgrender.Surface((0,0),True)
        self.rect = self.image.get_rect()
        self.paralaxValue = paralaxValue
        
    def update(self):
        pass
    
    def draw(self,screen,offset):
        w, h = (self.rect.width, self.rect.height)
        screen.blit(self.image,pygame.Rect(offset,(w,h)))
    
    def inScreen(self,screen):
        return self.rect.colliderect(screen) 
    
    """
    Update the location of the sprite.
    """
    def changeLocation(self,newPos):
        self.pos = newPos
        self.rect.topleft = newPos
        
    """
    Given a dictionary that maps one color to another, this function
    will apply all of those recolors across the image.
    """
    def recolorFromMap(self,image,colorDict):
        for fromColor,toColor in colorDict.iteritems():
            self.recolor(image, list(fromColor), list(toColor))

    def stageToScreen(self,camera_rect):
        x = self.rect.x - (camera_rect.x * self.paralaxValue)
        y = self.rect.y - (camera_rect.y * self.paralaxValue)
        return (x,y)
    
class StaticObject(ScreenObject):
    def __init__(self,img,pos,paralaxValue = 1.0):
        ScreenObject.__init__(self,paralaxValue)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
       
"""
Draws a long tile
imgList = [Left,Middle,Right] surface objects
startPos = the XY Position of the topleft of the bush
number = The number of tiles to place. Must be at least 2
"""
class LongTile(ScreenObject):
    def __init__(self,imgList,startPos,number,paralaxValue = 1.0):
        ScreenObject.__init__(self,paralaxValue)
        width, height = (imgList[0].get_width(),imgList[0].get_height())
        self.image = renpy.display.pgrender.Surface((width*number,height),True)
        for i in range(0,number):
            if i == 0:
                self.image.blit(imgList[0],(width*i,0))
            elif i == number - 1:
                self.image.blit(imgList[2],(width*i,0))
            else:
                self.image.blit(imgList[1],(width*i,0))
        self.rect = pygame.Rect(startPos,(width*number,height))

class RepeatTile(ScreenObject):
    def __init__(self,img,startPos,number,paralaxValue = 1.0):
        ScreenObject.__init__(self,paralaxValue)
        width, height = (img.get_width(),img.get_height())
        
        self.image = renpy.display.pgrender.Surface((width*number,height),True)
        for i in range(0,number):
            blitImage = StaticObject(img,(0,0))
            blitImage.draw(self.image, (width*i,0))
        self.rect = pygame.Rect(startPos,(width*number,height))
        
class InfiniteTile(ScreenObject):
    def __init__(self,img,startPos,screenSize,paralaxValue = 1.0):
        ScreenObject.__init__(self,paralaxValue)
        self.width, self.height = (img.get_width(), img.get_height())
        number = (screenSize[0] / self.width) + 3 # Plus 3 because 1 to make it the proper width (zero indexing fix), and one extra on each side.
        
        self.image = renpy.display.pgrender.Surface((self.width*number,self.height),True)
        for i in range(0,number):
            self.image.blit(img.convert_alpha(),(self.width*i,0))
        self.rect = pygame.Rect((startPos[0] - self.width,startPos[1]),(self.width*number,self.height))
    
    def stageToScreen(self,camera_rect):
        if self.rect.left - camera_rect.left >= 0:
            self.rect.x -= self.width
        if camera_rect.right - self.rect.right >= 0:
            self.rect.x += self.width
        
        x = self.rect.x - (camera_rect.x * self.paralaxValue)
        y = self.rect.y - (camera_rect.y * self.paralaxValue)
        
        return (x,y)
        
"""
An Animated Object takes a directory,
loads all of the images from that directory,
then animates them in order.

position - topleft of the sprite on screen
animLength - how many images are in the animation
Directory - where to gather the files from
prefix - what the file names start with, defaults to none (will take all images)
loop - whether or not the animation loops
"""
class AnimatedObject(ScreenObject):
    def __init__(self,position,animLength,directory,order=None,delay=1,prefix="",loop=True,paralaxValue = 1.0):
        ScreenObject.__init__(self,paralaxValue)
        self.pos = position
        
        self.frame = 0
        self.lastFrame = animLength - 1
        self.loop = loop
        self.delay = delay
        self.currentDelay = 0
        
        self.images = self.buildImageDict(directory,prefix)
        self.orderedImages = []
        if order:
            for o in order:
                self.orderedImages.append(self.images[o])
        else:
            self.orderedImages = self.images.values() # This will probably need to be fixed in the individual animation
        self.image = self.orderedImages[0]
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos
        
    """
    This will create the image dictionary.
    It will crawl the given directory, and everything that starts with prefix
    and is a supported file type will be added.
    The key in the dict is the remaining file name after the prefix and following underscore are
    stripped off. For example, the files nexus_pixel_animated_1.png and nexus_pixel_animated_2.png
    with the given prefix of nexus_pixel_animated will return a dict where images['1'] points to
    the first surface, and images['2'] points to the next.
    
    It's important to note that these names do not need to be numbers, so you can have, for example,
    ahri_idle1, ahri_idle2, ahri_idle3, ahri_attack1, ahri_attack2, ahri_attack3 in the same directory,
    and they'd be called with the prefix ahri, to get attack1 and idle1 stored as different entries.
    """
    def buildImageDict(self,directory,prefix):
        imageDict = {}
        supportedFileTypes = [".jpg",".png",".gif",".bmp",".pcx",".tga",".tif",".lbm",".pbm",".xpm"]
        
        for f in os.listdir(os.path.join(renpy.config.gamedir,directory)):
            fname, ext = os.path.splitext(f)
            if fname.startswith(prefix) and (ext in supportedFileTypes):
                spriteName = fname[len(prefix):]
                fp = directory+'/'+f
                sprite = renpy.display.pgrender.load_image(renpy.loader.load(fp), fp)
                imageDict[spriteName] = sprite
        return imageDict

    """
    Change the displaying image. If a number is given, it'll
    get that number in the orderedImages. If a string is given,
    it'll get the image named that string.
    """
    def changeImage(self,imageNameOrNumber):
        if isinstance(imageNameOrNumber,int):
            self.image = self.orderedImages[imageNameOrNumber]
        else:
            self.image = self.images[imageNameOrNumber]
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos
       
    """
    Animate the object.
    """     
    def update(self):
        if self.currentDelay == self.delay:
            self.currentDelay = 0
            self.frame += 1
            if self.frame <= self.lastFrame:
                self.changeImage(self.frame)
            elif self.frame > self.lastFrame:
                if self.loop:
                    self.frame = 0
                    self.changeImage(self.frame)
                else:
                    self.frame = self.lastFrame
                    # If we're not changing, no point in calling the function
        else:
            self.currentDelay += 1

class MultiAnimationObject(ScreenObject):
    def __init__(self,directory,prefix,startingImage,offset,colorMap = {},paralaxValue = 0.0):
        ScreenObject.__init__(self, paralaxValue)
        self.colorMap = colorMap
        self.imageLibrary = self.buildImageLibrary(ImageLibrary(directory,prefix), offset)
        
        self.startingImage = startingImage
         
        self.flip = "right"
        self.currentSheet = startingImage
        self.index = 0
        
        self.image = self.imageLibrary[self.flip][self.startingImage][self.index]
        
        self.rect = self.image.get_rect()
        self.boundingRect = self.getBoundingBox()
        
    def flipX(self):
        if self.flip == "right": self.flip = "left"
        else: self.flip = "right"
    
    def getBoundingBox(self):
        boundingRect = self.image.get_bounding_rect()
        boundingRect.top += self.rect.top
        boundingRect.left += self.rect.left
        return boundingRect
    
    def updatePosition(self,rect):
        self.rect = rect
        self.boundingRect = self.getBoundingBox()
                
    def changeImage(self,newImage,subImage = 0):
        self.currentSheet = newImage
        self.index = subImage
        self.get_image()
        
    def changeSubImage(self,index):
        self.index = index % len(self.imageLibrary[self.flip][self.currentSheet])
        self.get_image()
    
    def rotate(self,angle = 0):
        self.angle = angle
    
    def get_image(self):
        try:
            self.image = self.imageLibrary[self.flip][self.currentSheet][self.index]
        except:
            print "Error loading sprite ", self.currentSheet, " Loading default"
            self.image = self.imageLibrary[self.flip][self.startingImage][0]
        
        self.rect = self.image.get_rect(center=self.rect.center)
        self.boundingRect = self.getBoundingBox()
        return self.image
    
    def get_length(self):
        return len(self.imageLibrary[self.flip][self.currentSheet])
    
    def draw(self,screen,offset):
        self.get_image()
        ScreenObject.draw(self,screen,offset)
    
    def buildImageLibrary(self,lib,offset):
        library = {}
        flippedLibrary = {}
        for key,value in lib.imageDict.iteritems():
            imageList = self.buildSubimageList(value,offset)
            library[key] = imageList
            flipList = []
            for image in imageList:
                img = image.copy()
                img = pygame.transform.flip(img,True,False)
                flipList.append(img)
            flippedLibrary[key] = flipList

        return {"right": library, "left": flippedLibrary}
        
    def buildSubimageList(self,sheet,offset):
        index = 0
        imageList = []
        while index < sheet.get_width() / offset:
            sheet.set_clip(pygame.Rect(index * offset, 0, offset,sheet.get_height()))
            image = sheet.subsurface(sheet.get_clip())
            for fromColor,toColor in self.colorMap.iteritems():
                self.recolor(image, list(fromColor), list(toColor))
            imageList.append(image)
            index += 1
        return imageList     

class ImageLibrary():
    def __init__(self,directory,prefix=""):
        self.directory = os.path.join(os.path.dirname(__file__),directory)
        self.imageDict = {}
        supportedFileTypes = [".jpg",".png",".gif",".bmp",".pcx",".tga",".tif",".lbm",".pbm",".xpm"]
             
        for f in os.listdir(os.path.join(renpy.config.gamedir,self.directory)):
            fname, ext = os.path.splitext(f)
            if fname.startswith(prefix) and supportedFileTypes.count(ext):
                spriteName = fname[len(prefix):]
                fp = os.path.join(self.directory,f)
                sprite = renpy.display.pgrender.load_image(renpy.loader.load(fp),fp)
                self.imageDict[spriteName] = sprite
                
class BGChunk(ScreenObject):
    def __init__(self,startX,size):
        ScreenObject.__init__(self)
        self.rect = pygame.Rect((0,startX),size)    
        