######################################### EVENT DECLARATION
init:
    $ event("rumble_1", "act == 'library'", event.once(), "route == 'Leona'", priority = 191)
    $ event("rumble_2", "act == 'library'", event.once(), event.depends("rumble_1"), priority = 181)
    $ event("rumble_3", "act == 'vr'", event.once(), event.depends("rumble_2"), "day >= 3", priority = 171)
    $ event("rumble_4", "act == 'class'", event.once(), event.depends("rumble_3"), "period == 1", priority = 161)
    $ event("rumble_5", "act == 'museum'", event.once(), event.depends("rumble_4"), "period == 1", priority = 151)
    $ event("rumble_6", "act == 'museum'", event.once(), event.depends("rumble_5"), "day == 7", "period == 2", "rumble_rp >= 70", priority = 141)

######################################### RUMBLE SCRIPT
label rumble_1:
    $ rumble_scene = 1
    $ renpy.block_rollback()
    scene bg library
    "With so many club members anxious about the hacker dilemma, I take a stab at going 
     through the library."
    "I have to look for anything remotely useful to relay to the team before the sun sets
     once again ... is what I was thinking, until I catch a glimpse of Daniel."
    play music "music/ambient2.mp3" fadein 2.0
    show rumble flat at right with dissolve
    "The dazed expression he's wearing on his face kind of makes him twinkle. Maybe his 
     name should have been Edward."
    show rumble flat at center with dissolve
    voice "voice/leona/1/le_ru_scene1_1.ogg"
    mc happy "Hey, Daniel. What are you up to?"
    "Something stretched across the table catches my eye - an opened sketchbook filled 
     with doodles of random patterns."
    show rumble surprised
    voice "voice/rumble/1/ru_scene1_1.ogg"
    da "Oh, uh- drawing."
    voice "voice/leona/1/le_ru_scene1_2.ogg"
    mc happy "That's enlightening! What exactly are you drawing?"
    show rumble flat
    da "..."
    da "....."
    voice "voice/rumble/1/ru_scene1_2.ogg"
    da "The morni--"
    voice "voice/leona/1/le_ru_scene1_3.ogg"
    mc surprise "Ooh! Those triangles sort of look like the sun! And are those petals over there? 
        That's totally a flower! Wait, I think I see a little boy too."
    "Oops. I totally interrupted him. Hope he's not mad."
    show rumble flatmid with dissolve
    "Daniel looks at me with a blank face. He bats his eyes once, and then twice. He almost 
     looks surprised or confused; maybe a mix of both."
    voice "voice/leona/1/le_ru_scene1_4.ogg"
    mc happy "Was I wrong?"
    voice "voice/rumble/1/ru_scene1_3.ogg"
    show rumble happy with dissolve
    da "No. Just... amazed."
    voice "voice/leona/1/le_ru_scene1_5.ogg"
    mc surprise "Amazed? About what?"
    voice "voice/rumble/1/ru_scene1_4.ogg"
    da "Your interpretation."
    voice "voice/leona/1/le_ru_scene1_6.ogg"
    mc happy "But it really does look like that. See -- the triangles are bunched in a way that it
        looks like it's shining on the pot over here. It's brilliant."
    show rumble flatblush
    "I'm pretty sure those red streaks across his face aren't coming from the sun's glare."
    voice "voice/rumble/1/ru_scene1_5.ogg"
    da "Th-thanks."
    voice "voice/leona/1/le_ru_scene1_7.ogg"
    mc flat "Before I forget, there was something I wanted to ask."
    menu:
        "Have you heard anything about the hacker?":
            $ renpy.block_rollback()
            voice "voice/leona/1/le_ru_scene1_8.ogg"
            mc flat "Did you hear anything about the hacker thing that the club has been ranting about?"
            show rumble flat
            voice "voice/rumble/1/ru_scene1_6.ogg"
            da "Not really."
            voice "voice/leona/1/le_ru_scene1_9.ogg"
            mc flat "I was hoping to find helpful stuff in the library, like past hackers."
            voice "voice/rumble/1/ru_scene1_7.ogg"
            da "Nothing comes to mind."
            voice "voice/leona/1/le_ru_scene1_10.ogg"
            mc flat "Alright, thanks anyways. I guess I'll just look around before I head off."
            "Daniel nods and continues sketching away when I start to leave."
            voice "voice/rumble/1/ru_scene1_8.ogg"
            da "Wait!"
            da "..."
            voice "voice/leona/1/le_ru_scene1_11.ogg"
            mc flat "Yes?"
            voice "voice/rumble/1/ru_scene1_9.ogg"
            da "You should try the League of Legends section."
            voice "voice/leona/1/le_ru_scene1_12.ogg"
            mc happy "Seriously? We have something like that?! This school is so weird."
            show rumble happy
            "He flashes a quick grin at me when I turn towards that direction."
            $ rumble_rp = rumble_rp + 10
        
        "Do you like the sun?":
            $ renpy.block_rollback()
            voice "voice/leona/1/le_ru_scene1_13.ogg"
            mc flat "I know this is an odd question, but do you enjoy the sun?"
            voice "voice/leona/1/le_ru_scene1_14.ogg"
            mc happy "Personally, I think it's almost as if the sun protects you. It's there when you 
                wake up, and the sun always rises."
            voice "voice/leona/1/le_ru_scene1_15.ogg"
            mc happy "When I saw your art, it made me feel warm."
            "Daniel just looks at me, at a loss for words. He seems to be finding it difficult 
             to craft the right sentence."
            voice "voice/rumble/1/ru_scene1_10.ogg"
            da "...Yeah, I do."
            voice "voice/leona/1/le_ru_scene1_16.ogg"
            mc happy "Really? What do you like about it?"
            voice "voice/rumble/1/ru_scene1_11.ogg"
            da "The rays. They make everything feel more delicate... more \"alive\"."
            voice "voice/leona/1/le_ru_scene1_17.ogg"
            mc happy "I completely agree."
            "After a quick glance over his sketch, my impression of Daniel began to change."
            voice "voice/leona/1/le_ru_scene1_18.ogg"
            mc happy "It was really nice talking with you, Daniel. Maybe I'll see you around?"
            "Daniel only gives a nod before I head off to look for clues about the hacker."
            $ rumble_rp = rumble_rp + 2
    hide rumble with dissolve
    call gift_check("Daniel") from _call_gift_check_6
    scene bg black with dissolve
    stop music fadeout 2.0
    jump events_end_period
             
