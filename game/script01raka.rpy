######################################### EVENT DECLARATION
init:
    $ event("raka_1", "act == 'library'", event.once(), "route == 'Ezreal'", priority = 191)
    $ event("raka_2", "act == 'vr'", event.once(), event.depends("raka_1"), "period == 2", priority = 181)
    $ event("raka_3", "act == 'library'", event.once(), event.depends("raka_2"), "period == 1", priority = 171)
    #$ event("raka_3B", "act == 'class'", event.once(), priority = 165)
    $ event("raka_4", "act == 'vr'", event.once(), event.depends("raka_3"), priority = 161)
    $ event("raka_5", "act == 'vr'", event.once(), event.depends("raka_4"), "period == 2", priority = 151)
    $ event("raka_6", "act == 'park'", event.once(), event.depends("raka_5"),"day == 7", "period == 2", "raka_rp >= 70", priority = 141)

######################################### SORAKA SCRIPT

label raka_1:
    $ raka_scene = 1
    $ renpy.block_rollback()
    scene bg library
    # Real world
    "I walk to the library, hoping that I could find some information about 
     the hacker."
    show raka happy at right with dissolve
    "However, soon after I enter, I notice Sharon sitting in one of the chairs,
     reading what looks like a paperback novel."
    "She doesn’t seem to have noticed me, and I can’t decide if I should get 
     her attention..."
    "Sharon is probably one of the most reserved club members. Most of the 
     time, she just sits around reading, eating, and generally not talking to 
     anyone."
    "She appears perfectly content with that, but I wonder if she really is."
    "Regardless of her shy nature, she is usually pretty friendly, helping people
     whenever possible."
    "In fact, Sharon is, in my mind, rather innocent. She's the kind of person 
     you would expect to be a nurse - working hard behind the scenes just to 
     help people in need."
    "Her character, Soraka, is the same - a healer. Though, unlike Sharon, 
     Soraka is anything but shy - almost like what she wants to be."
    "Maybe she's discovered something about the hacker that she's too shy, or 
     humble, to tell us. I resolve to walk over and find out."
    hide raka with dissolve
    show raka happy at center with dissolve
    mc happy "Hi, Sharon, how’s it going?"
    
    #intentionally no voice file
    sh "..."
    
    mc surprise "Sharon?"
    show raka surprised with hpunch
    
    voice "voice/raka/1/so_scene1_1.ogg"
    sh "OH! Hi, [name]! I was kind of absorbed in this book."
    
    mc happy "What is it that you're reading?"
    show raka happy with dissolve
    voice "voice/raka/1/so_scene1_2.ogg"
    sh "Oh! Um, uh... Nothing really! Sorry for not seeing you." 
    
    "She slides the book under her. Looks like she really doesn't want anyone 
     to know what's written on that cover."
    
    voice "voice/raka/1/so_scene1_3.ogg"
    sh "So, uh... what did you want?"
    
    mc happy "I'm just wondering if you found anything concerning the hacker."
    show raka surprisedblush
    voice "voice/raka/1/so_scene1_4.ogg"
    sh "You're asking me? D-Do you really think I can help?"
    "Once again, she picks up the book but only to cover her face. She sure is shy."
    "I slowly lean forward to grab the book and lower it just enough to look at her 
     exquisitely bright eyes. They look almost panicked."
    mc flat "I don't see why not. You're just as capable as the rest of us."
    voice "voice/raka/1/so_scene1_5.ogg"
    sh "But, I'm just a healer... I can't really battle the hacker that well..."
    mc happy "You can still provide support. And, it looks like you know your way around 
        research. You could be more of a help than you think."
    show raka flat
    voice "voice/raka/1/so_scene1_6.ogg"
    sh "Really, I'm not that great... you're just trying to flatter me!"
    mc happy "I'm serious. Everyone says you're a really diligent worker, and I 
        completely agree. We need someone with your organizational skills, 
        something the team lacks."
    mc happyblush "Not to mention, you started the game just a few weeks ago, right? Now you're 
        level 30 with a ranked team at Platinum level!"
    show raka sad
    voice "voice/raka/1/so_scene1_7.ogg"
    sh "No, no. My skills are only a fluke and I would only bring the team down. You 
        shouldn't rely on me... {i}especially{/i} for hacker hunting." 
    
    mc happy "If anything, your dedication speaks true to how hard working and caring you 
        are about the game."
    
    voice "voice/raka/1/so_scene1_8.ogg"
    sh "I... I don't understand why you say all these nice things about me. I'm not 
        as good as you think." 
    
    mc happy "To top it all off, your character is so unique. I wouldn't think you'd have 
        designed her."
    show raka surprisedblush with dissolve
    pause 0.3
    voice "voice/raka/1/so_scene1_9.ogg"
    sh "Wait. You... you actually {i}like{/i} Soraka? What do you even 
        {i}mean{/i}?" #Surprised 
    "Sharon blushes, hiding her face in her hands."
    
    mc shyblush "Don't get the wrong idea. It's just..."
    $ renpy.block_rollback()
    menu:
        "She's really cute.":
            $ renpy.block_rollback()
            mc happy "Actually, I think she's pretty cute. Definitely well-crafted and lots 
                of thinking was put into it."
            show raka flatblush
            voice "voice/raka/1/so_scene1_10.ogg"
            sh "Stoooop! This is so embarrassing!"
            
            mc flat "What's so embarrassing about it? I definitely give kudos to 
                your character."            
            show raka angry
            voice "voice/raka/1/so_scene1_11.ogg"
            sh "Look, just... promise me you won't talk to me in the game. I'd 
                prefer not to play with people I know."
            mc surprise "What? Why?"
            show raka sad with dissolve
            pause 0.3
            voice "voice/raka/1/so_scene1_12.ogg"
            sh "I, I just don't like it, okay?" 

            mc flat "Do you not like the people at school?"
            show raka surprisedmid with dissolve
            voice "voice/raka/1/so_scene1_13.ogg"
            sh "Oh, no... no, nothing like that. It's just... I'm so clumsy, 
                and a klutz, and a total failure... Ahri is way better at being 
                more useful!"
            mc surprise "Ahri? But she has nothing to do with this."
            show raka sad with dissolve
            "I'm not quite sure why Sharon is so flustered at being asked to help. 
             She {i}is{/i} a club member, afterall."
            
            voice "voice/raka/1/so_scene1_14.ogg"
            sh "Ah - I'm sorry. I didn't mean to make you angry. If you need my help, 
                I'll try to be of assistance somehow." 
            
            mc flat "O-Okay... if you say so."
            
            "Not wanting to disturb the rest of her reading, I walk away from the 
             chair. She furtively pulls out her book and goes back to reading."
            hide raka with dissolve
            "That conversation was definitely odd to say the least."
            $ raka_rp = raka_rp + 11
            pause 0.5
            stop music fadeout 2.0
            jump events_end_period
            
        "I didn't mean it that way.":
            $ renpy.block_rollback()
            mc happy "Hey, I like her, but I don't... LIKE like her..."
            
            voice "voice/raka/1/so_scene1_15.ogg"
            sh "Oh... you don't? Phew... I was kind of scared for a minute there."
            show raka happy
            mc happy "You don't have to be scared. I'm sure you would do fine in helping 
                the team {i}and{/i} in romance."
            show raka surprised
            voice "voice/raka/1/so_scene1_16.ogg"
            sh "Oh, no... no, I'm really bad at that. I'm so clumsy, and a klutz, and 
                a total failure... Ahri is way better at that stuff than me!"
            
            mc happy "You seem perfectly capable to me. At least, when I see you in game."
            show raka sad with dissolve
            voice "voice/raka/1/so_scene1_17.ogg"
            sh "I have to try so hard not to break character, though. I don't want to 
                embarrass everyone by doing something stupid."
            
            mc flat "And that's exactly why we need your help! Your serious aptitude and 
                diligence is really commendable."
            mc happy "Just give it a shot... maybe it'll work out fine."
            show raka happy with dissolve
            voice "voice/raka/1/so_scene1_18.ogg"
            sh "O-Okay... thanks. I'll try to find some information on past hacking 
                attacks... but it probably won't help much. Hehe."
            show raka surprisedblushmid with dissolve
            pause 0.5
            show raka surprisedblush with dissolve
            "My hands slightly ruffle her hair before I turn around to head out."
            mc happy "Hey, don't sweat the small stuff. Things like flaws - everyone has 
                them; no one is perfect. I hope to see you in Summoner's Rift, nonetheless."
            show raka sad with dissolve
            pause 0.3
            voice "voice/raka/1/so_scene1_20.ogg"
            sh "M-mm..."
            
            "Her head does a slow nod, very cautiously. She only utters a weak 
             confirmation as I notice her looking away."
            "Not wanting to disturb the rest of her reading, I walk away from the chair. 
             She furtively pulls out her book and goes back to reading."
            $ raka_rp = raka_rp + 8
            pause 0.5
            stop music fadeout 2.0
            jump events_end_period

