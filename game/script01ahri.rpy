######################################### EVENT DECLARATION
init:
    $ event("ahri_1", "act == 'library'", event.once(), "route == 'Ezreal'", priority = 190)
    $ event("ahri_2", "act == 'vr'", event.once(), event.depends("ahri_1"), priority = 180)
    $ event("ahri_3", "act == 'museum'", event.once(), event.depends("ahri_2"), "day >= 3", priority = 170)
    $ event("ahri_4A", "act == 'library'", event.once(), event.depends("ahri_3"), "ahri4_flag == True", priority = 160)
    $ event("ahri_4B", "act == 'vr'", event.once(), event.depends("ahri_3"), "ahri4_flag == False", priority = 160)
    $ event("ahri_5A", "act == 'vr'", event.once(), event.depends("ahri_4A") or "ahri5_flag == True", priority = 150)
    $ event("ahri_5B", "act == 'vr'", event.once(), event.depends("ahri_4B"), priority = 150)
    $ event("ahri_6", "act == 'vr'", event.once(), event.depends("ahri_5A"), priority = 140)
    $ event("ahri_7", "act == 'park'", event.once(), event.depends("ahri_6"), "ahri_rp >= 70", priority = 130) # need to rewrite scene to start in park

######################################### AHRI SCRIPT
label ahri_1:
    $ ahri_scene = 1
    $ renpy.block_rollback()
    scene bg library
    play music "music/ambient2.mp3" fadein 2.0
    "I walk to the library, hoping that I could find some information about the hacker."
    show ahri happy2 at left with dissolve
    "However, quickly after entering, I notice Ami sitting close by."
    "She doesn’t seem to have noticed me, and I can’t decide if I should get her attention..."
    "Ami is one of the most well-known club members, and she is infamous throughout the school for 
     different reasons."
    "In the real world, she is Ami Kaminoka, the sole heir to the Kaminoka family: a fabulously wealthy 
     group that pays little mind to outsiders."
    "She always maintains an elegant air about her - one that seems to both draw you in, 
     and push you away."
    "However, her alter ego, \"Ahri, the Nine-Tailed Fox\", is anything but reserved. Like her or 
     not, no one can resist her charms."
    "She’s already developed a large fanbase; it’s surprising her sharp tongue and quick wits 
     actually worked in her favor to this regard."
    "Although it may not be the most proper hobby for such an esteemed goddess, 
     only a select few know about the face behind the character."
    "–however, be that as it may, I find it difficult to speak a word to her, in fear of being quickly 
     shut down. I've never seen her associate with anyone, much less someone like me. 
     Still, I have no choice. 
     I prepare myself for the worst, taking a deep breath..."
    show ahri surprised at center with dissolve
    voice "voice/ezreal/1/ez_ah_scene1_1.ogg"
    mc happy "Oh! Hey Ami, how’s it going?"
    show ahri angry at center with dissolve
    voice "voice/ahri/1/ah_scene1_1.ogg"
    am "Oh... [name]. What brings you here? Finally doing some real work for once?"
    "Unsurprisingly, she’s quick to start attacking me.."
    voice "voice/ezreal/1/ez_ah_scene1_2.ogg"
    mc flat "It's good to see that you know me already. Better than being completely ignored, I guess..." # voice says "already know me already
    voice "voice/ahri/1/ah_scene1_2.ogg"
    am "Don't think that just because I know you means I desire to help you. 
        You may as well just be another piece of trash, blowing in the wind that is this underachieving school."
    "And there’s the infamous kick in the gut..."
    voice "voice/ahri/1/ah_scene1_3.ogg"
    am "If even the developers can't catch the hacker, 
        what makes you believe that someone of your caliber would be able to produce any results?"
    voice "voice/ahri/1/ah_scene1_4.ogg"
    am "You won't find anything useful here. You may as well just quit while you're ahead."
    voice "voice/ezreal/1/ez_ah_scene1_3.ogg"
    mc flat "I didn't come here to ask for your advice - running into you was just a coincidence."
    voice "voice/ahri/1/ah_scene1_5.ogg"
    am "Oh... are you implying that I'm not worth asking?"
    voice "voice/ezreal/1/ez_ah_scene1_4.ogg"
    mc shyblush "N-No, I-"
    voice "voice/ahri/1/ah_scene1_6.ogg"
    am "Forget it. Just leave already..."

    menu:
        "I might as well do some research before searching aimlessly like the others.":
            $ renpy.block_rollback()
            "She obviously doesn’t like me all that much. 
             But, I guess being approached by strangers can get pretty tiresome after a while."
            "When all’s said and done, she despises commoners in general, not me because of me— I hope..."
            "If that is the case, then, as the one who started the conversation, 
             I have the responsibility of giving her a legitimate response."
            voice "voice/ezreal/1/ez_ah_scene1_5.ogg"
            mc flat "Well, there's a lot of people flooding the servers looking for clues within the game, 
                so I thought it’d be more efficient to check the road less ventured."
            voice "voice/ezreal/1/ez_ah_scene1_6.ogg"
            mc flat "Whatever they find inside the game will be known to the general public anyways, 
                so I figured I might as well check something other than the forums."
            show ahri surprised at center with dissolve
            voice "voice/ahri/1/ah_scene1_7.ogg"
            am "That does make sense... in a [name] sort of way."
            voice "voice/ezreal/1/ez_ah_scene1_6.5.ogg"
            mc shyblush "Uhh... thanks? I guess?"
            "I turn to leave, when Ami reaches out towards me, as if to stop me."
            show ahri angry at center with dissolve
            voice "voice/ahri/1/ah_scene1_8.ogg"
            am "Hey, [name]... before you start browsing the shelves, you should probably come up with a plan."
            voice "voice/ahri/1/ah_scene1_9.ogg"
            am "Otherwise, you're liable to waste your time. And that would be a shame, 
                considering the circumstances."
            "Unable to comprehend what has just occurred, I just stand there with my mouth open."
            "After believing she was just a cold-hearted demon from all those rumors just makes me feel all the more 
             flabbergasted by the current situation."
            "It’s not that she showed me any special form of kindness. 
             All she did was give me a reasonable opinion, but even just that makes me feel so much more at ease."
            "–or, that's what I’d like to say, but all that comes out of my mouth is a stifled squeak."
            voice "voice/ezreal/1/ez_ah_scene1_7.ogg"
            mc happy "I... didn't think of that. Well, I appreciate the kind help!"
            show ahri surprisedblush at center with dissolve
            voice "voice/ahri/1/ah_scene1_10.ogg"
            am "Kind...? 
                W-Wait, I didn't mean it like that! I was just trying to expedite things!"
            voice "voice/ezreal/1/ez_ah_scene1_8.ogg"
            mc happyblush "I dunno... it seemed to me like you really cared about me."
            show ahri angry at center with dissolve
            voice "voice/ahri/1/ah_scene1_11.ogg"
            am "That's not... you're just... I..."
            "She puts her book squarely over her face, to hide what appear to be blushing cheeks. 
             I can't understand this girl."
            "Figuring she won't be willing to talk to me any further, I amble away from the table."
            call gift_check("Ami") from _call_gift_check_12
            scene bg black with dissolve
            pause 0.5
            stop music fadeout 2.0
            $ ahri_rp = ahri_rp + 7
            jump events_end_period
            
        "Truth be told I just wanted to see what type of person you are.": #tense grammar, wanted vs want
            $ renpy.block_rollback()
            "This conversation is going nowhere. 
             I figure that if I can't talk with her, I might as well try to throw her off guard."
            voice "voice/ezreal/1/ez_ah_scene1_9.ogg"
            mc happy "Actually, I just wanted to see if the rumors were true. You know, whether you're an ice queen. 
                But, I have to say, they were right."
            show ahri angryclose at center with dissolve
            # The purpose of this isn't purely just for comedic purposes. In the long run this option could help unlock a small extra scene about how this bluntness is what helped her
            # better realize how people may view her due to her current guise.
            # In the long-run, this event may have been the better choice when it comes to unlocking more scenes with the heroine.
            voice "voice/ahri/1/ah_scene1_12.ogg"
            am "Wha— w-who told you I was... this is absolutely beyond the pale!"
            voice "voice/ahri/1/ah_scene1_13.ogg"
            am "How dare you? You... you cretin! Get out of my sight!"
            show ahri angry at center with dissolve
            "People in the library start to look around, hearing the commotion. 
               I realize that I may have gone a little too far... 
               hopefully, it doesn't attract too much attention."
            "I should try to minimize the damage before things get any worse.."
            voice "voice/ezreal/1/ez_ah_scene1_10.ogg"
            mc surprise "Uh, sorry, I just blurted it out without thinking..."
            voice "voice/ahri/1/ah_scene1_14.ogg"
            am "Sigh... it was a mistake to expect something resembling proper human interaction. 
                Clearly, you just want to have fun at my expense."
            hide ahri with moveoutleft
            "Ami quickly packs her study materials and storms out of the library. 
               Now that she’s gone, all eyes are directed towards me."
            "Because I’m not even able to focus with all of these curious stares, 
               I follow suit once a bit of time has passed to avoid a second awkward encounter."
            "Well, at least a cretin is better than a piece of trash..."
            call gift_check("Ami") from _call_gift_check_13
            scene bg black with dissolve
            pause 0.5
            stop music fadeout 2.0
            jump events_end_period