label rumble_2:
    $ rumble_scene = 2
    $ renpy.block_rollback()
    scene bg library
    "I hop on over to the library in hopes of bumping into Daniel again. Finding a way to defeat
     the hacker is on my checklist, too! I mean, that's my true intention, of course."
    show rumble flat at right
    "My lips betray a smile as I see him at the same table with the same notebook and the
     same, idle but charming gaze."
    play music "music/ambient2.mp3" fadein 2.0
    voice "voice/leona/2/le_ru_scene2_1.ogg"
    mc flat "It's definitely not a surprise seeing you here."
    show rumble happymid
    "Daniel looks up with something that hints at a tinge of joy. Maybe he's glad that I came over."
    "The chair next to him is empty, so I take the liberty to sit down. I lean over his 
     shoulder to see what he's drawing this time."
    voice "voice/leona/2/le_ru_scene2_2.ogg"
    mc angry "Hmm... I see a bit of frustration in this one. Almost like you can't speak your mind."
    voice "voice/rumble/2/ru_scene2_0.ogg"
    da "Yeah. You're quite perceptive."
    voice "voice/leona/2/le_ru_scene2_3.ogg"
    mc sad "Thank you! Though, I do get into trouble for speaking without thinking sometimes... 
        probably why I don't have a lot of friends." #sad face
    voice "voice/rumble/2/ru_scene2_1.ogg"
    da "I can see that."
    voice "voice/leona/2/le_ru_scene2_4.ogg"
    mc angry "What is that supposed to mean?! I mean, I know what it means, but couldn't you put 
        that in a nicer way?" #pouty face
    voice "voice/rumble/2/ru_scene2_laugh.ogg"
    "His laugh brings a smile to my face. It's more than pleasant."
    voice "voice/leona/2/le_ru_scene2_5.ogg"
    mc happy "Tell you what. How about you do something for me, and maybe I can forgive you for that."
    show rumble surprisedmid
    voice "voice/rumble/2/ru_scene2_2.ogg"
    da "Oh?"
    voice "voice/leona/2/le_ru_scene2_6.ogg"
    mc happy "Yeah! You need to... to draw me, and in any way, shape or form, Mr. Artist." #like one of your french girls
    show rumble flatmid
    "Without another word, Daniel buries his head into his book of art and I watch as his pencil
     dances along the edges of the paper."
    "Various swooshes and slashes make a melody that befits the air of this quiet library. It is
     in tune with the turning pages and footsteps heard on the other end of the bookshelves."
    "I almost don't notice that twenty minutes have passed since Daniel started drawing.
     I snap back to reality when Daniel sways his sketchbook in front of my face."
    show rumble happyclose with dissolve
    voice "voice/leona/2/le_ru_scene2_7.ogg"
    mc surprise "Omigosh... it's beautiful!"
    "It's like a page out of a storybook. Me, the Radiant Dawn, covered in gallant armor and 
     chosen by the sun. Daniel's use of circles, crosshatching, and lines makes it all the more impressive."
    voice "voice/rumble/2/ru_scene2_3.ogg"
    da "So, am I pardoned from my sins?"
    voice "voice/leona/2/le_ru_scene2_8.ogg"
    mc surprise "Y-Yeah, of course... at least towards me, anyway."
    voice "voice/rumble/2/ru_scene2_4.ogg"
    show rumble happyblushclose
    da "Thanks... I guess? Haha."
    voice "voice/leona/2/le_ru_scene2_9.ogg"
    mc happy "Heh. You're welcome. On another note, I should head off. You know, so I can do my \"real\" work.
        Finding the hacker and all that jazz. I need to be the hero of Summoner Academy!"
    show rumble happymid with dissolve
    voice "voice/rumble/2/ru_scene2_5.ogg"
    da "A hero... that sounds nice. Good luck!"
    "The more I spend time with Daniel, the more I feel like I don't want to leave. But leave him I do."
    hide rumble with dissolve
    $ rumble_rp = rumble_rp + 3
    call gift_check("Daniel") from _call_gift_check_7
    stop music fadeout 2.0
    jump events_end_period

