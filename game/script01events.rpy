label day2_pre:

    if route == "Ezreal":
        $ voice_mc = "ez"
    elif route == "Leona":
        $ voice_mc = "le"

    scene bg black with dissolve
    "Ahhh... it's already been a day since the hacker started wreaking havoc. I feel like
     I haven't accomplished much."
    "He said something about \"unspeakable powers\" and ultimate buffs, right?"
    "Now that I think about it, the jungle monsters from Summoner's Rift did seem a bit edgy."
    "Maybe I {i}am{/i} on the right track. My spidey senses are definitely tingling."
    "... but I don't think I can do this by myself. The team was right, at least in that way.
     I mean, the virtual reality is humongous, and I can only explore so much." #edited
    "My footfalls are heavy while I make my way towards the classroom door. Part of me wishes
     it would somehow snow, even though it's in the middle of Spring." #edited
    "I grit my teeth a little bit." #added
    "It feels like I'll never get anything done at this rate — school just doesn't seem important
     right now. League of Legends is in jeopardy; I'm sure the school can understand that." #edited
    scene bg classroom day
    play music "music/bedroom.mp3" fadein 1.5
    "When I open the door, I catch the tail end of an interesting conversation." #added
    #voice "voice/day2/.ogg"
    un "—team needs to get together."
    show raka flat at right with dissolve
    #voice "voice/day2/.ogg"
    sh "We really should try to get people to join."
    show vik flat at left with dissolve
    #voice "voice/day2/.ogg"
    cy "Tsk. We don't require anyone else."
    ## This entire conversation is kinda screwed up, because the mc is already established to 
    ## be working together with the club to figure out stuff about the hacker. I'd reccommend some
    ## changes, but lines would need to get re-recorded. As is, it doesn't make much sense.
    voice "voice/day2/2" + voice_mc + "1.ogg"
    mc flat "Who are you guys talking about?"
    "As I approach, I'm greeted by Cyrus' glare and, soon after, his silent snarl. He stomps away
     and out of the room." #edited
    show raka surprised
    hide vik with easeoutright
    pause 1.0
    voice "voice/day2/2" + voice_mc + "2.ogg"
    mc surprise "Uh, does he have something against me?"
    hide raka with dissolve
    show raka flat at center with dissolve
    #voice "voice/day2/.ogg"
    sh "Ah... I'm not sure. Sorry, [name]."
    voice "voice/day2/2" + voice_mc + "3.ogg"
    mc happy "Hey, it's not your fault. Don't worry about it."
    show raka sad
    sh "..."
    voice "voice/day2/2" + voice_mc + "4.ogg"
    mc happy "So, what were you two discussing?"
    show raka surprisedblush with vpunch
    "She blushes — a glaring flush of red spreads across her face. Her hands wave frantically
     in the air."
    #voice "voice/day2/.ogg"
    sh "Uwaah... I...  do you want to join our team of hacker fighters?"
    voice "voice/day2/2" + voice_mc + "5.ogg"
    mc flat "Hacker Fighters? Is that the name of your group now? I thought it was the League of
        Legends club. Not that that's any better."
    show raka flatblush with dissolve
    #voice "voice/day2/.ogg"
    sh "U-um. It's just a temporary one while we complete Rito's quest."
    voice "voice/day2/2" + voice_mc + "6.ogg"
    mc happy "Oh! That's a pretty good idea. What's the first step?"
    show raka flat
    #voice "voice/day2/.ogg"
    sh "Well, what we've gathered so far is that the hacker is targeting the players. And he
        can't do that here, in the real world, because he doesn't know who everyone is."
    voice "voice/day2/2" + voice_mc + "7.ogg"
    mc surprise "So there must be clues in the virtual reality is what you're saying?"
    show raka happy
    #voice "voice/day2/.ogg"
    sh "Yeah! And what better way to look for them than going with a bunch of friends, right?"
    if route == "Ezreal":
        show raka surprised
        voice "voice/day2/2" + voice_mc + "8.ogg"
        mc happy "Oh, so we're friends now?"
        show raka angry with hpunch
        #voice "voice/day2/.ogg"
        sh "O-Of course not!"
        hide raka with easeoutright
        "{i}Tap, tap, tap{/i}. The sounds of her footsteps ring throughout the hallways, spreading
         the sounds of her embarrassment." #edited
        "Interesting girl. That was kind of weird." #added
    elif route == "Leona":
        voice "voice/day2/2" + voice_mc + "8.ogg"
        mc happy "Couldn't have said it better myself."
        show raka happy with dissolve
        #voice "voice/day2/.ogg"
        sh "Hehe."
        hide raka with dissolve
    scene bg black with dissolve
    pause 0.5
    jump afterschool

