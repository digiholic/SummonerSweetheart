######################################### IMAGE DECLARATIONS
## Since config.automatic_images is on, image declarations are handled
## automatically. The defined separators are ' ', '/', and '_'.
## Examples: bg/black.png -> bg black
##           eileen_happy.png -> eileen happy
##           lucy/mad.png -> lucy mad

######################################### CHARACTER DECLARATION
$ narrator = Character(None)
define mc1 = Character('[name]', image = "mc1")
define mc2 = Character('[name]', image = "mc2")
define ez = Character('Ezreal', image = "ez")
define le = Character('Leona', image = "leo")

define am = Character('Ami', voice_tag="ahri")
define ah = Character('Ahri', voice_tag="ahri")

define sh = Character('Sharon', voice_tag = "raka")
define so = Character('Soraka',  voice_tag = "raka")

define gw = Character('Gwen', voice_tag = "rango")
define re = Character('Rengar', voice_tag = "rango")

define vi = Character('Viktor', voice_tag = "vik")
define cy = Character('Cyrus', voice_tag = "vik")

define da = Character('Daniel', voice_tag = "rum")
define ru = Character('Rumble', voice_tag = "rum")

define je = Character('Jason', voice_tag = "jayce") # yes, the tag is still je.
define ja = Character('Jayce', voice_tag = "jayce")

define ch = Character('Ms. Laurent')
define a = Character('Annie')
define mv = Character('Mysterious Voice')
define t = Character('Teacher')
define ca = Character('Calibration System')
define everyone = Character('Everyone')
define un = Character('???')
define s = Character('Shen')
define z = Character('Dr. Zen')
define te = Character('Teemo')
define h = Character('Hacker')
define na = Character('Baron Nashor')

init python:
  import pygame
  pygame.font.init()
  import renpygame
  import summonersRift
  
  dungeon = summonersRift.Dungeon()
  
  class DungeonRun(renpy.Displayable):
    def __init__(self, **kwargs):
      super(DungeonRun, self).__init__(**kwargs)
      self.width = 1024
      self.height = 768
      
    def render(self, width, height, st, at):
      global dungeon
      if dungeon is None:
        render = renpy.Render(self.width,self.height)
      else:
        retScreen = dungeon.update()
        render = renpy.Render(self.width,self.height)
        render.blit(retScreen, (0, 0))
        if dungeon.callScene != "":
          callScene = dungeon.callScene
          dungeon.callScene = ""
          renpy.call(callScene)
        if dungeon.finished:
          dungeon.finished = False
          renpy.end_interaction("Finished")
        else:
          renpy.redraw(self,0.03)
      return render
      
    def event(self, ev, x, y, st):
      global dungeon
      if dungeon:
        dungeon.addEvent(ev)    
      
  class DungeonScene(renpy.Displayable):
    def __init__(self, **kwargs):
      super(DungeonScene, self).__init__(**kwargs)
      self.width = 1024
      self.height = 768
      
    def render(self, width, height, st, at):
      global dungeon
      render = renpy.Render(self.width,self.height)
  
      if dungeon:
        retScreen = dungeon.getScreen()
        render.blit(retScreen, (0,0))
      
      renpy.redraw(self,0.03)
      return render
      
    def event(self,ev, x, y, st):
      return
      
      
  def set_mode():
    fsflag = 0
    if _preferences.fullscreen:
      fsflag = FULLSCREEN
    screen = renpygame.display.set_mode((1024,768), fsflag, 32)
    return screen

  def mc(what, **kwargs):
    if route == "Ezreal":
      mc1(what, **kwargs)
    elif route == "Leona":
      mc2(what, **kwargs)            

  def vrmc(what, **kwargs):
    if route == "Ezreal":
      ez(what, **kwargs)
    elif route == "Leona":
      mc2(what, **kwargs)
      
######################################### GAME SCRIPT
## The splash screen.
label splashscreen:
    python:
        if not persistent.set_volumes:
            persistent.set_volumes = True
            _preferences.volumes['music'] *= .60
    
    scene bg black
    $ renpy.pause(0.5, hard=True)
    
    show cg notice with dissolve
    $ renpy.pause(1.5, hard=True)
    
    scene bg black with dissolve
    $ renpy.pause(0.5, hard=True)
    return
    
