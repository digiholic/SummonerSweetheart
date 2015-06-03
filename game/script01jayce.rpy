######################################### EVENT DECLARATION
init:
    $ event("jayce_1", "act == 'soccer'", event.once(), "route == 'Leona'", "period == 1", priority = 190)
    $ event("jayce_2", "act == 'vr'", event.once(), event.depends("jayce_1"), priority = 180)
    $ event("jayce_3", "act == 'class'", event.once(), event.depends("jayce_2"), "day >= 3", priority = 170)
    $ event("jayce_4", "act == 'park'", event.once(), event.depends("jayce_3"), "period == 1", priority = 160)
    $ event("jayce_5", "act == 'soccer'", event.once(), event.depends("jayce_4"), "day == 7", "period == 2", "jayce_rp >= 70", priority = 150)

######################################### JAYCE SCRIPT
label jayce_1:
    $ jayce_scene = 1
    $ renpy.block_rollback()
    scene bg soccer day
    play music "music/Smooth Sailing.mp3" fadein 2.0
    "It's almost suffocating how much people have been smothering each other about the
     hacker. It's like watching a pack of hyenas compete for the last cup of cereal.
     Wait, that doesn't make sense."
    "See! That's how jumbled my mind is right now. At least the clean air from the soccer 
     field will be refreshing. I get to be out in the sun and nothing will disturb my investig--"
    voice "voice/jayce/1/KYA.ogg"
    un "KYAAAAAAA!" #JESSICA
    "I stand corrected."
    show jayce happy at right with dissolve
    voice "voice/jayce/1/ja_scene1_1A.ogg"
    je "Ladies, ladies. Thank you for coming out to support me today. Without each and every 
        one of you, I wouldn't have performed as well as I did."
    "It looks as though the soccer team just finished a game. All I see are a bunch of girls
     hovering over someone - probably the star of the show."
    "Why all the clamor for one person? If he's really that spectacular, maybe I missed the memo."
    voice "voice/jayce/1/ja_scene1_2B.ogg"
    je "... and our lucky winner for today is ..."
    hide jayce with dissolve
    "Everything goes completely silent. Why do I get the feeling that everyone has turned their gaze towards me?"
    "It's because they have! The girls stare in awe as Jason heads my way, a single rose in his outstretched hand."
    show jayce happymid with dissolve
    voice "voice/leona/1/le_ja_scene1_1.ogg"
    mc surprise "What? For me?"
    hide jayce with dissolve
    show jayce happy with dissolve
    voice "voice/jayce/1/ja_scene1_3A.ogg"
    je "Of course! It's a token of my appreciation. I make sure to thank everyone who cares enough to make 
        it out to my practices - {i}especially{/i} the ladies."
    "I'm not sure what he was expecting, but all he got out of my mouth was a groan."
    "I was there when Jason made the winning shot against Noxus High School in the world
     championship game last year. That might explain the fangirls, but that doesn't explain... this."
    voice "voice/jayce/1/ja_scene1_4A.ogg"
    je "Well? Don't tell me a girl like you isn't going to accept this lovely rose from a guy like {i}me{/i}."
    voice "voice/leona/1/le_ja_scene1_2.ogg"
    mc flat "...Am I supposed to know you or something? We just met..." ##... girl you in the club together
    show jayce surprised
    "The silence returns. This time, I stare back. His face blends into a mix of shock and confusion.
     It's only a second that I see it, and he returns back to his suave self."
    show jayce angry
    voice "voice/jayce/1/ja_scene1_5B.ogg"
    je "I see. It's really a shame. That you don't know me, I mean."
    hide jayce with dissolve
    "Jason's voice lingers in the air, my back turning in a curt farewell gesture as I walk away. 
     What kind of guy brings flowers to school?"
    "Alas, my stressful day gets even more tiresome as I feel a hand grab onto my shoulders.
     The hold was slight, yet ever so desperate."
    voice "voice/jayce/1/ja_scene1_6.ogg"
    je "Hey."
    "I roll my eyes. Is he trying to woo me?"
    show jayce happy with dissolve
    voice "voice/jayce/1/ja_scene1_7.ogg"
    je "I was thinking we should get to know each other."
    "What is this guy really up to?"
    $ renpy.block_rollback()

    menu:
        "Why the rose?":
            $ renpy.block_rollback()
            voice "voice/leona/1/le_ja_scene1_3.ogg"
            mc flat "What was all that about, giving me a rose?"
            voice "voice/jayce/1/ja_scene1_8B.ogg"
            je "It's not like I can take more than one girl to the Spring Fling next week,
                so I'm doing the rest of my special fans a favor."
            voice "voice/leona/1/le_ja_scene1_4.ogg"
            mc flat "Is this the way you always talk to people?"
            voice "voice/jayce/1/ja_scene1_9B.ogg"
            je "The best soccer player in the world can't be a pushover. A man like that has to deliver." #what, pizza?
            voice "voice/leona/1/le_ja_scene1_5.ogg"
            mc flat "I think the best soccer player in the world can be whatever he wants to be."
            show jayce surprised
            "It doesn't seem like Jason has a witty comeback for that one."
            voice "voice/leona/1/le_ja_scene1_6.ogg"
            mc happy "Getting to know someone means {i}really{/i} understanding that person. Not exactly 
                something you can do with a bunch of fangirls."
            je "..." 
            show jayce angry
            voice "voice/jayce/1/ja_scene1_10C.ogg"
            je "Then teach me."
            voice "voice/leona/1/le_ja_scene1_7.ogg"
            mc surprise "What?"
            show jayce happy
            voice "voice/jayce/1/ja_scene1_11A.ogg"
            je "A true master of the art always recognizes that he has more to learn. 
                Perhaps you can help me, Miss... Miss...?"
            voice "voice/leona/1/le_ja_scene1_8.ogg"
            mc angry "Why don't you start by learning to remember the name of the girl you're speaking with?"
            voice "voice/jayce/1/ja_scene1_12A.ogg"
            je "My sincerest apologies. Without a doubt, I would never forget the name of such 
                a dazzling -"
            voice "voice/leona/1/le_ja_scene1_9.ogg"
            mc flat"And enough with the gimmicky lines. You sound like you walked right out of a romance novel. 
                A bad one."
            show jayce surprised
            "A panicked look is plastered onto his dashing features. A straying thought of how
             entertaining it is to tease him briefly crosses my mind."
            voice "voice/leona/1/le_ja_scene1_10.ogg"
            mc flat "I'm [name]. And if you'll excuse me, I need to do some bad guy hunting! There's 
                a hacker on the loose."
            hide jayce
            "I brush off his attempts to prevent me from leaving, but I do hear his debonair
             voice call out:"
            voice "voice/jayce/1/ja_scene1_13A.ogg"
            je "See you later!"
            call gift_check("Jason") from _call_gift_check_10
            $ jayce_rp = jayce_rp + 7
            scene bg black with dissolve
            pause 0.5
            stop music fadeout 2.0
            jump events_end_period

        "I'll pass.":
            $ renpy.block_rollback()
            voice "voice/leona/1/le_ja_scene1_11.ogg"
            mc flat "I think I'll pass. Roses aren't really my thing."
            voice "voice/leona/1/le_ja_scene1_12.ogg"
            mc flat "Oh, and I think cheesy overtures from guys who don't even know my name aren't
                really my thing either."
            hide jayce
            show jayce surprised
            "Jason looks like he's never been turned down before."
            voice "voice/jayce/1/ja_scene1_14.ogg"
            je "Uh, overtures?"
            voice "voice/leona/1/le_ja_scene1_13.ogg"
            mc flat "Yes, like the classical music. Long, screechy, and boring to listen to."
            hide jayce
            show jayce happy
            voice "voice/jayce/1/ja_scene1_15.ogg"
            je "Ouch. You really know how to turn the screw."
            voice "voice/leona/1/le_ja_scene1_14.ogg"
            mc flat "At least I'm not afraid to speak my mind. Unlike you, Mr. Faker."
            hide jayce
            show jayce angry
            voice "voice/jayce/1/ja_scene1_16.ogg"
            je "Hey, that was just uncalled for. How about I prove to you that I'd like to know you better? 
                I promise I'll remember your name the next time we meet."
            mc flat "[name]."
            hide jayce
            show jayce happy
            voice "voice/jayce/1/ja_scene1_17A.ogg"
            je "I'll have to run into you in the hallway sometime."
            voice "voice/leona/1/le_ja_scene1_15.ogg"
            mc flat "Right, and maybe you can act like a normal person when you do."
            voice "voice/jayce/1/ja_scene1_18A.ogg"
            je "Jason is at your service."
            voice "voice/leona/1/le_ja_scene1_16.ogg"
            mc flat "I'll remember to call my knight in shining armor when I break a nail."
            "Knocking a jock off his high horse might be amusing, but I don't have time for this. 
             The hacker probably isn't sitting around talking to airheads, as good-looking as they may be."
            voice "voice/leona/1/le_ja_scene1_17.ogg"
            mc happy "Okay! I, uh, have to go."
            hide jayce with dissolve
            "I hear Jason chuckle as I walk away, my head spinning with conflicting thoughts."
            $ jayce_rp = jayce_rp + 2
            scene bg black with dissolve
            pause 0.5
            stop music fadeout 2.0
            jump events_end_period

