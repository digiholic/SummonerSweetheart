######################################### EVENT DECLARATION
init:
    $ event("rengar_1", "act == 'vr'", event.once(), "route == 'Ezreal'", priority = 192)
    $ event("rengar_2", "act == 'soccer'", event.once(), event.depends("rengar_1"), "day >= 3", "period == 1", priority = 182)
    $ event("rengar_3", "act == 'vr'", event.once(), event.depends("rengar_2"), priority = 172)
    $ event("rengar_4", "act == 'soccer'", event.once(), event.depends("rengar_3"), "period == 1", priority = 162)
    $ event("rengar_5", "act == 'vr'", event.once(), event.depends("rengar_4"), "day >= 6", priority = 152)
    $ event("rengar_6", "act == 'vr'", event.once(), event.depends("rengar_5"), "day == 7", "period == 2", "rango_rp >= 70", priority = 142)

######################################### RENGAR SCRIPT
label rengar_1:
    # meow
    $ rango_scene = 1
    $ renpy.block_rollback()
    scene bg fountain
    "I decide to check if anyone is logged on, and I realize there's someone 
     I haven't seen before in the club."
    play music "music/ambient1.mp3" fadein 2.0
    voice "voice/ezreal/1/ez_re_scene1_1.ogg"
    ez surprise "\"Rengar\"? Who is he?"
    "Could it be someone sent by the hacker? Or just a member I don't know about?"
    "I decide to go to find out."
    voice "voice/ezreal/1/ez_re_scene1_2.ogg"
    ez flat "Yeesh... this place is stifling."
    "It appears I've warped straight into a dense jungle. I can hardly see where I'm going."
    show rango vr silhouette with dissolve
    show rango vr silhouette at left with dissolve
    "Something shakes the underbrush nearby. I turn to look, but nothing is there."
    voice "voice/ezreal/1/ez_re_scene1_3.ogg"
    ez surprise "Hmm... monsters?"
    "Suddenly, something roars and pounces on me, pinning me to the ground before I can do anything."
    show rango vr silhouetteclose with dissolve
    "Hovering over me is a leonine face, wearing a glowering look. A rank smell drifts from 
     his stark white fur as he examines me, growling and beginning to speak in a gravelly voice."
    voice "voice/rango/1/re_scene1_1.ogg"
    un "Grrr... you are not what I was hunting."
    voice "voice/ezreal/1/ez_re_scene1_4.ogg"
    ez surprise "Then... maybe you could let me go!"
    show rango vr silhouetteclose with dissolve
    voice "voice/rango/1/re_scene1_2.ogg"
    un "Why should I let you go? You were invading my territory!"
    voice "voice/ezreal/1/ez_re_scene1_5.ogg"
    ez surprise "I didn't mean to - I just wanted to see who you were."
    show rango vr angryclose with dissolve
    "The beast gets off of me, brushing off his arms. He is at least a foot taller than I am
     and doesn't even look remotely human - the person behind the avatar is unrecognizable."
    voice "voice/rango/1/re_scene1_3.ogg"
    re "I am Rengar the Pridestalker. Now, grovel before me, lesser creature!"
    voice "voice/ezreal/1/ez_re_scene1_6.ogg"
    ez angry "I'm not groveling! You'll have to fight me if you want me to do that."
    voice "voice/rango/1/re_scene1_4.ogg"
    re "A human with spirit... I like that. Perhaps I will take you up on your offer."
    voice "voice/ezreal/1/ez_re_scene1_7.ogg"
    ez flat "I just want to ask you one thing. You're listed as a member of the club, but I've 
        never seen you in meetings. So, are you the missing member?"
    voice "voice/rango/1/re_scene1_5.ogg"
    re "And what of it?"
    voice "voice/ezreal/1/ez_re_scene1_8.ogg"
    ez flat "I seem to recall someone saying that the missing member was a girl."
    show rango vr surprised with dissolve
    voice "voice/rango/1/re_scene1_6.ogg"
    re "A... a girl, you say? Ha! I know nothing... nothing about any of that! Grrrar... 
        you dare insult me!?"
    voice "voice/ezreal/1/ez_re_scene1_9.ogg"
    ez happy"I don't know. You sounded awfully surprised when I mentioned it."
    show rango vr angrymid with dissolve
    voice "voice/rango/1/re_scene1_7.ogg"
    re "Keep talking, and I will take your head as a trophy!"
    voice "voice/ezreal/1/ez_re_scene1_10.ogg"
    ez flat "Is that a challenge? I'm going to find out who you really are."
    voice "voice/rango/1/re_scene1_8.ogg"
    re "I must take my leave now. I still have things to hunt."
    hide rango with dissolve
    voice "voice/rango/1/re_scene1_9.ogg"
    re "Do not dare try to find out who I am, impudent human!"
    scene bg black with dissolve
    pause 0.5
    stop music fadeout 2.0
    jump events_end_period
    