## The beginning of the game, where player chooses their route and name.
## Temp writing.
label start:
    $ day = 1
    $ period = 0
    $ preboss_flag = False
    $ afterconfession_flag = False
    $ afterdungeon_flag = False
    
    call screen char_select
    $ route = _return
    # add confirmation prompt?
    $ renpy.block_rollback()
    if route == "Ezreal":
        $ ahri_rp = 0
        $ raka_rp = 0
        $ rango_rp = 0
        $ ahri_combo = False
        $ raka_combo = False
        $ rango_combo = False
        $ ahri_scene = 0
        $ raka_scene = 0
        $ rango_scene = 0
        $ have_charm = False
        $ have_clip = False
        $ have_bone = False
        $ raka3_flag = False
        $ ahri4_flag = False
        $ ahri5_flag = False
        $ ahri_badend = False
        $ raka_confessed = False
        
    elif route == "Leona":
        $ jayce_rp = 0
        $ rumble_rp = 0
        $ vik_rp = 0
        $ jayce_combo = False
        $ rumble_combo = False
        $ vik_combo = False
        $ jayce_scene = 0
        $ rumble_scene = 0
        $ vik_scene = 0
        $ have_hammer = False
        $ have_rubix = False
        $ have_sketch = False
        $ vik_confessed = False
    $ renpy.block_rollback()

label name_input:
    scene cg name select
    $ name = renpy.input("And what was my name, again...?")
    $ name = name.strip() # ensures string has no leading or trailing whitespace
    if name == "":
        if route == "Ezreal":
            $ name = "Eric"
        elif route == "Leona":
            $ name = "Elizabeth"
    "[name], right?"
    $ renpy.block_rollback()
    menu:
        "That's it.":
            pass
        "That can't be right...":
            jump name_input
    "Of course."
    if route == "Ezreal":
        $ tag = "mc1"
        $ raka3B_flag = False
    elif route == "Leona":
        $ tag = "mc2"
    $ renpy.block_rollback()
    