label raka_2:
    $ raka_scene = 2
    $ renpy.block_rollback()
    # Virtual world
    scene bg fountain
    "After entering the game, I see a familiar figure in the moonlight. Her streaks of 
     white hair illuminate under the luscious, dark sky."
    "Although it may just be a virtual reality, the orange-tinted field leaves a 
     wonderfully whimsical atmosphere. My eyes can't help but be glued to the twinkling 
     scenery."
    "I nearly get caught up in that entrancing feeling, until I hear a familiar voice 
     echoing throughout the otherwise silent space."  
    show raka vr flat with dissolve
    voice "voice/raka/2/so_scene2_1.ogg"
    so "The power of the stars guides me..."
    
    voice "voice/raka/2/so_scene2_2.ogg"
    so "I am one with the universe. I shall banish the hatred in their hearts, lest it-"
    ez happy "Hey! How ya doin'?"
    show raka vr surprised with hpunch
    pause 0.2
    show raka vr angry with dissolve
    voice "voice/raka/2/so_scene2_3.ogg"
    so "What knave dares interrupt my meditation ritual?"
    ez happy "I have to say, this is pretty relaxing. I like what you've done with the place. 
        The night sky really brings out the accents in the, uh, grass."
    voice "voice/raka/2/so_scene2_4.ogg"
    so "Is that so? Well, I have no time to sit here for idle chatter. I must finish my 
        incantations to replenish my mana and support my comrades."
    ez happy "What about something that isn't so idle, then? Like, a battle!"
    voice "voice/raka/2/so_scene2_5.ogg"
    so "I am not in the mood for battling. I must finish my meditation."
    ez flat "But you just said you need to help your friends. That's not going to happen 
        with you just sitting here."
    show raka vr angrymid with dissolve
    voice "voice/raka/2/so_scene2_6.ogg"
    so "\"Just sitting here\"?! How offensive! I am performing a sacred ritual that 
        will heighten my senses."
    ez flat "Sounds more like an excuse to me."
    pause 0.5
    hide raka with dissolve
    show raka vr angry with dissolve
    voice "voice/raka/2/so_scene2_7.ogg"
    so "Are you planning on interrupting my entire ceremony? Grrr... Your crimes will catch 
        up with you, Ezreal."
    
    ez surprise "Uh... Is that a... warning?"
    show raka vr angryclose with hpunch
    voice "voice/raka/2/so_scene2_8.ogg"
    so "Yes!" #Super angry
    "Holy acrimony! I had no idea Soraka could be so... exasperated. That is definitely 
     quite odd, and very out of character."
    show raka vr angry with dissolve
    voice "voice/raka/2/so_scene2_9.ogg"
    so "I mean... no, of course not! I am a child of the stars - I will not stoop to 
        your base level."
    pause 0.2
    hide raka with dissolve
    pause 0.2
    show raka vr flat with dissolve
    "She stands up, her back facing me. I can feel the rage dissipate as her shoulders 
     ease into a more relaxed position and her arms maneuver to her side gracefully."
    "I hear her breathing in a rhythmic tempo. One, two, three... Maybe she's calm now?"
    
    ez happy "So~ you done there, missy?" #Slightly playful
    show raka vr angrymid with dissolve
    "Her body becomes so stiff that streams of energy start pulsating along her body and 
     her tattoos begin glowing a soft red color."
    show raka vr angry with dissolve
    "Man, I am {i}really{/i} bad at this whole talking with girls thing."
    
    voice "voice/raka/2/so_scene2_10.ogg"
    so "Hrgggk... You..."
    
    ez surprise "Whoa! Look, I'm sorry! I didn't mean to interrupt your whole ... routine thing. 
        I'll leave, so you can go back to it."
    
    voice "voice/raka/2/so_scene2_11.ogg"
    so "Why can't you just understand... You're just like everyone else..."
    
    ez surprise "Huh? Everyone else? There's no one here but us."
    
    voice "voice/raka/2/so_scene2_12.ogg"
    so "It's a figure of speech, stupid."
    "Something tells me that she's not being entirely truthful. Obviously, she's upset 
     at Nashor-knows-what."
    ez flat "Want to tell me what's on your mind? We've got all the time in the world."
    show raka vr sad
    "Uh oh. Her trembling is definitely a sign that I messed up. Again."
    voice "voice/raka/2/so_scene2_13.ogg"
    so "I-I can't... I won't... WAAAAAH!"
    ez surprise "Wait, wait - don't cry! I was just kidding!" with hpunch
    ez surprise "Do you want me to leave?! Or stay? Maybe I can grab some pot-"
    show raka vr angry
    voice "voice/raka/2/so_scene2_14.ogg"
    so "I'm... not crying... I am a b-bold warrior of... the heavens!"
    ez happy "Right! A perfect example of a courageous champion across the lands of Runeterra, 
        no doubt!" #Trying to console her
    
    "I have to tread carefully with this one. Best to change topics now."
    ez flat "Look, the real reason I came is - I kind of got injured in the last battle. So... 
        could you help me out?"
    
    #intentionally no voice file
    so "..."
    pause 1.0
    voice "voice/raka/2/so_scene2_15.ogg"
    so "All that trouble for a meager injury? Why did you not say so in the first place?"
    "A little sniffling here and there, and Soraka is back to her old, solemn self."
    show raka vr happy with dissolve
    "She picks up her staff, chanting some words in a mysterious language. An aura of 
     magic surrounds me, and my wounds quickly close."
    ez happy "Thanks, it's good to have someone like you to count on."
    show raka vr angry
    voice "voice/raka/2/so_scene2_16.ogg"
    so "Just for the record, I lend my aid for peace of mind, not because I want to help 
        {i}you{/i}."
    ez happy "I think that's pretty admirable. That is, you won't say no to players who are 
        hurt. Thank you."
    show raka vr flat
    voice "voice/raka/2/so_scene2_17.ogg"
    so "You are... welcome? Sigh... humans and their foolishness."
    
    ez flat "So, have you thought about what I said earlier? About helping the team?"
    show raka vr sad with dissolve
    voice "voice/raka/2/so_scene2_18.ogg"
    so "With my limited skills, I don't think I would be a good fit."
    
    ez happy "C'mon, don't tell me you never wanted to try."
    pause 0.5
    show raka vr happy with dissolve
    voice "voice/raka/2/so_scene2_19.ogg"
    so "Perhaps another day. Right now, I must complete this meditation if I wish to 
        attune my powers."
    
    ez surprise "Wait a second... that's weird. You have enough mana to join us, and then some."
    show raka vr angry
    voice "voice/raka/2/so_scene2_20.ogg"
    so "I simply do not feel like helping."
    $ renpy.block_rollback()

    menu:
        "The team needs you!":
            $ renpy.block_rollback()
            $ soraka_confession_pts = 1
            "Why won't she help? There are only so many explanations to give..."
            ez angry "You can't just wait here while people are getting hurt! You have to go and 
                help them!"            
            voice "voice/raka/2/so_scene2_21.ogg"
            so "Sometimes, people just have to learn to help themselves."
            ez angry "That doesn't sound like you at all. You used to run into battle to save 
                people."
            
            voice "voice/raka/2/so_scene2_22.ogg"
            so "Please; let us not discuss this matter further."            
            ez angry "We have to discuss it further! How are we supposed to be a club if we all 
                go off and do our own thing?"  
            show raka vr surprised
            voice "voice/raka/2/so_scene2_23.ogg"
            so "It's... it's just... I..."            
            show raka vr angry
            voice "voice/raka/2/so_scene2_24.ogg"
            so "If I can’t help those in danger right before my eyes, what makes you think 
                that I can save others, let alone myself?!"            
            ez angry "Aren't you a healer, though? Of course you save others!"
            pause 0.3
            show raka vr sad
            voice "voice/raka/2/so_scene2_25.ogg"
            so "No... I have failed as the Starchild."
            
            "What? Failed? I mean, I'm sure she can't save {i}everyone{/i} in battles, but 
             to say it like that is pretty extreme."
            
            voice "voice/raka/2/so_scene2_26.ogg"
            so "Not to mention, violence should not be dealt with such hatred in our hearts. 
                I am here only to heal and protect."
            
            ez flat "Then why don't you?"
            pause 0.5
            voice "voice/raka/2/so_scene2_27.ogg"
            so "I..."
            
            "Her voice wanders off until it becomes nothing but a muted silence. I 
             should probably stop prodding at this point."
            ez flat "Even though you're making no sense right now, I can tell you're bothered 
                by something."
            show raka vr angry with dissolve
            voice "voice/raka/2/so_scene2_28.ogg"
            so "Please, can you just go away?"
            ez surprise "Oh... uh... I'm sorry for getting you so worked up. I don't want to pry too 
                much into your... personal issues."
            pause 0.3
            show raka vr sad with dissolve
            voice "voice/raka/2/so_scene2_29.ogg"
            so "No... I'm fine. Just... leave me alone."
            
            ez flat "R-Right... uh... going now."
            hide raka with dissolve
            "Soraka's completely out of character now. What could have made her so angry 
             and upset? I probably won't be able to find out right now, so I figure I might 
             as well leave her be."
            $ raka_rp = raka_rp + 5
            
        "Fine, then.":
            $ renpy.block_rollback()
            $ soraka_confession_pts = 0
            ez flat "Fine, if you don't want to help, then, so be it."
            pause 0.3
            show raka vr sad with dissolve
            voice "voice/raka/2/so_scene2_30.ogg"
            so "Thank you for understanding. I simply don't want to... let you down."
            
            ez surprise "Why would you be afraid of that?"
            
            #intentionally no voice line
            so "..."
            
            "Her eyes don't even faze a bit as she looks away towards the misty ground."
            ez happy "Well, whatever. If that's what you want to do, then that's what you want to 
                do. I'm in no position to stop you."
            
            voice "voice/raka/2/so_scene2_31.ogg"
            so "Yes... I will just continue my meditation. Perhaps I should place 
                a \"do not disturb\" sign here from now on."
            hide raka with dissolve
            "Unsure of why Soraka is so reticient, I decide to leave her be, for fear 
             of starting an argument. It couldn't be something that important... right?"
            "In any case, I leave her where she sits and warp out of her realm."
            $ raka_rp = raka_rp + 8
    pause 0.5
    stop music fadeout 2.0
    jump events_end_period
   
