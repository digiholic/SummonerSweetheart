######################################### FILLER EVENTS
init:
    $ event("library_empty", "act == 'library'", event.solo(), priority = 250)
    $ event("park_empty", "act == 'park'", event.solo(), priority = 250)
    $ event("vr_empty", "act == 'vr'", event.solo(), priority = 250)
    $ event("soccer_empty", "act == 'soccer'", event.solo(), priority = 250)
    $ event("class_empty", "act == 'class'", event.solo(), priority = 250)
    $ event("museum_empty", "act == 'museum'", event.solo(), priority = 250)

label library_empty:
    $ renpy.block_rollback()
    scene bg library
    "I arrive at the library, but it seems to be pretty empty. I don't see anyone
     I recognize, and when I go to do research, my efforts come up empty."
    jump events_end_period

label park_empty:
    $ renpy.block_rollback()
    if period == 2:
        scene bg park night
    else:
        scene bg park day
    "The park is nice, but there's not really any reason to be here.
     I spend a couple of hours relaxing on the grass."
    jump events_end_period
    
label class_empty:
    $ renpy.block_rollback()
    if period == 2:
        scene bg classroom night
    else:
        scene bg classroom day
    "Dr. Zen is grading papers at his desk, and a couple of students I don't know very well
     are chatting around another desk. There's not much for me to do."
    jump events_end_period
    
label soccer_empty:
    $ renpy.block_rollback()
    if period == 2:
        scene bg soccer night
    else:
        scene bg soccer day
    "Is there no practice today or something? The field is empty. There aren't even
     any people playing around. I think I probably should have gone somewhere else..."
    jump events_end_period
    
    
label vr_empty:
    $ renpy.block_rollback()
    if period == 2:
        scene bg bedroom night
    else:
        scene bg bedroom day
    "I go home to check on League of Legends, but the hacker doesn't seem to be bothering anyone
     much right now, and none of the club members are online. I grind a little bit
     and chat around, but don't come away with anything useful."
    jump events_end_period
    
label museum_empty:
    $ renpy.block_rollback()
    if period == 2:
        scene bg museum night
    else:
        scene bg museum day
    "I head into the museum on a whim. It's quiet. The art looks pretty as usual, but unfortunately
     there aren't any new exhibits or anything. I look around for a while and then leave."
    jump events_end_period

######################################### GIFT EVENTS

label rengar_bone:
    $ renpy.block_rollback()
    mc happy "Gwen?"
    show rango angry with dissolve
    "From inside my pocket, I slowly unwrap the bonetooth necklace and dangle it in front of her before I gently toss it over."
    show rango surprisedmid with dissolve
    show rango surprised with dissolve
    voice "voice/rango/gift/re_gift_1.ogg"
    gw "W-what is this? ...Is it for me?"
    voice "voice/ezreal/gift/ez_re_giftBON1.ogg"
    mc happy "Yea. I thought it'd look nice with the one you have now."
    show rango flat
    gw "..."
    voice "voice/ezreal/gift/ez_re_giftBON2.ogg"
    mc surprise "What? You don't like it?"
    show rango blush
    voice "voice/rango/gift/re_gift_2.ogg"
    gw "I-idiot! ...I'll wear it to my next Super Smash competition. Only because you gave it to me and I don't want you to feel bad if I didn't."
    voice "voice/ezreal/gift/ez_re_giftBON3.ogg"
    mc happy "Haha, sure."
    voice "voice/rango/gift/re_gift_3.ogg"
    gw "Shut up."
    show rango happyblush with dissolve
    pause 0.3
    hide rango with dissolve
    # increase rengar rp
    return