label preboss1:
    $ preboss_flag = True
    scene bg black
    "I swear that going through the school campus should give me {i}something{/i} about the hacker's
     whereabouts."
    "Aren't we located in the heart of Demacia, for crying out loud?" #edited, this aint piltover
    scene bg classroom day with fade
    "My fingers massage my temples as I walk into the classroom and knock right into a familiar
     face." #edited
    play music "music/bedroom.mp3" fadein 1.0
    show jayce happy with dissolve
    pause 0.3
    voice "voice/preboss1/je1.ogg"
    je "Hey, [name]! Fancy seeing you here."
    voice "voice/preboss1/" + voice_mc + "1.ogg"
    mc flat "Oops, sorry about that. Should've looked where I was going."
    show jayce happyblush
    voice "voice/preboss1/je2.ogg"
    je "Don't sweat it. You definitely look like a bundle of nerves, though."
    voice "voice/preboss1/" + voice_mc + "2.ogg"
    mc sad "Ugh, yeah. I've been hoping that I'd find a clue or two about how to track down Mr. Hacker,
        but no luck."
    show jayce angry
    voice "voice/preboss1/je3.ogg"
    je "Ah, tough. But I have been hearing rumors that might cheer you up."
    "My head does a sudden ninety degress upwards to meet his gaze. I almost want to clasp his hands
     and shake the news out of him."
    show jayce happy
    voice "voice/preboss1/je4.ogg"
    je "Heh. The look of desperation is all over your face. Fear not, for I know a secret."
    voice "voice/preboss1/" + voice_mc + "3.ogg"
    mc surprise "Are you going to share it with me?!"
    show jayce happymid
    voice "voice/preboss1/je5.ogg"
    je "Should I tell you now? Hmm. No, that'd ruin the fun."
    "I don't know why he's having so much fun dangling the juicy piece of news in front of my
     despondent expression."
    "Doesn't he care that we're so close to losing our characters and the precious world of Summoner's
     Rift?"
    hide jayce with dissolve
    show jayce happy with dissolve
    voice "voice/preboss1/je6.ogg"
    je "Do a little dance for me and I'll tell you."
    mc flat "..."
    voice "voice/preboss1/" + voice_mc + "4.ogg"
    mc flat "What?"
    show jayce happyblush
    voice "voice/preboss1/je7.ogg"
    je "Yeah. Oppa Gangnam Style — everyone knows it. I'm sure you do too."
    "God forgid I do that absolutely horrific and ridiculous dance."
    "Sayonara, Jason. That was a was of time, no doubt."
    voice "voice/preboss1/je8.ogg"
    je "Wait, wait, I was just teasing you. Don't let me obstruct you in your path to justice."
    voice "voice/preboss1/" + voice_mc + "5.ogg"
    mc flat "... So?"
    show jayce happy
    voice "voice/preboss1/je9.ogg"
    je "Okay, so I heard gossip about how some players are forcibly changing."
    voice "voice/preboss1/" + voice_mc + "6.ogg"
    mc flat "Yeah, like buffs? We already know that."
    show jayce angry
    voice "voice/preboss1/je10.ogg"
    je "No, as in physical appearances. Not just that, but there has been audio differences, too."
    show jayce happy
    voice "voice/preboss1/je11.ogg"
    je "As much as it's hilarious seeing you running around the campus, I think there's more worth
        to checking out the game."
    "Hmm. Maybe he's right. I should check out what's happening in League of Legends, what with the
     mountain of reports about bugs and glitches piling sky high."
    stop music fadeout 2.0
    scene bg black with dissolve
    pause 0.5
    jump afterschool
        