label rengar_2:
    $ rango_scene = 2
    $ renpy.block_rollback()
    scene bg soccer day
    "After talking to the club advisor, I've finally gotten the name of the missing club 
     member - Gwen. A girl I've never even heard about, so much as met in person."
    play music "music/Smooth Sailing.mp3" fadein 2.0
    "I've resolved to track her down and see whether the mysterious character I've run into is really her."
    "It took having to ask about a hundred people, but I've finally narrowed down her location
     to the soccer field."
    show rango flat at Move((0.2, 0.3), (0.5, 0.3), 0.5) # code in ATL language
    pause 0.5
    show rango flat at Move((0.5, 0.3), (0.2, 0.3), 0.5)
    pause 0.5
    hide rango with dissolve
    show rango flat with dissolve
    "When I walk over, though, it doesn't appear that she's practicing with a team. Instead,
     she is just kicking the ball repeatedly into the net and retrieving it."
    voice "voice/ezreal/2/ez_re_scene2_1.ogg"
    mc flat "Um, hi?"
    show rango angry with dissolve
    gw "..."
    "She seems pretty absorbed in what she's doing. I walk closer and talk to her again."
    show rango angrymid with dissolve
    with hpunch
    hide rango with dissolve
    show rango angry with dissolve
    voice "voice/ezreal/2/ez_re_scene2_2.ogg"
    mc flat "I said, hi - oof!"
    "I feel the soccer ball hit my gut, sending me reeling backwards. I'm pretty sure this
     isn't regulation soccer."
    voice "voice/rango/2/re_scene2_1.ogg"
    gw "What do you want?"
    voice "voice/ezreal/2/ez_re_scene2_3.ogg"
    mc surprise "That wasn't very nice, you know. I could have broken something... or ruptured my spleen."
    voice "voice/rango/2/re_scene2_2.ogg"
    gw "Suck it up, crybaby. It should take more than that to bring a {i}real{/i} man down."
    voice "voice/ezreal/2/ez_re_scene2_4.ogg"
    mc flat "I'm not sure what your standards are, but I'm going to take a wild guess and say that
        they're too high."
    voice "voice/rango/2/re_scene2_3.ogg"
    gw "Let me guess... it's about the field, isn't it? Well, I have a permit, so you shouldn't bother."
    voice "voice/ezreal/2/ez_re_scene2_5.ogg"
    mc flat "Actually, no... I wanted to ask you about the club. You know, the Summoner's Rift Club."
    show rango surprised with dissolve
    voice "voice/rango/2/re_scene2_4.ogg"
    gw "What!? I'm surprised someone actually cared enough to bother finding me."
    voice "voice/ezreal/2/ez_re_scene2_6.ogg"
    mc happy "I'm a little curious. You're still listed as an active member, even though 
        you don't come to any meetings."
    show rango flat with dissolve
    voice "voice/rango/2/re_scene2_5.ogg"
    gw "That kind of stuff bores me. I'd rather play by myself, thank you very much."
    voice "voice/ezreal/2/ez_re_scene2_7.ogg"
    mc angry "Then, why did you even bother joining?"
    show rango confident with dissolve
    voice "voice/rango/2/re_scene2_6.ogg"
    gw "A real gamer always keeps tabs on their rivals. Otherwise, they might find
        themselves at a disadvantage."
    voice "voice/ezreal/2/ez_re_scene2_8.ogg"
    mc flat "So, you admit you play Summoner's Rift. Then, what's your character?"
    show rango surprised with dissolve
    voice "voice/rango/2/re_scene2_7.ogg"
    gw "Why the hell should I tell you?"
    voice "voice/ezreal/2/ez_re_scene2_9.ogg"
    mc flat "Um... because I'm your friend?"
    show rango angrymid with dissolve
    voice "voice/rango/2/re_scene2_8.ogg"
    gw "It'll take more than that to be {i}my{/i} friend. I'm not into sappy stuff like that."
    menu:
        "I'd still like you to be my friend.":
            $ renpy.block_rollback()
            voice "voice/ezreal/2/ez_re_scene2_10.ogg"
            mc happy "Even so, I'd still like you to be my friend. I think you're... cute."
            show rango surprised with dissolve
            voice "voice/rango/2/re_scene2_9.ogg"
            gw "Hnng!? W-What the hell do you mean by that?"
            voice "voice/ezreal/2/ez_re_scene2_11.ogg"
            mc happy "I said..."
            show rango blush with dissolve
            voice "voice/rango/2/re_scene2_10.ogg"
            gw "No, never mind. As I said before, you won't win me over with words. 
                You'll have to earn it."
            voice "voice/ezreal/2/ez_re_scene2_12.ogg"
            mc flat "Fine, then. I'm up to the challenge."
            show rango confident
            voice "voice/rango/2/re_scene2_11.ogg"
            gw "We'll just see about that."
            show rango flat 
            hide rango with moveoutleft
            pause 1.0
            show rango flat at Move((0.0, 0.7), (0.5, 0.7), 0.3,
                  xanchor="center", yanchor="center")
            pause 0.2
            with hpunch
            pause 0.1
            hide rango with dissolve
            "Gwen gives the ball another running kick, and it slams into the goal, dead center."
            show rango happymid with dissolve
            voice "voice/rango/2/re_scene2_12.ogg"
            gw "That's it, perfect. I'm done."
            $ rango_rp = rango_rp + 5
            
        "Then, forget I asked.":
            $ renpy.block_rollback()
            voice "voice/ezreal/2/ez_re_scene2_13.ogg"
            mc angry "Fine, then - forget I asked."
            show rango angrymid with dissolve
            voice "voice/rango/2/re_scene2_13.ogg"
            gw "Heh, crumpling under the pressure? I don't like saps, but I don't like cowards either."
            voice "voice/ezreal/2/ez_re_scene2_14.ogg"
            mc angry "That's not what I-"
            show rango angryclose
            voice "voice/rango/2/re_scene2_14.ogg"
            gw "If you came all this way to talk to me, you should at least be more assertive."
            voice "voice/ezreal/2/ez_re_scene2_15.ogg"
            mc angry "Come on, make up your mind already!"
            hide rango with dissolve
            show rango angry
            hide rango with moveoutleft
            voice "voice/rango/2/re_scene2_15.ogg"
            gw "Tch - you think I care about being friends with some club lackey?"
            show rango flat at Move((0.0, 0.7), (0.5, 0.7), 0.2,
                  xanchor="center", yanchor="center")
            pause 0.1
            with hpunch
            pause 0.1
            hide rango with dissolve
            show rango angry with dissolve
            "Gwen gives the ball another running kick, and it flies far away from the goal,
             missing it entirely."
            voice "voice/rango/2/re_scene2_16.ogg"
            gw "Screw this. I'm going home."
            
    voice "voice/ezreal/2/ez_re_scene2_16.ogg"
    mc flat "Umm... are you practicing for something?"
    show rango angry
    voice "voice/rango/2/re_scene2_17.ogg"
    gw "No, I just decided to try out soccer."
    voice "voice/ezreal/2/ez_re_scene2_17.ogg"
    mc flat "But... why bother?"
    show rango happy with dissolve
    voice "voice/rango/2/re_scene2_18.ogg"
    gw "If I can't be good at this, I'll never be good at my {i}real{/i} job."
    voice "voice/ezreal/2/ez_re_scene2_18.ogg"
    mc flat "What {i}is{/i} your real job, exactly?"
    show rango angry with dissolve
    voice "voice/rango/2/re_scene2_19.ogg"
    gw "As if I'm telling you. See ya, chump."
    hide rango with moveoutleft
    "Gwen walks away, holding her soccer ball. If I've learned anything today, it's that 
     she's completely unlike anyone I've ever known."
    "I decide not to report this to the rest of the club just yet. I need to find out more 
     before doing anything rash."
    "I'm especially interested in whatever she claims her real job is. I suppose there's 
     only one way to find out, and that's to get to know her better."
    call gift_check("Gwen") from _call_gift_check
    $ rango_rp = rango_rp + 6
    scene bg black with dissolve
    pause 0.5
    stop music fadeout 2.0
    jump events_end_period
    