label raka_3:
    $ raka_scene = 3
    $ renpy.block_rollback()
    # Library
    scene bg library
    "I decide to head to the library, figuring I might find someone familiar. My suspicions 
     are not far off the mark - Sharon is there, sitting in her usual seat."
    show raka flat at right with dissolve
    "My mind has been fixated on the events of the last time I saw her. Originally, I was 
     just going to let it go, but I've decided I can't just leave her alone."
    "Whatever her problems are, it's only going to keep eating at her if I don't intervene."
    show raka surprised at right with dissolve
    pause 0.3
    show raka flat at right with dissolve
    voice "voice/raka/3/so_scene3_1.ogg"
    sh "Oh... hey, [name]."
    mc flat "You look a little down. Anything I can do to help?"
    voice "voice/raka/3/so_scene3_2.ogg"
    sh "No... not really. I doubt you can help."
    mc happy "You'd be surprised."
    show raka angry at right
    voice "voice/raka/3/so_scene3_3.ogg"
    sh "I said, I don't need your help, okay? I'm fine on my own. There's nothing wrong. 
        Seriously."
    mc flat "I'm in your club. I've seen you play, and how you acted back there was not you."
    voice "voice/raka/3/so_scene3_4.ogg"
    sh "It really doesn't matter. It's just a game."
    mc angry "The last I heard, you loved your character... you spent hours designing her. It wasn't 
        just a game to you, and I don't think you feel that way now, either."
    
    voice "voice/raka/3/so_scene3_5.ogg"
    sh "Yeah, well, that doesn't matter when your close friends get hurt."
    
    mc surrpise "What does that mean? Did you hurt someone close to you?"
    pause 1.0
    "Think I hit the mark. Her head turning and avoiding eyes have definitely been commonplace 
     these days."
    hide raka with dissolve
    show raka angry at center with dissolve
    voice "voice/raka/3/so_scene3_6.ogg"
    sh "[name], why are you constantly badgering me?"
    with hpunch
    mc surprise "B-badgering?! I just want to help."
    show raka angrymid with dissolve
    voice "voice/raka/3/so_scene3_7.ogg"
    sh "You can help by going far, far away. Farther than the heavens."
    mc flat "Ouch. That's pretty harsh."
    show raka angry with dissolve
    "She doesn't budge. I'm met with a bleak, grim look that almost seems to be crying for 
     help. An expression filled with a pinch of pain - or maybe regret."
    "I always thought that she was the sweetest girl in school. It's not strange to see her 
     arranging the book shelves during lunch, or watering the plants in the school garden 
     on a sunny day."
    "For her to be so gloomy and cross is a rare sight, let alone twice in a row!"
    "I wonder..."
    $ renpy.block_rollback()

    menu:
        "Why don't you let anyone in?":
            $ renpy.block_rollback()
            $ soraka_confession_pts = soraka_confession_pts + 1
            mc flat "You don't have to burden yourself with whatever you're dealing with. It's okay 
                to let someone in."
            
            voice "voice/raka/3/so_scene3_8.ogg"
            sh "As much as I appreciate you \"trying to help,\" I can handle myself pretty well."
            hide raka with easeoutright
            "Her hair swooshes left to right as she gets up and turns around to head out the doors."
            "Before she gets a chance to leave the table, my hand reaches out and grabs her 
             shoulder without thinking; it's like it has a mind of its own."
            show raka surprisedblushmid with hpunch
            voice "voice/raka/3/so_scene3_9.ogg"
            sh "Wha-what are you doing?!"
            mc sad "I know you don't want to share your troubles, but it... upsets me when you're 
                like this."
            show raka angrymid with dissolve
            voice "voice/raka/3/so_scene3_10.ogg"
            sh "...Like what?"
            
            "Again, I notice her desolate, sinopia eyes and pale face. A chilling 
             loneliness fills her aura."
            "People talked about the elegant dances she would entertain to please the 
             celestial beings in League of Legends. I would have enjoyed seeing the 
             Sharon who once walked alongside the stars in the sky, at least in the game."
            "But today, she's not here. Not even a glimpse of the peaceful and 
             affectionate girl she was."
            mc flat "You ask for help, but you don't accept it when it's there."
            show raka angryclose with hpunch
            voice "voice/raka/3/so_scene3_11.ogg"
            sh "When did I ever say that?!"
            mc sad "I know that look - that agony. You feel alone... deserted... abandoned... 
                There's no one to turn to."
            "She winces as my words slowly slash away at her detached soul. Striking 
             against that cold wall she built for herself, I release my gentle hold of her arm."
            pause 0.5
            hide raka with dissolve
            show raka angry with dissolve
            pause 0.2
            voice "voice/raka/3/so_scene3_12.ogg"
            sh "D-don't pretend that you know me..." #Say quietly
            mc flat "I don't. That's why I want to know."
            
            #intentionally no voice line
            sh "..."
            
            voice "voice/raka/3/so_scene3_13.ogg"
            sh "Why are you... trying so hard?"
            
            "A long sigh escapes my throat as I take a quick look around the library: 
             no one is here except us and the books."
            "Is it weird to think she reminds me of myself somewhat?"
            mc happy "Because you deserve better. Everyone needs a friend."
            show raka sad with dissolve
            voice "voice/raka/3/so_scene3_14.ogg"
            sh "I... Whenever I'm around, bad things happen... And I don't want that."
            mc happy "Bad things will {i}always{/i} happen, whether you're here studying or on 
                League playing the game. You just need the courage to face them."
            
            voice "voice/raka/3/so_scene3_15.ogg"
            sh "B-but, people will seriously get hurt!"
            mc flat "A lot of the time, things like that are out of your control. Unless, 
                of course, you deliberately hurt people... but you don't seem like someone 
                to do that."
            mc happy "Like, take the hacker thing for example. It's a horrible tragedy, but 
                none of it is your fault. No one is blaming you for it."
            
            voice "voice/raka/3/so_scene3_16.ogg"
            sh "Yeah... That's true..."
            
            "For some reason, I feel a \"but\" easing its way into this conversation."
            
            voice "voice/raka/3/so_scene3_17.ogg"
            sh "But, what if for some reason, that hacker has a... good reason for being, 
                I don't know, evil?"
            
            "Right on the money."
            mc flat "I don't think there ever is a good reason for someone to hurt others."
            show raka flat with dissolve
            voice "voice/raka/3/so_scene3_18.ogg"
            sh "I see..."
            
            "At least the silence this time isn't as suffocating. She doesn't hate 
             my guts, or not as much."
            "I look up at the clock as soon as she does. It is getting pretty late, I admit."
            voice "voice/raka/3/so_scene3_19.ogg"
            sh "Well, gotta go - see ya, [name]."
            mc surprise "Wait, what?! Just like that?"
            "Sharon, surprisingly, walks out of the library to read somewhere else. By the 
             time I leave myself, she is gone."
            mc flat "Hmm... well, whatever."
            $ raka_rp = raka_rp + 6
        
        "Let's play a game.":
            $ renpy.block_rollback()
            $ soraka_confession_pts = soraka_confession_pts + 0
            mc happy "Hey, I have an idea. Let's play a game."
            voice "voice/raka/3/so_scene3_20.ogg"
            sh "A... game?"
            mc happy "Yeah! Have you heard of 20 Questions? It's where you think of an object and 
                the other person asks yes-or-no questions until he or she knows what it is."
            voice "voice/raka/3/so_scene3_21.ogg"
            sh "... Um, do we really have time for th-"
            mc happyblush "Don't worry! What's it gonna hurt to have a little fun? Loosen up a little, y'know?"
            voice "voice/raka/3/so_scene3_22.ogg"
            sh "O-Okay..."
            mc happy "I'll go first! And I'll give you a hint, being the nice guy I am."
            "I stroke my chin while looking up at the holes in the ceiling. A couple of 
             pencils are pinned against the lights, and I see a little crack in one of the tiles."
            mc happy "So, the person I'm thinking about is someone who I treasure a lot. Now, ask away!"
            show raka flat
            voice "voice/raka/3/so_scene3_23.ogg"
            sh "Let's see. Is it a girl?"
            mc surprise "... ... Yes."
            "Oh, crap. This isn't going the way I want it to."
            voice "voice/raka/3/so_scene3_24.ogg"
            sh "Your... girlfriend, perhaps?"
            mc happy "A friend who is a girl, yea, but not in a romantic way. Impossible."
            voice "voice/raka/3/so_scene3_25.ogg"
            sh "So you don't have feelings for her. Then... is she family?"
            mc happy "Hmm... you sure know how to pick the questions. She's family for sure, 
                but definitely not blood related."
            show raka surprised with dissolve
            pause 0.2
            show raka flat with dissolve
            "Sharon gives me the \"this-is-impossible\" stare. I know, I know, it sounds 
             pretty confusing, but I just tell her that I know she'll get it... through 
             telepathy, of course."
            mc happy "Wait, let me make this a little easier. This \"person\" isn't really 
                flesh and bones."
            show raka surprised with hpunch
            voice "voice/raka/3/so_scene3_26.ogg"
            sh "W-wha?! Is she like an animal? No, wait. They have bones... An insect, 
                maybe?! ...Do they have bones?" #Sound unsure near the end / almost whispering "Do they have bones?"
            
            mc happyblush "Pffft-- AHAHA! That was the cutest thing you've said since this whole 
                hacker disaster."
            show raka surprisedblush with dissolve
            voice "voice/raka/3/so_scene3_27.ogg"
            sh "C-c-cute?! I'm not..." #Mad blush
            show raka happy with dissolve
            "Man, now {i}that{/i} is a sight for sore eyes. With her face always 
             burrowed in frowns and angry wrinkles lately, I wondered if she forgot how 
             to smile. Glad to see I'm wrong."
            mc happy "Hehe. Anyways, do you give up?"
            show raka angry with dissolve
            voice "voice/raka/3/so_scene3_28.ogg"
            sh "Hnnng... No! Not yet, just one more question."
            "I give her a daring look, one brow raised and the other squished right 
             above my eye. Hit me with your best shot, Sharon!"
            show raka happymid with dissolve
            voice "voice/raka/3/so_scene3_29.ogg"
            sh "Oh, oh! Is it an alien? Or maybe even a celestial being?! That would be 
                totally cool."
            mc happy "Uhhh, I can't tell if you're joking... but either way, you're 
                actually pretty close."
            show raka happyclose with dissolve
            voice "voice/raka/3/so_scene3_30.ogg"
            sh "I know! It's a robot, isn't it?"
            "Her investigative skills are spot on. Now, if only I can get her to help us 
             catch the hacker in the actual game."
            mc surprise "Yeah. Wow, you're really good at this."
            show raka happy with dissolve
            voice "voice/raka/3/so_scene3_31.ogg"
            sh "Ehe~ I do like deductive games."
            mc happy "And now it's your turn, Nancy Drew."
            
            voice "voice/raka/3/so_scene3_32.ogg"
            sh "Wait! Before that, tell me more about this robot of yours. I want to hear 
                about your best friend."
            mc happy "Well, what's there to say? She's always been there for me since my 
                parents are always traveling."
            
            voice "voice/raka/3/so_scene3_33.ogg"
            sh "Cmon, there has to be more than that. Where did she come from? 
                What's her name?"
            
            "When did this suddenly turn into an interrogation... for me?!"
            mc happy "Her name is Pearl, and I just happened to know a little bit about 
                AI stuff. Then, poof! She was born."
            
            voice "voice/raka/3/so_scene3_34.ogg"
            sh "Poof?! Haha, that's a weird way of putting it."
            
            mc happy "My father is a big fan of exploring and seeing the unknown, so when 
                they're gone, she keeps me company. I'd say she can even read my mind!"
            show raka surprised with dissolve
            voice "voice/raka/3/so_scene3_35.ogg"
            sh "Wow... She sounds like someone I knew."
            "Sharon adamantly twiddles her thumbs as she looks at the table behind me. 
             Actually, they look like they're staring off into another world."
            show raka happy with dissolve
            pause 0.3
            voice "voice/raka/3/so_scene3_36.ogg"
            sh "Anyways, thanks. That was fun!"
            mc happy "It's no problem. As you can see, I'm willing to go great lengths for 
                a lady in need."
            
            voice "voice/raka/3/so_scene3_37.ogg"
            sh "Hahaha... you're one of the weirder people I've ever seen."
            mc happyblush "If you're happy, I'm happy."
            
            voice "voice/raka/3/so_scene3_38.ogg"
            sh "That's so cheesy!"
            
            "We both take a seat as our laughter grows and rings across the empty 
             but peacful halls."
            pause 0.3
            show raka sad with dissolve
            pause 0.3
            voice "voice/raka/3/so_scene3_39.ogg"
            sh "Um... [name]? This is only a \"what if\" type of question, but..."
            mc surprise "...? What is it?"
            pause 1.0
            show raka happy with dissolve
            voice "voice/raka/3/so_scene3_40.ogg"
            sh "...Actually, never mind. I hope we can find the hacker soon!"
            mc flat "Ah, um, yeah... see ya later, then!"
            hide raka with dissolve
            "For some reason, the smile on Sharon's face seems bittersweet as I see her 
             off. I just can't understand her, but I think today is a start."
            mc surprise "Ah!"
            "I totally forgot. She didn't let me guess her most important person."
            "Oh, well... I guess that's a tale for another day. I'll go and catch up on 
             some homework."
            $ raka_rp = raka_rp + 12
            
    pause 0.5
    stop music fadeout 2.0
    jump events_end_period
    