label rumble_3:
    $ rumble_scene = 3
    $ renpy.block_rollback()
    scene bg fountain
    "To change the pace a little, I think going into League of Legends would be the perfect choice.
     Who knows? Maybe the hacker left an opening in the game."
    play music "music/ambient1.mp3" fadein 2.0
    "Running around the fountain not sure exactly what I should be expecting, I notice a tall -- no wait,
     he's small; like, super short, but his machine is huge!"
    "Anyway, this guy is gracing the players near the shop with his presence, waving his stubby hands
     in the air."
    show rumble vr flat at right with dissolve
    voice "voice/rumble/3/ru_scene3_1.ogg"
    ru "Hahaha! I see all of you puny humans eyeing my baby right here. Who wants a piece of this?"
    "If I recall correctly, Rumble was Daniel. Boy is his virtual persona... different to say the least." 
    voice "voice/leona/3/le_ru_scene3_1.ogg"
    le surprise "Hey, Rumble!"
    show rumble vr flat at center with dissolve
    voice "voice/rumble/3/ru_scene3_2.ogg"
    ru "Leona? Perfect timing! I want to show you what I've been cookin'. Ever looked {i}up{/i}
        to a yordle? Hehe."
    voice "voice/leona/3/le_ru_scene3_2.ogg"
    le surprise "Nope. This is pretty cool, though. What can she do?"
    voice "voice/rumble/3/ru_scene3_3.ogg"
    ru "Thought you'd never ask. Bask in all the glory of Tristy, my mech! No one will be 
        callin' me little anymore, not with her they aren't."
    voice "voice/rumble/3/ru_scene3_4.ogg"
    ru "You've gotta see this! She can blast fire through her arms, and cast harpoons at enemies
        like \"Bam!\" \"Bam!\" And, we can't forget the equalizer!"
    voice "voice/rumble/3/ru_vi_scene3_1.ogg"
    un "Oh, stop with the incessant babbling, you cretin."
    show rumble vr surprised with dissolve
    "Rumble and I turn our heads towards the direction of a mechanical figure. Most of his 
     flesh is altered to encompass artificial limbs."
    show vik vr flat at right with moveinright
    voice "voice/rumble/3/ru_vi_scene3_2.ogg"
    vi "What a waste of precious metal. When designing ultimate perfection, your creation 
        must have the utmost efficiency."
    voice "voice/rumble/3/ru_vi_scene3_3.ogg"
    vi "That worthless pile of scrap has more weaknesses in one leg than I do in my entire body." #Sigh
    show rumble vr angry
    voice "voice/rumble/3/ru_scene3_5.ogg"
    ru "Grrr! I don't see {i}you{/i} achieving anything, Viktor! Whatever happened to your
        stupid \"glorious revolution\"? Oh, right - it failed." #Mocking voice for "glorious revolution"
    voice "voice/rumble/3/ru_vi_scene3_4.ogg"
    vi "Please. None of your pitiful attempts of provocation will prompt a frivolous response from me."
    show rumble vr angrymid at left with dissolve
    voice "voice/rumble/3/ru_scene3_6.ogg"
    ru "Oh, yeah? How about we take it to the field? Then, we'll see who's the {i}real{/i} mechanical genius!"
    show vik vr flatmid at right with dissolve
    voice "voice/rumble/3/ru_vi_scene3_5.ogg"
    vi "That inferior construct is no match for me. I accept your challenge."
    "This doesn't sound good. I don't want to see Rumble hurt. Not that I think he would lose to 
     Viktor, but you never know. Or maybe he'll win?"
    menu:
        "Prevent them from fighting.":
            $ renpy.block_rollback()
            voice "voice/leona/3/le_ru_scene3_3.ogg"
            le angry "That's enough, guys! We shouldn't be fighting with each other while the hacker is still 
                out there destroying the game."
            show rumble vr flatmid at left
            voice "voice/rumble/3/ru_scene3_7.ogg"
            ru "It's okay, Leona. Everything will be over in a jiffy, but this sure is gonna be 
                a bumpy ride!"
            voice "voice/rumble/3/ru_vi_scene3_6.ogg"
            vi "Quick it will be, but painless? Doubtful. I foresee a huge blow to your colossal ego."
            show rumble vr angrymid at left
            voice "voice/rumble/3/ru_scene3_8.ogg"
            ru "As if, poser!"
            voice "voice/leona/3/le_ru_scene3_4.ogg"
            le angry "Argh! Rumble, you don't need to prove anything. Don't be misguided by Viktor's
                silly opinions."
            voice "voice/rumble/3/ru_vi_scene3_7.ogg"
            vi "Back down if you wish. Just know that it will only accentuate my point that you are
                a failure."
            "I can tell that Rumble is experiencing an internal struggle as he trades glances with me.
             I really wish I had telepathy right now."
            voice "voice/leona/3/le_ru_scene3_5.ogg"
            le angry "Tristy is a wonderful machine, and she deserves to be treated better! Show her off
                not by a battle to the death, but by being a hero and helping me catch that wretched villain."
            ru "..."
            "The rockets that were aimed at Viktor seem to deactivate and his engines begin shutting down.
             Rumble jumps on top of his suit, gently placing his hands on Tristy."
            show rumble vr flat at left with dissolve
            voice "voice/rumble/3/ru_scene3_9.ogg"
            ru "You're right, Leona. Not to mention, it would take forever to scrape Viktor's
                face off my suit!"
            "We both chuckle at his haughty comment, but the player standing across from us 
             doesn't seem to find the mood all that amusing."
            show vik vr flat at right with dissolve
            voice "voice/rumble/3/ru_vi_scene3_8.ogg"
            vi "This is why people are incompetent. They are always consumed by their emotions."
            hide vik with moveoutright
            "Viktor’s shadow is the only thing left of his presence after he trudges away from the fountain."
            voice "voice/leona/3/le_ru_scene3_6.ogg"
            le flat "Well, that was pretty exhausting. Glad that it's over, though." 
            show rumble vr flat at center with dissolve
            voice "voice/rumble/3/ru_scene3_10.ogg"
            ru "Sorry. I did warn ya that it was gonna be bumpy." 
            voice "voice/leona/3/le_ru_scene3_7.ogg"
            le happy "Heh, yeah. I have to head out now, though! I'll catch you later."
            "I locate QUIT on the menu screen and just before I click it, Rumble shoots up his rockets in
             the air engulfing the sky in red and blue glimmer and raining small drops of harmless flame."
            "Elegant art like always."
            hide rumble with dissolve
            $ rumble_rp = rumble_rp + 5
        
        "Watch the battle unfold.":
            $ renpy.block_rollback()
            voice "voice/leona/3/le_ru_scene3_8.ogg"
            le angry "You can do it, Rumble!"
            "Students push and shove as a circle soon develops around the two mechanics. Echoes 
             of cheering fill the air, enough to make the ground rumble beneath us."
            "Though violence does not always solve everything, I feel that in Viktor's case, it does."
            show rumble vr angryclose at left with dissolve
            voice "voice/rumble/3/ru_scene3_11.ogg"
            ru "I'm all revved up! Get ready for a pounding, Viktor."
            show vik vr flat at right with dissolve
            voice "voice/rumble/3/ru_vi_scene3_9.ogg"
            vi "Not that an attack from you could ever make a dent in me."
            "The exchange of words is cut short as soon as Rumble shoots a harpoon aimed at Viktor.
             The spearhead flies in the air, only to hit the base of a rock."
            "Dashing towards the huge clunk of metal before him, Viktor swiftly activates a
             shield after landing his siphon on Rumble."
            hide vik with moveoutright
            show vik vr flat at right with dissolve
            show rumble vr angry at left with dissolve
            voice "voice/rumble/3/ru_scene3_12.ogg"
            ru "Ugh! You think a little ninja star is going to hurt me?"
            "A smirk appears on Viktor's mask as he howls in the sky, summoning Chaos Storm.
             Streaks of lightning sparks in the air and erupts into an arcane singularity."
            hide rumble with moveoutbottom
            "The slithering motion of the cloud makes its way towards Viktor as it compounds
             into a mass of magical darkness. Rumble kneels on the ground, hurt. Not just him 
             - everyone around him feels the electrical damage." #ru_scene3_13 not put in because there isn't a fitting place for it
            voice "voice/leona/3/le_ru_scene3_9.ogg"
            le surrpise "No!"
            with hpunch
            "Tears blur my vision as I activate Solar Flare. A beam of solar energy 
             apprehends Viktor, prohibiting him from attacking."
            voice "voice/leona/3/le_ru_scene3_10.ogg"
            le sad "R-rumble, stay still! I will protect you."
            "But he only shoves me aside in desperation. With a trembling arm, e calls out to activate the Equalizer."
            show rumble vr angryclose at left with vpunch
            voice "voice/rumble/3/ru_scene3_14.ogg"
            "A line of flaming rockets fall from above and burst into flames, lighting the air ablaze."
            show rumble vr angry at left with dissolve
            hide vik with moveoutright
            "I heard a cry of pain, not from the yordle but from the machine herald standing 
             three feet away. He clasps his arm as surges of energy flicker out of his mechanical
             limb, now apparently broken."
            show vik vr angry at right with moveinright
            "Viktor's eyes glow a radiant yellow resembling that of the sun."
            voice "voice/rumble/3/ru_vi_scene3_10.ogg"
            vi "Now, experience the defeat that should have been bestowed to you eons ago."
            voice "voice/rumble/3/ru_scene3_15.ogg"
            "With his other synthetic arm, Viktor sends a beam of energy straight at Rumble. 
             It cuts through his whole armor, exposing the small and weakened character. 
             Rumble falls, and lands in such a way that he bows before the victor."
            hide rumble with moveoutbottom
            # line missing
            vi "AHAHAHA! Even your character in game knows of defeat."
            "His maniacal laughter leaves a ringing trail as he leaves for the dungeon. 
             I could only look at Rumble as he logs off the game. Bits of pixels disperse 
             into the air when he does."
            hide vik with dissolve
    stop music fadeout 2.0
    jump events_end_period
    
