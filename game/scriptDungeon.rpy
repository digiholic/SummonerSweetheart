label quitScreen:
  show screen dungeon_run(False)
  $ renpy.block_rollback()
  menu:
    "Are you sure you want to retreat?"
    "Never!":
      pass
    "Flee!":
      $ battleFlag = "retreat"
  
  #$ current_battle.reActivate()
  call screen dungeon_run(True)
  return
  
label victoryScreen:
    show screen dungeon_run(False)
    $ renpy.block_rollback()
    "YOU WIN"
    if route == "Ezreal":
      if have_charm == False and random.randint(0,10) == 0:
        "Found Charm!"
        $ have_charm = True
      elif have_bone == False and random.randint(0,10) == 0:
        "Found Bone!"
        $ have_bone = True
      elif have_clip == False and random.randint(0,10) == 0:
        "Found Clip!"
        $ have_clip = True
    else:
      if have_hammer == False and random.randint(0,10) == 0:
        "Found Hammer!"
        $ have_hammer = True
      elif have_sketch == False and random.randint(0,10) == 0:
        "Found Sketch!"
        $ have_sketch = True
      elif have_rubix == False and random.randint(0,10) == 0:
        "Found Rubix!"
        $ have_rubix = True
    menu:
        "Press on":
            vrmc happy " Let's keep going!"
            $ battleFlag = "onward"
        "That's enough":
            vrmc flat " I think that's far enough for now, let's heal up and come back later!"
            $ battleFlag = "retreat"
    call screen dungeon_run(True)
    return

label afterFirstBattle:
  show screen dungeon_run(False)
  $ renpy.block_rollback()
  "YOU WIN"
  h "Congratulations, Summoner! You’ve defeated the first minion of the game. You must be brimming with pride and glee."
  h "Well, that will be short-lived, I assure you. No matter how you may try and struggle, you stand no chance of defeating {i}me{/i}!"
  h "If you still think you stand a chance, you are welcome to try! But, first, you have to get past all of my minions! *Cackling*"
  menu:
    "Get past all of his minions":
      vrmc happy " No problem! We can take anything you throw at us!"
      $ battleFlag = "onward"
    "I don't stand a chance":
      vrmc sad " He might be right. I'm not ready for this yet. I'll come back later."
      $ battleFlag = "retreat"
  call screen dungeon_run(True)
  return
            
label redBattle:
    show screen dungeon_run(False)
    $ renpy.block_rollback()
    if (route == "Ezreal" and (ahri_combo or raka_combo or rango_combo)) or (route == "Leona" and (jayce_combo or rumble_combo or vik_combo)):
      vrmc happy "All right, now I should use that combo that Teemo taught me."
    elif redCount == 0:
      vrmc sad "Why is this boss so hard to annihilate?! Nothing seems to be working."
      vrmc surprise "It’s as if this monster has some kind of buff... That’s it! This is the hacker’s doing."
      vrmc surprise "Wait, that golden stance – that’s Zhonya’s! A players-only item that lets you become invulnerable for a couple seconds. How does he have it?"
      vrmc angry "Argh. I think I need to ask someone for help."
    elif redCount == 1:
      vrmc angry "This is so hopeless. Although I hate to admit it, I {i}really{/i} need to ask the club for some advice."
      vrmc angry "At this rate, I’ll be wasting all my time bumping into the same problem over and over again."
      vrmc flat "There has to be {i}someone{/i} who knows what to do."
    elif redCount == 2:
      vrmc angry "Okay, now I’m just being stupid and stubborn."
      vrmc angry "Why am I diving into the dungeon when I know I can’t kill the boss without some sort of help?"
      vrmc sad "Me and my pride…"
      
    $ redCount += 1
    $ current_battle.reActivate()
    call screen dungeon_run(True)
    return
    
