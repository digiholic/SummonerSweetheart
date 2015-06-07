label victoryScreen:
    scene expression DungeonScene()
    "YOU WIN"
    menu:
        "Press on":
            vrmc happy " Let's keep going!"
            $ summonersRift.getDungeon().battle.onward()
            call screen dungeon_run()
        "That's enough":
            vrmc flat " I think that's far enough for now, let's heal up and come back later!"
            $ summonersRift.getDungeon().battle.retreat()
            call screen dungeon_run()
    return
            
label redBattle:
    scene expression DungeonScene()
    
    if redCount == 0:
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
    $ summonersRift.getDungeon().battle.retreat()
    call screen dungeon_run()
    return
    
label afterFirstBattle:
  scene expression DungeonScene()
  "YOU WIN"
  h "Congratulations, Summoner! You’ve defeated the first minion of the game. You must be brimming with pride and glee."
  h "Well, that will be short-lived, I assure you. No matter how you may try and struggle, you stand no chance of defeating {i}me{/i}!"
  h "If you still think you stand a chance, you are welcome to try! But, first, you have to get past all of my minions! *Cackling*"
  menu:
    "Get past all of his minions":
      vrmc happy " No problem! We can take anything you throw at us!"
      $ summonersRift.getDungeon().battle.onward()
      call screen dungeon_run()
    "I don't stand a chance":
      vrmc sad " He might be right. I'm not ready for this yet. I'll come back later."
      $ summonersRift.getDungeon().battle.retreat()
      call screen dungeon_run()
  return
  
label killBaron:
  scene expression DungeonScene()
  na "ARRGHH!"
  na "You’ll never get away with this…"
  vrmc surprise "Wait, what?!"
  "That was beyond weird."
  call screen dungeon_run()
  return
  
label waitBaron:
  scene expression DungeonScene()  
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
  call screen dungeon_run()
  return
  
label beforeHacker:
  scene expression DungeonScene()    
  h "Welcome to your doom, champions! Or should I say losers, since you will soon be {i}losing{/i} your lives."
  h "You are free to die at will. Just say the word and I’ll zap you into mindless bodies."
  vrmc angry "Seriously? You’re one sick hacker."
  h "Why, thank you. I’ll take that as a compliment, or maybe it’s a cry for help. There is no return for you now!"
  vrmc happy "Nah, it’s time to give you a piece of my mind!"
  
  if route == "Ezreal":
    if raka_confessed == False:
      show raka vr flatclose at right
      so "E-Ezreal! Wait!"
      ez flat "Huh? What is it?"
      show raka vr sadblushclose at right
      so "I… I need to tell you something."
      ez angry "Talk about poor timing – we’ve got a hacker to defeat, Soraka! Is it important?"
      show raka vr surprisedclose at right
      so "U-um, actually, nevermind."
      ez happy "Alright! Like I was saying, onward—"
      
      $ summonersRift.getDungeon().battle.betray()
      call screen dungeon_run()
      return
      
    elif raka_confessed == True:
      show raka vr flatclose at right
      so "E-Ezreal! Wait!"
      ez flat "Huh? What is it?"
      show raka vr sadblushclose at right
      so "I… I need to tell you something. It’s about the friend during the Virtual Reality testing."
      ez angry "Is this important? We’re kinda in the middle of battling a really big, bad guy."
      show raka vr angryclose at right
      so "That girl – my best friend – is the hacker’s daughter."
      ez  surprise "HNGUH… What?!"
      show raka vr angryclose at right
      so "In order to atone for my inability to save her, I joined the hacker to ease his pain. I’ve been helping him since her death."
      ez sad "I… I don’t know what to say."
      show raka vr sadclose at right
      so "I’m really sorry. I wanted to tell you earlier, but I couldn’t bear the thought of you hating me, too. I know it wasn’t right for me to do, but I just—"
      ez shyblush "Sigh. Didn’t I say it before? A real friend will see your flaws and continue to support you."
      show raka vr happyclose at right
      so "Thanks, Ezreal. I know this isn’t much, but at the least, I want to give you this buff that I stole from the hacker."
      so "It should make the battle a bit easier for you, but this is the most I can do outside of being in your party."

      #Ezreal starts glowing
      #TODO: In-game, Ez's stats go up a bunch
      
      ez happy "Wow! I’m sure this’ll come in handy for us! Thanks a ton!"
      show raka vr happyblushclose at right
      so "… I’m the one who should be saying thank you, but you’re welcome!"
      hide raka
      h "Hmm? Is that a look of defiance I see?"
      show raka vr angry 
      # Start battle music
      so "That’s right! I won’t assist you any further, Dr. Reveck! What you’re doing is wrong, no matter how I look at it."
      so "This isn’t about me anymore; even if I have to bear the weight of Orianna’s death, forcing that despair on others is a fate much worse."
      h "Unable to fulfill your duties until the end, I see. So be it! Fight me if you will, or knowing your own failures, will you turn tail now?"
      call screen dungeon_run()
      return
      
  elif route == "Leona":
      pass
  
label betrayal:
      scene expression DungeonScene()    
      hide raka
      ez surprise "Ergh. Wha… Wh—Huh?!"
      h "I can see your mind is all jumbled. Let me clarify it for you, petty player, since these will be your last thoughts!"
      h "After the death of my daughter, the parties to blame include Rito Games, myself, and your beloved \"friend\" Soraka."
      h "Because of her incompetent help, Soraka lay beside my daughter – her friend – unharmed while she was left to die a horrible death."
      h "As such, Soraka is now an instrument of aid for my tale of revenge; all to atone for her failure."
      ez sad "Soraka… is that true?"
      show raka vr sad at right
      so "…"
      so "I must correct my sins, Ezreal. I’m sorry."
      call screen dungeon_run()
      return
      
label AfterBetrayal:
    pass