label ahri_2:
    $ ahri_scene = 2
    $ renpy.block_rollback()
    # Virtual reality - ??
    scene bg fountain
    "When I log into the game, I notice that Ami is online."
    play music "music/ambient1.mp3" fadein 2.0
    "I decide to join her at the fountain. Though I've played against her several times, I haven't had much
     of a chance to talk to her character."
    "The only things I know about her are about the rumors about her online alter-ego 
     Ahri and her seductive personality."
    scene bg vr shop
    voice "voice/ezreal/2/ez_ah_scene2_1.ogg"
    ez happy "Hi, Ahri."
    show ahri vr happy at center with dissolve
    voice "voice/ahri/2/ah_scene2_1.ogg"
    ah "Oh, hello there. What compels a human to seek out little old me?"
    "A girl with luscious long hair and nine swaying tails steps closer, her gait perfectly
     measured. Could this really be someone I know?"
    voice "voice/ezreal/2/ez_ah_scene2_2.ogg"
    ez surprise "I... er... I just wanted to talk, I guess?"
    show ahri vr happy2mid at center with dissolve
    voice "voice/ahri/2/ah_scene2_2.ogg"
    ah "You guess? Oh ho hoh... how adorable. I think you'll soon find that I'm quite the fun
        person to be around."
    voice "voice/ezreal/2/ez_ah_scene2_3.ogg"
    ez happyblush "I really don't doubt that... ahaha."
    "Ahri approaches me with a slow but courtly pose, all the while her tails flicker
     upwards and around her elegant figure. Staring into her eyes as those fluffy ears twitch 
     ever so slightly makes me enter a captivating trance."
    "Pulses of flaming heartbeats drown out my ears as I am swallowed by her soft,
     glowing gaze that penetrates the deepest of my soul."
    show ahri vr happymid at center
    voice "voice/ahri/2/ah_scene2_3.ogg"
    ah "You've already fallen for my charms, haven't you?"
    voice "voice/ezreal/2/ez_ah_scene2_4.ogg"
    ez shyblush "Y-Yes! I mean, no! I mean... maybe?"
    voice "voice/ahri/2/ah_scene2_4.ogg"
    ah "What's the matter? Don't you trust me?~"
    voice "voice/ezreal/2/ez_ah_scene2_5.ogg"
    ez surprise "Of course I do, I think."
    show ahri vr happy2mid at center
    voice "voice/ahri/2/ah_scene2_5.ogg"
    ah "Then, surrender to me... as you fall prey to my graceful magic."
    voice "voice/ezreal/2/ez_ah_scene2_6.ogg"
    ez happy "Wow, Ami. You're so into your character, it's really impressive."
    voice "voice/ahri/2/ah_scene2_6.ogg"
    ah "Then surrender to me..."
    voice "voice/ezreal/2/ez_ah_scene2_7.ogg"
    ez surprise "Aren't you even a tad bit afraid that people might find out about this... \"other\" you, Ami?"
    voice "voice/ahri/2/ah_scene2_7.ogg"
    ah "Hmm, Who's Ami? My {i}name{/i} is Ahri, the Nine-Tailed Fox. And
        I am seeking the essence of life across this world. Now, submit
        yours to me."
    voice "voice/ezreal/2/ez_ah_scene2_8.ogg"
    ez flat "But I thought you didn't like me."
    show ahri vr surprised with dissolve
    pause 0.2
    show ahri vr angry with dissolve
    voice "voice/ahri/2/ah_scene2_8.ogg"
    ah "This is my character, not me. She's different. I mean, I'm different from
        her...Ami, that is...ARGH! Now you ruined the mood."
    "Ahri's alluring voice is still there, but speaking in Ami's tone - it's weird,
     to say the least."
    voice "voice/ezreal/2/ez_ah_scene2_9.ogg"
    ez happy "Heh. I guess I was able to defeat your so-called \"charms\" after all."
    voice "voice/ahri/2/ah_scene2_9.ogg"
    ah "Grr. You really are good. I'll have to think of some new strategies."
    voice "voice/ezreal/2/ez_ah_scene2_10.ogg"
    ez happy "You have so much dedication to keeping in-character -- the Ahri life
        must be exciting for you."
    show ahri vr happy
    voice "voice/ahri/2/ah_scene2_10.ogg"
    ah "Yes, indeed. Maybe this time I might just suck the life out of you."
    voice "voice/ezreal/2/ez_ah_scene2_11.ogg"
    ez flat "Erm...{i}that{/i} kind of sounds less than exciting."
    show ahri vr wink
    voice "voice/ahri/2/ah_scene2_11.ogg"
    ah "Ah, but to maintain my foxy figure, it is very necessary~ ♥"
    show ahri vr happy
    voice "voice/ezreal/2/ez_ah_scene2_12.ogg"
    ez happy "I can see that your features do include some sort of {i}enchantment{/i} technique, 
        obviously something I don’t plan on falling prey to. Heh."
    voice "voice/ahri/2/ah_scene2_12.ogg"
    ah "Hmph, just you wait, Ezreal. You’ll fall soon, too! Like all the others."
    "A ringing chuckle vibrates throughout the air as I shoot a disapproving glance at her. 
     As if I would let that happen!"
    voice "voice/ezreal/2/ez_ah_scene2_13.ogg"
    ez flat "What do you even mean by \"life essence\" and \"charming\" anyways?"
    voice "voice/ahri/2/ah_scene2_13.ogg"
    ah "Oh? You want to know about my ways? I guess I’ll tell you, since you’ll be bedazzled 
        by me sooner or later."
    "A wave of wind fills her extending chest as an airy gust enwraps her persona. Her eyes 
     open soon after staying closed for a brief but tense moment."
    voice "voice/ahri/2/ah_scene2_14.ogg"
    ah "My transformation is dependent on collecting as many human souls as possible, so of 
        course I need to allure easily gullible people to fulfill my needs." 
    voice "voice/ezreal/2/ez_ah_scene2_14.ogg"
    ez flat "Hm, that sounds really intricate. How did you come up with that background?"
    show ahri vr angry
    voice "voice/ahri/2/ah_scene2_15.ogg"
    ah "I... I've always known that the role I was bred to be, the perfect cunning fox with a
        flawless image, isn't meant for me."
    show ahri vr happy2
    voice "voice/ahri/2/ah_scene2_16.ogg"
    ah "So, what better way to defy the forced identity of who I am by becoming someone 
        completely different?"
    show ahri vr sad
    voice "voice/ahri/2/ah_scene2_17.ogg"
    ah "...They can’t impose all their values onto me forever."
    voice "voice/ezreal/2/ez_ah_scene2_15.ogg"
    ez surprise "Huh? \"They\"?"
    voice "voice/ahri/2/ah_scene2_18.ogg"
    ah "Just because I happen to be born under the same house, they think I live and breathe 
        their rules. What about {i}me{/i}? I’m my own person."
    "It’s almost as if Ahri became entranced by her own tricks. Her eyes dart off in the near 
     distance toward the horizon, filled with anguished enmity."
    voice "voice/ezreal/2/ez_ah_scene2_16.ogg"
    ez flat "Uh, Ahri? You okay?"
    ah "..."
    show ahri vr surprisedblush with hpunch
    voice "voice/ahri/2/ah_scene2_19.ogg"
    ah "Oh! Sorry, I totally just rambled on there. Don’t tell any—"
    "She stopped mid-sentence, as if her voice was cut off. A moment ago Ahri had been speaking with animated,
     sweeping gestures. Now her arms hang from her sides as if she were a lifeless doll."
    "She’s not moving at all... I wonder what happened to make her freeze."
    "Her eyes lost their usual passionate glaze and the reflection of the sun leaves no trace 
     on her character. The whole body is just gray and motionless."
    "Is it the glitch or..."
    show ahri vr angry
    voice "voice/ahri/2/ah_scene2_20.ogg"
    ah "I told you! It’s not just a stupid game. It’s my life, my {i}home{/i}. You would never 
        understand."
    "Whoa! Talk about a surprise; that came out of nowhere. She’s not looking at me 
     though. Her glare is directed towards the sky. What is she looking at? Who is she talking to?"
    voice "voice/ahri/2/ah_scene2_21.ogg"
    ah "Ugh, whatever. You just want me to continue playing your perfect daughter."
    hide ahri with dissolve
    "And just like that, Ahri logs off. No room for me to butt in or anything. I’m guessing it was her mom or dad."
    "I think I witnessed something that I'm not supposed to see."
    scene bg black with dissolve
    pause 0.5
    stop music fadeout 2.0
    $ ahri_rp = ahri_rp + 6
    jump events_end_period
    