label killRed:
  show screen dungeon_run(False)
  $ renpy.block_rollback()
  rb "Urgh…"
  rb "…"
  vrmc surprise "W-what was that?"
  vrmc surprise "Did the boss just {i}talk{/i}? I mean, if you can call it talking."
  vrmc flat "Nah, that must be my imagination."
  "-ZZZZZZZZ-"
  vrmc angry "Again with the static? It’s getting old, Mr. Hacker. Speaking of which, where is he—"
  h "You! It seems you are truly intent on disturbing my plans! You dare defy me?!"
  vrmc angry "Well, duh. I mean, you were the one who invited us after all."
  h "Heh. Fair enough. When the day strikes seven, I will offer you a special portal to enter into my lair for the final challenge. You will receive a very warm welcome."
  h "Be sure to gather as many allies until then – members that you can {i}trust{/i}. Keke."
  vrmc flat "That I can trust? What does he mean by that…"
  $ bosses_defeated += 1
  $ current_battle.reActivate()
  $ current_battle.enemies[0].die()
  call screen dungeon_run(True)
  return
    
label killBaron:
  show screen dungeon_run(False)
  $ renpy.block_rollback()
  na "ARRGHH!"
  na "You’ll never get away with this…"
  vrmc surprise "Wait, what?!"
  "That was beyond weird."
  $ bosses_defeated += 1
  $ current_battle.reActivate()
  $ current_battle.enemies[0].die()
  call screen dungeon_run(True)
  return
    
  
label waitBaron:
  show screen dungeon_run(False)
  $ renpy.block_rollback()
  $ renpy.music.stop(fadeout=5)
  vrmc surprise "Wait! Nashor, I have a question."
  na "Ergh?!"
  vrmc flat "Yea, I know you can talk. You’re a player aren’t you?"
  na "… Yea."
  vrmc angry "Why are helping the hacker? I mean, other than the fact that you can look {i}so{/i} cool."
  na "Look, it’s not like I {i}want{/i} to be a villain. He just popped out of nowhere and told me he’d delete my character if I didn’t help."
  vrmc angry "What, so that justifies what you’re doing?"
  na "I’m in the Master League; spent four years on the game going from Bronze V to where I am now. You think I want him to make all my progress go POOF! just like that?"
  vrmc sad "…"
  "That would actually suck."
  na "Well, whatever. It won’t matter now since he’ll destroy the game anyways."
  vrmc happy "Hey! Don’t worry – I’ll catch him before he can."
  na "Psh. You can die trying, literally."
  vrmc angry "W-what do you mean by that?"
  na "He has this hack that doesn’t let you leave the game once you face him. You’re stuck in here forever, and if you die, well… You can do the math."
  vrmc sad "…"
  "I never signed up for a death wish. Is this {i}really{/i} worth it?"
  $ bosses_defeated += 1
  scene bg black with fade
  return
    