label rengar_charm:
    $ renpy.block_rollback()
    "I catch Gwen's attention once again."
    show rango angry with dissolve
    "The box so delicately wrapped holds the glowing crimson fox charm. I present it to her by untying the sapphire ribbon and sliding off the lid that reveals the gift."
    show rango surprised with dissolve
    show rango angry with dissolve
    voice "voice/rango/gift/re_gift_4.ogg"
    gw "What the heck is that?"
    voice "voice/ezreal/gift/ez_re_giftCHA1.ogg"
    mc happy "It's a phone charm! We have matching ones, see?"
    "I flash the one drooping and swaying from my phone. The light's glare makes the flaming keychain illuminate the room."
    voice "voice/rango/gift/re_gift_5.ogg"
    gw "Gross! Like I can do anything with {i}that{/i} garbage. It would just get in the way." with hpunch
    voice "voice/ezreal/gift/ez_re_giftCHA2.ogg"
    mc sad "But it's for you..."
    voice "voice/rango/gift/re_gift_6.ogg"
    gw "I don't need anything so useless."
    hide rango with dissolve
    # decrease rengar rp
    return

label rengar_hairclip:
    $ renpy.block_rollback()
    "I get Gwen's attention."
    show rango angry with dissolve
    "Reaching inside my pouch, I hide the starry hair clip behind my back before flauting the yellow barrette."
    voice "voice/ezreal/gift/ez_re_giftHAI1.ogg"
    mc happy "For you."
    show rango surprised with dissolve
    show rango flat with dissolve
    voice "voice/rango/gift/re_gift_7.ogg"
    gw "Uh. Are you expecting a thank you?"
    voice "voice/ezreal/gift/ez_re_giftHAI2.ogg"
    mc surprise "No... not really? Do you not like it?"
    voice "voice/rango/gift/re_gift_8.ogg"
    show rango angry with dissolve
    gw "I don't like putting flashy accessories in my hair."
    voice "voice/ezreal/gift/ez_re_giftHAI3.ogg"
    mc surprise "But you have braids!"
    voice "voice/rango/gift/re_gift_9.ogg"
    gw "They're {i}weaves{/i}, not pigtails. And stars aren't my thing."
    hide rango with dissolve
    return

label ahri_bone:
    $ renpy.block_rollback()
    "I get Ami's attention once again."
    show ahri happy with dissolve
    "From within my pocket, I slowly unwrap the bonetooth necklace and dangle it in front of her before I gently toss it over."
    voice "voice/ahri/gift/ah_gift_1.ogg"
    show ahri angry with dissolve
    am "Ew, what is that ugly monstrosity?"
    voice "voice/ezreal/gift/ez_ah_giftBON1.ogg"
    mc happy "A necklace! I thought you liked jewelry."
    voice "voice/ahri/gift/ah_gift_2.ogg"
    am "It's freakishly gross, that's for sure."
    voice "voice/ezreal/gift/ez_ah_giftBON2.ogg"
    mc surprise "So you won't wear it?"
    voice "voice/ahri/gift/ah_gift_3.ogg"
    am "I wouldn't be caught dead wearing something so barbaric."
    hide ahri with dissolve
    # decrease ahri RP
    return
    
label ahri_charm:
    $ renpy.block_rollback()
    "I get Ami's attention once again."
    show ahri happy with dissolve
    "The box so delicately wrapped holds the glowing crimson fox charm. I present it to her by untying the sapphire ribbon and sliding off the lid that reveals the gift."
    show ahri surprised
    show ahri surprisedclose with dissolve
    pause 0.3
    show ahri happy2mid with dissolve
    pause 0.3
    voice "voice/ahri/gift/ah_gift_4.ogg"
    am "Is this for me?!"
    voice "voice/ezreal/gift/ez_ah_giftCHA1.ogg"
    mc happyblush "Yea! I was lucky enough to get it at the market. It was the last pair."
    show ahri surprised
    voice "voice/ahri/gift/ah_gift_5.ogg"
    am "Pair?"
    voice "voice/ezreal/gift/ez_ah_giftCHA2.ogg"
    mc happy "Look - I have the exact one."
    show ahri surprisedmid
    "I flash the one drooping and swaying from my phone. The light's glare makes the flaming keychain illuminate the room."
    show ahri happy2mid
    voice "voice/ahri/gift/ah_gift_6.ogg"
    am "Oh, my. So bold~ It's like we're {i}one{/i} now."
    hide ahri with dissolve
    # increase ahri RP
    return