## MC-neutral prologue.
label prologue:
    $ dungeon_visited = False
    $ dungeon_visits_no_combo = 0
    $ redCount = 0
    
    $ bosses_defeated = 0
    stop music fadeout 1.0
    scene bg black
    "BZZT."
    scene cg hackerlogo
    voice "voice/prologue/ha1.ogg"
    un "Greetings, fellow Summoners! As many of you may have noticed over the recent months,
        there have been an increasing number of... issues... in the game known as League of Legends."
    voice "voice/prologue/ha2.ogg"
    un "Within the past few weeks, a select few members among the League community have suddenly received
        unspeakable powers... ones that have led to their accusations of cheating."
    voice "voice/prologue/ha3.ogg"
    un "But make no mistake... this is entirely my doing. In fact, it is proof that I have bypassed
        the supposedly unbreakable security and am able to modify this game at will."
    voice "voice/prologue/ha4.ogg"
    un "Some of you may ask - why would I go to such lengths? To that I answer... why does it matter?
        After all, none of you will be able to stop me."
    voice "voice/prologue/ha5.ogg"
    un "In only seven days, this game will be terminated forever. But don't worry... when your precious
        characters are deleted, there will always be other games to play. Like checkers! HAHAHA!"
    scene bg black # placeholder
    "BZZT."
    scene bg classroom day with dissolve
    "I'm [name]. Just your typical high school student... except for my extracurricular
     activities. They're what most people would call a little unusual."
    play music "music/bedroom.mp3" fadein 2.0
    voice "voice/prologue/z1.ogg"
    t "Class dismissed!"
    "Every day after class, I meet up with a certain group of people... a club. But, in
     this group, we do something a little different than just play sports."
    "We go... into Summoner's Rift. A virtual reality video game that requires complete
     dedication to your character."
    "That day, everyone was in an uproar. Little did I know that the mysterious hacker
     shown on the news would turn out to be much closer than I thought..."
    "... and would change my friends and I forever."
    
    scene bg classroom day # is there another sprite?
    voice "voice/prologue/ch1.ogg"
    show char fiora at center with dissolve
    ch "Hear ye, hear ye! I hereby call to order this meeting of the League of Legends
        Club!"
    if route == "Ezreal":
        voice "voice/prologue/ez1.ogg"
    elif route == "Leona":
        voice "voice/prologue/le1.ogg"
    mc sad "Couldn't you guys think about a more... unique name? Something more... adventurous?"
    hide char
    show ahri angry at left with dissolve
    voice "voice/prologue/am1.ogg"
    am "Who cares about that? Did you guys hear about the hacker?"
    if route == "Ezreal":
        voice "voice/prologue/ez2.ogg"
    elif route == "Leona":
        voice "voice/prologue/le2.ogg"
    mc flat "I think {i}everyone's{/i} heard about it."
    show raka flat at right with dissolve
    voice "voice/prologue/sh1.ogg"
    sh "Whatever... it's probably no big deal."
    voice "voice/prologue/am2.ogg"
    am "But, what if he's really serious? Do you think he can really shut it down just
        like that?"
    show raka angry at right
    voice "voice/prologue/sh2.ogg"
    sh "He's just blowing hot air. There's no way he would be able to hack into their
        system and not get caught."
    if route == "Ezreal":
        voice "voice/prologue/ez3.ogg"
    elif route == "Leona":
        voice "voice/prologue/le3.ogg"
    mc sad "Yeah, I guess so. But, still, everyone on the Internet is talking about it..."
    hide ahri
    show vik flat at left with dissolve
    voice "voice/prologue/cy1.ogg"
    cy "You shouldn't underestimate the power of a determined fool."
    hide raka
    show rumble surprised at right with dissolve
    voice "voice/prologue/da1.ogg"
    da "I dunno... I'm kinda scared."
    hide vik
    show jayce happy at left with dissolve
    voice "voice/prologue/je1.ogg"
    je "Well, don't be. It's only a game, man. What's the worst that could happen?"
    hide jayce
    hide rumble with dissolve
    voice "voice/prologue/ch2.ogg"
    ch "All right, everyone, settle down. I know everybody's worked up about this, but I
        just received some interesting information for you guys to look at. Take a look
        at this."
    voice "voice/prologue/am3.ogg"
    am "\"Rito Games offers one million Rito Points for the capture of the hacker...\""
    ### need to record a voice for this! ###
    everyone "{b}ONE MILLION POINTS!?{/b}" with hpunch
    show jayce surprised at left with dissolve
    voice "voice/prologue/je2.ogg"
    je "*whistle* That's some serious virtual dough."
    show jayce happy at left
    show vik flat at right with dissolve
    voice "voice/prologue/cy2.ogg"
    cy "Hmph. They're running scared. The weaklings... I could shut him down in an instant."
    hide jayce
    hide vik with dissolve
    show char fiora at center
    voice "voice/prologue/ch3.ogg"
    show char fiora with dissolve
    ch "It looks like the hacker was really serious if they're offering this big of a
        prize."
    if route == "Ezreal":
        voice "voice/prologue/ez4.ogg"
    elif route == "Leona":
        voice "voice/prologue/le4.ogg"
    mc happy "Honestly, if that prize will make someone catch him faster, I'm okay with that. I
        spent over 4 years of my life in the game... there's no way they can let it be
        shut down!"
    hide char
    show ahri happy2 at left with dissolve
    voice "voice/prologue/am4.ogg"
    am "Ooh, I've got an idea. Why don't {i}we{/i} go after the prize? After all, we're
        pretty skilled players, right? Who says we can't split it amongst ourselves?"
    hide char
    show raka sad at right with dissolve
    voice "voice/prologue/sh3.ogg"
    sh "There's only one problem... how are we supposed to do what the creators can't?"
    if route == "Ezreal":
        voice "voice/prologue/ez5.ogg"
    elif route == "Leona":
        voice "voice/prologue/le5.ogg"
    mc happy "Actually, I think that's a good idea. We can probably figure something out."
    show raka angry at right
    voice "voice/prologue/sh4.ogg"
    sh "Sigh... when you're coming up with big plans, you have to have some kind of strategy."
    voice "voice/prologue/am5.ogg"
    show ahri happy at left
    am "What about if we split up, and start doing detective stuff~"
    if route == "Ezreal":
        voice "voice/prologue/ez6.ogg"
    elif route == "Leona":
        voice "voice/prologue/le6.ogg"
    mc flat "I was thinking more along the lines of... me going over and beating up the hacker."
    show raka angrymid at right
    voice "voice/prologue/sh5.ogg"
    sh "You can't just beat up a hacker over the Internet. There's no way he'll play by the
        rules - he'll probably hack your character two ways from Tuesday."
    show ahri happy2 at left
    voice "voice/prologue/am6.ogg"
    am "Plus, this is Demacia, the biggest city in Runeterra. I'm sure we'll be able to
        find plenty of information."
    hide raka with dissolve
    show ahri behind raka
    show raka flat at center with dissolve
    voice "voice/prologue/sh6.ogg"
    sh "R-Really? You guys are serious? All right, fine. I'll help if it means saving
        Summoner's Rift."
    show rumble flat at right with dissolve
    voice "voice/prologue/da2.ogg"
    da "I don't know about this...  it seems awfully dangerous."
    hide raka
    hide ahri
    show jayce happy at center with dissolve
    voice "voice/prologue/je3.ogg"
    je "Buck up, dude. It'll probably be fun."
    hide jayce
    hide rumble
    show vik flat at center with dissolve
    voice "voice/prologue/cy3.ogg"
    cy "If you want something done right... do it yourself."
    hide vik
    show ahri happy2 at center with easeinleft
    voice "voice/prologue/am7.ogg"
    am "That's the spirit! Oh, and since I'm the team leader, I'll get a 50\% cut of the
        prize once we get it."
    if route == "Ezreal":
        voice "voice/prologue/ez7.ogg"
    elif route == "Leona":
        voice "voice/prologue/le7.ogg"
    mc angry "HEY! That's not something we'd ever agree to!"
    hide ahri
    show raka angry with dissolve
    voice "voice/prologue/sh7.ogg"
    sh "Yeah, talk about hogging the spotlight."
    hide raka
    show ahri happy2 at center with dissolve
    voice "voice/prologue/am8.ogg"
    am "Fine, then... why don't you be the team leader, [name]?"
    if route == "Ezreal":
        voice "voice/prologue/ez8.ogg"
    elif route == "Leona":
        voice "voice/prologue/le8.ogg"
    mc flat "What!? But, why does there have to be a team? I can probably handle it."
    show ahri happy at center
    voice "voice/prologue/am9.ogg"
    am "And if you can't we're all doomed. I think it would be better to have some people
        backing you up, don't you think?"
    if route == "Ezreal":
        voice "voice/prologue/ez9.ogg"
    elif route == "Leona":
        voice "voice/prologue/le9.ogg"
    mc flat "Sigh... you just want the hacker to target me instead. Okay, okay, I'll do it!"
    hide ahri
    show vik flat at left with dissolve
    voice "voice/prologue/cy4.ogg"
    cy "I agree. If the hacker is targeting a specific individual, the rest of us can do our job."
    show rumble angry at right with dissolve
    voice "voice/prologue/da3.ogg"
    da "As long as he doesn't come after me!"
    if route == "Ezreal":
        voice "voice/prologue/ez10.ogg"
    elif route == "Leona":
        voice "voice/prologue/le10.ogg"
    mc flat "Thanks for the vote of confidence..."
    hide vik
    hide rumble
    show char fiora at center with dissolve
    voice "voice/prologue/ch4.ogg"
    ch "I see you're already thinking up plans. Just don't get too carried away, or I might
        be out of a job."
    if route == "Ezreal":
        voice "voice/prologue/ez11.ogg"
    elif route == "Leona":
        voice "voice/prologue/le11.ogg"
    mc flat "I think that first things first, we should check out the dungeon itself when I get
        home."
    voice "voice/prologue/ch5.ogg"
    ch "We do have a spare headgear if you want to try it out right now."
    if route == "Ezreal":
        voice "voice/prologue/ez12.ogg"
    elif route == "Leona":
        voice "voice/prologue/le12.ogg"
    mc angry "No way, I don't want to go through all the trouble of calibrating the settings.
        That'd take way too much time... I'd rather just check later-"
    voice "voice/prologue/ch6.ogg"
    ch "We all want to know about the current situation in the game. This {i}is{/i} a club,
        you should at least do the responsible thing and fulfill your duties."
    if route == "Ezreal":
        voice "voice/prologue/ez13.ogg"
    elif route == "Leona":
        voice "voice/prologue/le13.ogg"
    mc flat "All right, all right, I'll put it on. Here we go..."
    hide char with dissolve
    stop music fadeout 2.0
    
    scene bg black with fade
    voice "voice/prologue/ca1.ogg"
    ca "Now entering calibration mode... being transported to training grounds for simple
        calibration."
    scene cg tut1
    pause
    scene cg tut2
    pause
    scene cg tut3
    pause
    
    scene bg black
    "... let's pretend we had a working tutorial here. WOOHOO! Everything's good!"
    
    scene bg classroom day with fade
    play music "music/bedroom.mp3" fadein 2.0
    if route == "Ezreal":
        voice "voice/prologue/ez14.ogg"
    elif route == "Leona":
        voice "voice/prologue/le14.ogg"
    mc flat "I don't see anything wrong. Even the basic lobby looks fine to me."
    if route == "Ezreal":
        voice "voice/prologue/ez15.ogg"
    elif route == "Leona":
        voice "voice/prologue/le15.ogg"
    mc flat "Everyone here seems pretty nonchalant about this; I guess all the ones that care
        are running around outside or grinding..."
    if route == "Ezreal":
        voice "voice/prologue/ez16.ogg"
    elif route == "Leona":
        voice "voice/prologue/le16.ogg"
    mc flat "I am hearing some weird rumors about \"ultimate buffs\", though."
    show ahri flat at center with dissolve
    voice "voice/prologue/am10.ogg"
    am "Ultimate Buffs? You mean, people's characters are being powered up?"
    if route == "Ezreal":
        voice "voice/prologue/ez17.ogg"
    elif route == "Leona":
        voice "voice/prologue/le17.ogg"
    mc flat "That's what it looks like. Strange..."
    hide ahri
    show vik flat at center with dissolve
    voice "voice/prologue/cy5.ogg"
    cy "The hacker must be using psychological warfare. Interesting."
    if route == "Ezreal":
        voice "voice/prologue/ez18.ogg"
    elif route == "Leona":
        voice "voice/prologue/le18.ogg"
    mc flat "It doesn't seem like anything else is unstable, though. For the most part, the game's
        completely intact."
    show char fiora at left with dissolve
    voice "voice/prologue/ch7.ogg"
    ch "Hmm, I expected a more aggressive approach with the release of that video within the
        League servers."
    hide vik
    show raka flat at center with dissolve
    voice "voice/prologue/sh8.ogg"
    sh "Maybe everyone is just in denial. Or ignoring it."
    hide char
    show rumble surprised at left with dissolve
    voice "voice/prologue/da4.ogg"
    da "Or maybe it's a hoax! That's always a possibility... right?"
    show vik flat at right with dissolve
    voice "voice/prologue/cy6.ogg"
    cy "I highly doubt that, but you can keep believing it if you want."
    hide vik
    hide rumble
    hide raka
    show char fiora at center with dissolve
    voice "voice/prologue/ch8.ogg"
    ch "All right everyone, club hours are officially over! Everyone head home and make
        sure to finish all of your assigned work before even thinking of playing League."
    voice "voice/prologue/ch9.ogg"
    ch "I don't have any personal issues with wanting to try to catch the hacker, but make sure
        to always put your safety first."
    ### WE NEED A VOICE HERE BOIZ ###
    everyone "Yes, ma'am!"
    hide char with dissolve
    if route == "Ezreal":
        voice "voice/prologue/ez19.ogg"
    elif route == "Leona":
        voice "voice/prologue/le19.ogg"
    mc surprise "... huh? I thought we had another member in the club. Oh well, it's probably my imagination..."
    scene bg black #temp
    stop music fadeout 0.5
    pause 1.0
    
    $ renpy.movie_cutscene("video/op.ogg")
    
    ## Start of first day's events begins here.
    jump afterschool
        