label beforeHacker:
  show screen dungeon_run(False)
  $ renpy.block_rollback()
  if day != 7:
    vrmc angry "There's some sort of... force pushing me back. I think the hacker's set up a force field. He'll have to lower it to destroy the game, I'll have to come back right before that happens!"
    $ battleFlag = "retreat"
    call screen dungeon_run(True)
    return
  
  h "Welcome to your doom, champions! Or should I say losers, since you will soon be {i}losing{/i} your lives."
  h "You are free to die at will. Just say the word and I’ll zap you into mindless bodies."
  vrmc angry "Seriously? You’re one sick hacker."
  h "Why, thank you. I’ll take that as a compliment, or maybe it’s a cry for help. There is no return for you now!"
  vrmc happy "Nah, it’s time to give you a piece of my mind!"
  
  if route == "Ezreal":
    if raka_confessed == False:
      show raka vr flatclose at right onlayer screens
      so "E-Ezreal! Wait!"
      ez flat "Huh? What is it?"
      show raka vr sadblushclose at right onlayer screens
      so "I… I need to tell you something."
      ez angry "Talk about poor timing – we’ve got a hacker to defeat, Soraka! Is it important?"
      show raka vr surprisedclose at right onlayer screens
      so "U-um, actually, nevermind."
      ez happy "Alright! Like I was saying, onward—"
      hide raka onlayer screens
      $ current_battle.betray()
      $ current_battle.reActivate()
      call screen dungeon_run(True)
      return
    
    elif raka_confessed == True:
      show raka vr flatclose at right onlayer screens
      so "E-Ezreal! Wait!"
      ez flat "Huh? What is it?"
      show raka vr sadblushclose at right onlayer screens
      so "I… I need to tell you something. It’s about the friend during the Virtual Reality testing."
      ez angry "Is this important? We’re kinda in the middle of battling a really big, bad guy."
      show raka vr angryclose at right onlayer screens
      so "That girl – my best friend – is the hacker’s daughter."
      ez  surprise "HNGUH… What?!"
      show raka vr angryclose at right onlayer screens
      so "In order to atone for my inability to save her, I joined the hacker to ease his pain. I’ve been helping him since her death."
      ez sad "I… I don’t know what to say."
      show raka vr sadclose at right onlayer screens
      so "I’m really sorry. I wanted to tell you earlier, but I couldn’t bear the thought of you hating me, too. I know it wasn’t right for me to do, but I just—"
      ez shyblush "Sigh. Didn’t I say it before? A real friend will see your flaws and continue to support you."
      show raka vr happyclose at right onlayer screens
      so "Thanks, Ezreal. I know this isn’t much, but at the least, I want to give you this buff that I stole from the hacker."
      so "It should make the battle a bit easier for you, but this is the most I can do outside of being in your party."
      
      $ current_battle.getBeefy()
      
      ez happy "Wow! I’m sure this’ll come in handy for us! Thanks a ton!"
      show raka vr happyblushclose at right onlayer screens
      so "… I’m the one who should be saying thank you, but you’re welcome!"
      hide raka onlayer screens
      h "Hmm? Is that a look of defiance I see?"
      show raka vr angry onlayer screens
      $ renpy.music.play(current_battle.music)
      so "That’s right! I won’t assist you any further, Dr. Reveck! What you’re doing is wrong, no matter how I look at it."
      so "This isn’t about me anymore; even if I have to bear the weight of Orianna’s death, forcing that despair on others is a fate much worse."
      h "Unable to fulfill your duties until the end, I see. So be it! Fight me if you will, or knowing your own failures, will you turn tail now?"
      hide raka onlayer screens
      $ current_battle.reActivate()
      call screen dungeon_run(True)
      return
    
  elif route == "Leona":
    if vik_confessed == False:
      show vik vr flatclose at right onlayer screens
      vi "Leona."
      le flat "Huh? What’s wrong?"
      show vik vr sadclose at right onlayer screens
      vi "I must inform you of an important development because withholding such information leads to regret."
      le angry "What are you talking about? Are you saying you regret helping us get this far? It’s pretty late for that."
      vi "It is as you say: a bit too late to attempt to rationalize and justify my regrets."
      le sad "We’re all just as uneasy as you, Viktor. Don’t worry about it too much, okay?"
      vi "..."
      hide vik onlayer screens
      $ current_battle.betray()
      $ current_battle.reActivate()
      call screen dungeon_run(True)
      return
    elif vik_confessed == True:
      show vik vr flatclose at right onlayer screens
      vi "Leona."
      le flat "Huh? What’s wrong?"
      show vik vr sadclose at right onlayer screens
      vi "I must inform you of an important development because withholding such information leads to regret."
      le angry "If it’s about being the hacker’s helper, you told me already."
      show vik vr flatclose at right onlayer screens
      vi "I wish to expand your knowledge of the situation."
      vi "Those lines of coding you witnessed in the classroom were none other than preparations for the demise of League of Legends. The hacker was the former head of the Virtual Reality department, and there were many things I learned under his guidance."
      vi "Although it seems that he is working under the concept of both revenge and atonement, I did not find the need to implore any further."
      le shyblush "I’m surprised you were confident enough to work on it right in front of me."
      show vik vr surprisedblushclose at right onlayer screens
      vi "... Whatever the case may be, I am aware that my actions were not justified, even if it was for the pursuit of greater knowledge."
      show vik vr happyclose at right onlayer screens
      vi "As a form of compensation, I was able to emulate a buff immune to the limitations of this world. Although it is a trivial amount, it may assist you in defeating the hacker. Please accept it as well as my apology for not informing you sooner."

      $ current_battle.getBeefy()
      
      le happyblush "Well, I guess you gotta do it the Viktor way, don’t you? I accept your apology!"
      le happy "Come on, let’s go, Viktor! We have a hacker’s butt to kick! And thanks for the buff~!"
      hide vik onlayer screens
      h "Hmm? Is that a look of defiance I see?"
      show vik vr angry onlayer screens
      $ renpy.music.play(current_battle.music)
      vi "I will abstain from any further support for your actions, Dr. Reveck. I will battle you alongside my allies. Although they may be less than ideal partners, they hold signs of great promise."
      le flat "You know, those aren’t exactly comforting words..."
      vi "Although you possess the intellectual capacity of an average person, you fall short when it comes to the influences of society."
      h "So be it! Fight me if you will, or knowing the incompetence of your partners, will you turn tail now?"
      hide vik onlayer screens
      $ current_battle.reActivate()
      call screen dungeon_run(True)
      return
    