label jayce_2:
    $ jayce_scene = 2
    $ renpy.block_rollback()
    scene bg fountain
    play music "music/ambient1.mp3" fadein 2.0
    "Not sure why I hadn't thought of looking through Summoner's Rift earlier. If there's a hacker 
     running around in the game, he's bound to leave some clues, am I right?"
    "Did I mention that I love the warping sounds? They're so awesome! But my admiration comes to end
     when a beam of blue light flashes; someone just recalled."
    "My vision slowly clears of all the stars after that blinding entrance, as I try to make out 
     the player. Whoever it is, he has a huge hammer."
    show jayce vr happymid at right with dissolve
    voice "voice/jayce/2/ja_scene2_1.ogg"
    ja "For a brighter tomorrow!"
    with hpunch
    "Jayce leaps into the air and smashes his hammer down with a powerful slam. A cloud of 
     electricity sparks all around him and forms a sparkling mist of energy."
    "He has a triumphant expression on his face that bears the faintest hint of a smirk.
     I can't help but be impressed."
    voice "voice/leona/2/le_ja_scene2_1.ogg"
    le surprise "Not bad, Jason. That's a cool hammer."
    hide jayce with dissolve
    show jayce vr happy with dissolve
    voice "voice/jayce/2/ja_scene2_2.ogg"
    ja "Why, thank you. But, I'm afraid I don't know a Jason - you can call me Jayce."
    "I was almost expecting him to say something stupid. On the contrary, he seems so relaxed now."
    voice "voice/leona/2/le_ja_scene2_2.ogg"
    le surprise "Well, in that case, you can refer to me as Leona, chosen of the - hey!! Don't eat that!"
    "Cuddling against my feet, a scuttle crab tries to nibble at the end of my sword. Its petite 
     teeth chomp away at the lining of my blade and I hear \"NOMNOM\"  as it chews on the metal."
    voice "voice/leona/2/le_ja_scene2_3.ogg"
    le surprise "Why is there a scuttle crab here? There aren’t supposed to be any jungle monsters at the fountain!"
    voice "voice/jayce/2/ja_scene2_3.ogg"
    ja "He must be lost. C’mon, let’s take him back to his home. I'll pave the way."
    hide jayce with moveoutleft
    "Jason's gentle maneuver as he wraps the creature in his hands catches me off guard. Those 
     athletic arms know the ways of tenderness and protection, not just flashy tricks to allure women."
    "I tread along cautiously behind him. Not because I want to - no, not that. Of course not.
     It's just not safe to go into the jungle alone! Who knows what's lurking in the bushes?"
    voice "voice/leona/2/le_ja_scene2_4.ogg"
    le flat "There were rumors that you were in the League of Legends Club, but to be honest, 
        I didn't know you actually had time to play the game." # uh girl you in da club with him.
    show jayce vr happy with dissolve
    voice "voice/jayce/2/ja_scene2_4.ogg"
    ja "I try to make time for it. I enjoy the freedom of Summoner's Rift. Nothing to stifle me, either."
    "Jason catches on to my inquisitive gaze as I attempt to imagine {i}him{/i} being troubled by anything."
    voice "voice/jayce/2/ja_scene2_5.ogg"
    ja "Hey now! I have problems, too. In here, I don't have to think about stuff like soccer and grades.
        And girls."
    "Even the people back at the fountain can probably hear my modest chuckle."
    voice "voice/leona/2/le_ja_scene2_5.ogg"
    le flat "You didn't quite strike me as the kind of guy who has issues at school."
    voice "voice/jayce/2/ja_scene2_6.ogg"
    ja "I just have to practice my game so I get even better for the next two years! Imagine what
        they would all say if I couldn't keep my title."
    show jayce vr surprised
    voice "voice/leona/2/le_ja_scene2_6.ogg"
    le flat "I think the Jason I know would still be the Jason everyone likes, even without the 
        incredible reputation."
    "Nothing but the whispers of the wind and swaying grass keeps us company as we approach 
     the dragon's lair."
    "Perhaps it's a habit of his to keep quiet when he doesn't know what to say."
    show jayce vr angry
    voice "voice/jayce/2/ja_scene2_7.ogg"
    ja "Hey, Leona."
    voice "voice/leona/2/le_ja_scene2_7.ogg"
    le flat "What is it?"
    show jayce vr happy
    voice "voice/jayce/2/ja_scene2_8.ogg"
    ja "Think I can punt this crab all the way to the river?"
    voice "voice/leona/2/le_ja_scene2_8.ogg"
    le surprise "Don't even think about it! What if it comes back trying to exact revenge?"
    "A quick look at the crab's squabbling and glowing, red eyes tell me my assumptions 
     aren't far off. Phew."
    voice "voice/jayce/2/ja_scene2_9.ogg"
    ja "Woah, there. I wasn't actually serious."
    voice "voice/leona/2/le_ja_scene2_9.ogg"
    le flat "What happened to the gentleman from earlier? You were so eager to return the 
        scuttle crab and make things right. I think I like you better that way."
    voice "voice/jayce/2/ja_scene2_10.ogg"
    ja "Really?"
    "His fingers stroke the bottom of his chin as he hums in thought. But, the 
     critter takes the chance to break free from its captor and scurries away, leaving 
     only tiny footprints behind."
    hide jayce with moveoutleft
    show jayce vr surprised with moveinright
    hide jayce with moveoutleft
    show jayce vr angry with moveinright
    hide jayce with moveoutleft
    voice "voice/leona/2/le_ja_scene2_10.ogg"
    le surprise "It's getting away!"
    show jayce vr angry with dissolve
    voice "voice/jayce/2/ja_scene2_11.ogg"
    ja "Shoot! That thing's faster than a rolling golem!"
    "We run after it but to no avail. Every time we corner the scuttle crab it scuttles 
     in a different direction, zigzagging here and there."
    voice "voice/jayce/2/ja_scene2_12.ogg"
    ja "I've got this! Accelerate!"
    show jayce vr angry at right
    hide jayce with moveoutleft
    "A glowing gate of light unfolds before me, exuding a slight magnetic pull towards the center 
     of the entrance. It consumes Jayce as he rushes pas tthe majestic glare, and {i}POOF!{/i} he's gone."
    "Now isn't a time for questions! I bolt straight through the portal, realizing that my 
     feet now have a touch of heightened agility."
    with hpunch
    "I'm fast! So fast that I trip over my own boots, and an \"Oof!\" emanates from below me 
     as I crash land to the damp grasslands."
    show jayce vr surprised with dissolve
    voice "voice/jayce/2/ja_scene2_13.ogg"
    ja "A-are you okay, Leona?"
    show jayce vr surprised
    voice "voice/leona/2/le_ja_scene2_11.ogg"
    le surprise "Oops... I mean, my apologies. I was simply taken by surprise."
    "My hands reach down to help Jayce regain his footing as he pushes himself off the ground.
     As his hands grip mine and those brazen red eyes fixate on my own, his face makes even a
     young, ripe tomato look pale."
    voice "voice/leona/2/le_ja_scene2_12.ogg"
    le flat "Hey, buddy. Don't stare directly at me for too long."
    show jayce vr surprised
    voice "voice/jayce/2/ja_scene2_14.ogg"
    ja "R-right. I'm alright."
    voice "voice/leona/2/le_ja_scene2_13.ogg"
    le surprise "Darn! That crab is long gone by now. Not even my Zenith Blade can catch it."
    "It isn't until we pass by the entrance to the dragon pit that the crab comes rushing back to us, 
     and then zooms by into the nearest burrow."
    show jayce vr angry
    voice "voice/leona/2/le_ja_scene2_14.ogg"
    le surprise "Was that the-"
    with hpunch
    "The roar of Vilemaw doesn't trail too far behind the poor, trembling creature. Its hissing
     radiates a mystic aura that encompasses a web of string." 
    voice "voice/jayce/2/ja_scene2_15.ogg"
    ja "What the-! That thing doesn’t even spawn on this map!"
    "Neither of us are equipped enough to take down this jungle boss. I think we should run,
     but looking at Jayce, he doesn't seem to hold the same impression."
    $ renpy.block_rollback()

    menu:
        "Run as fast as the wind and take Jayce with me!":
            $ renpy.block_rollback()
            voice "voice/leona/2/le_ja_scene2_15.ogg"
            le flat "Jayce! Quick. On my word, run. I'll use Solar Flare to stun it for a few seconds."
            show jayce vr surprised
            voice "voice/jayce/2/ja_scene2_16.ogg"
            ja "What! I'm not leaving you behind."
            voice "voice/leona/2/le_ja_scene2_16.ogg"
            le angry "It's not up for debate - just do it!"
            "If it wasn't for the stupid spider dilemma right now, I'd probably be laughing
             at the ridiculous face that Jayce was wearing. He wants to tell me I'm crazy. Cute."
            "...I so didn't just call him that."
            voice "voice/leona/2/le_ja_scene2_17.ogg"
            le angry "Rally to me... and now! Go!"
            "A spinning ray of light thunders down from the skies, seizing the monstrous
             creature that was just moments ago rampaging the fields."
            show jayce vr angry at right
            hide jayce with moveoutleft
            "Not a split second later, Jayce and I use his Acceleration Gate to boost us
             through the next forty yards."
            "It takes a moment of huffs and puffs to be thankful to see familiar faces at the shop
             - even Viktor's. But I regret thinking that as soon I as do."
            show jayce vr angry at right with moveinright
            "He's been chugging a couple red potions to heal from a very apparently difficult 
             battle, and I can tell Jayce has a few punchlines up his sleeves."
            show jayce vr happy at right with dissolve
            show vik vr flat at left with dissolve
            voice "voice/jayce/2/ja_scene2_17.ogg"
            ja "I guess even \"superior constructs\" still have moments of weakness."
            "Ooh, I think he just went for the jugular."
            voice "voice/jayce/2/ja_vi_scene2_1.ogg"
            vi "I am bound by the limitations of this game mode. It is not possible to 
                eliminate useless teammates. If not, I would vaporize you in an instant."
            voice "voice/jayce/2/ja_scene2_18.ogg"
            ja "Jeez, you're just like a Saturday morning cartoon villain."
            voice "voice/leona/2/le_ja_scene2_18.ogg"
            le flat "We're on the same team, guys. No need for petty side battles."
            voice "voice/jayce/2/ja_vi_scene2_2.ogg"
            vi "Hmph."
            hide vik with moveoutleft
            "Viktor says no more as he returns to the battle field, leaving behind nothing 
             but a bad taste in our mouths."
            voice "voice/leona/2/le_ja_scene2_19.ogg"
            le angry "There was no need to provoke him, Jayce."
            hide jayce with dissolve
            show jayce vr happy with dissolve
            voice "voice/jayce/2/ja_scene2_19.ogg"
            ja "I wasn't. I just wanted to take note of his... less-than-superior features."
            voice "voice/jayce/2/ja_scene2_20.ogg"
            ja "Not to mention that guy is such a {i}nerd{/i}! I bet his only friends are robots
                and chat bots."
            voice "voice/leona/2/le_ja_scene2_20.ogg"
            le flat "You shouldn't make fun of people for their interests, even if {i}you{/i} don't
                think it's cool."
            hide jayce
            show jayce vr angry with dissolve
            "Jayce purses his lips and forms wrinkles on the top of his forehead.
             Or maybe they're stress lines?"
            voice "voice/jayce/2/ja_scene2_21.ogg"
            ja "You're right. Sorry."
            voice "voice/leona/2/le_ja_scene2_21.ogg"
            le flat "Well, as long as you know that you could have handled that better."
            "I think his contrite expression is enough of a good-bye as my fingers motion over 
             the \"QUIT\" option on the menu screen."  
            hide jayce with dissolve
            $ jayce_rp = jayce_rp + 8
            scene bg black with dissolve
            pause 0.5
            stop music fadeout 2.0
            jump events_end_period

        "Can't surrender now; we have to prepare to fight!":
            $ renpy.block_rollback()
            voice "voice/leona/2/le_ja_scene2_22.ogg"
            le happy "It's the ancient duty of the Solari to banish the darkness. There's no way I'm gonna
                back down now. Are you ready, Jayce? It's time to prove your worth as a MAN!"
            show jayce vr happy
            voice "voice/jayce/2/ja_scene2_22.ogg"
            ja "Watch me solo this guy. I'm going in!"
            voice "voice/leona/2/le_ja_scene2_23.ogg"
            le surprise "Wait – let me use my Solar Flare to stun it!"
            hide jayce with moveoutleft
            "Jayce runs in before I can even react, the golden glow of his hammer lighting the way
             in the shadow of the giant spider. He deftly dodges its huge, crushing legs. 
             I have no choice but to follow after him."
            "I have to protect Jayce."
            voice "voice/leona/2/le_ja_scene2_24.ogg"
            le surprise "You'll have to get through me first, Vilemaw!"
            voice "voice/leona/2/le_ja_scene2_25.ogg"
            le surprise"Jayce? Where are you?!"
            with hpunch
            "My heart stops when I realize that I can't see him anymore. Amidst the massive webs,
             eight unblinking eyes loom before me."
            "I take cover under my shield to deflect a spray of venom. As I get down, 
             my shield clangs as it hits something metal. Jayce lies at my feet... not moving."
            "The two of us are enveloped in a bubble of purple light."
            un "Our wills align."
            with fade
            show char shen at left with dissolve
            "Somehow I didn't notice that a ninja appeared out of nowhere. He's strong enough to grab
             us both, and we dash through the shadows to safety. Then I recognize that it's our club advisor."
            "I don't know what would have happened if Mr. Zen – er, Shen – didn't rescue us from Vilemaw.
             I'm about to voice my thanks when he puts up a hand to shush me."
            s "My students did not demonstrate superior judgement today."
            show jayce vr angry at right with dissolve
            ja "..."
            s "The Eye of Twilight must preserve balance in other lanes."
            "He teleports away without another word. Mr. Zen is much more talkative offline."
            hide char with dissolve
            voice "voice/leona/2/le_ja_scene2_26.ogg"
            le flat "I guess ninjas are supposed to act mysterious."
            "Jayce doesn't say anything. I don't know if he's too beat up or if he's thinking about
             something, or both. He looks down, away from me."
            voice "voice/leona/2/le_ja_scene2_27.ogg"
            le happy "At least we didn't have to respawn."
            voice "voice/jayce/2/ja_scene2_23.ogg"
            ja "...Don’t tell anyone this happened..."
            voice "voice/leona/2/le_ja_scene2_28.ogg"
            le happy "Why? Are you embarrassed?"
            voice "voice/jayce/2/ja_scene2_24.ogg"
            ja "...No."
            voice "voice/leona/2/le_ja_scene2_29.ogg"
            le flat "I think you're not telling the truth."
            "I'd cross my arms if I wasn't holding a sword and shield."
            voice "voice/jayce/2/ja_scene2_25.ogg"
            ja "I hope Mr. Zen doesn't say anything at the next meeting. I better go talk to him right now."
            voice "voice/leona/2/le_ja_scene2_30.ogg"
            le flat "You're making a big deal out of this. We just got caught off-guard and things got out of hand."
            hide jayce with dissolve
            "With the last of whatever mana he has, Jayce uses an Acceleration Gate to get us back
             to the fountain."    
            $ jayce_rp = jayce_rp + 19
            scene bg black with dissolve
            pause 0.5
            stop music fadeout 2.0
            jump events_end_period