label raka_3B:
    $ renpy.block_rollback()
    $ raka3B_flag = True
    scene bg classroom day
    play music "music/bedroom.mp3" fadein 1.0
    "With all the other students exiting the classroom, I'm about to do the same 
     until I bump into someone right outside the door."
    show raka sad at right with dissolve
    mc happy "Oh, hey Sharon!"
    "She stands there, head low and looking at her feet, which are doing this 
     oddly charming tap dance with all the fidgeting."
    hide raka with dissolve
    show raka sad at center with dissolve
    mc flat "What's up? Are you just going to block the door or step inside?"
    show raka surprised with hpunch
    voice "voice/raka/3/so_scene3_41.ogg"
    sh "Uwahh! Sorry! I didn't mean to get in your way."
    show raka flat
    mc happyblush "Haha, I'm just teasing."
    "I pat her head enough times to make her hair clunk up into a hairball that a 
     cat coughed up. We head over to my seat and she stays standing as I perch 
     onto my table."
    show raka sadmid with dissolve
    voice "voice/raka/3/so_scene3_42.ogg"
    sh "Umm... [name]? Let's say you had a friend, a friend who put all their trust 
        in you. They make a promise with you, and then you break it."
    voice "voice/raka/3/so_scene3_43.ogg"
    sh "Do you think they would forgive you? Even if what you did was terrible... 
        unforgivable?"
    mc surprise "Most friends probably wouldn't. But, I think that a true friend would 
        forgive you. To err is human, you know?"
    show raka surprisedmid with dissolve
    pause 0.2
    voice "voice/raka/3/so_scene3_44.ogg"
    sh "You... you really think so?"
    mc happy "A real friend sees your flaws, they don't just stay with you until you mess 
        up. People make mistakes... that's real life."
    mc happy "You just have to accept that and keep moving. Life is more than atoning for 
        your mistakes - you can use that energy to do something positive."
    pause 0.3
    hide raka with dissolve
    show raka happy with dissolve
    pause 0.3
    voice "voice/raka/3/so_scene3_45.ogg"
    sh "Thanks... I think that helped. You're a good friend, too, [name]."
    "Soraka smiles at me, and I can't help but blush. I awkwardly stumble backwards, 
     almost disturbing a pile of books that was on the desk next to mine."
    mc happyblush "Aww, shucks... I didn't mean it that way, I was just giving advice."
    "She walks up towards the sliding doors of the classroom but stops the moment 
     before she leaves."
    show raka happy
    voice "voice/raka/3/so_scene3_46.ogg"
    sh "Thanks for... not giving up on me as well."
    hide raka with easeoutright
    "And with that, she makes her goodbye and the tips of her hair sneak a peek 
     through the windows as she turns and takes off."
    "That was certainly a surprise - a pleasant one."
    $ raka_rp = raka_rp + 6
    pause 0.5
    stop music fadeout 2.0
    return