label betrayal:
    if route == "Ezreal":
      show screen dungeon_run(False)
      $ renpy.block_rollback()
      hide raka onlayer screens
      ez surprise "Ergh. Wha… Wh—Huh?!"
      h "I can see your mind is all jumbled. Let me clarify it for you, petty player, since these will be your last thoughts!"
      h "After the death of my daughter, the parties to blame include Rito Games, myself, and your beloved \"friend\" Soraka."
      h "Because of her incompetent help, Soraka lay beside my daughter – her friend – unharmed while she was left to die a horrible death."
      h "As such, Soraka is now an instrument of aid for my tale of revenge; all to atone for her failure."
      ez sad "Soraka… is that true?"
      show raka vr sad at right onlayer screens
      so "…"
      so "I must correct my sins, Ezreal. I’m sorry."
      hide raka onlayer screens
      jump afterBetrayal
      
    else:
      show screen dungeon_run(False)
      $ renpy.block_rollback()
      hide vik onlayer screens
      le surprise "Hnng?! Why did you –"
      h "To fulfill my revenge, I have recruited one of the most brilliant minds to carry out my plans! That is, of course, none other than Viktor, the Machine Herald!"
      h "With his thirst for knowledge and my conviction to avenge my daughter’s death –"
      le angry "Viktor? Then what I saw before was..."
      show vik vr angry at right onlayer screens
      vi "That is correct, Leona. Those lines of texts you lauded were for your own demise. For the sake of knowledge, I will do whatever it takes."
      hide vik onlayer screens
      jump afterBetrayal
    
label afterBetrayal:
    h "Ahem. As I was saying before being {i}rudely{/i} interrupted – Orianna volunteered to help Rito test their new headgear prototype, but that wretched stormy accident left her defenseless in the lab."
    h "Her personality slowly deteriorated, her moods bordered the volatility of that of schizophrenia, and her mental condition only further decayed."
    h "I attempted to use Rito’s technology to cure her illness, if not to at least alleviate her pain! But, before I could make any substantial progress, Rito pulled me from my seat and dismissed me on the terms of unauthorized use of their technology!"
    h "To this day, I do not forgive them or myself for ultimately killing my daughter."
    vrmc angry "T... That doesn’t legitimize your actions to harm others!"
    h "I can see your heart wavers. However, remember: this and that are separate issues. Better yet, if you have the resolve to join me in my path to revenge, you may."
    vrmc angry "I won’t laugh at your determination, but the last thing I would do is join you!"
    h "Hahahah, I expected those words! Your journey ends here, Hero!"
    $ renpy.music.play(current_battle.music)
    $ current_battle.reActivate()
    call screen dungeon_run(True)
    return
    
label hackerHalfHealth:
  show screen dungeon_run(False)
  $ renpy.block_rollback()
  $ renpy.music.stop(fadeout=3)
  h "I see you come with more than mere determination!"
  h "I will wager everything on you, to see how strong your resolve is! I will delete your teammates so that we may have a fair match, with the future of League of Legends at stake!"
  vrmc angry "Delete my teammates? You can’t do that, not in this world. You have to be crazy! They’ll di—"
  everyone "W-what’s going on? AHHH!"
  
  $ current_battle.oneOnOne()
  $ current_battle.reActivate()
  call screen dungeon_run(True)
  return
  
