label TestTrigger:
    show expression DungeonScene()
    show raka vr flat at right
    ez flat "Testing dialogue scene"
    call screen dungeon_run()
    
label victoryScreen:
    scene expression DungeonScene()
    "YOU WIN"
    menu:
        "Press on":
            ez happy " Let's keep going!"
            $ summonersRift.getDungeon().battle.onward()
            call screen dungeon_run()
        "That's enough":
            ez flat " I think that's far enough for now, let's heal up and come back later!"
            $ summonersRift.getDungeon().battle.retreat()
            call screen dungeon_run()
            
label redBattle:
    scene expression DungeonScene()
    $ redCount = 0
    
    if redCount == 0:
      ez sad "Why is this boss so hard to annihilate?! Nothing seems to be working."
      ez surprise "It’s as if this monster has some kind of buff... That’s it! This is the hacker’s doing."
      ez surprise "Wait, that golden stance – that’s Zhonya’s! A players-only item that lets you become invulnerable for a couple seconds. How does he have it?"
      ez angry "Argh. I think I need to ask someone for help."
    elif redCount == 1:
      ez angry "This is so hopeless. Although I hate to admit it, I {i}really{/i} need to ask the club for some advice."
      ez angry "At this rate, I’ll be wasting all my time bumping into the same problem over and over again."
      ez flat "There has to be {i}someone{/i} who knows what to do."
    elif redCount == 2:
      ez angry "Okay, now I’m just being stupid and stubborn."
      ez angry "Why am I diving into the dungeon when I know I can’t kill the boss without some sort of help?"
      ez sad "Me and my pride…"
      
    $ redCount += 1
    #call endRun
    call screen dungeon_run()
    
label afterFirstBattle:
  scene expression DungeonScene()
  "YOU WIN"
  h "Congratulations, Summoner! You’ve defeated the first minion of the game. You must be brimming with pride and glee."
  h "Well, that will be short-lived, I assure you. No matter how you may try and struggle, you stand no chance of defeating {i}me{/i}!"
  h "If you still think you stand a chance, you are welcome to try! But, first, you have to get past all of my minions! *Cackling*"
  menu:
    "Get past all of his minions":
      ez happy " No problem! We can take anything you throw at us!"
      $ summonersRift.getDungeon().battle.onward()
      call screen dungeon_run()
    "I don't stand a chance":
      ez sad " He might be right. I'm not ready for this yet. I'll come back later."
      $ summonersRift.getDungeon().battle.retreat()
      call screen dungeon_run()