label jayce_3:
    $ jayce_scene = 3
    $ renpy.block_rollback()
    scene bg classroom day
    play music "music/bedroom.mp3" fadein 2.0
    "As much as I have been putting my heart and soul into finding that wretched hacker,
     my mind has been distracted lately."
    "Mr. Zen mentioned that he'd be in the classroom today. He can help me think of ways to
     track down the culprit."
    "I take a seat closest to the window at the front of the classroom, placing my notebooks of
     research and observations on the desk."
    "Now, I can finally get my mind off of -"
    voice "voice/jayce/3/ja_scene3_1.ogg"
    je "Mind if I sit next to you, miss?"
    show jayce happy at left with moveinleft
    "An oh-so-recognizable face peeks from the corner of my eye. Just the guy I want to see! ...{i}Not{/i}."
    "Don't get me wrong. He's a... nice guy. But because of him, I haven't been able to really 
     dig into the League of Legends investigation."
    show jayce happy with dissolve
    voice "voice/jayce/3/ja_scene3_2.ogg"
    je "So, do you know anything about soccer?"
    voice "voice/leona/3/le_ja_scene3_1.ogg"
    mc happy "Just that you kick a ball and try to get it into the goal. I think my favorite part would
        have to be the sun - you can feel its warmth all day long."
    voice "voice/jayce/3/ja_scene3_3.ogg"
    je "Yeah, I did notice the blaring heat on that day against Noxus. You know,
        when I made that glorious kick that won us the game in the world championships."
    voice "voice/leona/3/le_ja_scene3_2.ogg"
    mc happy"Right! You were facing... Darius, I think. He was the goalkeeper."
    "I still remember all the cheering. It was raining cats and dogs with all the shouts of praise that day."                                                                                                              
    voice "voice/jayce/3/ja_scene3_4.ogg"
    je "It wasn't an easy feat, that's for sure. And the pressure of three-hundred thousand people 
        scrutinizing every move I make was anything but pleasant."
    "Everyone, including me, marveled at the stadium design, with its steep seating that allowed us 
     to feel close to the action. I only went because Gwen dragged me along."
    voice "voice/jayce/3/ja_scene3_5.ogg"
    je "Sometimes I get the feeling that the scorpion kick was just a fluke. But that's what got 
        me the unanimous election to captainhood, I guess."
    voice "voice/leona/3/le_ja_scene3_3.ogg"
    mc flat "Fluke or not, you {i}did{/i} make the victory shot. You deserve every award you got."
    "His smile was like its own victory shot... right into my heart."
    voice "voice/leona/3/le_ja_scene3_4.ogg"
    mc shyblush "By the way, what are you even doing here? This isn't even your classroom."
    show jayce angry
    voice "voice/jayce/3/ja_scene3_6.ogg"
    je "Is it a crime to see the girl I like?"
    voice "voice/leona/3/le_ja_scene3_5.ogg"
    mc shyblush "W-what?! A girl you... what are you saying?!"
    show jayce happy
    voice "voice/jayce/3/ja_scene3_7.ogg"
    je "Hahaha. You're so cute when you're flustered."
    "Grrr. This guy! See what I mean? How am I supposed to concentrate with all his nonsense?"
    voice "voice/jayce/3/ja_scene3_8.ogg"
    je "Speaking of girls I like, I actually might have a date this year. Last year during
        the Spring Fling, I was cooped in my room hacking away at my hammer."
    voice "voice/jayce/3/ja_scene3_9.ogg"
    je "It was an unenventful evening to say the least."
    mc angry "..." #angry
    voice "voice/jayce/3/ja_scene3_10.ogg"
    je "Sorry~ Forgive me. Tell me what you did... please?"
    voice "voice/leona/3/le_ja_scene3_6.ogg"
    mc happy "... Last year I went stargaziging with Sharon. We caught sight of a few shooting stars. 
        I don't think you need to have a date to enjoy a school dance."
    voice "voice/jayce/3/ja_scene3_11.ogg"
    je "Maybe you're right. You think we could - "
    hide jayce with fade
    ### VOICEUUU? ###
    un "You should go back to kindergarten and make chalk pictures on the sidewalk!"
    show rumble flat at right with dissolve
    "Daniel's desk was only a few away from mine and a crowd slowly gathered around him.
     Colored pencils lay across the edges of his table and his notebook was filled with sketches of the sun."
    "I catch a glimpse of arm bands wrapped around some of the students. They were privileged
     accessories only worn by the top athletes of Summoner Academy."
    voice "voice/leona/3/le_ja_scene3_7.ogg"
    mc surprise "Hey! Aren't those guys on the soccer team? You're the captain – you can't let your 
        fellow teammates act like this."
    show jayce surprised at left with dissolve
    voice "voice/jayce/3/ja_scene3_12.ogg"
    je "Well, I'm only captain on the soccer field..."
    "Ugh. What's with the cop-out of the century?!"
    $ renpy.block_rollback()

    menu:
        "Berate Jason to do the right thing.":
            $ renpy.block_rollback()
            voice "voice/leona/3/le_ja_scene3_8.ogg"
            mc angry "What, are you going to hide behind the facade of the \"perfect\" high school
                soccer star and not stand up for your classmate?"
            show jayce angry at left
            voice "voice/jayce/3/ja_scene3_13.ogg"
            je "It's not like it's any of our business."
            voice "voice/leona/3/le_ja_scene3_9.ogg"
            mc angry "I can't believe you. A {i}real{/i} gentleman would do the honorable thing of 
                defending his fellow colleagues."
            "It isn't until the feet of my chair paint black streaks on the floor after shoving it
             aside that Jason takes action."
            "There's a newfound glint in Jason's eyes as he approaches the band of soccer players."
            hide jayce with moveoutright
            hide rumble
            voice "voice/jayce/3/ja_scene3_14.ogg"
            je "Hey, back off."
            un "Dude... Don't tell me you're defending this runt."
            voice "voice/jayce/3/ja_scene3_15.ogg"
            je "There's no need for namecalling. We're all students of the same school."
            un "Tch. Just because you're the captain."
            show jayce happy with dissolve
            show rumble flat at right with dissolve
            "Their pouting faces are the last of whatever is left of their deplorable attitude
             in the room, and Daniel nods his head as an indication of his thanks."
            hide rumble with moveoutright
            voice "voice/leona/3/le_ja_scene3_10.ogg"
            mc happy "I'm glad you did that, although it was a bit... clumsy. Heh."
            show jayce blush
            voice "voice/jayce/3/ja_scene3_16.ogg"
            je "Likewise."
            "We both exchange smiles that soon erupt into synonymous laughter - and one that's
             contagious. Even students who didn't witness the scene were chuckling."
            call gift_check("Jason") from _call_gift_check_11
            $ jayce_rp = jayce_rp + 19
            scene bg black with dissolve
            pause 0.5
            stop music fadeout 2.0
            jump events_end_period
            
        "Stand up for Daniel myself.":
            $ renpy.block_rollback()
            "I make sure that all the feelings of disappointment and frustration roll back onto
             Jason as I shoot a glaring scowl at him, all while marching toward the surly juniors 
             continuing to belittle poor Daniel."
            with hpunch
            pause 0.3
            with hpunch
            "Flinging the clenched fists onto a random table definitely caught everyone's attention.
             Even Mr. Zen awoke from his lackluster slumber."
            voice "voice/leona/3/le_ja_scene3_11.ogg"
            mc angry "Pick someone your own size, punks."
            voice "voice/jayce/3/BULLY1.ogg" #MICHAEL
            un "Yea? What's it to you?"
            voice "voice/leona/3/le_ja_scene3_12.ogg"
            mc flat "You're all dastardly people who need to learn some manners."
            voice "voice/jayce/3/BULLY2.ogg"
            un "Like you're one to talk - butting into someone else's conversation."
            voice "voice/leona/3/le_ja_scene3_13.ogg"
            mc flat "You talk so loud that even Cleopatra would raise from the dead."
            "Before I could hurl any more of my outrage at them, an arm descends from above my
             head to imepede the argument."
            show char shen at left with dissolve
            voice "voice/jayce/3/ja_zen_scene3_1.ogg"
            s "There is no need for insults, even when defending your friends, [name]."
            voice "voice/leona/3/le_ja_scene3_14.ogg"
            mc surprise "I was just - I'm sorry."
            "That large, stern hand that was used to diffuse a heated alteraction is now comforting 
             my discouraged concerns with a pat on the head."
            voice "voice/jayce/3/ja_zen_scene3_2.ogg"
            s "Advisory period will now consist of strictly verbal silence. No one has permission to 
               speak until class commences."
            hide char
            "My treading is met with a gaze from Jason, who drags his feet across the room as an adieu. 
             Thanks for the help, knight in shining armor."
            $ jayce_rp = jayce_rp + 9
            scene bg black with dissolve
            pause 0.5
            stop music fadeout 2.0
            jump events_end_period                                     