label rengar_3:
    $ rango_scene = 3
    $ renpy.block_rollback()
    scene bg fountain
    "After logging in to the game, I notice the mysterious club member has also logged back in."
    voice "voice/ezreal/3/ez_re_scene3_1.ogg"
    mc flat "Huh... whoever this Rengar is, they sure are taking on a lot of people at once."
    "I resolve to enter their world and find out what exactly is going on."
    show rango vr confident at left with dissolve
    voice "voice/rango/3/re_scene3_1.ogg"
    re "Ha! Is that all you have? None of you can so much as dent my armor!"
    voice "voice/rango/3/re_scene3_2.ogg"
    re "Yes, that's right... run away to your mommies and daddies. You have no place in my jungle!"
    "A number of other Summoners lie on the ground, broken and defeated. Several of them scramble 
     to their feet and limp away, disappearing into the haze."
    "The others just disappear out of existence, too humbled to even stand. Rengar glowers over
     them happily, loosing a guttural roar."
    voice "voice/ezreal/3/ez_re_scene3_2.ogg"
    ez happy "Ahem. Is there room for one more, or am I too late to join the party?"
    show rango vr surprised with vpunch
    "Startled, Rengar turns around, his grin turning into a frown."
    show rango vr angry with dissolve
    voice "voice/rango/3/re_scene3_3.ogg"
    re "No, as a matter of fact, you're not. I'd say you're right on time... for me to grind
        you into a bloody mist!"
    voice "voice/ezreal/3/ez_re_scene3_3.ogg"
    ez happy "I beg to differ. I think you'll find that my bark definitely matches my bite."
    show rango vr confidentmid with dissolve 
    with vpunch
    "Rengar wastes no time in bounding towards me. He swipes his claws, but I dodge deftly
     and counter-attack."
    voice "voice/ezreal/3/ez_re_scene3_4.ogg"
    ez angry "How about a point blank shot to the face?"
    hide rango with dissolve
    show rango vr confident at right with dissolve
    "I try to hit him with a magic blast, but he dodges out of the way far faster than his
     bulky frame would suggest."
    with hpunch
    show rango vr angry
    voice "voice/rango/3/re_scene3_4.ogg"
    re "You will not hit me that easily, fool- OOF!" with vpunch
    "Finally landing a blow on Rengar, I send him slamming to the ground. He quickly gets to
     his feet - despite my skill, he is far more resourceful than I anticipated."
    voice "voice/ezreal/3/ez_re_scene3_5.ogg"
    ez angry "I think you're just full of hot air."
    hide rango with dissolve
    show rango vr confidentmid with dissolve
    voice "voice/rango/3/re_scene3_5.ogg"
    re "Better than being full of holes when I'm done with you."
    with vpunch
    pause 0.1
    with hpunch
    "Whoever this is, they are a master at the game. Both of us stare at each other, on the brink."
    voice "voice/rango/3/re_scene3_6.ogg"
    re "There is no way I will lose. It would be a dishonor."
    voice "voice/ezreal/3/ez_re_scene3_6.ogg"
    ez surprise "A dishonor to who?"
    show rango vr angrymid 
    voice "voice/rango/3/re_scene3_7.ogg"
    re "That is none of your concern."
    voice "voice/ezreal/3/ez_re_scene3_7.ogg"
    ez flat "You know you're going to lose. Why else would you be stalling?"
    voice "voice/rango/3/re_scene3_8.ogg"
    re "You're good. But, -HISS-"
    show rango vr confidentmid
    #narration
    voice "voice/rango/3/re_scene3_9(gwen).ogg"
    re "Not good enough."
    voice "voice/ezreal/3/ez_re_scene3_8.ogg"
    ez surprise "Oh, yeah? Well, I- wait, what?"
    hide rango with dissolve
    show rango vr confident with dissolve
    voice "voice/rango/3/re_scene3_10(gwen).ogg"
    re "Finally ready to turn tail and run home?"
    "Rather than intimidated, I am a bit confused. For, coming from the deadly lion's mouth is 
     clearly the voice of a young girl."
    show rango vr surprised
    pause 0.5
    "Rengar seems to realize this at about the same time as I do, and steps backwards in shock."
    voice "voice/rango/3/re_scene3_11(gwen).ogg"
    re "What the- What happened to my voice?! Did the hacker- oh no."
    "I cringe as a screeching noise fills my eardrums, and Rengar's voice buzzes loudly."
    show rango vr angry
    with hpunch
    pause 0.3
    with hpunch
    voice "voice/rango/3/re_scene3_12(gwen).ogg"
    re "Come on, turn this thing back on! Why is it NOT WORKING?!"
    voice "voice/ezreal/3/ez_re_scene3_9.ogg"
    ez surprise "Wait a minute - I recognize that voice. You're Gwen, aren't you?"
    voice "voice/rango/3/re_scene3_13(gwen).ogg"
    show rango vr surprised with dissolve
    pause 0.3
    show rango vr angry with dissolve
    re "Gwen? I have never heard of such a- work, you stupid voice changer! Who programmed this garbage?!"
    "Finally, Rengar's voice goes back to normal. But, the damage has been done - by the hacker,
     that is. He must be quite the prankster to go around targeting player voices."
    voice "voice/rango/3/re_scene3_14.ogg"
    re "Rrrr... I must have had something stuck in my throat."
    voice "voice/ezreal/3/ez_re_scene3_10.ogg"
    ez happy "OK, you're definitely Gwen. I'd recognize that voice anywhere."
    show rango vr angrymid with dissolve
    voice "voice/rango/3/re_scene3_15.ogg"
    re "No! I am Rengar, the Pridestalker! FEAR ME!"
    voice "voice/ezreal/3/ez_re_scene3_11.ogg"
    ez happy "Aha... hahah...."
    show rango vr angryblushmid with dissolve
    voice "voice/rango/3/re_scene3_16.ogg"
    re "Don't laugh, feeble human! I will feast on your bones! I WILL DEVOUR YOU!"
    voice "voice/ezreal/3/ez_re_scene3_12.ogg"
    "Er... maybe I should get out of here before he makes good on his promise."
    hide rango with easeoutright
    "Just in time, I warp away, before Rengar pounces on me with all the force of a raging tornado."
    "If Rengar really is Gwen, that raises even more questions than it answers. Like, why the
     choice of avatar... and who were all those other people she was fighting?"
    "I resolve to find out for myself. The fact that she was hit by the hacker's attack has 
     lowered my suspicions, but one can never be too careful."
    $ rango_rp = rango_rp + 4
    scene bg black with dissolve
    pause 0.5
    jump events_end_period
    