## What happens after school hours, when the user begins the event-choosing part of the game.
label afterschool:        
    "Day [day]. Time to get something done..."
    
label period_1:
    "Okay, off we go!"
    $ period = 1
    call event_menu
    if act == "dungeon":
        $ renpy.block_rollback()
        call dungeon
    else:
        $ renpy.block_rollback()
        call events_run_period
    call normalize_rp
    
label period_2:
    "I've got time for one more thing today..."
    $ period = 2
    call event_menu
    if act == "dungeon":
        $ renpy.block_rollback()
        call dungeon
    else:
        $ renpy.block_rollback()
        call events_run_period
    call normalize_rp

label night:
    scene bg black
    pause 1.0
    "... just like that, it's already become night time. I head back home to get some sleep and get
     ready for the next day." # temp
    call events_end_day
    if day >= 4 and bosses_defeated < 2:
        # jump unlock_combo2
        pass
    if day == 6 and bosses_defeated < 3:
        # jump unlock_combo3
        pass
    $ day += 1
    $ period = 0
    
label morning:
    if (day < 8):
        if day == 2:
            jump day2_pre
        elif day == 6 and not afterconfession_flag:
            if route == "Ezreal":
                if raka_confessed:
                    jump day6_afterconfession
            elif route == "Leona":
                if vik_confessed:
                    jump day6_afterconfession
        elif day == 7:
            jump day7_pre
        elif day >= 3:
            if bosses_defeated >= 1 and not afterdungeon_flag:
                jump afterdungeon
            elif dungeon_visited and not preboss_flag:
                jump preboss1
        elif route == "Ezreal":
            if raka_scene >= 3 and not raka3B_flag:
                call raka_3B
        call normalize_rp
        jump afterschool
    else:
        jump day8
        return
        