label ahri_3:
    $ ahri_scene = 3
    $ renpy.block_rollback()
    scene bg museum day
    "All this business with hackers has gotten me worn out. I decide to take a trip to
     the museum to cool my nerves."
    "But, as I walk through the doors into the main hall, I catch a glimpse of someone
     I recognize."
    #play music 
    show ahri angry at left with dissolve
    hide ahri with moveoutleft
    "She turns the corner, going out of sight, and I rush to meet her before she can
     pass the ticket counter."
    voice "voice/ezreal/3/ez_ah_scene3_1.ogg"
    mc happy "Ami!"
    show ahri surprised with moveinright
    voice "voice/ahri/3/ah_scene3_1.ogg"
    am "Wha- Is that, [name]? I can't believe you're-- I mean, what brings someone like
        you to a place like this?"
    $ renpy.block_rollback()    
    menu:
        "What about you?":
            $ ahri4_flag = True
            $ renpy.block_rollback()
            voice "voice/ezreal/3/ez_ah_scene3_2.ogg"
            mc happy"And? What do {i}you{/i} like about art?"
            show ahri flat with dissolve
            voice "voice/ahri/3/ah_scene3_2.ogg"
            am "Just for your information, everything. Not everyone can make art."
            voice "voice/ezreal/3/ez_ah_scene3_3.ogg"
            mc happy "It sounds like you have some artsy aspirations."
            show ahri surprised
            pause 0.5
            show ahri flat with dissolve
            voice "voice/ahri/3/ah_scene3_3.ogg"
            am "Me? No, that’s not really my thing. I just happen to appreciate the freedom of 
            expression."
            "Speaking of which, she seemed to have an awful lot to say last time. I wonder if I can 
             get her to \”express\" her thoughts more."
            voice "voice/ezreal/3/ez_ah_scene3_4.ogg"
            mc happy "So, care to show me what that looks like with words?"
            show ahri angry with dissolve
            voice "voice/ahri/3/ah_scene3_4.ogg"
            am "Um... what do you mean?"
            "Her fidgeting isn’t very convincing at hiding her I-don’t-know-what-you’re-talking-
             about tone. She knows {i}exactly{/i} what I mean."
            voice "voice/ezreal/3/ez_ah_scene3_5.ogg"
            mc flat "Let me help you."
            voice "voice/ahri/3/ah_scene3_5.ogg"
            am "Huh, wha—"
            "My feet stomp on the tiled, white floor creating a small shake on the paintings lined 
             against the walls."
            voice "voice/ezreal/3/ez_ah_scene3_6.ogg"
            mc happy "I would not wish any companion in the world but you."
            "I attempt a clumsy twirl with my arms hovering over my head and knees landing in 
             front of her gaze."
            show ahri surprisedblushmid with dissolve
            voice "voice/ezreal/3/ez_ah_scene3_7.ogg"
            mc happy "I count myself in nothing else so happy as in a soul remembering my good friends."
            show ahri angrymid
            voice "voice/ahri/3/ah_scene3_6.ogg"
            am "Oh my gosh, you are {i}so{/i} embarrassing. Stop! Enough with the cheesy 
               Shakespeare."
            hide ahri with dissolve
            show ahri angry with dissolve
            "I got to say, her flustering blush is the definition of adorable. The way she digs her 
             face into those pale, delicate fingers and bites her rosy lips is hands-down too cute for 
             words."
            voice "voice/ezreal/3/ez_ah_scene3_8.ogg"
            mc happyblush "Okay, okay! I think you got the picture."
            show ahri happy2 with dissolve
            "Her giggles mix in with the sounds of clattering footsteps across the hall. It adds a nice 
             flavor to the quiet ambience and spotlights of the pearl tints shining around the museum."
            voice "voice/ezreal/3/ez_ah_scene3_9.ogg"
            mc happy "It’s your turn. What’s up?"
            am "..."
            pause 0.5
            show ahri sad with dissolve
            pause 0.5
            show ahri flat with dissolve
            "Tap, tap. Her footsteps lift themselves so gently that even a breath of air could knock 
             Ami off balance. And those hands – they almost dance a tango with how much she frets."
            voice "voice/ahri/3/ah_scene3_7.ogg"
            am "I... My character is based off... my situation, if you couldn’t already tell."
            voice "voice/ahri/3/ah_scene3_8.ogg"
            am "The Kaminoka family is a brilliant one; they hold monopoly over all the hotel chains 
                in West Demacia. Our business has been passed down for generations; no one could be 
                more honored to be a part of it than me."
            show ahri sad with dissolve
            voice "voice/ahri/3/ah_scene3_9.ogg"
            am "But..."
            "Her voice trails off with a lonely sentiment. She sure does pent up a lot of stuff inside. 
             Maybe I can get past her icy wall one day."
            show ahri happy2
            voice "voice/ahri/3/ah_scene3_10.ogg"
            am "Anyways! What about you, the Prodigal Explorer? Why are you so adamant about 
                exploring Summoner’s Rift?"
            voice "voice/ezreal/3/ez_ah_scene3_10.ogg"
            ez flat "Well, my family has always been moving. I mean, this is the longest that we’ve 
                stayed in one place so far."
            show ahri happy
            voice "voice/ahri/3/ah_scene3_11.ogg"
            am "Heh~ Is that why you have no friends? Don’t worry, you’ll make some soon 
                enough."
            show ahri happymid with dissolve
            voice "voice/ahri/3/ah_scene3_12.ogg"
            am "On another note, why are you so keen on learning about me? Do you have a crush, 
                perhaps?"
            voice "voice/ezreal/3/ez_ah_scene3_11.ogg"
            ez shyblush "What!? No! I, uh... My –"
            hide ahri with dissolve
            show ahri happy2 with dissolve
            voice "voice/ahri/3/ah_scene3_13.ogg"
            am "Haha. The cool and aloof Ezreal, jumbled."
            "Ami looks up at the clock in the corner of the museum as it shows half past the hour."
            show ahri surprised at left with dissolve
            voice "voice/ahri/3/ah_scene3_14.ogg"
            am "Oh, shoot! I have to leave for a family conference. I’ll give you some time to think 
             about it."
            show ahri happy2
            voice "voice/ahri/3/ah_scene3_15.ogg"
            am "I’ll be at the library the next few days to work on my project about Shurima 
                hieroglyphics. Maybe I’ll see you around?"
            hide ahri with easeoutleft
            "Hey, that’s not fair! Leaving like that before I could give her an answer. Ami is Ami, I 
             suppose."
            $ ahri_rp = ahri_rp + 7

                     
        "Just so you know, I like art!":
            $ renpy.block_rollback()
            $ ahri4_flag = False
            voice "voice/ezreal/3/ez_ah_scene3_12.ogg"
            mc angry "For your information, I have an appreciation for fine art."
            show ahri angry
            voice "voice/ahri/3/ah_scene3_16.ogg"
            am "The only thing you can appreciate is a comic book. You don't deserve to be in this 
                establishment."
            voice "voice/ezreal/3/ez_ah_scene3_13.ogg"
            mc flat "You're still going to be like that? What happened to the cunning Ahri?"
            "That scowling almost looks cute. Almost."
            show ahri angrymid with dissolve
            voice "voice/ahri/3/ah_scene3_17.ogg"
            am "Don't mention that in public! I told you, that's just how my character works."
            voice "voice/ezreal/3/ez_ah_scene3_14.ogg"
            mc flat "Oh, really? And there's no ulterior motive there?"
            hide ahri with dissolve
            show ahri angry with dissolve
            voice "voice/ahri/3/ah_scene3_18.ogg"
            am "Of course not! Look, just... leave me alone, okay? I can't associate with people 
            like you."
            voice "voice/ezreal/3/ez_ah_scene3_15.ogg"
            mc surprise "What? Says who?"
            show ahri sad
            voice "voice/ahri/3/ah_scene3_19.ogg"
            am "My family. They don't want me talking to the \"normal people\". I'm supposed to 
                study and get into a Challenger League School, like Cloud 9 University."
            voice "voice/ezreal/3/ez_ah_scene3_16.ogg"
            mc sad "I... didn't realize you were that dedicated. At least, not in the real world."
            show ahri angry
            voice "voice/ahri/3/ah_scene3_20.ogg"
            am "Do I not look dedicated enough to you? Well, excuse me."
            voice "voice/ezreal/3/ez_ah_scene3_17.ogg"
            mc sad "It's just that... you were so completely different."
            show ahri angryclose
            with hpunch
            voice "voice/ahri/3/ah_scene3_21.ogg"
            am "I said, DON'T TALK ABOUT THAT!"
            hide ahri with dissolve
            show ahri angry at left with dissolve
            voice "voice/ahri/3/ah_scene3_22.ogg"
            am "Now, if you'll excuse me, I'm leaving. I have to bone up on my knowledge of 
                early Shurima hieroglyphics."
            voice "voice/ezreal/3/ez_ah_scene3_18.ogg"
            mc flat "What kind of crazy class project is that?"
            voice "voice/ahri/3/ah_scene3_23.ogg"
            am "Sigh... that imbecile..."
            hide ahri with easeoutleft
            $ ahri_rp = ahri_rp + 4
    scene bg black with dissolve
    pause 0.5
    stop music fadeout 2.0
    jump events_end_period