label jayce_4:
    $ jayce_scene = 4
    $ renpy.block_rollback()
    scene bg park day
    "You know what's silly? Me, waiting for Jason. At the park. \"Let's go on a date!\" he says." #blush
    play music "music/Market Breeze.mp3" fadein 2.0
    "I don't really have time for this. If it weren't for those charming, crimson eyes of his and 
     the way his soft strands of midnight hair massage the air with its delicate weave..."
    "... and the nape of his neck so pristine; elegance emitting from every inch of his dreamy build,
     and not to mention his enticing smile of perfection... Yea, if it wasn't for that, I'd be long gone by now."
    "Even as he dashes up to me after spotting me underneath the shades of a sakura tree, he still shines brilliantly."
    show jayce happy with moveinright
    voice "voice/jayce/4/ja_scene4_1.ogg"
    je "Hey! Thanks for coming."
    voice "voice/leona/4/le_ja_scene4_1.ogg"
    mc surprise "N-no problem. But I didn't know you were into this kind of thing."
    "Today is special. It's the annual Inventor's Fair. Bundles of technological innovations 
     surround all the students, parents, faculty, and everyone who is anyone."
    "In one corner stood an automatic skateboard, motorized by a solar-powered fan. There was
     a clever laser-guided pair of scissors by the tables; it drew a temporary red line directing your
     hands where to cut for flawless accuracy."
    show jayce blush
    voice "voice/jayce/4/ja_scene4_2.ogg"
    je "Oh! Uh. I'm not into it that much. I thought it was interesting."
    voice "voice/leona/4/le_ja_scene4_2.ogg"
    mc happy "Really, now? Why do I get the hunch that's not exactly how you feel?"
    show jayce angry
    je "..."
    voice "voice/jayce/4/ja_scene4_3.ogg"
    je "I... didn't have time to enter this year with all the extra soccer practice."
    "A smile slowly eases onto my face, glad to see Jason learning to open up honestly."
    voice "voice/jayce/4/ja_scene4_4.ogg"
    je "Sometimes, it's hard for people to understand how these creations can {i}truly{/i} help society.
        There's no question that our future will be bright."
    show jayce happy
    voice "voice/jayce/4/ja_scene4_5.ogg"
    je "To make progress, you need to appreciate the intracicies of design and imminent development of
        our paths to greatness."
    voice "voice/leona/4/le_ja_scene4_3.ogg"
    mc sad "You almost sound like Cyrus."
    show jayce blush
    voice "voice/jayce/4/ja_scene4_6.ogg"
    je "No! I'm nothing like that psycho mechanist. I look at a brighter tomorrow, but him... 
        He's all about his own selfish ambitions: improving himself, not others."
    "Muddled voices of student chatter drown out the slight murmurs of the blowing leaves."
    show jayce blushhappy
    voice "voice/jayce/4/ja_scene4_7.ogg"
    je "I really want to get into engineering after graduation. Make stuff - 
        stuff that actually helps, not frivolous gadgets."
    "He says it with such hardheaded determination that when he looks at me, I let out a little jolt."
    show jayce happy
    voice "voice/jayce/4/ja_scene4_8.ogg"
    je "What about you? What will you do?"
    "My head makes it way down to my feet, following the cemented sidewalk that arches its way 
     through the blanket of trees standing not too far away."
    voice "voice/leona/4/le_ja_scene4_4.ogg"
    mc flat "My parents want me to take over the family business."
    show jayce surprisedmid with dissolve
    voice "voice/jayce/4/ja_scene4_9.ogg"
    je "That's cool. What is it?"
    voice "voice/leona/4/le_ja_scene4_5.ogg"
    mc flat "No. It's not. They run Rakkor Boxing."
    show jayce surprised2close with dissolve
    voice "voice/jayce/4/ja_scene4_10.ogg"
    je "What?! {i}The{/i} Rakkor Boxing? Don't they have legendary fighters that hold all 
        the pride and respect in the boxing world?"
    hide jayce with dissolve
    show jayce surprisedmid with dissolve
    voice "voice/leona/4/le_ja_scene4_6.ogg"
    mc sad "There is more to than meets the eye, Jason. My parents are only interested in profits and totally disregard any ethics behind their 
        practices. They've exploited many of my friends in their young boxers program."
    hide jayce with dissolve
    show jayce angry at left with dissolve
    "My family spiel comes to a halt when Jason stumbles onto the trunk of a nearby tree, 
     muttering under his breath in pain."
    voice "voice/jayce/4/ja_scene4_11.ogg" # BRUH LOL
    je "Ow ow. Ow."
    voice "voice/leona/4/le_ja_scene4_7.ogg"
    mc surprise "What's wrong? Are you okay?"
    voice "voice/jayce/4/ja_scene4_12.ogg"
    je "Yea, it's nothing really."
    with hpunch
    hide jayce with moveoutleft
    "Again, with the hiding! I push him hard enough that he would gently fall onto the patch of 
     grass below him, and he makes a graceful \"thud\" as he lands."
    voice "voice/jayce/4/ja_scene4_13.ogg"
    je "What are you do - Ow!!"
    "The suffering he endures this time isn't from his injury but from my hand clamping down
     on his obviously swollen ankle."
    voice "voice/leona/4/le_ja_scene4_8.ogg"
    mc angry "{i}This{/i} is nothing?" # angry
    show jayce happy with dissolve
    voice "voice/jayce/4/ja_scene4_14.ogg"
    je "Aha. Guess you found out."
    mc angry "..." # angry
    show jayce angry
    voice "voice/jayce/4/ja_scene4_15.ogg"
    je "Sorry, but can you keep it a secret between us? There's an important game tomorrow
        against Ionia Senior High and everyone is relying on me."
    voice "voice/leona/4/le_ja_scene4_9.ogg"
    mc angry "Save me the excuses. You need proper rest."
    voice "voice/jayce/4/ja_scene4_16.ogg"
    je "It's the qualifiers match into the All-Stars League. My teammates would kill me if I missed it."
    voice "voice/leona/4/le_ja_scene4_10.ogg"
    mc flat "You're hung up on what everyone thinks of you. Again."
    "Jason's eyes flash a mountain of remorse as my words shred through every bit of confidence
     he held in his voice."
    voice "voice/leona/4/le_ja_scene4_11.ogg"
    mc sad"You need to start worrying about yourself and not the judgments of others. Or else..."
    "... You could get really hurt."
    "Of course, I keep that to myself. I'm not going to give him the benefit of knowing how
     concerned I am about him. That's too good for this idiot."
    hide jayce
    "I leave him struggling to stand back up. Jason doesn't say a word as I head toward 
     the other end of the science fair, and a long ways away from him."
    $ jayce_rp = jayce_rp + 10
    scene bg black with dissolve
    pause 0.5
    stop music fadeout 2.0
    jump events_end_period