label raka_4:
    $ raka_scene = 4
    $ renpy.block_rollback()
    # Bedroom
    scene bg bedroom day
    "Alriiiight~ I'm feeling like another solo queue adventure up my sleeve. I can 
     sense it; it's my lucky day!"
    "I have to catch up with all the others. Joining the school during the middle 
     of the year really pushed me back. A lot of people have been recruited to teams 
     or even professional schools!"
    "There have been rumors that Ami is shooting for Cloud 9 Uni. That girl is 
     over-the-top ambitious. I'd be happy to have one of their members so much as 
     bat an {i}eyelash{/i} at me."
    "Challenger League... everyone's dream, but only a handful live that reality."
    mc flat "..."
    "You know what? I change my mind - I'm going to go on a journey to find that 
     perfect duo partner. We can aim for the top together!"
    # Change location - Virtual Reality
    scene bg fountain with fade
    "After entering Summoner's Rift, I patrol the fountain looking for anyone who 
     shows the slightest bit of synergy with me."
    show jayce vr happy at left with dissolve
    pause 0.2
    hide jayce with dissolve
    "There's Jayce, but he likes to show off his muscles as much as he likes to 
     admire himself in the school bathroom... which is a lot. Trust me."
    show rumble vr flat at right with dissolve
    pause 0.2
    hide rumble with dissolve
    "Rumble... eh, he's cool, but overconfident. That can get pretty distracting in 
     team fights." 
    show vik vr angry with easeinleft
    hide vik with easeoutright
    "Ah, and then Viktor is over there, terrorizing those poor little Yordles 
     into hiding. Nope, not him either."
    "Guess today isn't my lucky day afterall. What a shame. I trot right over to Doran, 
     the shopkeeper, hoping he can cheer me up."
    "Actually... I'm sure he'll have a good idea of the players here! And 
     he's always so friendly to boot. Maybe he'll know the right person for me."
    ez flat "Hey, Doran! Do you possibly know anyone who's free to join me in bottom lane?"
    "Doran" "Ah, welcome, Ezreal. Soraka should be in the river already. 
             I commend her healing and tactical abilities."
    ez happy "Awesome, thank you!"
    "This is perfect. Soraka has been opening up to me more lately. I think this 
     is a great chance to talk to her more."
    show raka vr flat at left with dissolve
    hide raka with easeoutleft
    "I run off following the Northeastern winds, blowing me toward the direction 
     of the dragon pit. I hear the howls of the breeze as I approach the recognizable, 
     mauve-colored, horned character."
    ez happy "Sora-"
    "My hands cover my mouth as my feet drag me into the nearest bush. 
     What better way to surprise her then... to surprise her?! Heh."
    "I don't have time to admire the long, sparkling strands of grass, painted 
     with droplets of water because Soraka is walking towards me."
    "She's getting closer... and then she walks away... Wait! She's coming nearby... 
     Oh, and there she goes again."
    "Awful antsy, if you ask me. I wonder why she's pacing around. Her creased 
     forehead returns, along with that dreaded, worried look that I've been seeing too much."
    "I arcane shift right outta the shrubs and teleport in front of her small figure."
    ez happy "You don't look so peaceful today, Soraka. Does that mean you're ready for a fight?" with vpunch
    show raka vr surprisedclose with hpunch
    voice "voice/raka/4/so_scene4_1.ogg"
    so "Bwuaan-rrgh?!"
    hide raka with dissolve
    show raka vr surprisedblush with dissolve
    "She stumbles away from me, making a little splash on the ground as she 
     falls. A big puddle of mud blankets over her legs as they dig into the ground."
    "Oops, I forgot I was planning on surprising her... Uh... Surprise!"
    show raka vr angry
    voice "voice/raka/4/so_scene4_2.ogg"
    so "Oh my gosh – how did you get here?"
    "Her hands pat off the patches of mud and grass streaks as she gets up."
    ez happyblush "Haha, sorry – I didn't meant to surprise you, kinda. Although that scream 
        was pretty hilarious."
    show raka vr angrymid with dissolve
    "She shoots me a friendly glare that I reciprocate with a wink and a smile."
    ez surprise "Anyways, you look like something's bugging you. What's on your mind?"
    pause 0.1
    hide raka with dissolve
    show raka vr angry with dissolve
    pause 0.5
    show raka vr sad with dissolve
    voice "voice/raka/4/so_scene4_3.ogg"
    so "Sigh. Summoner's Rift is so beautiful. I'm sad that it'll be gone soon."
    
    ez happy "That's only if the hacker gets his way."
    "I wonder how many times she's shown me her face turned away. Well, this adds 
     to the count. It's like she {i}wants{/i} me to think she's the hacker."
    ez happy "Well don't just stand by and watch it happen. We can both do something 
        about it, together."
    show raka vr angry
    voice "voice/raka/4/so_scene4_4.ogg"
    so "Can't we talk about something else for once?"
    "You don't even have to tell me that she's upset. Her tone of voice is enough."
    ez flat "...Okay."
    pause 0.3
    show raka vr happy with dissolve
    "Soraka sits down on dry ground with her legs crossed and eyes closed. Her 
     arms relax parallel to each other, resting at the tips of her knees."
    "She's back to her meditation, breathing in and out. I can hear the streams 
     of air intertwine as she controls the gust enveloping around her."
    hide raka with dissolve
    show raka vr happy at left with dissolve
    "I definitely learned my lesson from last time. I join her in 
     her \"quiet relaxing\" thing that she goes on and on about. Who does it hurt, right?"
    hide raka with dissolve
    "Hmmm..."
    ez flat "..."
    ez flat "... ... *Cough*"
    pause 0.7
    show raka vr happy at left with dissolve
    "My left eye can't keep still and it opens to glance over at Soraka, who 
     hasn't moved an inch. Not even two feet away is the scuttle crab, 
     scurrying in all sorts of directions, and its antennas darting here and there."
    hide raka with hpunch
    "Oh, right! Gotta concentrate..."
    "One... Two... Ten..."
    "..."
    "ARGH! This isn't working!" with hpunch
    ez flat "Heyyy. What are you thinking about right now?"
    show raka vr happy at center with dissolve
    voice "voice/raka/4/so_scene4_5.ogg"
    so "Even the sky here is so pretty. I know it's virtual, but still."
    ez surprise "Really. I've never bothered to look up at the sky while playing, to be honest."
    voice "voice/raka/4/so_scene4_6.ogg"
    so "You'd be surprised at the things you miss when you're not paying attention."
    ez flat "Hm?"
    show raka vr surprised with dissolve
    pause 0.3
    show raka vr happy with dissolve
    voice "voice/raka/4/so_scene4_7.ogg"
    so "Uh, never mind. They should make a night mode for this place. I'd 
        like to see the stars here. Sometimes it gets too cloudy in the real world."
    ez happy "Well you know, stars are always there, even if you can't see them."
    show raka vr surprised
    voice "voice/raka/4/so_scene4_8.ogg"
    so "Huh... you're right."
    show raka vr flat
    ez flat "It's too bad the stars are too far away to explore. Unless you go to 
        space, of course."
    show raka vr happy
    voice "voice/raka/4/so_scene4_9.ogg"
    so "But you can see the sky wherever you are. So in that way, they're 
        always close by."
    "My lips curve upwards, showing off my teeth. For some reason, it's really 
     relaxing just sitting here and talking with her under the milky dark sky."
    "As we continue to admire the scenery, a party of five pass us by."
    ez happy "Hey, want to wander the Rift with me? Think about the new things we 
        could find here."
    "Soraka nods and accompanies me on our walk toward battle. In front of us 
     are the players we saw earlier."
    "Score! I have a lane partner, and it's someone I can trust. This day 
     couldn't get any better."
    ez happyblush "I've always thought about the day I would adventure with a friend by my 
        side - so much better than exploring alone any day."
    ez happy "To be honest, I was struggling to find one today, but Doran was 
        the one who told me you'd be here. He-"
    show raka vr surprised with dissolve
    "Suddenly, Soraka stops dead in her tracks, leaving me a few steps ahead, 
     confused."
    ez surprise "What? Don't worry, he didn't say anything bad about you, I promise. 
        He praised your healing skills!"
    voice "voice/raka/4/so_scene4_10.ogg"
    so "...{i}Why{/i} would he say that? Oh no, we should go back to base. 
        What if something bad happens?"

    ez angry "Hey, it's fine. I haven't seen any signs of the hacker since-"
    un "UWAARGHH!" with hpunch
    "The party of five that treaded five minutes ahead became a party of four... 
     and soon, three."
    un "W-what's happening?! My arm... it's gone!"
    un "H...half my leg disappeared!"
    "What in the world?! I've seen glitches happening that make people 
     freeze or disconnect, but never anything like {i}this{/i}."
    un "H-help..."
    ez surprise "Hang on! We're coming!"
    "Turning towards Soraka, I motion her to follow suit as I run towards the 
     struggling gamers, or at least what's left of them."
    ez angry "Are you coming?!"
    hide raka with dissolve
    show raka vr sad at left with dissolve
    "Am I going blind or... did she just shake her head? Soraka, the healer and 
     protector of Summoner's Rift, rejecting to aid those in need? Something is really wrong here."
    voice "voice/raka/4/so_scene4_11.ogg"
    so "I... I can't do this. I need to go..."
    ez angry "Wait! We need to help them. Why are you just leaving?!"
    voice "voice/raka/4/so_scene4_12.ogg"
    so "I'm so sorry, Ezreal..."
    hide raka with easeoutleft
    "The cries of the mages and marksmen just inches away from me resonate a 
     powerfully eerie sorrow that tear at my heart."
    "Their pained expressions of desperation pierce a million arrows through my 
     chest. Some of them are crying, while others are wailing in sheer horror."
    "All the while, Soraka flees in the opposite direction without turning back."
    $ renpy.block_rollback()

    menu:
        "Chase after her!":
            $ renpy.block_rollback()
            $ soraka_confession_pts = soraka_confession_pts + 1
            ez angry "Hold on!" #Calling after Soraka
            "I'm sorry, forlorn travelers... I need to get to the bottom of this - 
             whatever \"this\" is."
            "My legs run faster than they've ever ran, using arcane shift along the 
             way to boost my speed."
            show raka vr sad at left with fade
            "I finally catch up to Soraka, who's sitting at the fountain crying. Her 
             hair droops over her face, only showing bits of her tears streaming down her cheeks."
            ez flat "Sora...ka... Why... Why are you crying?" #Out of breath
            voice "voice/raka/4/so_scene4_13.ogg"
            so "Oh, Ezreal... This whole thing is a mess. No one was supposed to get 
                hurt."
            
            ez surprise "W-what are you saying? Are you-"
            show raka vr sad at center with dissolve
            pause 0.5
            hide raka with dissolve
            "Her soft, delicate fingers press against my lips to hush them. Before 
             another word slips through, she logs off and disappears into trickling pixel bits."
            "This has been the weirdest... {i}thing{/i} ever. I really need to talk 
             to her as soon as I can."
            $ raka_rp = raka_rp + 5

        "Help the poor guys.":
            $ renpy.block_rollback()
            $ soraka_confession_pts = soraka_confession_pts + 0
            "The shadow of Soraka's sprinting character leaves nothing but a trace of 
             her fading betrayal."
            "...But the howls of the helpless warriors behind me make my body tremble 
             with guilt. I can't leave them behind... like her."
            "I turn around and bolt straight towards a red-haired assassin with an 
             eye scar."
            ez angry "Hey guys, speak to me; what's wrong?!"
            "I hadn't noticed before, but now there are only two of them remaining. 
             One is clutching his throat, unable to speak."
            "The girl with the sinister blade leans against the cemented walls, 
             shaking and almost too weak to grab hold of the concrete."
            ez angry "You need to say something, or else I don't know what to do! There's 
                no time to waste!"
            "It's no use: neither of the summoners can utter the strength to reply... 
             Oh! He's mouthing words... His lips pucker into a straight line. R...\"Run\"."
            "With that, they disperse into fragments of pixelated data."
            ez flat "..."
            "This is a very... sad and unlucky day."
            $ raka_rp = raka_rp + 4
    
    pause 0.5
    stop music fadeout 2.0
    jump events_end_period