label rengar_4:
    $ rango_scene = 4
    $ renpy.block_rollback()
    scene bg soccer day
    "I wonder where Gwen could possibly be now. I checked the soccer field already, but she's
     not there any longer."
    "Just then, I recieve a message on my phone. It's an in-game message, from Rengar of all people."
    "\"Meet me at the Arcade. Galactic Pinball. Bring no one!\""
    "I stroke my chin in contemplation over the peculiar message. Could Gwen finally be fessing up, 
     or is it someone else entirely?"
    "There's only one way to find out, and that's to travel to the Arcade."
    
    scene bg arcade
    "As the only arcade in town, it has miraculously stayed in business in an age of virtual reality."
    "In fact, it seems like the more technology advances, the more the retro kind is coming back into vogue."
    "As I walk in the doorway, I enter a sea of blinkling lights and beeping machines. I search for 
     anything that could match the description of the message."
    show rango flat at left with dissolve
    "Finally, I see it - the Galactic Pinball machine. Someone is already there, playing it incessantly. 
     As I get closer, I realize that it's none other than Gwen from school."
    hide rango with dissolve
    show rango flat with dissolve
    voice "voice/ezreal/4/ez_re_scene4_1.ogg"
    mc flat "So, it really is you..."
    show rango sad with dissolve
    voice "voice/rango/4/re_scene4_1.ogg"
    gw "Yeah. I figured there was no use hiding it any more."
    voice "voice/ezreal/4/ez_re_scene4_2.ogg"
    mc flat "But, why?"
    voice "voice/rango/4/re_scene4_2.ogg"
    gw "Right now, I'm not just a student... I'm also a member of the professional gaming circuit."
    voice "voice/ezreal/4/ez_re_scene4_3.ogg"
    mc surprise "You're a pro gamer!?"
    "Gwen appears to have run out of pinballs, and gives up on the machine, turning around to face me."
    hide rango with dissolve
    show rango sadmid with dissolve
    voice "voice/rango/4/re_scene4_3.ogg"
    gw "Yeah. But, you know how it is... people look down on you for being a girl. They say you must
        have used your feminine wiles to get to the top."
    show rango angrymid with dissolve
    voice "voice/rango/4/re_scene4_4.ogg"
    gw "Like that girl from school, Ami. All she does is blow a few kisses with that fox of hers and
        the whole damn universe kneels at her feet. That's not skill!"
    voice "voice/ezreal/4/ez_re_scene4_4.ogg"
    mc flat "You sure sound like you don't like her..."
    show rango angry with dissolve
    voice "voice/rango/4/re_scene4_5.ogg"
    gw "Damn right I don't. She's so rich and coddled... she doesn't know what it is to have to fight 
        to survive. Her greatest challenge is figuring out which brand of handbag to buy."
    voice "voice/rango/4/re_scene4_6.ogg"
    gw "Me, on the other hand - I just wanted my opponents to see me as a competitor... someone they 
        wouldn't hold back against. So, I decided to make the toughest avatar there was."
    voice "voice/ezreal/4/ez_re_scene4_5.ogg"
    mc angry "Isn't that just making it harder for yourself?"
    show rango happy
    voice "voice/rango/4/re_scene4_7.ogg"
    gw "That's the idea. I'll never know what I'm truly capable of if people don't take me seriously."
    voice "voice/ezreal/4/ez_re_scene4_6.ogg"
    mc flat "I'd fight you on equal terms no matter what your avatar was, but I guess not everyone thinks that way."
    show  rango confident
    voice "voice/rango/4/re_scene4_8.ogg"
    gw "Well, there's that, and there's also the fact that I like being the one that people fear."
    menu:
        "You never scared me.":
            $ renpy.block_rollback()
            voice "voice/ezreal/4/ez_re_scene4_7.ogg"
            mc happy "Pssh - I was never scared of you."
            show rango confidentmid with dissolve
            voice "voice/rango/4/re_scene4_9.ogg"
            gw "Oh, really? I could tell you were shaking in your boots during that fight. Your aim
                was all off!"
            voice "voice/ezreal/4/ez_re_scene4_8.ogg"
            mc flat "Okay... maybe I was a little scared. But, not a lot!"
            show rango confidentclose with dissolve
            voice "voice/rango/4/re_scene4_10.ogg"
            gw "In that case, maybe I should work extra hard to drill the fear into you the next 
                time we fight."
            voice "voice/ezreal/4/ez_re_scene4_9.ogg"
            mc happy "I don't think that will be necessary..."
            show rango confidentmid with dissolve
            voice "voice/rango/4/re_scene4_11.ogg"
            gw "I'm already picturing it now. Ezreal, screaming like a little girl."
            mc happy "..."
            voice "voice/rango/4/re_scene4_12.ogg"
            gw "...Heh."
            $ rango_rp = rango_rp + 1
            
        "It definitely worked.":
            $ renpy.block_rollback()
            voice "voice/ezreal/4/ez_re_scene4_10.ogg"
            mc happy "You definitely got me good back there."
            show rango happy with dissolve
            voice "voice/rango/4/re_scene4_13.ogg"
            gw "At least you're honest. Most people like to hide their weaknesses."
            voice "voice/ezreal/4/ez_re_scene4_11.ogg"
            mc happy "It's no use lying to you. How else are we supposed to trust each other?"
            show rango angry with dissolve
            voice "voice/rango/4/re_scene4_14.ogg"
            gw "You're still on about that trust business? Give it a rest."
            voice "voice/ezreal/4/ez_re_scene4_12.ogg"
            mc happy "Come on... you know you want to come back into the fold."
            show rango blush with dissolve
            voice "voice/rango/4/re_scene4_15.ogg"
            gw "I'll consider it."
    
    show rango surprised with dissolve
    voice "voice/ezreal/4/ez_re_scene4_13.ogg"
    mc flat "I just have one other question - why are you so competitive? It's almost as if you're
        trying to prove something."
    show rango sad with dissolve
    voice "voice/rango/4/re_scene4_16.ogg"
    gw "Uh..."
    voice "voice/ezreal/4/ez_re_scene4_14.ogg"
    mc flat "That is... unless you'd rather not say."
    voice "voice/rango/4/re_scene4_17.ogg"
    gw "No, it's fine... I just want to be able to stand on my own two feet. My dad always 
        raised me by himself, but now he's sick."
    voice "voice/ezreal/4/ez_re_scene4_15.ogg"
    mc surprise "Your dad's... ill?"
    voice "voice/rango/4/re_scene4_18.ogg"
    gw "Not exactly. He was a professional boxer... at one time, he recieved the title of world champion."
    show rango angry with dissolve
    voice "voice/rango/4/re_scene4_19.ogg"
    gw "But, now he's in a lot of debt. It's all because of that one fight. His opponent hit him so hard,
        he got a concussion. And, now, the doctors aren't sure if his brain will recover."
    voice "voice/ezreal/4/ez_re_scene4_16.ogg"
    mc sad "That's terrible..."
    show rango sad with dissolve
    voice "voice/rango/4/re_scene4_20.ogg"
    gw "I know it's not my fault. But, I feel like... maybe, if I become truly independent, he can stop
        worrying about me and he'll get better. The game is where I make my money... so, I have to be the best."
    show rango flat with dissolve
    voice "voice/rango/4/re_scene4_21.ogg"
    gw "But, don't think that means you should go easy on me. I've got no time for sentimental crap."
    voice "voice/ezreal/4/ez_re_scene4_17.ogg"
    mc surprise "Oh, no, of course not. (And that's not just because you'd probably destroy me if I did...)"
    hide rango with dissolve
    show rango angryclose with dissolve
    voice "voice/rango/4/re_scene4_22.ogg"
    gw "And don't bug me while I'm in character. If you say my real name to any of the club members, there'll be
        hell to pay..."
    voice "voice/ezreal/4/ez_re_scene4_18.ogg"
    mc flat "Ulp... I- I think I'll be leaving now."
    call gift_check("Gwen") from _call_gift_check_1
    hide rango with dissolve
    $ rango_rp = rango_rp + 17
    scene bg black with dissolve
    pause 0.5
    jump events_end_period
    