label ahri_hairclip:
    $ renpy.block_rollback()
    "I get Ami's attention once again."
    show ahri happy with dissolve
    "I reach inside my pouch and hide the starry hair clip behind my back before flauting the yellow barrette."
    voice "voice/ahri/gift/ah_gift_7.ogg"
    am "I didn't know you had an interest in astrological things."
    voice "voice/ezreal/gift/ez_ah_giftHAI1.ogg"
    mc happy "...It's a star, and it's for you."
    show ahri sad with dissolve
    voice "voice/ahri/gift/ah_gift_8.ogg"
    am "Huh? Me? I can't wear anything so frivolous. My parents will disapprove."
    voice "voice/ezreal/gift/ez_ah_giftHAI2.ogg"
    mc surprise "I thought it would look good in your long, dark hair."
    voice "voice/ahri/gift/ah_gift_9.ogg"
    am "Thanks for the gesture I guess, but stars are too childish."
    hide ahri with dissolve
    return

label soraka_bone:
    $ renpy.block_rollback()
    "I get Sharon's attention once again."
    show raka happy with dissolve
    "From within my pocket, I slowly unwrap the bonetooth necklace and dangle it in front of her before I gently toss it over."
    voice "voice/raka/gift/so_gift_1.ogg"
    sh "What an interesting necklace."
    voice "voice/ezreal/gift/ez_so_giftBON1.ogg"
    mc happy "Glad you think so. It's for you."
    show raka sad
    voice "voice/raka/gift/so_gift_2.ogg"
    sh "Oh..."
    voice "voice/ezreal/gift/ez_so_giftBON2.ogg"
    mc happy "How do you like it?"
    voice "voice/raka/gift/so_gift_3.ogg"
    sh "Uh, thanks, [name]. But I think this is better fit for someone more rambunctious."
    hide raka with dissolve
    return

label soraka_charm:
    $ renpy.block_rollback()
    "I get Sharon's attention once again."
    show raka happy with dissolve
    "The box so delicately wrapped holds the glowing crimson fox charm. I present it to her by untying the sapphire ribbon and sliding off the lid that reveals the gift."
    voice "voice/raka/gift/so_gift_4.ogg"
    sh "Um...?"
    voice "voice/ezreal/gift/ez_so_giftCHA1.ogg"
    mc happy "I got this for you so we could parade our friendship together."
    show raka angry
    voice "voice/raka/gift/so_gift_5.ogg"
    sh "T-together?!"
    "I flash the one drooping and swaying from my iPhone 6. The light's glare makes the flaming keychain illuminate the room."
    "Her face turns fifty shades of red before she turns her head."
    voice "voice/raka/gift/so_gift_6.ogg"
    sh "It's... pretty embarrassing, sorry! Thanks anyways."
    hide raka with dissolve
    return

label soraka_hairclip:
    $ renpy.block_rollback()
    "I get Sharon's attention once again."
    show raka happy with dissolve
    "I reach inside my pouch and hide the starry hair clip behind my back before flauting the yellow barrette."
    voice "voice/ezreal/gift/ez_so_giftHAI1.ogg"
    mc happy "I was thinking about the clip in your hair and thought it was pretty lonely by itself."
    show raka surprised with dissolve
    voice "voice/raka/gift/so_gift_7.ogg"
    sh "Eh?! This is for me? Really?"
    voice "voice/ezreal/gift/ez_so_giftHAI2.ogg"
    mc happyblush "You have such a starry persona that it would be a shame not to give it to you."
    show raka happymid with dissolve
    show raka happy with dissolve
    voice "voice/raka/gift/so_gift_8.ogg"
    sh "Th-thanks a lot!" #blush
    show raka sad with dissolve
    "Just a pinch of melancholy paints its way onto her face."
    voice "voice/ezreal/gift/ez_so_giftHAI3.ogg"
    mc surprise "Is there something wrong?"
    show raka happy
    voice "voice/raka/gift/so_gift_9.ogg"
    sh "Oh, no. It just reminds me of an old friend of mine."
    hide raka with dissolve
    return