label jayce_5:
    $ jayce_scene = 5
    $ jayce_rp = jayce_rp + 17
    $ renpy.block_rollback()
    # Jason meets her somewhere. They hug. He ditches the soccer practice to meet MC.
    scene bg soccer day
    play music "music/Smooth Sailing.mp3" fadein 2.0
    "The whistle blows, calling for the end of the sprint-back pedal repeats." 
    "I see Jason casually wiping away his sweat with his forearms with a smile bright enough 
     to shame the sun... Ugh, I have work to do."
    "But I can't help looking at his gorgeous figure. He's prepping for the next exercise in his No. 
     8 jersey."
    "Being able to attack mid-range while closing gaps, huh? I guess there's no position better 
     suited for him."
    "I close my eyes and smile while taking in the light breeze, the direct sunlight, and the 
     heavy voices that dart across the field. I open up my eyes again only to see Jason's 
     shining white teeth beaming at me."
    voice "voice/leona/5/le_ja_scene5_1.ogg"
    mc surprise "Geh, caught red-handed."
    "As soon as the next drill ends, I already see him running in my direction."
    show jayce blushhappy with dissolve
    voice "voice/jayce/5/ja_scene5_1.ogg"
    je "Hey, [name]! If you were here to watch me, I could've introduced you to the members if you 
        told me earlier."
    "Oh, that beautiful smile plastered all over his face is absolutely mesmerizing."
    "But I can't let him know that!"
    voice "voice/leona/5/le_ja_scene5_2.ogg"
    mc happyblush "As if - I don't want to boost your ego any more than it already has." #Flirty
    show jayce blush
    voice "voice/jayce/5/ja_scene5_2.ogg"
    je "Aha, your jokes can be pretty harsh sometimes."
    voice "voice/leona/5/le_ja_scene5_3.ogg"
    mc flat "Who says it's a joke?"
    voice "voice/leona/5/le_ja_scene5_4.ogg"
    mc happy "...Just kidding. But anyway, why do you have your jersey on during practice?"
    show jayce happy
    voice "voice/jayce/5/ja_scene5_3.ogg"
    je "You never know when a foxy lady impressed by my macho reputation might pass by."
    "A sigh sneaks past my lips accompanied by a slight smile, again falling victim to his upbeat attitude."
    voice "voice/leona/5/le_ja_scene5_5.ogg"
    mc happy "Do as you please~"
    show jayce blushhappy
    voice "voice/jayce/5/ja_scene5_4.ogg"
    je "Oh, really?"
    "Jason shines another smile. This time, a little more daring or even...mischievous. And with 
     that he takes me by the arm."
    show jayce happyclose
    voice "voice/leona/5/le_ja_scene5_6.ogg"
    mc shyblush "W-what are you doing?!"
    "Of course he doesn't allow me the answer as he pulls me along, leaving behind only the confused 
     expressions of his fellow teammates."
    hide jayce with dissolve
    stop music fadeout 1.0
    scene bg park day
    play music "music/Market Breeze.mp3" fadein 2.0
    voice "voice/leona/5/le_ja_scene5_7.ogg"
    mc happy "The soon-to-be captain of the regional high school team skipping practice? Are you sure this is a good idea?"
    show jayce blushhappymid
    voice "voice/jayce/5/ja_scene5_5.ogg"
    je "Not at all!"
    voice "voice/leona/5/le_ja_scene5_8.ogg"
    mc happyblush "... I don't understand you sometimes."
    "Even I can't deny the smirk creeping into the edge of my lips. I'm here, alone with Jason."
    show jayce blushclose
    "The gaze of his eyes penetrates the deepest part of my hearts; so heavy yet profound. 
     Nothing like the devious little child that he was a few days ago."
    voice "voice/jayce/5/ja_scene5_6.ogg"
    je "Ever since fate entertwined us, I've thought about what you've said about being truer to myself. 
        And that's what got us right here, right now."
    "W-what's with this unexpected change of pace?! I can feel my face burning with embarrassment."
    hide jayce with dissolve
    scene cg jayce end with fade
    voice "voice/jayce/5/ja_scene5_7.ogg"
    je "I really am thankful to whoever led you to tread the grassy fields that day I met you and that we 
        could spend all this time together."
    voice "voice/leona/5/le_ja_scene5_9.ogg"
    mc shyblush "...But I'm just your average girl doing average things. I don't have special hobbies like you nor 
        the big dreams that I hope to achieve one day. All I can do is be there for you and support yours."
    voice "voice/jayce/5/ja_scene5_8.ogg"
    je "Hey, don't go all spouting all this teenage angst on me now. You'll sound just like me! And that's my job."
    voice "voice/jayce/5/ja_scene5_9.ogg"
    je "I don't need you to be special or the next HotShot. I just need you by my side. You 
        support me with your straightforward attitude and make sure I don't stray from my path."
    voice "voice/jayce/5/ja_scene5_10.ogg"
    je "I can't dream of anything more glamorous than that. So let's face the future together, okay?"
    "He subtly leans against me while lying his gentle, soft head on top of mine."
    "The sun slowly starts to dim. The scent of the fresh air. His warm, sincere presence leaning against me. 
     The comfort that surrounds me in this sublime silence... I wish we could just stay like this forever."
    voice "voice/leona/5/le_ja_scene5_10.ogg"
    mc shyblush "Ahem. Well I guess there's nothing to do other than for me to do my best as well." #Flirty
    voice "voice/jayce/5/ja_scene5_11.ogg"
    je "Yeah."
    scene bg black with dissolve
    if bosses_defeated == 3:
        voice "voice/leona/5/le_ja_scene5_11.ogg"
        mc happyblush "Hey, want to play some League together tonight?"
        voice "voice/jayce/5/ja_scene5_12.ogg"
        je "Without fear."
    pause 0.5
    stop music fadeout 2.0
    jump events_end_period