label ahri_4A:
    $ ahri_scene = 4
    $ renpy.block_rollback()
    scene bg library
    # GO TO SCENE 5A AFTERWARDS
    "You know, I came here specifically because {i}someone{/i} said she would be here."
    "Not only is she completely not here, but I’m alone. Super alone. Like, seriously, where is everyone?"
    "I don’t know why I let myself get so distracted. 
     I only have so many days until the hacker absolutely demolishes the game, 
     and then I’ll be back to scraping up whatever free-to-play games I can get my hands on."
    "Why am I even waiting for her anyways?"
    "I shuffle my feet slowly past the receptionist. This is the fourth time I’ve circled the library...
     It beats pacing back and forth."
    "Suddenly, I change my mind and my body swivels an entire 180 degrees towards the back of the room. 
     I’m going to wait for her like the gentlemanly guy I am."
    "Not even ten minutes pass by before a familiar face illuminates the entire room."
    play music "music/ambient2.mp3" fadein 2.0
    show ahri surprised with dissolve
    voice "voice/ahri/4/ah_scene4_1.ogg"
    am "[name]? You’re still here?"
    mc shyblush "Ah, um, yea."
    show ahri blush with dissolve
    "Ami’s blushing face is worth a half hour wait. The beet red color spreads up to her ears, 
     and maybe even the tips of her hair."
    voice "voice/ahri/4/ah_scene4_2.ogg"
    am "Thanks for waiting, even without me telling you."
    mc surprise "Hm? What do you mean by that?"
    show ahri surprised
    voice "voice/ahri/4/ah_scene4_3.ogg"
    am "Wait – uh, I didn’t ... Forget I said that."
    mc happy "No way! Tell me."
    show ahri flat
    voice "voice/ahri/4/ah_scene4_4.ogg"
    am "... Sigh. My family is extremely sensitive about the crowd I surround myself with. 
        They despise commoners like no tomorrow."
    show ahri happy2
    voice "voice/ahri/4/ah_scene4_5.ogg"
    am "So, I usually need to tell my friends when and where it’s appropriate, but by then, they usually leave."
    mc happy "Does that mean ... {i}I’m{/i} special?" #Playful tone
    show ahri sad
    "Uh oh, that doesn’t look good. Her fidgeting is back again, and this time with a burrowed frown. 
     Something tells me I shouldn’t have said that."
    mc happyblush "Haha, I’m just kidd—"
    show ahri sadmid with dissolve
    voice "voice/ahri/4/ah_scene4_6.ogg"
    am "I’m sorry. I didn’t mean to hurt you. It’s okay though, you don’t need to meet with me anymore."
    hide ahri with dissolve
    show ahri sad with dissolve
    voice "voice/ahri/4/ah_scene4_7.ogg"
    am "My family is so unpredictable; who knows what would happen if they found out about our... 
        friendship. It was fun while it lasted though."
    voice "voice/ahri/4/ah_scene4_8.ogg"
    am "I’ll hold our memories close to heart."
    mc surprise "Wait, wait. You don’t have to stop seeing me just because you think your family might do something unpleasant."
    show ahri angry
    voice "voice/ahri/4/ah_scene4_9.ogg"
    am "You don’t know the Kaminoka household like I do – they get what they want. Every time."
    mc sad "Still..."
    show ahri happy2 with dissolve
    "My waning voice is only met with a shy smile from Ami. 
     The rays from the sun uncover an affectionate light in the corner of her eyes."
    mc sad "Ami, you’re a great person, and you can’t let your parents be your dictators forever."
    show ahri sad
    voice "voice/ahri/4/ah_scene4_10.ogg"
    am "It’s not that easy. If I even hint at a little rebellion, they would shun me out of the family 
        and make sure I never see the light of day again."
    mc flat "That sounds rough."
    show ahri happy2
    voice "voice/ahri/4/ah_scene4_11.ogg"
    am "Yeah... Living under that roof for the past sixteen years takes its toll."
    mc happy "But you’ve got friends to support you, and that includes me. Through thick and thin, 
        I’m positive we’ll be here to help."
    show ahri happy
    "Her shining white teeth catches a bit of the sunshine peeking in through the windows 
     and its sheen reflects off the glare."
    voice "voice/ahri/4/ah_scene4_12.ogg"
    am "Alright. You do what you think is best. I’ll respect your courage and determination as you do mine."
    "And off she goes, only leaving behind the sweet aroma of her floral scent for the library to admire."
    hide ahri with dissolve
    $ ahri_rp = ahri_rp + 11
    scene bg black with dissolve
    pause 0.5
    stop music fadeout 2.0
    jump events_end_period
    