label jayce_hammer:
    $ renpy.block_rollback()
    mc flat "Hey, Jason?"
    show jayce happy with dissolve
    "I dig through my pencil pouch to pass the giftbox holding the miniature hammer to him. It even lights up when you press the gem on the top!"
    voice "voice/leona/gift/le_ja_giftHAM1.ogg"
    mc flat "What do you think?"
    show jayce blush with dissolve
    pause 0.3
    voice "voice/jayce/gift/ja_gift_1.ogg"
    je "You really got this for me?"
    voice "voice/leona/gift/le_ja_giftHAM2.ogg"
    mc happy "Thought that this would remind you of who you are, not the image you're married to."
    show jayce happy with dissolve
    voice "voice/jayce/gift/ja_gift_2.ogg"
    je "Shocking." #playful tone
    voice "voice/jayce/gift/ja_gift_3.ogg"
    je "This will undeniably energize me while I'm out in the fields."
    voice "voice/leona/gift/le_ja_giftHAM3.ogg"
    mc happy "Heh. I'm glad it will!"
    hide jayce with dissolve
    return
    
label jayce_rubix:
    $ renpy.block_rollback()
    mc flat "Hey, Jason?"
    show jayce happy with dissolve
    "The rubix cube almost tumbles out of my hand as I reach for it in the pockets of my iris handbag."
    "Luckily before it hits the floor, Jason catches it with his superhuman reflexes."
    show jayce surprised2 with dissolve
    pause 0.2
    voice "voice/jayce/gift/ja_gift_4.ogg"
    je "What's this?"
    voice "voice/leona/gift/le_ja_giftRUB1.ogg"
    mc happy "Oh! It's a gift I brought for you."
    show jayce angry with dissolve
    pause 0.2
    voice "voice/jayce/gift/ja_gift_5.ogg"
    je "Hey, not bad. I guess it could keep my company when you're not here."
    voice "voice/leona/gift/le_ja_giftRUB2.ogg"
    mc happy "You and your silly attempts at flirting."
    voice "voice/jayce/gift/ja_gift_6.ogg"
    je "They're not!"
    hide jayce with dissolve
    return

label jayce_sketch:
    $ renpy.block_rollback()
    mc flat "Hey, Jason?"
    show jayce happy with dissolve
    "Swinging the notebook in front of his unsuspecting eyes, I watch for the signs of gratitude that I hope he'll display."
    show jayce surprised2
    voice "voice/jayce/gift/ja_gift_7.ogg"
    je "You into drawing now?"
    voice "voice/leona/gift/le_ja_giftBOO1.ogg"
    mc flat "No, I thought you'd like it."
    show jayce happy
    voice "voice/jayce/gift/ja_gift_8.ogg"
    je "For me? I haven't drawn anything but cats and ninjas since middle school."
    voice "voice/leona/gift/le_ja_giftBOO2.ogg"
    mc happy "I know you secretly draw doodles in class."
    show jayce surprised
    voice "voice/jayce/gift/ja_gift_9.ogg"
    je "Nah, I'll pass, as much as I like anything that you'd give me."
    show jayce happy
    hide jayce with easeoutright
    "Though his charming wink and gorgeous smile make my heart soar, it sure doesn't lessen the disappointment."
    return

label viktor_hammer:
    $ renpy.block_rollback()
    mc flat "Hey, Cyrus?"
    show vik flat with dissolve
    "I dig through my pencil pouch to pass the giftbox holding the miniature hammer to him. It even lights up when you press the gem on the top!"
    show vik angry with dissolve
    voice "voice/viktor/gift/vi_gift_1.ogg"
    cy "What rubbish is this?"
    voice "voice/leona/gift/le_vi_giftHAM1.ogg"
    mc angry "It's not rubbish! It's a present for you."
    voice "voice/viktor/gift/vi_gift_2.ogg"
    cy "In which world gave you the impression that a small forged weapon would satisfy my needs?"
    voice "voice/leona/gift/le_vi_giftHAM2.ogg"
    mc angry "Um, mine."
    pause 0.5
    show vik flat with dissolve
    voice "voice/viktor/gift/vi_gift_3.ogg"
    cy "Your stupidity baffles me."
    voice "voice/leona/gift/le_vi_giftHAM3.ogg"
    mc angry "Don't you like metal and machinery?"
    voice "voice/viktor/gift/vi_gift_4.ogg"
    cy "There is a difference between innovations made for progress and creations solely for entertainment."
    hide vik with dissolve
    return