label rumble_4:
    $ rumble_scene = 4
    $ renpy.block_rollback()
    scene bg classroom day
    # (w/ Jason and Cyrus - provoking Rumble, but Leona helps him to calm down)
    "I act like I forgot my bag in the classroom, but it's just an excuse to see Daniel.
     I know that he's staying after school to catch up on his homework."
    "When I get there, though, I find an unexpected sight. Jason and Cyrus are huddled 
     over little Daniel, who seems to be overwhelmed by their height."
    show jayce happy at left with dissolve
    show vik flat at right with dissolve
    show rumble flat at center with dissolve
    play music "music/Battle Stance.mp3" fadein 2.0
    voice "voice/rumble/4/ru_vi_scene4_1.ogg"
    cy "Don't get me started on how qualified you are to be here. We all know that your
        skills are below-par." with hpunch
    "Cyrus... he always seems to be looking for the next excuse to make people miserable.
     But, why is Jason here, too?"
    voice "voice/rumble/4/ru_ja_scene4_1.ogg"
    je "I hardly ever see you study. You're always scribbling something in class.
        Sucking up might work on the teachers, but it won't fool me." with hpunch
    voice "voice/rumble/4/ru_vi_scene4_2.ogg"
    cy "For once, I agree with you. This guy is getting a free ride!" with hpunch
    da "..."
    "An alliance between the jock and the nerd: definitely an odd sight. Their mission?
     To make Daniel feel miserable and lonely."
    "The jeering laughter and echoes in the classroom create such a grim air that other 
     students begin shifting in their chairs or shutting the doors behind them as they leave." 
    "I think it's time to take matters into my own hands - that is, until Daniel beats me to the punch."
    show rumble angrymid at center with dissolve
    voice "voice/rumble/4/ru_scene4_1.ogg"
    da "You're just using me to blow off steam. Go air your problems somewhere else!" with hpunch
    show rumble angry at center with dissolve
    show jayce surprised2 at left
    voice "voice/rumble/4/ru_ja_scene4_2.ogg"
    je "H-hey! I wasn't being rude, just said it how I see it."
    hide jayce with moveoutleft
    "Jason makes an about-face, stomping past the crowd of curious juniors. It's no surprise 
     that a bevy of fangirls and admirers follow the dejected soccer star as he leaves."
    voice "voice/rumble/4/ru_vi_scene4_3.ogg"
    cy "My only \"issue\" is how much embarrassment you bring to our club with your
        buffoonish tactics. I think you should quit this game while you're behind."
    mc angry "Cyrus! Don't you think you've done enough damage? What has Daniel done to 
        deserve this harassment?"
    show vik happy at right
    voice "voice/rumble/4/ru_vi_scene4_4.ogg"
    cy "Existing, mostly."      
    "This guy... What the heck is his problem?"
    voice "voice/rumble/4/ru_vi_scene4_5.ogg"
    cy "Now, if you'll excuse me - there are more important things I have to deal with."
    "Cyrus only lingers long enough to sigh in contempt. He makes for the door, but not without a parting shot."
    voice "voice/rumble/4/ru_vi_scene4_6.ogg"
    cy "It's just plain embarrassing, needing a girl to defend you."
    hide vik with moveoutright
    stop music fadeout 3.0
    # play new song here?
    "Today has been such a downer."
    "I turn to Daniel, hoping he's been able to handle Cyrus' bullying."
    voice "voice/leona/4/le_ru_scene4_1.ogg"
    mc sad "You okay, Daniel?"
    show rumble flatclose with dissolve
    da "..."
    show rumble flatblushclose
    "His sparkling essence seems to glow around his cheeks as a flush of red engulfs his face. 
     Is he embarrassed?"
    voice "voice/rumble/4/ru_scene4_2.ogg"
    da "Yeah - don't worry about it."
    voice "voice/leona/4/le_ru_scene4_2.ogg"
    mc angry "No! I want to worry. I want to help you."
    voice "voice/rumble/4/ru_scene4_3.ogg"
    da "...Why do you care so much?"
    "That question caught me off by surprise. My feet sort of dance around each other 
     making me stumble into the desk next to his."
    "How do I answer such a delicate question?"
    menu:
        "Because I like you.":
            $ renpy.block_rollback()
            voice "voice/leona/4/le_ru_scene4_3.ogg"
            mc sad "I... I think..."
            "Daniel's eyes have this piercing stare that makes my heart flutter, as cliché
             as that sounds. But it's true!"
            voice "voice/leona/4/le_ru_scene4_4.ogg"
            mc sadblush "I like you."
            show rumble surprisedblushclose
            da "..."
            show rumble happyclose
            voice "voice/rumble/4/ru_scene4_4.ogg"
            da "Well, you're a good friend, too."
            voice "voice/leona/4/le_ru_scene4_5.ogg"
            mc surprise "No, no. Not like that. I mean, I {i}really{/i} like you."
            voice "voice/leona/4/le_ru_scene4_6.ogg"
            mc surprise "I love watching you draw, and I love... I love..."
            "Slight giggles almost escape my lips when I see Daniel make this face: a 
             face that only means he understands what I meant."
            show rumble flatblushclose
            voice "voice/rumble/4/ru_scene4_5.ogg"
            da "O-Oh..."
            "The silence that fills the room is nearly magical. Murmurs in the distance
             chime together with the chuckles of students making jokes."
            "Daniel fidgets with his notebook, flipping pages and shuffling his papers. 
             All the while, sneaking peaks at me while I stand beside him."
            voice "voice/leona/4/le_ru_scene4_7.ogg"
            mc happy "I should be going now. My duty as a hero isn't over just yet. The hacker 
                is still out there."
            "Are those looks of disappointment that I see in his gaze?"
            voice "voice/rumble/4/ru_scene4_6.ogg"
            da "Right. Don't let me keep you here, protector of justice."
            voice "voice/leona/4/le_ru_scene4_8.ogg"
            mc happyblush "Ha!"
            hide rumble with dissolve
            call gift_check("Daniel") from _call_gift_check_8
            "I wave good-bye as I head out the door, but not before stopping to glance
             back at Daniel. Although his head is hidden in his textbook, his bright red 
             ears are as clear as sunlight."
            $ rumble_rp = rumble_rp + 18
        
        "I'm not sure.":
            $ renpy.block_rollback()
            voice "voice/leona/4/le_ru_scene4_9.ogg"
            mc happy "I... I don't know. It's probably my sense of justice. I can't stand the 
                sight of others in pain."
            "Maybe I said the wrong thing, judging from how Daniel looked up at me with 
             such wistful eyes. Almost expected to see tears trickling down his cheeks."
            show rumble flatclose # there's not really a sad rumble...
            voice "voice/rumble/4/ru_scene4_7.ogg"
            da "I see."
            voice "voice/leona/4/le_ru_scene4_10.ogg"
            mc angry "With the way Cyrus treats you and everyone else, it's only a matter of time
                before he gets scolded by the teacher."
            voice "voice/leona/4/le_ru_scene4_11.ogg"
            mc angry "In the meantime, I want to do my best to prevent anyone else from getting hurt."
            voice "voice/rumble/4/ru_scene4_8.ogg"
            da "You have such a strong sense of justice."
            "Is it me or did he say that with a pinch of detachment?"
            voice "voice/leona/4/le_ru_scene4_12.ogg"
            mc flat "Thanks."
            voice "voice/rumble/4/ru_scene4_9.ogg"
            da "I should go now. This assignment's not gonna finish itself."
            hide rumble with moveoutleft
            "Daniel didn't give me a chance to say good-bye before he slipped past me.
             His hair fluttered in the air as he hurried his way out the door."
            "I hope he's not mad."
            $ rumble_rp = rumble_rp + 10
    stop music fadeout 2.0
    jump events_end_period