label rengar_5:
    $ rango_scene = 5
    $ renpy.block_rollback()
    scene bg fountain
    "Strangely enough, I see that both Ahri and Rengar are signed on... and on the same server, no less."
    "Could there be something going down that I don't know about? I decide to find out,
     even if it might be a bad idea to intervene."
    show ahri vr happy at right with dissolve
    show rango vr flat at left with dissolve
    voice "voice/rango/5/re_ah_scene5_1.ogg"
    ah "Oh, hello, Ezreal. Me and the furball over here were about to find out which one was superior."
    show rango vr angry at left
    voice "voice/rango/5/re_scene5_1.ogg"
    re "I am not a furball! I am Ren-"
    show ahri vr angrymid at center with dissolve
    voice "voice/rango/5/re_ah_scene5_2.ogg"
    ah "Oh, please. I can smell you from across the map. Honestly, don't you know how to take a bath?"
    show rango vr angrymid at left with dissolve
    voice "voice/rango/5/re_scene5_2.ogg"
    re "I would rather my prey can smell me... it makes the hunt all the more exciting."
    show rango vr angry at left with dissolve
    hide ahri with dissolve
    show ahri vr happy at right with dissolve
    voice "voice/rango/5/re_ah_scene5_3.ogg"
    ah "How crude. I always keep my tails silky smooth... a bit of conditioner works wonders."
    show rango vr angrymid at left with dissolve
    voice "voice/rango/5/re_scene5_3.ogg"
    re "I'm not here to stroke your tail, woman! I'd rather put a few new scars on that smug face of yours."
    show rango vr angry at left with dissolve
    show ahri vr winkmid at center with dissolve
    voice "voice/rango/5/re_ah_scene5_4.ogg"
    ah "I'm sure Ezreal here would love to nestle within my fluffy bosom, wouldn't you?"
    show ahri vr surprised at center with dissolve
    voice "voice/ezreal/5/ez_re_scene5_1.ogg"
    ez flat "Honestly? I'm not so sure about that. Rengar has a point... this game is about competition, not looks."
    show ahri vr angry at right with dissolve
    voice "voice/rango/5/re_ah_scene5_5.ogg"
    ah "You're seriously allying yourself with that monstrosity? Even when I can offer you 
        so many... additional benefits?"
    voice "voice/ezreal/5/ez_re_scene5_2.ogg"
    ez surprise "B-eh..Benefits...?"
    show ahri vr angrymid at right with dissolve
    voice "voice/rango/5/re_ah_scene5_6.ogg"
    ah "What can that beast give you? All he'll do is rip you apart when he's done with little old me."
    show ahri vr angrymid behind rango
    show rango vr angrymid at center with dissolve
    voice "voice/rango/5/re_scene5_4.ogg"
    re "That is a lie! I can give you much! Combat training, stealth training, weapons training..."
    show rango vr angrymid behind ahri
    show ahri vr winkclose at center with dissolve
    voice "voice/rango/5/re_ah_scene5_7.ogg"
    ah "Who cares about training? That's soooo boring. I'm offering you my undivided attention... 
        and love~"
    voice "voice/ezreal/5/ez_re_scene5_3.ogg"
    ez surprise "Your... love!? Gauntlet... stiffening..." #o//o
    show ahri vr winkclose behind rango
    show rango vr blushclose at center
    with hpunch
    voice "voice/rango/5/re_scene5_5.ogg"
    re "Wait! She's not the only one who can be cute! I can be cute, too! *Purrr... purrr* See?
        You can pet me if you want! Just don't join that fiend!"
    show rango vr blushclose behind ahri
    show ahri vr angryclose at center
    with hpunch
    voice "voice/rango/5/re_ah_scene5_8.ogg"
    ah "So, make your choice. Who are you going to ally yourself with... me, or that embarrassing excuse
        for a Champion?"
    show ahri vr blushmid at right
    show rango vr blushmid at left
    menu:
        "Join Ahri":
            $ renpy.block_rollback()
            voice "voice/ezreal/5/ez_re_scene5_4.ogg"
            ez flat "Sorry, but... I'm going to have to go with Ahri on this one. You might be strong, but you
                lack that certain... something."
            show ahri vr blushmid behind rango
            show rango vr angryclose at left
            voice "voice/rango/5/re_scene5_6.ogg"
            re "Grrr... traitorous human! How dare you ally yourself with her?"
            show rango vr angry at left
            show ahri vr wink at right
            voice "voice/rango/5/re_ah_scene5_9.ogg"
            ah "See? I can turn even your closest allies into your enemies in an instant. You have no 
                chance against me."
            show rango vr angrymid at left with dissolve
            voice "voice/rango/5/re_scene5_7.ogg"
            re "We'll see about that. I'll grind both of you into dust!"
            show rango vr angry at left
            show ahri vr winkmid at right with dissolve
            voice "voice/rango/5/re_ah_scene5_10.ogg"
            ah "Do you really think you can beat us? Ezreal here is one of the most skilled Champions.
                If you keep on going like this, you might be deleted~"
            with hpunch
            voice "voice/rango/5/re_scene5_8.ogg"
            re "Raaaaagh! I will have my revenge on you, wretch! My claws will be the last thing you see!"
            hide rango with moveoutleft
            voice "voice/ezreal/5/ez_re_scene5_5.ogg"
            ez flat "Oooh, so scary. As if!"
            $ rango_rp = rango_rp - 50
            $ ahri_rp = ahri_rp + 20
            jump events_end_period     
            
        "Join Rengar":
            $ renpy.block_rollback()
            show ahri vr surprised at right
            show rango vr surprised at left with dissolve
            voice "voice/ezreal/5/ez_re_scene5_6.ogg"
            ez flat "I'm not falling for your tricks. I'm sticking with Rengar on this one."
            show rango vr happymid at left
            voice "voice/rango/5/re_scene5_9.ogg"
            re "Hah! See? He has acknowledged that I am superior!"
            show ahri vr angrymid at right with dissolve
            ah "How disappointing. I see that I'll have to put you both in your place with my foxfire..."
            show rango vr confidentmid at left with dissolve
            voice "voice/rango/5/re_scene5_10.ogg"
            re "Just try it. But, don't think I'll be taken in by your charms."
            show ahri vr winkmid at right with dissolve
            ah "I wouldn't be so sure. Maybe I should try out my ultimate sexy technique on you~"
            show rango vr surprised at left
            with hpunch
            voice "voice/rango/5/re_scene5_11.ogg"
            re "N-NO! I mean... no... that won't be necessary. Because we would wipe you out before you even tried...
                right?"
            voice "voice/ezreal/5/ez_re_scene5_7.ogg"
            ez surprise "Erm... right."
            show rango vr flat at left
            show ahri vr sad at right with dissolve
            show ahri vr wink at right with dissolve
            ah "Sigh... I suppose I am outmatched here. I have to run... au revoir, mon amis!"
            hide ahri with moveoutright
            "As Ahri leaves, both of us breathe a sigh of relief."
            hide rango with dissolve
            show rango vr happymid with dissolve
            voice "voice/rango/5/re_scene5_12.ogg"
            re "Thank you for standing by me. I didn't think you would choose me over the likes of her. For a human,
                you are truly honorable."
            voice "voice/ezreal/5/ez_re_scene5_8.ogg"
            ez happy "Does that mean you'll stop trying to hunt me down?"
            show rango vr confident with dissolve
            voice "voice/rango/5/re_scene5_13.ogg"
            re "Yes, indeed. In fact, you may hunt alongside me whenever you wish. We are now brothers in blood!"
            voice "voice/ezreal/5/ez_re_scene5_9.ogg"
            ez surprise "Yeah! brothers! W-Wait, what? How does that even make sense?"
            show rango vr angrymid with dissolve
            voice "voice/rango/5/re_scene5_14.ogg"
            re "What did you say, human!?"
            voice "voice/ezreal/5/ez_re_scene5_10.ogg"
            ez happyblush "Euh... sure, whatever you say!"
            show rango vr happy with dissolve
            voice "voice/rango/5/re_scene5_15.ogg"
            re "I thought as much. Now, I must bid you farewell. And, good hunting!"
            hide rango with moveoutleft
            $ rango_rp = rango_rp + 20
            $ ahri_rp = ahri_rp - 20
            scene bg black with dissolve
            pause 0.5
            jump events_end_period