label hackerBeforeDuel:
  show screen dungeon_run(False)
  $ renpy.block_rollback()
  vrmc angry "What have you done?? I’ll never forgive you for this!"
  h "Fear not! Even now, your loved ones suffer!"
  vrmc sad "D... Does that mean..?"
  h "Hero, face me with all you have, and show me how much you are willing to risk for the happiness of others!"
  $ renpy.music.play(os.path.join(*['music','Boss Battle.mp3']))
  $ current_battle.reActivate()
  call screen dungeon_run(True)
  return
  
label loseFinalBattle:
  show screen dungeon_run(False)  
  scene bg black with fade
  $ renpy.block_rollback()
  $ renpy.music.stop(fadeout=1)
  vrmc sad "I... I can’t go on. Will I die here?"
  h "AHAHA! Now {i}that{/i} is the face of defeat. I should put this picture on my wall."
  un "Stand united!"
  play sound "music/standUnited.wav"
  #Shen POOFs on screen
  $ renpy.pause(1, hard=True)
    
  show char shen at left with dissolve
  s "Leona/Ezreal, I have come to assist you. While the classroom remains in panic, I believe my help will benefit in your valiant quest."
  vrmc surprise "Shen? What are you doing here?"
  hide shen
  h "So, it was {i}you{/i}. You have been chasing my trail, Shen?"
  s "That is so. As a former colleague, I would not forget your presence, even after five years."
  h "You are the one who condemned me for the sake of your own profits! Are you here to take away the last form of self-gratification I can offer myself?"
  vrmc angry "Shen, what’s going on? Who are you?"
  s "I am not your typical club advisor."
  s "As for you, Doran – or should I say Corin – you seem to have misunderstood the intentions of Rito."
  h "You? A club advisor? Hah, do you expect me to believe you, someone who so quickly forsakes the life of a child, have the right to provide guidance to students?"
  s "Let me explain the aftermath of our previous discussion."
  s "You were relieved of your duties under violation of the contract. The process hastened to allow you time with your family."
  s "Meanwhile, we had developed a secondary unit to investigate the malfunctions of the headgear and arrive at a solution to your daughter’s dilemma."
  h "What lies! I was never notified of such efforts."
  s "Your emotions prevented any reasonable actions on your behalf. We attempted to inform you when we discussed the terms of your discharge, but during the barrage of anger, you refused to listen."
  s "Regardless, we continued our analysis, but were unable to heal your daughter before her passing."
  s "For that, we are deeply sorry. Unable to save the life of a child, the project was soon canceled and all operations ceased."
  s "With nothing to offer for condolences, we decided it best not mention our activity, as it would simply be pouring salt in open wounds."
  s "To atone for our failure, many of the individuals involved in the project, including myself, resigned from our positions and resolved to help those in our local communities."
  h "…"
  h "It can’t be..."
  h "Are you saying my efforts for revenge were for naught?"
  s "If you feel compelled to destroy this world as part of a relief effort, you are free to exact your revenge to Summoner’s Rift. There has been no real alleviation for your sorrows."
  s "However, I am obliged to protect the students that have been entrusted to me, so I must save this life that I hold dear."
  h "Shen..."
  h "…"
  h "What? Impossible. To think such simple words could sway my resolve."
  vrmc sad "You know what I think? I think you’ve proven your despair to the world, already."
  vrmc sad "Even though I may be a kid in an adult world, I doubt your daughter would be happy knowing you were erasing lives in the game she helped create."
  h "Very well, you may keep your beloved world, so long as no harm comes about this game as it had been done to me."
  h "I will direct my efforts to something that will please Orianna. I will aim to reinstitute the research done to utilize Virtual Reality technology for the sake of the medical sciences."
  h "Perhaps, I will create an exact replica to honor my daughter."
  h "…"
  h "This will be our final meeting, Shen. Never again will I run into you because of this accursed game. Take pride in the students you have taken care of."
  h "…"
  scene bg black with fade
  
  if route == "Ezreal" and raka_confessed == False:
    h "Soraka."
    show raka surprise onlayer screens with dissolve
    so "Y-yes, Dr. Reveck?!"
    h "The end was inevitable. Orianna was sure to die without the appropriate equipment."
    h "I understand your regret for failing to save your friend, but there is no reason for you to shoulder the weight of her death on your shoulders."
    h "As long as you grow from this experience, I hold no true sense of contempt towards you."
    show raka happyblush onlayer screens
    so "…!"
    so "Yes, thank you, doctor."

    h "With that, farewell."
    scene bg black with fade
    
    hide raka
    $ renpy.pause(0.5, hard=True)
    "The end of an unthinkably torrential event has finally ended."
    "What was there to say after this nightmare? We all silently returned to our homes with our respective VR helmets and called in for the night after a short salutation, with our advisor nowhere in sight."
    
  elif route == "Leona" and vik_confessed == False:
    h "Viktor. You are a man of great wisdom, but your definition of knowledge is too narrow."
    show vik angry onlayer screens with dissolve
    vi "Are you saying I am incompetent?"
    h "In some ways, yes."
    show vik flat onlayer screens
    h "Do not limit your definition of knowledge to strictly the physical world. There are many things to observe in this intricate society created by people."
    h "I expect great things from you, Viktor. But to be able to hold your head high, I hope you will learn to be intertwined within the fine parts of society and acquire more than what can be taught through books and logic."
    vi "Understood, Dr. Reveck."

    h "With that, farewell."
    scene bg black with fade
    hide vik
    $ renpy.pause(0.5, hard=True)
    "The end of an unthinkably torrential event has finally ended."
    "What was there to say after this nightmare? We all silently returned to our homes with our respective VR helmets and called in for the night after a short salutation, with our advisor nowhere in sight."
  return
  