label raka_5:
    $ raka_scene = 5
    $ renpy.block_rollback()
    scene bg bedroom night
    "Earlier today might have been eventful, but I didn't do much for the rest of 
     the day. I'm still the new kid at this school, and I don't have a lot of people 
     to hang out with yet."
    "Still, it was relaxing to walk around and visit places that looked cool... 
     I guess. I just wandered around the city by myself until the sun set."
    "It's dark out now and I'm sitting in my bedroom, about to log on to Summoner's 
     Rift. I hope I meet someone cool tonight online. A classmate? Or even a new friend." 
    "I'm about to put on my headphones when I hear the doorbell ring."
    "Who could it be this late? I want to get into the game..."
    "Walking downstairs, I open the front door a crack and peek my head out. I am 
     surprised to see that it's none other than Sharon."
    voice "voice/raka/5/so_scene5_1.ogg"
    sh "Um, hey, can I come in?"
    "Part of me hesitates, remembering the... whatever happened last time. The thing 
     with the player disappearances still haunts me."
    "But, what the heck. Better to hear her story before jumping to conclusions, I guess."
    mc surprise "Sure, of course. Make yourself at home. Oh, but my bedroom's upstairs."
    "I let her into the house, and we both climb the stairs up to my room."
    "I'm surprised that shy Sharon doesn't object to hanging out in my bedroom. In 
     fact, she doesn't say anything at all. Until I open the door to my room, that is."
    show raka surprisedblush with dissolve
    voice "voice/raka/5/so_scene5_2.ogg"
    sh "Oh!"
    
    mc surprise "What's wrong?"
    pause 0.2
    show raka flat with dissolve
    voice "voice/raka/5/so_scene5_3.ogg"
    sh "That’s... a really nice window."
    
    mc flat "...Yeeeah? It came with the house when we moved in." # {A little sarcastic here.} 
    show raka surprised
    voice "voice/raka/5/so_scene5_4.ogg"
    sh "No, I mean, you can see so much of the sky in it!"
    show raka happy
    voice "voice/raka/5/so_scene5_5.ogg"
    sh "My room is too small for a window like that. I have to go outside to look at 
        the stars."
    
    mc happy "I'm sure you'll get the chance to do that when the clouds go away."
    "... Why is she talking about windows and stars? I'm sure she didn't come all 
     this way just to talk about divine things."
    "Whatever it is, she's taking her sweet time bringing it up. The only thing between her and me is this deadly silence."
    pause 1.0
    "That and the ticking of the clock in the corner of my room. Its sounds fill up more of the room than my bed - it's practically blaring through my ears."
    "Is she going to say {i}anyth{/i}-"
    show raka flat
    voice "voice/raka/5/so_scene5_6.ogg"
    sh "So, what did you do today?" # Still awkward
    mc flat "Uh, I walked around the city... on my own. I just moved to this school, and 
        I’m still finding my friends."
    show raka surprised
    voice "voice/raka/5/so_scene5_7.ogg"
    sh "Oh, is it hard moving so much?"
    mc flat "Pretty much. It's hard to leave behind the people you care about. I still 
        miss a lot of my old friends."
    pause 0.2
    show raka sad with dissolve
    pause 0.3
    voice "voice/raka/5/so_scene5_8.ogg"
    sh "I – I know what you mean."
    "Oh? Is Sharon ready to share?"
    "I turn to look her straight in the eye - I'm ready to listen to everything she 
     has to say, with an open heart."
    voice "voice/raka/5/so_scene5_9.ogg"
    sh "Actually, there's something that I wasn't telling you. That's what was really 
        on my mind."
    mc flat "Mhm..."
    voice "voice/raka/5/so_scene5_10.ogg"
    sh "I had... a really good friend. Back when they invented the VR Gear, she and I
        had volunteered to test them out."
    voice "voice/raka/5/so_scene5_11.ogg"
    sh "I promised to test them with her. But, I didn't come... I was too busy doing 
        something else. I didn't honor our promise."
    voice "voice/raka/5/so_scene5_12.ogg"
    sh "The next day, I heard that the interface had malfunctioned. She had put it on 
        by herself without supervision and... I couldn't save her."
    
    voice "voice/raka/5/so_scene5_13.ogg"
    sh "Something had gone horribly wrong. She just wasn't the same anymore. She had 
        changed. Her dad had to take her out of school."
    
    voice "voice/raka/5/so_scene5_14.ogg"
    sh "I was supposed to go there after our dance class and test it out with her... 
        But I was so selfish, I couldn't keep my promise. I wasn't there to help her."
    mc surprise "N -No way..."
    voice "voice/raka/5/so_scene5_15.ogg"
    sh "So, I feel like I'll never be good enough. No matter how hard I try to help 
        people, something bad always happens!"
    
    mc angry "Sharon, you shouldn't blame yourself. You really are helping people with what 
        you're doing. Life can be unfair, but that doesn't mean you should stop trying."
    show raka angry
    voice "voice/raka/5/so_scene5_16.ogg"
    sh "But, what's the point anymore?"
    mc flat "You shouldn't question yourself. I'm your friend, and I can tell you that you've 
        been a great help to me, and everyone here. We would be worse off without you."
    show raka surprisedblush
    voice "voice/raka/5/so_scene5_17.ogg"
    sh "R-Really? I... I..."
    show raka surprisedblushclose with hpunch
    "A huge wave of emotions sweeps me into embracing her tightly, not wanting to 
     let her go. My hands clutch her quivering arms and her head lightly collides with mine."
    pause 1.0
    hide raka with dissolve
    show raka surprisedblushmid with dissolve
    mc sad "I'm sorry. I-I don't know what to say..."
    show raka sadmid with dissolve
    voice "voice/raka/5/so_scene5_18.ogg"
    sh "It's alright. I'm just sick and tired of not doing anything anymore."
    
    voice "voice/raka/5/so_scene5_19.ogg"
    sh "That other day... when those players were reaching out for our help, I got 
        scared and I ran away..."
    "Of this entire week, Sharon has never looked as remorseful as she does now. 
     Her hands completely hide her face as her shoulders shake from her sobbing."
    "The moonlit-filled room lightens and as if on purpose, accentuates Soraka's 
     beautiful white lockets of hair, which sinks to the floor and curls along the bedsheets."
    "As if draining my energy from the elegance of the scenery, she tilts her head 
     just enough to almost illustrate her faint features as that of a pearly angel."
    mc sad "S-Sharon... you..."
    pause 0.5
    hide raka with dissolve
    show raka angry with dissolve
    voice "voice/raka/5/so_scene5_20.ogg"
    sh "I know; I won't avoid the reality anymore!."
    
    voice "voice/raka/5/so_scene5_21.ogg"
    sh "I've decided - I'm going to make things right! I've stood by for too long 
        doing nothing because I was so afraid."
    pause 0.3
    show raka happy with dissolve
    pause 0.2
    "She shows me the darn cutest smile ever, with just a tinge of mischief."
    show raka blushhappy
    voice "voice/raka/5/so_scene5_22.ogg"
    sh "We're going to apprehend that hacker... together! Hehe."
    "Sharon, the hacker hunter, is it? Why is it that she suddenly became a 
     hundred times more adorable?"
    $ raka_rp = raka_rp + 10
    $ renpy.block_rollback()

    menu:
        "Smile at her.": #REVEAL HACKER ASSISTANT = SUCCESS #JK CHANGING IT UP - KEVIN K
            $ renpy.block_rollback()
            $ soraka_confession_pts = soraka_confession_pts + 2
            pause 0.5
            show raka flat with dissolve
            voice "voice/raka/5/so_scene5_23.ogg"
            sh "Um, [name]? I have a question..."
            
            mc flat "Ask away."
            show raka sad
            voice "voice/raka/5/so_scene5_24.ogg"
            sh "If... If for {i}some{/i} reason, I... was somehow i-involved with 
                the hacker, would you... hate me?"
            
            "That came out of the blue."
            mc flat "... Hate is a strong word. No, I wouldn't hate you... but I would want 
                to know why."
            show raka sadmid with dissolve
            voice "voice/raka/5/so_scene5_25.ogg"
            sh "I-I..."
            pause 1.0
            hide raka with dissolve
            pause 0.2
            show raka sad with dissolve
            voice "voice/raka/5/so_scene5_26.ogg"
            sh "I should go. It's getting pretty late."
            
            mc surprise "Oh, right. It is."
            hide raka with dissolve
            scene bg black with fade
            "Both of us take the stairs down to the front door. I open it for her, 
             and before she leaves, she says a few words."
            
            voice "voice/raka/5/so_scene5_27.ogg"
            sh "Thanks for listening. It means a lot to me."
            
            mc happy "Of course! Any time, Sharon."
            "She nods before she makes her way out of the driveway and before long, 
             she vanishes behind the corner of Warwick Avenue."
            scene bg bedroom night with fade
            "I leave to go back to my room, thinking about what she meant by being 
             involved with the hacker... Is she?"
            "Well, no time to think about it now; I've got homework to do, and it's 
             not going to finish by itself!"
            $ raka_rp = raka_rp + 8
    
        "We’ll be partners in crime!": #DON'T REVEAL ... FAIL = NO CG ENDING #JK CHANGING IT UP - KEVIN K
            $ renpy.block_rollback()
            $ soraka_confession_pts = soraka_confession_pts + 0
            mc happy "I like the sound of that. We'll be the bot duo that he won't see coming."
            
            voice "voice/raka/5/so_scene5_28.ogg"
            sh "Hehe! Now I'm excited. Let's jump into Summoner's Rift now!"
            mc surprise "Erm... as much as I'd like to join your quest... I only have one VR 
                Gear. I didn't exactly expect company."
            show raka surprisedblush with vpunch
            voice "voice/raka/5/so_scene5_29.ogg"
            sh "O-OH! Oops... sorry. I think I should just go back home, then. But, 
                when the time comes, I'll be ready to help."
            show raka happy with dissolve
            mc happyblush "I'm down for that anytime."
            hide raka with dissolve
            scene bg black with fade
            "Both of us take the stairs down to the front door. I open it for her, 
             and before she leaves, she says a few words."
            
            voice "voice/raka/5/so_scene5_29.ogg"
            sh "Thanks for listening. It means a lot to me."
            mc happy "Of course! And thanks to you, too. See you later!" 
            "She nods before she makes her way out of the driveway and before long, 
             she vanishes behind the corner of Warwick Avenue."
            "I leave to go back to my room, dreading the mountain of homework 
             awaiting to be finished."
            "Oh, lordie. Why didn't I start this sooner..."
    if soraka_confession_pts > 2:
        $ raka_confessed = True    
    pause 0.5
    stop music fadeout 2.0
    jump events_end_period