label afterdungeon:
    $ afterdungeon_flag = True
    #plays if the mc has completed the first dungeon
    scene bg classroom day
    play music "music/bedroom.mp3" fadein 1.0
    "This whole dungeon crawling thing isn't really working out." #edited
    "It's been a few days since the Hacker Fighters have attempted to uncover anything about
     the cyber terrorist, but nothing has shown up."
    "Everyone's going to lose everything. Half the week has already gone by."
    "We must be missing something."
    show rango angryclose with dissolve
    voice "voice/afterdun/gw1.ogg"
    gw "Are you an idiot? Stop with your stupid wrinkly brows. We already found a clue."
    voice "voice/afterdun/" + voice_mc + "1.ogg"
    mc surprise "You! You're... uh... who are you again?"
    hide rango with dissolve
    show rango blush with dissolve
    voice "voice/afterdun/gw2.ogg"
    gw "D-Does it matter who I am? Stop worrying about the small things and help out with
        the search!"
    show rango flat
    "I'm hit with a flash of recognition."
    "This girl must be the club member that was missing the other day!"
    voice "voice/afterdun/" + voice_mc + "2.ogg"
    mc flat "Anyways... did we?" # I would edit this to add "... did we? Did we find a clue?"
    voice "voice/afterdun/gw3.ogg"
    gw "Yeah, duh. Does battling against the red buff not count for anythiing?"
    voice "voice/afterdun/" + voice_mc + "3.ogg"
    mc flat "What? Uh, let's see. I recall he... used Zhonya's a few times."
    voice "voice/afterdun/gw4.ogg"
    gw "Which means what?"
    "She looks impatient. I look away from her glare and think for a second." #added
    voice "voice/afterdun/" + voice_mc + "4.ogg"
    mc surprise "The hacker... buffed him?"
    "Of course. Since when can mobs use active items? The girl nods in agreement." #
    voice "voice/afterdun/gw5.ogg"
    gw "Right, and that gives us a key piece of information."
    "As much as I appreciate her help, I'm not really following what's so significant about it."
    "Let's recap: the other day, when we fought the boss, he used a special skill because the
     buffed him. How?"
    show rango angry with dissolve
    pause 0.5
    voice "voice/afterdun/gw6.ogg"
    gw "... Because the hacker altered the code. C'mon, use your brain for once."
    "She read me again. How does she do that?" #added
    voice "voice/afterdun/gw7.ogg"
    gw "If he was able to manipulate the values of the character, then that means the boss came
        contact with the hacker."
    voice "voice/afterdun/" + voice_mc + "5.ogg"
    mc surprise "OH!"
    mc surprise "..." #added
    voice "voice/afterdun/" + voice_mc + "6.ogg"
    mc flat "Wait. But monsters aren't played by real people."
    show rango angrymid with hpunch
    voice "voice/afterdun/gw8.ogg"
    gw "Have you not been paying attention? Your attitude can be really annoying."
    show rango angry with dissolve
    voice "voice/afterdun/gw9.ogg"
    gw "Sometimes I wonder if you even have a brain in that thick head of yours."
    "She might be right. Kinda. Didn't red buff say something right before he died?"
    voice "voice/afterdun/" + voice_mc + "7.ogg"
    mc flat "So, you're saying that the creatures are controlled by students like you and me?" # players?
    voice "voice/afterdun/" + voice_mc + "8.ogg"
    mc flat "Or maybe they were changed {i}into{/i} monsters?"
    hide rango with easeoutright
    "She made her exit without any warning, passing by the double rows of desks that lead
     up to the sliding doors of the classroom."
    "Not even a wave of goodbye as she left."
    scene bg black
    "At least that was helpful, though. So that means we should talk to the bosses rather than just
     defeat them, huh?"
    stop music fadeout 2.0
    jump afterschool
    