label winFinalBattle:
  show screen dungeon_run(False)  
  scene bg black with fade
  $ renpy.block_rollback()
  $ renpy.music.stop(fadeout=1)
  h "This is impossible! I am stronger!"
  vrmc flat "That may be true, but I have the support of all my comrades, and a few tricks up my sleeve."
  h "To think my plan would be foiled by a system in the game that I failed to recognize. How can this be?"
  vrmc angry "Well, it’s over now! Give it up!"
  "-SHIIING"
  play sound "music/standUnited.wav"
  $ renpy.pause(1.0, hard=True)
    
  show char shen at left with dissolve
  s "Doran."
  vrmc surprise "Shen?!"
  h "Shen…"
  vrmc surprise "What? You know him, too?"
  h "Of course. I would never forget the face who forsake my daughter."
  vrmc flat "What is he talking about? What’s going on?"
  s "It is a story for another day, young one."
  h "Did you come here to gloat about my defeat, Shen? That some puny Summoner thwarted my plans?"
  s "On the contrary, I want to clear up a misunderstanding that should have been done sooner."
  s "We tried everything to save your daughter, Corin. You were blinded by your hatred that you could not see our efforts."
  h "Oh, please. Save me the sob story. All you’re doing now is trying to save face and appeasing my years of rage."
  h "You and I both know that whatever petty excuses Rito devised isn’t worth either of our times."
  s "They’re not –"
  h "Well, whatever. You’ve won for now. I’ll be back another day, Summoners."
  
  scene bg black with fade
  $ renpy.pause(0.5, hard=True)
    
  "The end of an unthinkably torrential event has finally ended."
  "We all slowly come to consciousness and shine a weak smile to each other, recognizing our accomplishment. Although the hacker did make the others unable to act, apparently they were merely transferred to a spectating state to oversee the events."
  "Our advisor joins and congratulates us on our achievements, although we’re all too tired to do more than give a weak response."
  "He sends us home with our respective VR helmets, and we quickly head off to bed as a reward for our achievements."
  return
  
label gameOver:
  $ renpy.music.stop(fadeout=1)
  scene bg black with fade
  $ renpy.block_rollback()
  "CONNECTION LOST{w}.{w}.{w}."
  "GAME OVER"
  