label raka_6:
    $ raka_scene = 6
    $ raka_rp = raka_rp + 12
    $ renpy.block_rollback()
    scene bg black
    "While walking home from school, I recieve a text message on my phone from Sharon. 
     \"Come to the park at 8 PM! Meet me on the Great Lawn.\""
    "I wonder what this could be about. And, why at night? I decide not to speculate 
     until I get there, figuring it could be just about anything."
    scene bg park night with fade
    "Later that day, I get dressed again and leave, headed to the park. The nice, 
     cool breeze gently pat my face as I walk across the grassy pathway."
    show raka blushhappy with dissolve
    pause 0.3
    "When I finally do arrive, I find Sharon lying on the grass, looking up into the sky."
    "A small -thump- chimes underneath my back as I plop right on over next to Sharon. 
     The field is slightly moist, which leaves a refreshing sensation against my body."
    mc happy "You know, this reminds of something that I've always wanted to do."
    show raka surprisedblush
    voice "voice/raka/6/so_scene6_0.1.ogg"
    sh "Yeah? What's that?"
    
    mc happyblush "Traveling to faraway lands, seeing things that you can only dream of."
    show raka blushhappy
    voice "voice/raka/6/so_scene6_0.2.ogg"
    sh "I know what you mean - I want to see the heavens. Stars are so close, yet so far."
    
    mc happy "Hmm... What do you think is over there on the other side of the galaxy?"
    
    voice "voice/raka/6/so_scene6_0.3.ogg"
    sh "I'm sure tons of beautiful things exist somewhere out there. There's no way 
        of knowing, though."
    
    mc happyblush "I guess that's true. But I do know {i}one{/i} thing... If I could, 
        I would want to show you the world."
    "Even though the dark sky makes it hard to see, the sky painted its stars in 
     just the right spots to show Soraka's pink face."
    "The flush soon goes away when her eyes grow and stare off into the sky."
    mc surprise "Umm... Sharon? What exactly are you looking at?"
    
    voice "voice/raka/6/so_scene6_1.ogg"
    sh "Sssh! Wait, just a few more seconds!"
    
    mc surprise "I don't see- huh?"
    hide raka
    scene cg raka end with fade
    "To my surprise, several glowing streaks fly across the sky."
    
    voice "voice/raka/6/so_scene6_2.ogg"
    sh "See? It's a meteor shower!"
    
    mc surprise "A meteor shower!? Are you sure that's not dangerous?"
    
    voice "voice/raka/6/so_scene6_3.ogg"
    sh "No, silly... it's just a bunch of harmless rocks burning up in the sky!"
    
    mc happy "For a bunch of rocks, they sure look beautiful."
    
    voice "voice/raka/6/so_scene6_4.ogg"
    sh "You should sit here and watch! It's due to last for another half hour, anyway."
    
    mc happyblush "I think I'll take you up on that generous offer."
    "I sit down on the grass, next to Sharon, and continue looking up at the sky. 
     The breeze buffets my face as both of us sit there, peacefully."
    
    voice "voice/raka/6/so_scene6_5.ogg"
    sh "Isn't this great! Sometimes, you don't need virtual reality to see something 
        incredible."
    
    mc happy "Heh... I already knew that. In fact, I'm looking at something incredible 
        right on the ground."
    
    voice "voice/raka/6/so_scene6_6.ogg"
    sh "W-What?"
    
    "Both of us break into laughter at Sharon's surprised expression. As we 
     continue to watch the stars, she scooches closer to me."
    
    voice "voice/raka/6/so_scene6_7.ogg"
    sh "Maybe after the meteor shower ends, we could do something else." #in bed?
    mc happy "Don't worry - you can invite me anywhere, anytime. You're the kindest 
        person I've had the honor of knowing."
    
    voice "voice/raka/6/so_scene6_8.ogg"
    sh "Th-thanks, [name]. I don't think I'll ever forget you, either."
    pause 0.5
    stop music fadeout 2.0
    jump events_end_period