label dungeon:
    scene bg black
    stop music fadeout 0.5
    "Time to be patient... sometimes, it takes a little while."
    if route == "Leona":
        $ giftsInventory = [have_hammer, have_sketch, have_rubix]
        $ comboSkillsUnlocked = [jayce_combo, rumble_combo, vik_combo]
        $ SceneKeys = (sum(comboSkillsUnlocked), dungeon_visits_no_combo, bosses_defeated, vik_confessed)
        $ pass_list = [False, giftsInventory, comboSkillsUnlocked, SceneKeys]
        $ dungeon().loadFromVN(pass_list)
        call screen dungeon_run()
        scene bg black with dissolve
        $ [giftsReturned,n_bossesDefeated] = dungeon.getRetList()
        $ have_hammer = giftsReturned[0]
        $ have_sketch = giftsReturned[1]
        $ have_rubix = giftsReturned[2]
    elif route == "Ezreal":
        $ giftsInventory = [have_charm, have_bone, have_clip]
        $ comboSkillsUnlocked = [ahri_combo, rango_combo, raka_combo]
        $ SceneKeys = (sum(comboSkillsUnlocked), dungeon_visits_no_combo, bosses_defeated, raka_confessed)
        $ pass_list = [True, giftsInventory, comboSkillsUnlocked, SceneKeys]
        $ dungeon.loadFromVN(pass_list)
        call screen dungeon_run()
        scene bg black with dissolve
        $ [giftsReturned,n_bossesDefeated] = dungeon.getRetList()
        $ have_charm = giftsReturned[0]
        $ have_bone = giftsReturned[1]
        $ have_clip = giftsReturned[2]
    if n_bossesDefeated > bosses_defeated:
        $ bosses_defeated = n_bossesDefeated
        if route == "Ezreal":
            $ ahri_rp = ahri_rp + 15
            $ rango_rp = rango_rp + 15
            $ raka_rp = raka_rp + 15
        elif route == "Leona":
            $ jayce_rp = jayce_rp + 15
            $ rumble_rp = rumble_rp + 15
            $ vik_rp = vik_rp + 15
    else:
        if route == "Ezreal":
            if not ahri_combo and not rango_combo and not raka_combo and redCount > 0:
                call unlock_combo1
        elif route == "Leona":
            if not jayce_combo and not vik_combo and not rumble_combo and redCount > 0:
                call unlock_combo1
        $ dungeon_visits_no_combo = dungeon_visits_no_combo + 1
        if route == "Ezreal":
            $ ahri_rp = ahri_rp + 5
            $ rango_rp = rango_rp + 5
            $ raka_rp = raka_rp + 5
        elif route == "Leona":
            $ jayce_rp = jayce_rp + 5
            $ rumble_rp = rumble_rp + 5
            $ vik_rp = vik_rp + 5
    call normalize_rp
    return