label day6_afterconfession:
    $ afterconfession_flag = True
    scene bg library
    play music "music/ambient2.mp3" fadein 1.0
    "And... I'm back to the novels on the wall. I guess the comfort of these books never disappear."
    "I know the hacker won't be caught idling in hte library, but there is always something
     reassuring being surrounded by such a vast amount of knowledge in the early hours."
    "It's like I can almost hear the whipsers of the pages telling me to approach the shelves lined
     against the window."
    un "Psst."
    "... Huh? What was that?" #edited
    un "[name]."
    "Am I so desperate that I'm starting to hear voices?"
    "My hands form a fist as I slowly approach the bookcase, filled with text about \"Rito Culture\".
     This is really spooky. Are the books {i}seriously{/i} talking to me?"
    if route == "Leona":
        show vik flat at left with dissolve
        cy "Ahem."
        voice "voice/day6/" + voice_mc + "1.ogg"
        mc surprise "C-Cyrus?"
        cy "Pleasant morning."
        voice "voice/day6/" + voice_mc + "2.ogg"
        mc flat "Uh, yeah. But what are you doing here?"
        cy "I saw you pass by this morning and wanted to deliver a note."
        hide vik with dissolve
        show vik flatmid at center with dissolve
        pause 0.3
        hide vik with dissolve
        show vik flat with dissolve
        pause 0.2
        hide vik with easeoutright
        "He produces a folded white piece of paper from his pocket and quickly hands it to me. Then
         he runs off, not even giving me a chance to say thanks before he leaves."
    elif route == "Ezreal":
        show raka flat at right with dissolve
        sh "U-um..."
        voice "voice/day6/" + voice_mc + "1.ogg"
        mc happy "Oh, Sharon! A surprise seeing you here — definitely unexpected."
        show raka surprised at right
        voice "voice/day6/" + voice_mc + "2.ogg"
        sh "Huh? Why? Should I leave?"
        voice "voice/day6/" + voice_mc + "3b.ogg"
        mc happy "No, no. I didn't mean it like that. I just thought that... nothing, nevermind."
        voice "voice/day6/" + voice_mc + "4b.ogg"
        mc happy "Anyways, what brings you here?"
        with hpunch
        sh "Oh! I wanted to give you something. It's pretty important."
        show raka flatmid at right with dissolve
        pause 0.3
        show raka flat at right with dissolve
        hide raka with easeoutleft
        "A creased piece of paper with clusters of wrinkles catches my eye as she brings it forward.
         It's not long before she darts out of the glass doors of the library after shoving the note
         into my hands."
    "I bring up the piece of paper, a little bit bewildered." #added
    "\"Rito Headhear Development Error\"...."
    "Huh? I don't remember anything like tha-"
    voice "voice/day6/" + voice_mc + "3.ogg"
    mc angry "O-ow!" with hpunch
    "What in the world? How did a book just drop three shelves above me?"
    "... Now that's pretty creepy. \"The Process of Rito Headgear Engine.\" It can't be a coincidence
     that it just happened to fall after I received the note."
    "The chair I pull out lets out a small squeak as I sit down and open up the first few pages.
     My fingers dart through the sheets of paper, turning one by one, and I notice one thing: most of
     the words are blacked out."
    "Something is definitely fishy. I see diagrams and blueprints of the devices, but anything
     about the trials during development is either ripped out or marked over."
    "I finally find something on page 243. It mentions something about a mishap with a technical
     error during testing."
    voice "voice/day6/" + voice_mc + "4.ogg"
    mc flat"... Demacia hailstorm causing an unfortunate eletrical circuit disaster..."
    voice "voice/day6/" + voice_mc + "5.ogg"
    mc flat"... Young female participant casualty during procedural accident..."
    voice "voice/day6/" + voice_mc + "6.ogg"
    mc flat"... Resignation of professor and civil case trial attempt fails two years later..."
    voice "voice/day6/" + voice_mc + "7.ogg"
    mc flat"... Dr. Rev-? His name is crossed out, weird."
    "Well, that was a startling discovery. I wonder what it means, though."
    scene bg black
    stop music fadeout 2.0
    pause 0.5
    jump afterschool
    