label viktor_rubix:
    $ renpy.block_rollback()
    mc flat "Hey, Cyrus?"
    show vik flat with dissolve
    "The rubix cube almost tumbles out of my hand as I reach for it in the pockets of my iris handbag."
    show vik surprised with dissolve
    pause 0.2
    show vik surprisedmid with hpunch
    "Luckily before it hits the floor, Cyrus catches it with his superhuman reflexes."
    pause 0.3
    hide vik with dissolve
    pause 0.1
    show vik flat with dissolve
    voice "voice/leona/gift/le_vi_giftRUB1.ogg"
    mc happy "Good catch!"
    show vik surprised
    voice "voice/viktor/gift/vi_gift_5.ogg"
    cy "I am ...surprised."
    voice "voice/leona/gift/le_vi_giftRUB2.ogg"
    mc happy "I take it you like the gift?"
    show vik happy with dissolve
    voice "voice/viktor/gift/vi_gift_6.ogg"
    cy "Your attempts to befriend me with donations are futile."
    voice "voice/leona/gift/le_vi_giftRUB3.ogg"
    mc happyblush "I'm trying, and I think it's working." #smile
    cy "..."
    hide vik with dissolve
    return
                                                                                                                                                   
label viktor_sketch:
    $ renpy.block_rollback()
    mc flat "Hey, Cyrus?"
    show vik flat with dissolve
    "Swinging the notebook in front of his unsuspecting eyes, I watch for the signs of gratitude that I hope he'll display."
    show vik angry
    voice "voice/viktor/gift/vi_gift_7.ogg"
    cy "Stop flailing your foolish notebook within my periphery."
    voice "voice/leona/gift/le_vi_giftBOO1.ogg"
    mc happy "I got it for you. I thought it could help you sketch out ideas!"
    show vik flat
    voice "voice/viktor/gift/vi_gift_8.ogg"
    cy "My skills need no such item to maximize its efficiency."
    hide vik with dissolve
    pause 0.1
    show vik flatmid with dissolve
    pause 0.5
    show vik flat with dissolve
    "Although he says that, he takes the notebook to flip through the empty pages and tosses it back."
    voice "voice/leona/gift/le_vi_giftBOO2.ogg"
    mc sad "So you don't like it?"
    voice "voice/viktor/gift/vi_gift_9.ogg"
    cy "No."
    hide vik with easeoutright
    return

label daniel_hammer:
    $ renpy.block_rollback()
    show rumble flat with dissolve
    mc flat "Hey, Daniel?"
    "I dig through my pencil pouch to pass the giftbox holding the miniature hammer to him. It even lights up when you press the gem on the top!"
    da "...?"
    voice "voice/leona/gift/le_ru_giftHAM1.ogg"
    mc flat "I was passing by the market when it was having a sale on weaponry models. Maybe you could use it?"
    show rumble surprised
    voice "voice/rumble/gift/ru_gift_1.ogg"
    da "Oh."
    pause 1.0
    "The silence is enough of a gesture to illustrate his disapproval."
    voice "voice/leona/gift/le_ru_giftHAM2.ogg"
    mc sad "Or, you know, think of me when you see it?"
    show rumble flatblush
    "His adorable streaks of red make it difficult not to giggle a little on the inside."
    voice "voice/rumble/gift/ru_gift_2.ogg"
    da "S-sure."
    hide rumble with dissolve
    return

label daniel_rubix:
    $ renpy.block_rollback()
    mc flat "Hey, Daniel?"
    show rumble surprised with dissolve
    "The rubix cube tumbles out of my hand as I reach for it in the pockets of my iris handbag. It rolls on the ground, inching away as it spins."
    voice "voice/leona/gift/le_ru_giftRUB1.ogg"
    mc surprise "Oops! This is for you. I hope it didn't break."
    show rumble sad
    voice "voice/rumble/gift/ru_gift_3.ogg"
    da "I don't really like puzzles."
    voice "voice/leona/gift/le_ru_giftRUB2.ogg"
    mc surprise "Really? I just thought with the symbolism and unique interpretations in your drawings, you'd enjoy a little challenge."
    show rumble flat
    voice "voice/rumble/gift/ru_gift_4.ogg"
    da "I'd rather focus my energy on improving my technique."
    voice "voice/leona/gift/le_ru_giftRUB3.ogg"
    mc sad "Oh, okay."
    hide rumble with dissolve
    return