label normalize_rp:
    if route == "Ezreal":
        if ahri_rp > 100:
            $ ahri_rp = 100
        if raka_rp > 100:
            $ raka_rp = 100
        if rango_rp > 100:
            $ rango_rp = 100
    elif route == "Leona":
        if jayce_rp > 100:
            $ jayce_rp = 100
        if rumble_rp > 100:
            $ rumble_rp = 100
        if vik_rp > 100:
            $ vik_rp = 100
    return

## Helper label for updating character location data.
label update_whois:
    $ whois_museum = "None"
    $ whois_park = "None"
    $ whois_library = "None"
    $ whois_vr = "None"
    $ whois_class = "None"
    $ whois_soccer = "None"
    $ park_priority = -1
    $ museum_priority = -1
    $ library_priority = -1
    $ vr_priority = -1
    $ soccer_priority = -1
    $ class_priority = -1
    if route == "Ezreal":
        if ahri_scene == 0:
            $ whois_library = "Ahri"
            $ library_priority = ahri_scene
        elif ahri_scene == 1:
            $ whois_vr = "Ahri"
            $ vr_priority = ahri_scene
        elif ahri_scene == 2 and day >= 3:
            $ whois_museum = "Ahri"
            $ museum_priority = ahri_scene
        elif ahri_scene == 3:
            if ahri4_flag:
                $ whois_library = "Ahri"
                $ library_priority = ahri_scene
            else:
                $ whois_vr = "Ahri"
                $ vr_priority = ahri_scene
        elif ahri_scene == 4:
            $ whois_vr = "Ahri"
            $ vr_priority = ahri_scene
        elif ahri_scene == 5:
            if not ahri_badend:
                $ whois_vr = "Ahri"
                $ vr_priority = ahri_scene
        elif ahri_scene == 6 and day == 7 and period == 2 and ahri_rp >= 70:
            $ whois_park = "Ahri"
            $ park_priority = ahri_scene
            
        if raka_scene == 0 or (raka_scene == 2 and period == 2):
            if library_priority < raka_scene:
                $ whois_library = "Soraka"
                $ library_priority = raka_scene
        elif (raka_scene == 1 and period == 2) or raka_scene == 3 or (raka_scene == 4 and period == 2):
            if vr_priority < raka_scene:
                $ whois_vr = "Soraka"
                $ vr_priority = raka_scene
        elif raka_scene == 5 and day == 7 and period == 2 and raka_rp >= 70:
            if park_priority < raka_scene:
                $ whois_park = "Soraka"
                $ park_priority = raka_scene
            
        if rango_scene == 0 or rango_scene == 2 or (rango_scene == 4 and day >= 6):
            if vr_priority < rango_scene:
                $ whois_vr = "Rengar"
                $ vr_priority = rango_scene
        elif (rango_scene == 1 and day >= 3 and period == 1) or (rango_scene == 3 and period == 1):
            if soccer_priority < rango_scene:
                $ whois_soccer = "Rengar"
                $ soccer_priority = rango_scene
        elif rango_scene == 5 and day == 7 and period == 2 and rango_rp >= 70:
            $ whois_vr = "Rengar"
            $ vr_priority = rango_scene
            
    elif route == "Leona":
        if jayce_scene == 0 and period == 1:
            $ whois_soccer = "Jayce"
            $ soccer_priority = jayce_scene
        elif jayce_scene == 1:
            $ whois_vr = "Jayce"
            $ vr_priority = jayce_scene
        elif jayce_scene == 2 and day >= 3:
            $ whois_class = "Jayce"
            $ class_priority = jayce_scene
        elif jayce_scene == 3 and period == 1:
            $ whois_park = "Jayce"
            $ park_priority = jayce_scene
        elif jayce_scene == 4 and day == 7 and period == 2 and jayce_rp >= 70:
            $ whois_soccer = "Jayce"
            $ soccer_priority = jayce_scene
            
        
        if rumble_scene == 0 or rumble_scene == 1:
            if library_priority < rumble_scene:
                $ whois_library = "Rumble"
                $ library_priority = rumble_scene
        elif rumble_scene == 2 and day >= 3:
            if vr_priority < rumble_scene:
                $ whois_vr = "Rumble"
                $ vr_priority = rumble_scene
        elif rumble_scene == 3 and period == 1:
            if class_priority < rumble_scene:
                $ whois_class = "Rumble"
                $ class_priority = rumble_scene
        elif rumble_scene == 4 and period == 1:
            if museum_priority < rumble_priority:
                $ whois_museum = "Rumble"
                $ museum_priority = rumble_scene
        elif rumble_scene == 5 and day == 7 and period == 2 and rumble_rp >= 70: # add the wait-a-day criteria
            if museum_priority < rumble_priority:
                $ whois_museum = "Rumble"
                $ museum_priority = rumble_scene
                
        if vik_scene == 0 or vik_scene == 3 or (vik_scene == 5 and day >= 5):
            if class_priority < vik_scene:
                $ whois_class = "Viktor"
                $ class_priority = vik_scene
        elif vik_scene == 1 or (vik_scene == 4 and day >= 4 and period == 2):
            if vr_priority < vik_scene:
                $ whois_vr = "Viktor"
                $ vr_priority = vik_scene
        elif (vik_scene == 2 and day >= 3) and day >= 4:
            if library_priority < vik_scene:
                $ whois_library = "Viktor"
                $ library_priority = vik_scene
        elif vik_scene == 6 and day == 7 and period == 2 and vik_rp >= 70:
            if library_priority < vik_scene:
                $ whois_library = "Viktor"
                $ library_priority = vik_scene
    return
    