label rengar_6:
    $ rango_scene = 6
    $ rango_rp = rango_rp + 10
    $ renpy.block_rollback()
    scene bg bedroom day # but mc goes downstairs to get her first, so maybe something else first for bg
    "I get a message on my phone - it's from Gwen, of all people. 
     And she says she's actually coming to my house!?"
    "I wonder what it could possibly be about. 
     Well, it's not as if I'm otherwise preoccupied."
    "I wait in my room until I hear a knock at the door. 
     My parents are out, so it's just me here. 
     Rushing downstairs, I answer it, and see her standing there, in the flesh."
    show rango confident at left with moveinleft
    voice "voice/rango/6/re_scene6_1.ogg"
    gw "Hiya. Bet you're surprised I came over, huh?"
    voice "voice/ezreal/6/ez_re_scene6_1.ogg"
    mc surprise "Yeah, I didn't expect to see you here. What's up?"
    show rango happy at left
    voice "voice/rango/6/re_scene6_2.ogg"
    gw "Nothing much. I just figured you might want to try this out."
    hide rango with dissolve
    show rango confident at center with dissolve
    "Gwen pulls out what looks like a video game from behind her."
    voice "voice/ezreal/6/ez_re_scene6_2.ogg"
    mc surprise "Woah... is that what I think it is? I didn't think anyone had Mega Smash Fighters Extreme in stock!"
    voice "voice/rango/6/re_scene6_3.ogg"
    gw "I was able to find a copy in a store that I know. They held it for me - I'm a regular customer."
    voice "voice/ezreal/6/ez_re_scene6_3.ogg"
    mc happy "So, you've come to lord it over me?"
    show rango happy with dissolve
    voice "voice/rango/6/re_scene6_4.ogg"
    gw "Heh... of course not. Actually, I was thinking that maybe we could play a few rounds."
    voice "voice/ezreal/6/ez_re_scene6_4.ogg"
    mc surprise "S-Seriously?"
    show rango sad with dissolve
    voice "voice/rango/6/re_scene6_5.ogg"
    gw "If you don't want to, that's fine too..."
    show rango surprised with dissolve
    voice "voice/ezreal/6/ez_re_scene6_5.ogg"
    mc happyblush "Are you kidding? Of course I want to! I'd love to!"
    hide rango with dissolve
    with fade
    "I let Gwen in the house, and show her to my room."
    show rango angry at left with dissolve
    voice "voice/rango/6/re_scene6_6.ogg"
    gw "Is your room always this messy?"
    voice "voice/ezreal/6/ez_re_scene6_6.ogg"
    mc surprise "W-Wait! I can clean up, just give me a-"
    hide rango with dissolve
    show rango happy with dissolve
    voice "voice/rango/6/re_scene6_7.ogg"
    gw "Just messing with you. It's fine. 
        But, I'm flattered that you care enough to bend over backwards for me."
    show rango surprised with dissolve
    voice "voice/ezreal/6/ez_re_scene6_7.ogg"
    mc shyblush "Well, the thing is... I really like you."
    with hpunch
    show rango angryclose
    voice "voice/rango/6/re_scene6_8.ogg"
    gw "You what!? This is 'cuz I'm a gamer, isn't it?"
    show rango surprised with dissolve
    voice "voice/ezreal/6/ez_re_scene6_8.ogg"
    mc angry "No, it's not about that. I like YOU."
    show rango surprisedblush with dissolve
    "Gwen blushes, putting her hand over her mouth. She looks down, fumbling nervously with the game box."
    show rango surprisedblush at left with dissolve
    voice "voice/rango/6/re_scene6_9.ogg"
    gw "Well, that's... that's nice of you... to say."
    voice "voice/ezreal/6/ez_re_scene6_9.ogg"
    mc shyblush "Um... are you all right?"
    show rango sad at left with dissolve
    voice "voice/rango/6/re_scene6_10.ogg"
    gw "Y-Yeah, I'm... this is kind of the first time anyone's said something like that to me, so... ahaha."
    voice "voice/ezreal/6/ez_re_scene6_10.ogg"
    mc happyblush "What's the matter, big strong Rengar can't handle it?"
    show rango angry at center with dissolve
    with hpunch
    voice "voice/rango/6/re_scene6_11.ogg"
    gw "D-Don't bring Rengar into this! Let's just play the game, okay?"
    voice "voice/ezreal/6/ez_re_scene6_11.ogg"
    mc happy "Sure thing. Hmm... I almost forgot how a non-VR system worked. I'm really getting rusty."
    hide rango
    scene cg rango end with fade
    voice "voice/rango/6/re_scene6_12.ogg"
    gw "All the better to beat the stuffing out of you with."
    voice "voice/ezreal/6/ez_re_scene6_12.ogg"
    mc happy "Wow - this game looks just as good as I thought. If not better!"
    voice "voice/rango/6/re_scene6_13.ogg"
    gw "All right, time to do this!"
    "Gwen and I play for a long time, both of us too engrossed in competition to take a break. 
     Finally, we decide to pause for a minute."
    voice "voice/rango/6/re_scene6_14.ogg"
    gw "Phew, I'm pooped." #do girls poop
    voice "voice/ezreal/6/ez_re_scene6_13.ogg"
    mc happyblush "I can't believe you lost so many times. Don't tell me you were holding back." #UR DONGER?
    voice "voice/rango/6/re_scene6_15.ogg"
    gw "No, nothing like that. I just couldn't concentrate... 
        my mind was focusing on other things. Like being next to you..." #in bed
    "She looks at me and smiles."
    voice "voice/rango/6/re_scene6_16.ogg"
    gw "So, up for another round?" #in bed
    voice "voice/ezreal/6/ez_re_scene6_14.ogg"
    mc happy "You bet! Just... let me get some water first. I'm parched..." #thirsty for what, man
    scene bg black with dissolve 
    pause 0.5
    jump events_end_period
    # anything else here? nahhh