label ahri_4B: 
    $ ahri_scene = 4
    $ renpy.block_rollback()
    scene bg fountain
    # GO TO SCENE 5B AFTERWARDS
    "To my surprise, Ami - or, should I say, Ahri, is online again."
    play music "music/ambient1.mp3" fadein 1.0
    "She appears to be in the same place as usual, the fountain. I figure I might as well go and say hello, 
     although I fear what might be awaiting me."
    show ahri vr happy with dissolve
    voice "voice/ahri/4/ah_scene4_13.ogg"
    ah "Well, well, if it isn't Ezreal. Come back for more?"
    voice "voice/ezreal/4/ez_ah_scene4B_1.ogg"
    ez surprise "I just wanted to-"
    voice "voice/ahri/4/ah_scene4_14.ogg"
    ah "Now, now, you don't have to say a word. I know ex-ac-tly what you desire."
    voice "voice/ezreal/4/ez_ah_scene4B_2.ogg"
    ez surprise "You do!?"
    hide ahri with dissolve
    show ahri vr happymid with dissolve
    voice "voice/ahri/4/ah_scene4_15.ogg"
    ah "Let's have some real fun."
    "I gasp as Ahri surrounds herself with a blue aura, her tails standing on end as 
     she lifts me off the ground."
    "She floats upwards, cradling me in her tails. Gripping my body, she slowly begins to envelop me in a glow of a 
     purple and teal hue. The air grows thicker and much warmer, almost to the point of agonizing pain."
    voice "voice/ezreal/4/ez_ah_scene4B_3.ogg"
    ez flat "A-Ahri. Stop, it hurts. Are you {i}trying{/i} to crush me?"
    show ahri vr winkmid with dissolve
    voice "voice/ahri/4/ah_scene4_16.ogg"
    ah "It's too late for mercy. Now I'll sap every last bit of your delicious strength."
    "I feel a pleasurable, paralyzing sensation envelop my body. She moves closer towards me, her long, black hair draping over 
     my face as the sweet smell of perfume wafts through the air."
    voice "voice/ahri/4/ah_scene4_17.ogg"
    ah "Feel the power of my charms..."
    "With the firm grasp of her tails cloaked around my character, I can do nothing but struggle in the air. 
     More like miserably flailing around, actually. She floats there for a moment, smirking, 
     before looking around with surprise."
    show ahri vr surprised with dissolve
    pause 0.5
    show ahri vr angrymid with dissolve
    voice "voice/ahri/4/ah_scene4_18.ogg"
    ah "I said, my {i}charms{/i}!"
    hide ahri with dissolve
    pause 0.2
    show ahri vr angry with dissolve
    "She floats away from me, with an annoyed look on her face."
    voice "voice/ahri/4/ah_scene4_19.ogg"
    ah "My magic is glitching out! Stupid hacker... my controls aren't - okay, here we go!"
    with vpunch
    "Far from hypnotizing me, we both drop to the ground, the aura flickering away from her body."
    show ahri vr sad
    voice "voice/ahri/4/ah_scene4_20.ogg"
    ah "OWW!"
    voice "voice/ezreal/4/ez_ah_scene4B_4.ogg"
    ez happy "Hey, you're lucky you have those tails to cushion your fall..."
    show ahri vr angry
    voice "voice/ahri/4/ah_scene4_21.ogg"
    ah "Forget that, I was hoping I could absorb more of your spirit. Sigh... this sucks."
    voice "voice/ezreal/4/ez_ah_scene4B_5.ogg"
    ez happy "In character, remember?"
    show ahri vr surprised with dissolve
    pause 0.2
    show ahri vr wink with dissolve
    voice "voice/ahri/4/ah_scene4_22.ogg"
    ah "Oh... right. Erm... it seems that my spells had no effect. You are stronger than I thought. 
        I like a man who's strong~"
    show ahri vr happy with dissolve
    voice "voice/ezreal/4/ez_ah_scene4B_6.ogg"
    ez shyblush "I think I'll just... excuse myself for now."
    voice "voice/ahri/4/ah_scene4_23.ogg"
    ah "You'll be back... I know you can't resist me. None of my other fans can, either."
    hide ahri with dissolve
    "The scary thing is, she might be right. Even if it might mean bad news for me if I come back..."
    "Sometimes I think it’s scary how much she’s willing to put into developing her character so 
     perfectly. Even if it might mean bad news for others."
    $ ahri_rp = ahri_rp + 8
    scene bg black with dissolve
    pause 0.5
    stop music fadeout 2.0
    jump events_end_period
    
    label ahri_5A: 
    $ ahri_scene = 5
    $ renpy.block_rollback()
    scene bg bedroom night
    play music "music/bedroom.mp3" fadein 1.0
    "It's nighttime, but I don't feel like logging onto Summoner's Rift today. 
     After all, I have plenty of homework to catch up on."
    "I've just finished taking out my books and making myself comfortable when the doorbell rings."
    "Figuring my parents have just ordered takeout, I pay it no mind. But a few moments later..."
    ### VOICE? ###
    "Dad" "Hey, [name]! There's someone here to see you! Do you know an \"Ami\"?"
    voice "voice/ezreal/5/ez_ah_scene5A_1.ogg"
    mc surprise "Uhh, sure... let her in."
    "Dad" "Don't worry, we won't come upstairs. We know your \"privacy\" is important!"
    voice "voice/ezreal/5/ez_ah_scene5A_2.ogg"
    mc angry "It's not like that!"
    "I hear someone walking upstairs to my room, and, to my surprise, Ami, in the flesh, 
     walks in, shutting the door behind her."
    show ahri angry at left with easeinleft
    voice "voice/ezreal/5/ez_ah_scene5A_3.ogg"
    mc happy "Well, well... what brings you to my humble abode?"
    am "... ... ..."
    voice "voice/ezreal/5/ez_ah_scene5A_4.ogg"
    mc happy "Here to gloat about how sparse my accommodations are? Or that I don't have a butler?"
    hide ahri with dissolve
    show ahri sadclose with dissolve
    with hpunch
    voice "voice/ezreal/5/ez_ah_scene5A_5.ogg"
    mc surprise "Oh, I know... it's probably because I don't have the latest model of virtual-- OOF!"
    "Ami puts her arms around me in a very atypical way. I wasn't expecting a hug, 
     but I can't exactly complain."
    voice "voice/ezreal/5/ez_ah_scene5A_6.ogg"
    mc shyblush "Woah, what's the big idea? Did your brain get replaced by aliens on the way here?"
    voice "voice/ahri/5/ah_scene5_1.ogg"
    am "No, you idiot... I just wanted to see someone who was on my side."
    voice "voice/ezreal/5/ez_ah_scene5A_7.ogg"
    mc shyblush "On your side? As opposed to what, exactly?"
    pause 1.0
    hide ahri with dissolve
    show ahri sad with dissolve
    voice "voice/ahri/5/ah_scene5_2.ogg"
    am "I got into an argument with my stupid, moronical parents. They were angry that I was spending 
        too much time with... people like you."
    voice "voice/ezreal/5/ez_ah_scene5A_8.ogg"
    mc sad "Maybe you are. I'm not really rich person material, anyway..."
    show ahri angrymid
    voice "voice/ahri/5/ah_scene5_3.ogg"
    am "That's not the point! How wealthy you are doesn't determine your character. 
        At least, to me, it doesn't."
    hide ahri with dissolve
    show ahri flat with dissolve
    voice "voice/ahri/5/ah_scene5_4.ogg"
    am "You may not be the sharpest tool in the shed, but at least you have a shred of decency left... 
        unlike them."
    voice "voice/ezreal/5/ez_ah_scene5A_9.ogg"
    mc happy "I guess, coming from you, that's a pretty big compliment."
    with hpunch
    "Ami pulls away and sits down on my bed, taking off her shoes."
    hide ahri with dissolve
    show ahri happy2mid with dissolve
    voice "voice/ahri/5/ah_scene5_5.ogg"
    am "Well, as long as I'm here, I might as well get comfortable."
    voice "voice/ezreal/5/ez_ah_scene5A_10.ogg"
    mc surprise "C-Comfortable?"
    show ahri angrymid
    voice "voice/ahri/5/ah_scene5_6.ogg"
    am "Stop thinking about weird things. It’s just stuffy, you know?"
    voice "voice/ezreal/5/ez_ah_scene5A_A.ogg"
    mc flat "Oh... right."
    "Part of me is relieved and the other half is slightly disappointed. Wait... disappointed about what? 
     This is Ami I’m talking about!"
    voice "voice/ezreal/5/ez_ah_scene5A_B.ogg"
    mc flat "Uh, so. What now?"
    show ahri sadmid
    am "..."
    hide ahri with dissolve
    show ahri happy2close with dissolve
    voice "voice/ahri/5/ah_scene5_7.ogg"
    am "It’s too late for mercy~ You’re mine now ♥"
    voice "voice/ezreal/5/ez_ah_scene5A_C.ogg"
    mc surprise "Mercy? For wha—"
    with hpunch
    with vpunch
    pause 0.2
    with hpunch
    pause 0.1
    with hpunch
    with hpunch
    "Suddenly, a barrage of pillows come tumbling down on my face. Small pangs of fluffy 
     strikes come from all directions."
    show ahri happyclose
    "During the pauses in the middle of our intense pillow fight, I can make out the sounds of an adorable laughter."
    voice "voice/ezreal/5/ez_ah_scene5A_D.ogg"
    mc angry "Why are you so good at this?!"
    hide ahri with dissolve
    show ahri happyblushmid with dissolve
    voice "voice/ahri/5/ah_scene5_8.ogg"
    am "You’re just not on my level, boy. Hehe."
    "Seeing Ahri talk to me in virtual reality was one thing, but listening to Ami's soft yet playful voice 
     in real life is something else entirely. Too cute for words."
    "And then, she leans towards me, her breathing listless."
    show ahri happyblushclose with dissolve
    voice "voice/ahri/5/ah_scene5_9.ogg"
    am "Ready for the final act?"
    "With me defenseless on the bed, her hovering figure makes the scene all the more intimidating... and scary."
    hide ahri with dissolve
    with hpunch
    "What is she -- *BAM!*" #Shake screen
    "It’s just like in those cartoons, you see those stars and birds circling above your head when you get hit. 
     Hard. Yeah, that’s exactly what I’m seeing."
    with fade
    with fade
    "A ringing headache begins to rise from all the action."
    "My hands are covering the sore spot as my eyes stay closed, trying not to cry. It really hurt, no lie."
    voice "voice/ezreal/5/ez_ah_scene5A_E.ogg"
    mc flat "Ami?"
    show ahri happy2 with dissolve
    voice "voice/ahri/5/ah_scene5_10.ogg"
    am "Ready for another round?"
    voice "voice/ezreal/5/ez_ah_scene5A_F.ogg"
    mc flat "No, no. For the love of Nashor, no more. You’ve won, that’s definitely a given."
    voice "voice/ezreal/5/ez_ah_scene5A_G.ogg"
    mc flat "And... this isn't you. As much as I enjoy your playful mischief, you're just trying to escape from reality."
    show ahri surprised with dissolve
    pause 0.2
    show ahri angry with dissolve
    voice "voice/ahri/5/ah_scene5_11.ogg"
    am "I am not-"
    voice "voice/ezreal/5/ez_ah_scene5A_H.ogg"
    mc flat "Look, I get it. You don’t want to think about all the nasty stuff at home, so you create this character who knows how to have fun."
    voice "voice/ezreal/5/ez_ah_scene5A_I.ogg"
    mc flat "I don’t know exactly what you’re going through, but I {i}do{/i} know that you're Ami the 
        person, not Ahri the character. Don't just try to run away from your real self."
    show ahri sad
    voice "voice/ahri/5/ah_scene5_12.ogg"
    am "But... but, I can't..."
    voice "voice/ezreal/5/ez_ah_scene5A_11.ogg"
    mc flat "Come on, what do you really want? I know you didn't just come here to hang out."
    voice "voice/ahri/5/ah_scene5_13.ogg"
    am "I want... to actually be able to control something for once."
    voice "voice/ezreal/5/ez_ah_scene5A_12.ogg"
    mc flat "Coming from someone like you, that's surprising. You've got legions of fans under your thumb."
    show ahri angry
    voice "voice/ahri/5/ah_scene5_14.ogg"
    am "Yeah, the virtual world is the only place where I actually am in control. Everyone loves me! 
        I'm beautiful, powerful..."
    show ahri sad
    voice "voice/ahri/5/ah_scene5_15.ogg"
    am "But, in real life, my parents tell me what to do and when to do it. I have to act that way, to secure my future. 
        I feel like a lone little fox."
    voice "voice/ezreal/5/ez_ah_scene5A_13.ogg"
    mc happy "Don't give up. The last thing I would want is to see you lose your \"self\" and become someone else. 
        The \"you\" right now is a good person."
    voice "voice/ahri/5/ah_scene5_16.ogg"
    am "You... you really think that? I... I'm sorry for being so dismissive towards you before. 
        Will you forgive me?"
    voice "voice/ezreal/5/ez_ah_scene5A_14.ogg"
    mc happyblush "Yeah, of course."
    show ahri happy2 with dissolve
    voice "voice/ahri/5/ah_scene5_17.ogg"
    am "Thank you."
    show ahri happy
    voice "voice/ahri/5/ah_scene5_18.ogg"
    am "I’ll save the life sucking sessions strictly to League." #Flirty
    hide ahri with dissolve
    show ahri surprised at left with dissolve
    voice "voice/ahri/5/ah_scene5_19.ogg"
    am "Oh... I should probably get going, or my parents are going to be even more pissed."
    voice "voice/ezreal/5/ez_ah_scene5A_15.ogg"
    mc happy "Probably. But, it was nice meeting you without the histrionics for once."
    show ahri angry at left
    voice "voice/ahri/5/ah_scene5_20.ogg"
    am "What!? That wasn't... nnnrgh, you have some nerve! I should have just gone to someone else's house instead!"
    voice "voice/ezreal/5/ez_ah_scene5A_16.ogg"
    mc happy "I'd really like it if you came back to mine, though."
    show ahri happy2 at left with dissolve
    voice "voice/ahri/5/ah_scene5_21.ogg"
    am "Hmph. I'll consider it. Au revoir."
    hide ahri with easeoutleft
    "Ami tromps down the stairs, back to her usual self again. This certainly didn't turn out to be the night 
     I thought it was going to be."
    "Now, where was I? Oh, homework..."
    "*SLAM*" with hpunch
    $ ahri_rp = ahri_rp + 11
    scene bg black with dissolve
    pause 0.5
    stop music fadeout 2.0
    jump events_end_period