## Menu for choosing location. Must be called.
label event_menu:
    call update_whois
    call screen school_map
    $ act = _return
    return

## Gift dialogue control label. Must be called.
label gift_check(target="blank"):
    if route == "Ezreal":
        if have_bone: # hue
            "I turn to leave, but remember the unfamiliar heft to one of my pockets. The necklace!
             Maybe [target] would like it?"
            menu:
                "What should I do?"
                "Hand it over.":
                    if target == "Ami":
                        call ahri_bone from _call_ahri_bone
                        return
                    elif target == "Gwen":
                        call rengar_bone from _call_rengar_bone
                        return
                    elif target == "Sharon":
                        call soraka_bone from _call_soraka_bone
                        return
                "Keep it for another time.":
                    "I decide against it, this time."
                    return
        elif have_charm:
            "I stop in my tracks, remembering something I had forgotten about earlier."
            "The charm I found in the dungeon... should I give it to [target]?"
            menu:
                "What should I do?"
                "Hand it over.":
                    if target == "Ami":
                        call ahri_charm from _call_ahri_charm
                        return
                    elif target == "Gwen":
                        call rengar_charm from _call_rengar_charm
                        return
                    elif target == "Sharon":
                        call soraka_charm from _call_soraka_charm
                        return
                "Keep it for another time.":
                    "No, I don't think this is the right situation."
                    return
        elif have_clip:
            "... wait. I have that hairclip I found in the dungeon. I could give it to
             [target]."
            menu:
                "What should I do?"
                "Hand it over.":
                    if target == "Ami":
                        call ahri_hairclip from _call_ahri_hairclip
                        return
                    elif target == "Gwen":
                        call rengar_hairclip from _call_rengar_hairclip
                        return
                    elif target == "Sharon":
                        call soraka_hairclip from _call_soraka_hairclip
                        return
                "Keep it for another time.":
                    "Not right now, I think. I'd better hold onto it."
                    return
    elif route == "Leona":
        if have_hammer:
            "Wait a moment. Didn't I find something [target] might like? The hammer?"
            menu:
                "What should I do?"
                "Present time!":
                    if target == "Jason":
                        call jayce_hammer from _call_jayce_hammer
                    elif target == "Cyrus":
                        call viktor_hammer from _call_viktor_hammer
                    elif target == "Daniel":
                        call daniel_hammer from _call_daniel_hammer
                    return
                "Keep it for now.":
                    "No, I don't think this is the right time. I'll keep it for now!"
                    return
        elif have_rubix:
            "Didn't I find a rubix cube in the dungeon? Maybe [target] would like it!"
            menu: 
                "What should I do?"
                "Present time!":
                    if target == "Jason":
                        call jayce_rubix from _call_jayce_rubix
                    elif target == "Cyrus":
                        call viktor_rubix from _call_viktor_rubix
                    elif target == "Daniel":
                        call daniel_rubix from _call_daniel_rubix
                    return
                "Keep it for now.":
                    "No, I don't think this is the right time. I'll keep it for now!"
                    return
        elif have_sketch:
            "Suddenly, I remember about the the sketchbook I found in the dungeon. I still have it...
             maybe [target] would like it?"
            menu: 
                "What should I do?"
                "Present time!":
                    if target == "Jayce":
                        call jayce_sketch from _call_jayce_sketch
                    elif target == "Viktor":
                        call viktor_sketch from _call_viktor_sketch
                    elif target == "Rumble":
                        call daniel_sketch from _call_daniel_sketch
                    return
                "Keep it for now.":
                    "No, I don't think this is the right time. I'll keep it for now!"
                    return
    return