label rumble_5:
    $ renpy.block_rollback()
    scene bg museum day
    # (looking for inspiration. asks for 24 hours of no visits // KEY SCENE)
    play music "music/museum.mp3" fadein 2.0
    "The past few days have certainly been \"busy,\" to say the least. Art has its way 
     of giving me time to relax, especially..."
    voice "voice/leona/5/le_ru_scene5_1.ogg"
    mc flat "Daniel!"
    show rumble flat at left
    "I see him looking at the walls of portraits lined against each other under the 
     gleaming lights. I think I recognize one of them."
    voice "voice/leona/5/le_ru_scene5_2.ogg"
    mc surprise "Hey, isn't that the picture I saw at the library when I first met you?"
    show rumble surprised at left with dissolve
    pause 0.5
    hide rumble with dissolve
    show rumble flat with dissolve
    voice "voice/leona/5/le_ru_scene5_3.ogg"
    mc surrpise "I mean, I've seen you before in class and all, but that day was when I actually
        {i}really{/i} met you."
    "Daniel only looks at me with his clear, soft amber eyes, and his lips slowly curve into a smile."
    show rumble happy with dissolve
    voice "voice/rumble/5/ru_scene5_1.ogg"
    da "Say... what do you like?"
    with vpunch
    voice "voice/leona/5/le_ru_scene5_4.ogg"
    mc surprise "W-what? That was - huh? What do I like?"
    "I am completely enraptured by his presence. His silky, flowing blue hair and the 
     faint color of his skin make him seem like the prince of some faraway land."
    voice "voice/leona/5/le_ru_scene5_5.ogg"
    mc happyblush "You."
    pause 0.5
    show rumble surprisedblush with dissolve
    pause 0.5
    "Daniel's blush is a slap to the face. What did I just say?!"
    voice "voice/leona/5/le_ru_scene5_6.ogg"
    mc surprise "I-I-I mean your art. Y-you know, I've taken in interest in your drawings since I
        saw the sunflowers. And apparently, I'm not the only one to think so."
    "Phew! Safe call."
    show rumble flat with dissolve
    pause 0.5
    show rumble happy with dissolve
    voice "voice/rumble/5/ru_scene5_2.ogg"
    da "Thanks. What do you like about it? You never struck me as an art aficionado until recently."
    voice "voice/leona/5/le_ru_scene5_7.ogg"
    mc flat "Well..."
    "I close my eyes as I begin recalling how stressful things are at home."
    voice "voice/leona/5/le_ru_scene5_8.ogg"
    mc sad "You see, my parents aren't exactly the most pleasant. Have you heard of Rakkor Boxing?"
    show rumble flat with dissolve
    voice "voice/rumble/5/ru_scene5_3.ogg"
    da "Not that I know a lot about boxing, but I have heard of them before. Weren't 
        they pretty famous? Something about a bunch of world champions training there..."
    voice "voice/leona/5/le_ru_scene5_9.ogg"
    mc sad "Their training wasn't always the cleanest, though. They want me to take over as soon 
        as I graduate, but I'm not sure I can run a gym that lives up to their expectations."
    voice "voice/leona/5/le_ru_scene5_10.ogg"
    mc sad "I'm not going to say they were responsible for what happened to Gwen's father, 
        but... they push people too hard."
    hide rumble with dissolve
    show rumble flatclose with dissolve
    "I feel a warm hand on my shoulders as I attempt to fight back the impending tears."
    voice "voice/leona/5/le_ru_scene5_11.ogg"
    mc happy "Art. It's different. You can speak your mind and convey your emotions without 
        the need for violence. And I only realized that when I saw your sketches."
    show rumble surprisedmid with dissolve
    voice "voice/rumble/5/ru_scene5_4.ogg"
    da "Mine?"
    voice "voice/leona/5/le_ru_scene5_12.ogg"
    mc happy "Yeah. I always thought paintings were just window dressing. But, yours - they told 
        me when you were angry, happy, frustrated, or sad."
    voice "voice/leona/5/le_ru_scene5_13.ogg"
    mc happy "Not like boxing. Boxing is just violence. How do you protect your dignity without
        knowing how to defend or protect others?"
    show rumble flat with dissolve
    "Daniel looks up to the ceiling, almost searching for an answer to everything I poured
     out to him."
    voice "voice/leona/5/le_ru_scene5_14.ogg"
    mc surprise "Oh my gosh, I'm sorry... I was just blathering on there."
    show rumble surprised with dissolve
    show rumble happy with dissolve
    voice "voice/rumble/5/ru_scene5_5.ogg"
    da "Nah, it's fine. I'm glad you did."
    voice "voice/leona/5/le_ru_scene5_15.ogg"
    mc flat "Huh?"
    hide rumble with dissolve
    show rumble flatblushmid with dissolve
    voice "voice/rumble/5/ru_scene5_6.ogg"
    da "I have an art show next week, and I want you to be my topic of interest."
    voice "voice/leona/5/le_ru_scene5_16.ogg"
    mc surprise "M-me?! But why? There are so many things you could draw!"
    show rumble happyblushmid with dissolve
    voice "voice/rumble/5/ru_scene5_7.ogg"
    da "And I choose you."
    "Uwahhhh. I never knew Daniel could be so forward."
    voice "voice/rumble/5/ru_scene5_8.ogg"
    da "It should be done soon. I hope to see you there."
    call gift_check("Daniel") from _call_gift_check_9
    hide rumble with dissolve
    "With that, Daniel leaves me behind as I stand motionless in front of the swinging doors."
    $ rumble_rp = rumble_rp + 12
    stop music fadeout 2.0
    jump events_end_period
    