label ahri_5B: ### WHERE ARE THOU FKN VOICE FILES ###
    $ ahri_scene = 5
    $ renpy.block_rollback()
    scene bg fountain
    play music "music/ambient1.mp3" fadein 2.0
    "I reckon it’s one of those kind of days – a day to play some League of Legends. 
     You know what I’m talking about; can’t get the feeling out of you."
    "And the series of click, click, clanks pop up the main screen. \”Welcome, Ezreal\" it says. 
     As classy as always."
    "In the corner of my eye, long and battered tails spread across the river scenery. 
     The fleece-like silky texture that Ahri’s tails once boasted is no longer so gleaming."
    show ahri vr sad at left with dissolve
    "A hand clutches the cusp of her stomach as she clenches the bloody red mud with her other."
    "Slow, steady breaths make her chest rise sluggishly as her back absorbs the water from underneath."
    "I grab a couple potions from Doran, the shopkeeper, and run up to her."
    hide ahri with dissolve
    show ahri vr surprised at center with dissolve
    voice "voice/ahri/5/ah_scene5_22.ogg"
    ah "E-Ezreal? Is that you?" #Sound weak
    ez surprise "Yeah, what’s wrong?! What happened?"
    "After laying her fragile body on my legs, I grab hold of her neck to set her delicate face against my chest."
    show ahri vr angry with dissolve
    voice "voice/ahri/5/ah_scene5_23.ogg"
    ah "Ugh. It was that deplorable Rengar. He came out of nowhere and pounced on me."
    "Her hushed silence fills the air as the red liquid pours into her mouth and I soon hear a sigh of relief."
    voice "voice/ahri/5/ah_scene5_24.ogg"
    ah "If it wasn’t for my Spirit Rush, I would have been dead meat." ## rengar is still mentioned as a he
    ez angry "...Why was there a scuffle? Our priority should be finding the hacker, not fighting each other."
    voice "voice/ahri/5/ah_scene5_25.ogg"
    ah "We have our differences. Rengar with his privileged life: no rules, no restrictions, just his freedom. 
        And me... well, quite the opposite."
    "What am I supposed to say to that? The air is pretty tense right now."
    $ renpy.block_rollback()

    menu:
        "What’s on your mind?":
            #NEXT SCENE IS 5A
            $ renpy.block_rollback()
            $ ahri5_flag = True
            "She’s acting pretty different right now. I guess the fight really got to her."
            ez flat "Something is troubling you, isn’t it? Is it your family again?"
            show ahri vr surprised
            voice "voice/ahri/5/ah_scene5_26.ogg"
            ah "W-wha?" with hpunch
            show ahri vr sad with dissolve
            "Ahri looks up at me with her stunning golden eyes, almost sucking me into her pace again. 
             I can’t quite make out the expression on her face right now; is it sadness? Confusion? Longing?"
            show ahri vr wink
            voice "voice/ahri/5/ah_scene5_27.ogg"
            ah "It’s just a prank. No need to be so {i}serious{/i}. I was just trying to lure a man to save a damsel in distress... 
                so I could suck the life out of them ♥"
            show ahri vr happy2
            voice "voice/ahri/5/ah_scene5_28.ogg"
            ah "And that man came waltzing right up to me. But it happened to be you, which wasn’t part of my plan."
            show ahri vr happy
            voice "voice/ahri/5/ah_scene5_29.ogg"
            ah "Why is it you always spoil the fun? You sure have a knack for that."
            ez surprise "Wait, wait. So that whole Rengar thing was a lie?"
            show ahri vr happy2
            voice "voice/ahri/5/ah_scene5_30.ogg"
            ah "I wouldn’t call it a lie~"
            "Is it that she doesn’t trust me that she won’t tell me? Her pacing and swaying of her hands tell me t
             his whole charade isn’t just nothing."
            "Well, I won’t push for the whole story if she feels compelled to hide it."
            ez flat "I’m not quite sure what’s going on, but I’ll be your support when you need it, Ahri."
            voice "voice/ahri/5/ah_scene5_31.ogg"
            ah "Aha. Ezreal, the support? That’s a new one!"
            pause 1.0
            show ahri vr surprised with dissolve
            "My candid stare must have spooked her into a more solemn attitude because she’s no longer smiling."
            voice "voice/ahri/5/ah_scene5_32.ogg"
            ah "S-sure."
            show ahri vr happyblush with dissolve
            "Now she returns my smile with a delightful one of hers, along with a few red freckles of blush."
            "I no longer see her in the distance as I turn to head towards the grassy fields for some hunting of my own."
            $ ahri_rp = ahri_rp + 6
            scene bg black with dissolve
            pause 0.5
            stop music fadeout 2.0
            jump events_end_period

        "I’m always here for you.":
            #BAD ENDING (NO FINAL CG)
            $ renpy.block_rollback()
            $ ahri5_flag = False
            $ ahri_badend = True
            ez happy "Don’t worry, Ahri. I’ll be here to help you anytime."
            show ahri vr happy2
            voice "voice/ahri/5/ah_scene5_33.ogg"
            ah "How tempting~"
            show ahri vr happy
            voice "voice/ahri/5/ah_scene5_34.ogg"
            ah "Just kidding. Play time’s over. I was just teasing you."
            "Ahri looks up at me with her stunning golden eyes, almost sucking me into her pace again. She catches me off by surprise with her 
             charming giggles resonating in the air."
            voice "voice/ahri/5/ah_scene5_35.ogg"
            ah "No need to be a worrywart. Though I must say, your shabby attempt to console me was worth the effort."
            "What is she saying? That her pain was all an act?"
            ez flat "I’m not playing games, Ahri. I was really trying to help."
            show ahri vr wink
            voice "voice/ahri/5/ah_scene5_36.ogg"
            ah "Right. If you'd like to play with me, you'd better be sure you know the game. 
                That is, if you think you're in my league. Hehe." #GIGGLING
            ez flat "Why are you being so cold? You don’t need to –"
            show ahri vr angry
            voice "voice/ahri/5/ah_scene5_37.ogg"
            ah "{i}Cold{/i}? Don’t pretend you know me, because you don’t."
            voice "voice/ahri/5/ah_scene5_38.ogg"
            ah "I hate shallow commoners who think they understand {i}me{/i} after only a few chit chats."
            ez angry "A few \”chit chats\"? What are you even saying anymore?"
            "Her bleak glare doesn’t show the smallest hint of changing. Obviously, I’m not as important to her as I thought."
            ez angry "Okay, you know what. You’re right – I don’t understand you, 
                and that’s where our friendship ends, I guess."
            "The silence is deafening. Enough of it has led me to a coughing fit to break the awkward lull."
            ez sad "I thought we were good friends."
            show ahri vr happy2
            voice "voice/ahri/5/ah_scene5_39.ogg"
            ah "You thought wrong, obviously. You were a great way to pass the time."
            ez flat "..."
            show ahri vr angry
            voice "voice/ahri/5/ah_scene5_40.ogg"
            ah "If I am as helpless as you think I am, which I’m not, you would be the last person I would run to."
            "Part of me thinks that her insults are coming from the stress at home, but nothing
             I’m saying is getting through to her."
            "Maybe if I had approached this differently, things would have gone better."
            "Guess it isn’t happening today though. Ahri just glides right on by to her next victim as I’m left to 
             ponder on my actions in the creek."
            scene bg black with dissolve
            pause 0.5
            stop music fadeout 2.0
            jump events_end_period
            
