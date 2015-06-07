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