label rumble_6:
    $ rumble_rp = rumble_rp + 15
    $ renpy.block_rollback()
    scene bg museum day
    "A huge crowd defines the museum's walls. I feel lost in a sea of people."
    "Left and right - I only see painting after painting with people circling around me like flies.
     I nervously walk across the hall with my head spinning around."
    play music "music/Edge of Mist.mp3" fadein 4.0
    "That is, until I stumble upon a drawing that completely and utterly captivates me."
    "Then I see it: a melancholic hue of indigo. There's a sublime, lonely blue that sinks as deep
     as the depths of the ocean."
    "Along the edges of the bottom half of the canvas is what seems to be the floor of that abyss.
     Saddening, yes. Yet, the sense of calmness and tranquility put my soul at ease as I lose 
     track of time, delving into the world of this breathtaking illustration."
    "Even within the chilling depths of the painting..."
    voice "voice/rumble/6/ru_scene6_1.ogg"
    stop music fadeout 2.0
    da "I can still feel the warmth when I look at it."
    voice "voice/leona/6/le_ru_scene6_1.ogg"
    mc surprise "Wha- when did you get here?"
    show rumble happy at right with dissolve
    play music "music/museum.mp3" fadein 2.0
    voice "voice/rumble/6/ru_scene6_2.ogg"
    da "I was around, but I had to talk to a few of the other artists, so I had to step away for
        a moment."
    voice "voice/leona/6/le_ru_scene6_2.ogg"
    mc flat "So, this really is..."
    show rumble happyblush at right
    voice "voice/rumble/6/ru_scene6_3.ogg"
    da "Heh. It's just like you to be able to find this among all the other artists."
    "Ba-bump goes my heart. Gosh, that smile of his gets me every time."
    hide rumble with dissolve 
    scene cg rumble end with fade
    voice "voice/rumble/6/ru_scene6_4.ogg"
    da "I've always felt lost. Like I'm drowning in my own thoughts and unable to tell up from down.
        It was truly an abyss, as if nothing exists but me."
    voice "voice/leona/6/le_ru_scene6_4.ogg"
    mc surprise "Huh? But... there's definitely some sort of floor in the painting."
    voice "voice/rumble/6/ru_scene6_5.ogg"
    da "Have you forgotten? This is a painting about you, not me."
    "Art talk. I don't think I'll ever get it. All I {i}do{/i} know is that my ears are on fire!"
    voice "voice/rumble/6/ru_scene6_6.ogg"
    da "Although the depths cover the canvas, there's a foundation to give it a unique orientation."
    voice "voice/rumble/6/ru_scene6_7.ogg"
    da "That \"floor,\" as you put it, is the source of the warmth that encompasses the piece, no 
        matter how dark it may appear. It gives a {i}significance{/i} to that darkness as well as a purpose." 
    voice "voice/leona/6/le_ru_scene6_4.ogg"
    mc flat "A purpose?"
    voice "voice/rumble/6/ru_scene6_8.ogg"
    da "Yes."
    voice "voice/rumble/6/ru_throat.ogg"
    "He clears his throat for a moment."
    voice "voice/rumble/6/ru_scene6_9.ogg"
    da "I'll be here to help you gleam more brilliantly than the most serene shades of the midnight lights."
    "WHOA! That came out of nowhere... or somewhere?!"
    voice "voice/leona/6/le_ru_scene6_5.ogg"
    mc flat "U-um. Wow."
    "Daniel smiles towards me, then looks back at the canvas."
    voice "voice/rumble/6/ru_scene6_10.ogg"
    da "You've done that for me already. What would just be a dark abyss turned into a scenery more
        enchanting than its sole essence."
    "I turn to look towards him, and I’m met with that same comfort and loneliness that I see
     while looking into his picture."
    "Just like a sailor at sea during motionless breezes, I find myself in serenity."
    scene bg museum day with fade
    show rumble happyblush at right
    voice "voice/rumble/6/ru_ja_scene6_1.ogg"
    je "This really is amazing when I see it in person. I really am impressed."
    with vpunch
    voice "voice/leona/6/le_ru_scene6_6.ogg"
    mc surprise "J-Jason?!"
    show jayce happy with dissolve
    voice "voice/rumble/6/ru_ja_scene6_2.ogg"
    je "Yo, I just wanted to get a look at what this bugger here was doing, but now that I've seen
        it, I can't find any other words to say."
    voice "voice/leona/6/le_ru_scene6_7.ogg"
    mc angry "For starters, how about formally apologizing for the other day?"
    show jayce angry
    show rumble flat
    with dissolve
    voice "voice/rumble/6/ru_ja_scene6_3.ogg"
    je "Yeah, I guess I got carried away by the mood. Sorry for that."
    voice "voice/rumble/6/ru_scene6_11.ogg"
    da "Uh, no problem."
    show jayce happy with dissolve
    "Jayce then reciprocates with a warm smile; as expected of the ace of the soccer team."
    voice "voice/rumble/6/ru_vi_scene6_1.ogg"
    cy "Hmm, so this is where your talents have been spent?"
    show jayce surprised with dissolve
    pause 0.5
    hide jayce with dissolve
    show jayce surprised at left
    show vik flat at center
    with dissolve
    pause 0.2
    "And now Cyrus joins the picture."
    show jayce angry at left
    "I shoot back that same dorky look at Daniel. You never know what to expect from this guy...
     well, except for some insults."
    voice "voice/rumble/6/ru_vi_scene6_2.ogg"
    cy "I cannot comprehend this art form; it lacks science."
    show vik flat behind rumble
    show rumble angrymid at right with dissolve
    voice "voice/rumble/6/ru_scene6_12.ogg"
    da "Not everything is based off science. This is something that understanding and research
        alone won't help you achieve."
    show rumble flat at right with dissolve
    "The tension in the air is unmistakable. It’s to be expected when these two encounter each other.
     But this time, Daniel seems resolute."
    show rumble flat behind vik
    voice "voice/rumble/6/ru_vi_scene6_3.ogg"
    cy "Correct. This is not something I can simply replicate because I so desire, let alone
        analyze. I have no reason to scorn those who are able to produce results within their own expertise."
    voice "voice/rumble/6/ru_vi_scene6_4.ogg"
    cy "Continue to progress and advance, Daniel. Our only duty is to be immersed in the pursuit
        of progress. That is the sole justification for your existence."
    hide vik with easeoutright
    show jayce surprised at left with dissolve
    pause 0.2
    hide jayce with easeoutright
    "With that, Cyrus walked off with his prideful gait, with Jason following close behind him."
    "Since when were those two so close? Hmm..."
    hide rumble
    show rumble flat
    voice "voice/leona/6/le_ru_scene6_8.ogg"
    mc angry "Cyrus is as pompous as ever."
    voice "voice/rumble/6/ru_scene6_13A.ogg"
    da "Yeah."
    show rumble flatmid with dissolve
    voice "voice/leona/6/le_ru_scene6_9.ogg"
    mc flat "Daniel?"
    "I guess the resolution of their internal strife has brought him more peace of mind than I had
     expected. His gaze still lingers where Cyrus disappeared."
    show rumble flatclose with dissolve
    voice "voice/leona/6/le_ru_scene6_10.ogg"
    mc sad "You know, Daniel. The other day, when I said I liked you, I didn't mean only your art..."
    "Here it comes!" #aah
    show rumble surprisedblushclose with dissolve
    voice "voice/rumble/6/ru_scene6_14.ogg"
    da "Huh?"
    voice "voice/leona/6/le_ru_scene6_11.ogg"
    mc happy "One of the reasons I enjoy your art so much is that it allows me to understand just how
        interesting of a person you are..."
    voice "voice/leona/6/le_ru_scene6_12.ogg"
    mc happyblush "...and just how much I like you."
    hide rumble with dissolve
    show rumble surprisedblush with dissolve
    "Two strikes and he's out! First, the whole Cyrus thing, and now my confession was another
     blow to the heart."
    "Something comes over me as I take his hand and drag him off somewhere more secluded."
    hide rumble with easeoutleft
    voice "voice/leona/6/le_ru_scene6_13.ogg"
    mc happyblush "Come on! Let's learn about all these different worlds inside and outside this museum, together!"
    stop music fadeout 3.0
    jump events_end_period