label ahri_6: 
    $ ahri_scene = 6
    # Virtual world
    $ renpy.block_rollback()
    scene bg fountain
    "I log into Summoner's Rift, and realize that Ahri is there. I wonder what she'll say if I enter her world. 
     It might be foolhardy, but I feel like I should at least try."
    "When I arrive, there doesn't seem to be anyone around. Strange..."
    "Suddenly, I hear the bushes shake and swing around. I realize that there's someone hiding in the grass."
    voice "voice/ezreal/6/ez_ah_scene6_1.ogg"
    ez angry "Show yourself!"
    "I point my blaster at the bushes, but to my surprise, Ahri herself walks out, looking a bit embarrassed."
    show ahri vr happyblush with dissolve
    voice "voice/ezreal/6/ez_ah_scene6_2.ogg"
    ez happy "What's that matter, Ahri? Having another magical mishap? Or are you hiding from your family?"
    show ahri vr happy2
    voice "voice/ahri/6/ah_scene6_1.ogg"
    ah "Oh, no, nothing like that. In fact, everything is working perfectly fine. Strangely enough, there haven't been any 
        issues with my magic so far."
    show ahri vr happy
    voice "voice/ahri/6/ah_scene6_2.ogg"
    ah "As far as my family goes... I'm just ignoring them now. I won't let them tell me who I can play with."
    voice "voice/ezreal/6/ez_ah_scene6_3.ogg"
    ez flat "So, then, what's the problem?"
    show ahri vr sad
    voice "voice/ahri/6/ah_scene6_3.ogg"
    ah "I was going to mess around with you some more, but then I just got this... horrible feeling."
    pause 0.5
    show ahri vr sadblush with dissolve
    voice "voice/ahri/6/ah_scene6_4.ogg"
    ah "It's not like I'm charming you... it's like you're charming me! How could this be... you're the one sapping my powers of love!"
    voice "voice/ezreal/6/ez_ah_scene6_4.ogg"
    ez surprise "I was sapping them? Without even being here?"
    show ahri vr angry
    voice "voice/ahri/6/ah_scene6_5.ogg"
    ah "Yes, that's right... all I can think about is you!"
    show ahri vr angrymid with dissolve
    voice "voice/ahri/6/ah_scene6_6.ogg"
    ah "Day and night, images of your silly, stupid face fill my thoughts. Whether I’m at school, at home, on League, doing homework..."
    voice "voice/ahri/6/ah_scene6_7.ogg"
    ah "It’s like a fruit fly with your picture that keeps buzzing around me all day: annoying and always in my face."
    voice "voice/ezreal/6/ez_ah_scene6_5.ogg"
    ez flat "I... don’t think you had to put it like {i}that{/i}."
    voice "voice/ahri/6/ah_scene6_8.ogg"
    ah "And while I was devising ways to make that cycle stop, that monstrous creature, Rengar, showed himself and challenged me to a duel! 
        But my powers were too weak, and I had to flee." 
    hide ahri with dissolve
    show ahri vr angry with dissolve
    voice "voice/ahri/6/ah_scene6_9.ogg"
    ah "Losing to a beast like him... how pitiful. This is terrible... at this rate, my abilities will be completely useless!"
    
    ez flat "Well, is it as bad as you say? I mean, thinking about me all the time. There’s got to be a reason for that, right?"
    show ahri vr surprised with hpunch
    voice "voice/ahri/6/ah_scene6_10.ogg"
    ah "Wh-what!?"
    
    ez happy "Gaze upon the mighty Ezreal, conqueror of worlds! *flex* *flex*"
    show ahri vr happy2 with dissolve
    voice "voice/ahri/6/ah_scene6_11.ogg"
    ah "Pffthahaha! Now you're just embarrassing yourself~"
    
    ez happy "Hey... I thought I was pretty cool."
    show ahri vr happy
    voice "voice/ahri/6/ah_scene6_12.ogg"
    ah "Actually, I do feel a tad tempted... maybe your idea wasn't so bad after all."
    show ahri vr happymid with dissolve
    "Ahri slinks up to me, placing her faint fingers on my chest and playing at the ends of my scarf, tugging ever so slightly."
    show ahri vr happyblushmid with dissolve
    voice "voice/ahri/6/ah_scene6_13.ogg"
    ah "In here, we can have complete peace and quiet. Nothing to disturb us whatsoever."
    voice "voice/ahri/6/ah_scene6_14.ogg"
    ah "I promise I won't use any magic this time. I won't try to sap your life force, either. What you're looking at is 
        my true self... hehehe~"
    
    ez happyblush "Oh, wow... this I've gotta see."
    
    ez flat "Hang on a minute... I didn’t say that just so you—"
    show ahri vr happyblushclose with dissolve
    "Ahri puckers her lips and leans towards me as she wraps her arms around my waist, her tails grazing 
     against my legs. I can't believe it..."
    "Does she really intend on reverting back to her seductive ways after she just admitted to something 
     so innocent and genuine?"
    show ahri vr surprised with hpunch
    
    ez flat "Hey! Was everything you said in the library a lie? Did you say all that just so I could fall for you?"
    voice "voice/ahri/6/ah_scene6_15.ogg"
    ah "Oh, Ezreal, I- huh?"
    
    ez flat "You’ve been acting like I’m nothing other than for some side fun. I really thought we had a 
        connection... something {i}deeper{/i}."
    show ahri vr sad with dissolve
    pause 0.2
    show ahri vr happy with dissolve
    voice "voice/ahri/6/ah_scene6_16.ogg"
    ah "No, no! I didn’t mean to do that. I just... It’s another one of my tricks, you see~" #VA NOTE: Tries to play it off coolly
    pause 0.5
    show ahri vr sad
    voice "voice/ahri/6/ah_scene6_17.ogg"
    ah "... Sigh. I’m just really frustrated."
    
    ez sad"Why...?"
    show ahri vr angrymid with dissolve
    voice "voice/ahri/6/ah_scene6_18.ogg"
    ah "That I lost to Rengar! Of all the people, it had to be him. I guess the defeat turned my salty 
        anger into a type of gamer rage." #Slightly try to laugh off the issue.
    
    ez flat "It’s okay. Although I’m not sure why you have such a vendetta against Rengar – but hey, rage quit happens."
    hide ahri with dissolve
    show ahri vr angry with dissolve
    voice "voice/ahri/6/ah_scene6_19.ogg"
    ah "But I didn’t rage quit..."
    
    ez flat "Right. I was talking about myself."
    "She looks at me, utterly confused. Ahri tilts her head to the side in such an adorable fashion I almost let out an awkward, unmanly squeal."
    
    ez flat "I... You’re not the only one thinking about a person all day. I can’t get you out of my head."
    
    ez happyblush "Getting to know you these past few days has been such a... refreshing adventure. There were ups and downs, laughs and flustering. 
        Definitely more than a few embarrassing moments."
    show ahri vr happy2 with dissolve
    "We both chuckle at the thought of the stupid things I’ve done – like that Shakespeare act. Oh boy."
    show ahri vr happy
    
    ez flat "Because of that, I’ve realized that you don’t need your Ahri character. Or more like, I don’t enjoy it."
    
    ez happyblush "There’s no reason for you to protect yourself through this charming, foxy persona anymore because... 
        {i}I’ll{/i} be there for you instead."
    
    ez happyblush "Any time you need a shoulder to cry on or someone’s opinion, I’m all ears."
    pause 3.0
    "And then there was silence. Lots of it. I mean, are those crickets I hear? Does League even have crickets?!"
    "The air is so chilling, too. They really need to lower the air conditioner in here."
    
    ez shyblush "*Cough* To put it bluntly, you are Ez Real as it gets." #Pronounce "Ez Real” as "As Real”
    voice "voice/ahri/6/ah_scene6_20.ogg"
    ah "Did you just – with your name?"
    
    ez flat "Y...yea."
    show ahri vr happy2 with dissolve
    "The beautiful sounds of her laughing mixes with my boisterous chuckling, and echoing within the game’s walls. 
     It was absolutely invigorating hearing her happiness resounding in the breeze."
    show ahri vr wink
    voice "voice/ahri/6/ah_scene6_21.ogg"
    ah "Hahaha! I just can’t get enough of you, Ezreal."
    show ahri vr happy
    voice "voice/ahri/6/ah_scene6_22.ogg"
    ah "But, you know what. You’re right! I don’t need the Charming Ninetailed Fox to be happy... with you."
    "Ah, I can’t stop the red flush from covering my face. Can I just squeal like a fangirl for just a moment?"
    voice "voice/ahri/6/ah_scene6_23.ogg"
    ah "Next time, I’ll ditch the silly charade."
    
    ez happy "Deal! Until next time, then."
    "I look down and realize that Ahri's kimono is flickering in different places. A few glitchy holes appear in it, 
     not leaving much to the imagination. She screams and puts her hands over it, her ears twitching wildly."
    show ahri vr surprised with dissolve
    voice "voice/ahri/6/ah_scene6_24.ogg"
    ah "EEK! What's going on!? What the- kimono.exe has encountered an error, attempting to reboot!?"
    show ahri vr angry with dissolve
    voice "voice/ahri/6/ah_scene6_25.ogg"
    ah "The hacker didn't attack my magic this time... he attacked my clothes! THAT PERVERT!"
    
    ez flat "Um... yeah. I should probably help you stop that attack. This is totally... unacceptable. 
        And wrong. Can't stop looking..."
    show ahri vr angryclose with dissolve
    voice "voice/ahri/6/ah_scene6_26.ogg"
    ah "Don't tell me you're in league with him too! Grr... maybe this should do it. There!"
    hide ahri with dissolve
    pause 0.5
    show ahri vr angry with dissolve
    "Ahri's clothes phase back into reality. She puts her hands on her hips, clearly miffed."
    ah "Well, so much for having a private moment. Now I have to worry about attacks like these... I should probably just lay low for now."
    
    ez flat "I guess maybe that would be for the best. But as long as we can count on your support in the upcoming battle, 
        we should have nothing to fear!"
    voice "voice/ahri/6/ah_scene6_27.ogg"
    ah "Oh, trust me, you do. That hacker is going to be sent to the deepest depths of Jigoku for this."
    "I warp out, leaving Ahri to her battle practice. Even if that didn't go as planned, I still count it as a success."
    hide ahri with dissolve
    $ ahri_rp = ahri_rp + 6
    scene bg black with dissolve
    pause 0.5
    stop music fadeout 2.0
    jump events_end_period            
    