label daniel_sketch:
    $ renpy.block_rollback()
    mc flat "Hey, Daniel?"
    show rumble flat with dissolve
    "Swinging the notebook in front of his unsuspecting eyes, I watch for the signs of gratitude that I hope he'll display."
    voice "voice/leona/gift/le_ru_giftBOO1.ogg"
    mc happy "With all the time you put into sketching, maybe you're in need of a new sketchbook?"
    show rumble surprised with dissolve
    pause 0.3
    show rumble happy with dissolve
    voice "voice/rumble/gift/ru_gift_5.ogg"
    da "I actually just finished filling my fifth artbook yesterday."
    "Daniel's delightful smile is like a jab of sun rays piercing through my chest."
    voice "voice/leona/gift/le_ru_giftBOO2.ogg"
    mc happyblush "Glad you like it."
    show rumble happyblush with dissolve
    voice "voice/rumble/gift/ru_gift_6.ogg"
    da "... Thank you. I'll use it to prepare my art show."
    voice "voice/leona/gift/le_ru_giftBOO3.ogg"
    mc happyblush "I'd love to see your illustrations!"
    hide rumble with dissolve
    return
    
########################################## SKILL EVENTS

label unlock_combo1:
    $ dungeon_visits_no_combo = 0
    $ renpy.block_rollback()
    "I realize soon that I forgot something from the classroom and head back."
    scene bg classroom night
    "In the corner of my eyes, the fragile features of Thomas radiate under the glow of the lights."
    "His light beryl eyes glint as he approaches me with a smirk."
    show char teemo at left
    voice "voice/teemo/unlockscene_teemo_scenepow_line1.ogg"
    te "That's gotta sting."
    mc surprise "What stings?"
    voice "voice/teemo/unlockscene_teemo_scenepow_line2.ogg"
    te "Y'know, when you take a long walk through the jungle, you gotta watch your step! Jungle monsters are nasty."
    mc surprise "How'd you know? That we got outplayed, I mean."
    voice "voice/teemo/unlockscene_teemo_scenepow_line3.ogg"
    te "Hehe. I'm everywhere. You just don't {i}see{/i} me."
    show char teemo angry at left with dissolve
    pause 0.2
    voice "voice/teemo/unlockscene_teemo_scenepow_line4.ogg"
    te "But aye, that's not why I'm here. You and I are survivors, buddy. I'll let you in on a little secret."
    "For such an adorable guy, the ringing of his voice almost sings with a hint of slight villainy." 
    voice "voice/teemo/unlockscene_teemo_scenepow_line5.ogg"
    te "You gotta \"power\" through your \"shots\" and wing it!"
    hide char with easeoutright
    "And with that, he totters off scouting ahead for who knows what."
    "I learn a little something, somehow."
    if route == "Ezreal":
        "Attack myself, then with Rengar, then Ahri? Huh."
        if ahri_rp >= rango_rp and ahri_rp >= raka_rp:
            $ ahri_combo = True
        elif rango_rp >= ahri_rp and rango_rp >= raka_rp:
            $ rango_combo = True
        else:
            $ raka_combo = True
    elif route == "Leona":
        "I should attack, and then have Viktor and then Jayce follow me up!"
        if jayce_rp >= rumble_rp and jayce_rp >= vik_rp:
            $ jayce_combo = True
        elif rumble_rp >= jayce_rp and rumble_rp >= vik_rp:
            $ rumble_combo = True
        else:
            $ vik_combo = True
    scene bg black with fade
    return