label day7_pre:
    scene bg fountain
    if route == "Ezreal":
        voice "voice/day7/" + voice_mc + "1.ogg"
        ez sad "Sigh... the day's drawing near."
    elif route == "Leona":
        voice "voice/day7/" + voice_mc + "1.ogg"
        le sad "Sigh... the day's drawing near."
    "The day to do or die is coming, quite literally. I mean... it's today. I'm on league in the morning
     to get my mind in the right mood."
    "If the crew and I don't figure out the culprit behind this prank, we're screwed."
    "BZZT." with hpunch
    "What was that?"
    scene cg hackerlogo
    h "Hello? Is this thing working?"
    h "Just kidding~! Of course it is, and all you precious little scrubs are
       staring straight into my screen!"
    h "A lovely date with League is well overdue, so I'll be taking it out for lunch. With me.
       {i}Permanently{/i}."
    h "AHAHA!"
    h "Oh, but don't worry. You can have your tear-jerking goodbye soon. I'll let you have
       your moment of boo-hoos later today."
    h "I'm not {i}that{/i} evil. I may be a villain, but I have a heart. Keke."
    h "After all, I get to see everyone's face smothered in snot and tears as the game comes
       crashing down."
    h "Here's to officially greeting all your summoners in the \"Fields of Justice\"!"
    "That entire message was so sudden that I stumble on the stone outline of the fountain
     and fall onto the corner of the cement statue."
    "So, it's really happening? Doomsday is today?"
    "A horrible feeling grabs hold of the pit of my stomach and I begin to feel nausea
     overwhelm my body."
    "BZZT." with hpunch
    h "And one more thing: I've given you all a farewell gift. Come by in the evening to unwrap
       the surprise I've prepared!"
    "Wait, he'll be here? Is this our chance to finally get rid of the hacker?"
    "I'd better not miss it! Time to give him a piece of my mind."
    jump afterschool
    
label day8:
    scene bg black
    if bosses_defeated == 3: # hacker is dead
        pass
    else: # we didn't save league of legends
        pass
    ### TEMPORARY HEARTFELT SHIT FROM US. YEAHHHH. #
    scene bg black
    un "H-Hello!"
    un "Over here!"
    un "We're the developers of Summoner Sweetheart."
    un "You've reached the end of the game!"
    un "Um, if there were any troubles... sorry."
    un "We tried really hard to get everything in."
    un "Buuuuut... yeaah..."
    un "Still, I hope you enjoyed our game, whether you were able to beat the hacker or not!"
    un "... if you did, I really have no idea how..."
    un "*ahem*"
    un "Really, from the bottom of our hearts, thank you for downloading this game after the 
        stupid amount of delays, and for supporting us by doing so!"
    un "What started out as something that was supposed to be a one-month project ended up to be
        something a biiiit more than we could all handle."
    "Kevin" "{s}Especially the dungeon.{/s}"
    un "Still, we're proud of it."
    un "If you ran across any bugs or crashes, please let us know so that we can fix them as soon
        as possible!"
    un "I know you were expecting a real ending, and, well, I think that we'll get to it!"
    un "But for now, please accept our apologies and heartfelt thanks that you actually bothered to play
        this game in the first place."
    un "Really. Thank you."
    un "I'd put up an image of all of us smiling really big if I had one. But I don't."
    un "That said... congratulations once again!"
    un "Back to the title screen with you! If you stay any longer I might cry..."
    un "Bye-bye! Thank you!"
    return