label ahri_7:
    $ ahri_scene = 7
    $ ahri_rp = ahri_rp + 10
    $ renpy.block_rollback()
    scene bg black
    # no idea what music to play here
    "I get a message on my phone from Ami as soon as I get to the park, telling me to meet her at Star Karaoke."
    "That's unusual. No one said anything about a karaoke night anytime soon. Or, maybe I just missed something."
    "Whatever the case, I high-tail it over there to see what she's planning."
    un "The guest of honor has finally arrived!"
    voice "voice/ezreal/7/ez_ah_scene7_1.ogg"
    mc surprise "Who, me?"
    show ahri happyblush with dissolve
    "When I walk into the room, it's empty - as I expected. The only person there is Ami, who is standing on stage with a mic."
    voice "voice/ezreal/7/ez_ah_scene7_2.ogg"
    mc surprise "What in the world is going on?"
    hide ahri
    scene cg ahri end with dissolve
    voice "voice/ahri/7/ah_scene7_1.ogg"
    am "I rented out the karaoke room, of course! As thanks for your help, I wanted to give you a suitable reward."
    voice "voice/ezreal/7/ez_ah_scene7_3.ogg"
    mc surprise "T-That really wasn't necessary-"
    voice "voice/ahri/7/ah_scene7_2.ogg"
    am "Oh, come on - tell me you didn't like the surprise."
    voice "voice/ezreal/7/ez_ah_scene7_4.ogg"
    mc happy "Like it? I love it! I mean, this is... incredible."
    voice "voice/ahri/7/ah_scene7_3.ogg"
    am "Don't get too excited yet - you still haven't seen the main event. My performance!"
    voice "voice/ezreal/7/ez_ah_scene7_5.ogg"
    mc surprise "No way, you can sing?"
    voice "voice/ahri/7/ah_scene7_4.ogg"
    am "I've been taking singing lessons for a long time. But, it's something I don't usually show to my fans."
    voice "voice/ahri/7/ah_scene7_5.ogg"
    am "For you, though, I wanted to do something really special."
    voice "voice/ezreal/7/ez_ah_scene7_6.ogg"
    mc happy "Should I sit down?"
    voice "voice/ahri/7/ah_scene7_6.ogg"
    am "You can come up on stage if you want. There's certainly room."
    "I walk up on stage and look out at where the seats would normally be filled with others."
    voice "voice/ezreal/7/ez_ah_scene7_7.ogg"
    mc happy "You know, it's funny - you probably have this many fans in real life."
    voice "voice/ahri/7/ah_scene7_7.ogg"
    am "Yes... perhaps. But, you're a true fan... I'm the one who should feel lucky having you, not the other way around."
    voice "voice/ezreal/7/ez_ah_scene7_8.ogg"
    mc shyblush "I don't know what to say..."
    voice "voice/ahri/7/ah_scene7_8.ogg"
    am "You don't have to say anything. Just listen!"
    with fade
    "She starts singing... I close my eyes and listen."
    stop music fadeout 0.5
    voice "voice/ahri/7/ah_songEND.ogg"
    $ renpy.pause(17.0, hard=True)
    voice "voice/ezreal/7/ez_ah_scene7_9.ogg"
    mc happyblush "Wow, that was really good."
    voice "voice/ahri/7/ah_scene7_9.ogg"
    am "Just good? Not incredible?"
    voice "voice/ezreal/7/ez_ah_scene7_10.ogg"
    mc shyblush "O-Of course... I mean..."
    voice "voice/ahri/7/ah_scene7_10.ogg"
    am "Just kidding. I don't really mind how it went, just doing this with you was reward enough."
    voice "voice/ezreal/7/ez_ah_scene7_11.ogg"
    mc happy "Thanks, Ami. Hopefully, I can get to know you even better when this is all over."
    voice "voice/ahri/7/ah_scene7_11.ogg"
    am "Hehe, count on it!"
    # more romantic stuff?
    scene bg black with dissolve
    pause 0.5
    jump events_end_period