label unlock_combo2:
    $ dungeon_visits_no_combo = 0
    $ renpy.block_rollback()
    scene bg classroom night
    show char teemo at center with dissolve
    voice "voice/teemo/unlockscene_teemo_sceneflu_line1.ogg"
    te "Captain Teemo on duty!"
    "Whoa, this guy came out of nowhere! He wasn't there before; it's like he's camouflaged."
    mc angry "Wait, what? We aren't in game, Thomas."
    show char teemo angry
    voice "voice/teemo/unlockscene_teemo_scenepow_line6.ogg"
    te "Doesn't mean you can't scout ahead. That's why you're stumped again, my friend!"
    voice "voice/teemo/unlockscene_teemo_sceneflu_line2.ogg"
    te "You gotta be armed and ready, no matter where you go."
    mc flat "I suppose that's true. But how am I supposed to defeat something that has no weakness - or at least, a weakness I don't know?"
    show char teemo
    voice "voice/teemo/unlockscene_teemo_sceneflu_line3.ogg"
    te "And that is why I'm reporting in! Dig deeper and don't dawdle behind your foes."
    mc angry "What is that supposed to mean?"
    voice "voice/teemo/unlockscene_teemo_sceneflu_line4.ogg"
    te "A flux that never stops growing will aid you on your journey. Now, swiftly!"
    hide char with dissolve
    "Gusts of wind muddy my vision as his blurry shadow disappears into the distance."
    "That was pretty weird... but I come away with some new knowledge."
    scene bg black with fade
    if route == "Ezreal":
        if ahri_rp >= rango_rp and ahri_rp >= raka_rp and not ahri_combo:
            $ ahri_combo = True
        elif rango_rp >= ahri_rp and rango_rp >= raka_rp and not rango_combo:
            $ rango_combo = True
        else:
            $ raka_combo = True
    elif route == "Leona":
        if jayce_rp > rumble_rp and jayce_rp > vik_rp:
            $ jayce_combo = True
        elif rumble_rp > jayce_rp and rumble_rp > vik_rp:
            $ rumble_combo = True
        else:
            $ vik_combo = True
    return
    # Notice: Player unlocked Growing Flux
    
label unlock_combo3:
    $ dungeon_visits_no_combo = 0
    $ renpy.block_rollback()
    scene bg classroom night
    "I can hear the humming of \"The Lazy Song\" by Bruno Mars resonate in the air as a familiar student pulls up to me."
    show char teemo with easeinleft
    hide char teemo with easeoutright
    voice "voice/teemo/unlockscene_teemo_sceneen_line1.ogg"
    te "Today I don't feel like doing anything~ ♫"
    show char teemo with easeinright
    hide char teemo with easeoutright
    voice "voice/teemo/unlockscene_teemo_sceneen_line2.ogg"
    te "I just wanna lay in my bed..."
    "How is he marching toward me with his eyes closed?"
    show char teemo with easeinleft
    voice "voice/teemo/unlockscene_teemo_sceneen_line3.ogg"
    te "So leave a message at the tone! ☆"
    mc angry "Uh, I think you missed a line."
    show char teemo confused at center with dissolve
    voice "voice/teemo/unlockscene_teemo_sceneen_line4.ogg"
    te "That's not the point, silly. That message was for you!"
    mc surprise "Huh? For me?"
    show char teemo
    hide char with easeoutleft
    voice "voice/teemo/unlockscene_teemo_sceneen_line5.ogg"
    te "Yes I said it. I said it. I said it 'cause I can~"
    mc flat "Haha, what is it this time?"
    show char teemo with easeinright
    hide char teemo with easeoutleft
    voice "voice/teemo/unlockscene_teemo_sceneen_line6.ogg"
    te "Don't be loungin' on the couch just chillin' in yo snuggie."
    show char teemo with easeinleft
    hide char teemo with easeoutright
    voice "voice/teemo/unlockscene_teemo_sceneen_line7.ogg"
    te "Just strut in yo birthday suit, and let your energy hang true-ooh~ ♪"
    "... And he leaves just like that. His riddles sure are eccentric. But I realize something new. And 
     I have a song stuck in my head."
    scene bg black with fade
    if route == "Ezreal":
        $ rango_combo = True
        $ raka_combo = True
        $ ahri_combo = True
    elif route == "Leona":
        $ jayce_combo = True
        $ vik_combo = True
        $ rumble_combo = True
    return
    # Notice: Player unlocked True Energy
    