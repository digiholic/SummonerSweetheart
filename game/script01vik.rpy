######################################### EVENT DECLARATION
init:
    $ event("vik_1", "act == 'class'", event.once(), "route == 'Leona'", priority = 192)
    $ event("vik_2", "act == 'vr'", event.once(), event.depends("vik_1"), priority = 182)
    $ event("vik_3", "act == 'library'", event.once(), event.depends("vik_2"), "day >= 3", priority = 172)
    $ event("vik_4", "act == 'class'", event.once(), event.depends("vik_3"), priority = 162)
    $ event("vik_5", "act == 'vr'", event.once(), event.depends("vik_4"), "day >= 4", "period == 2", priority = 152)
    $ event("vik_6", "act == 'class'", event.once(), event.depends("vik_5"), "day >= 5", priority = 142)
    $ event("vik_7", "act == 'library'", event.once(), event.depends("vik_6"),"day == 7", "period == 2", "vik_rp >= 70", priority = 132)

######################################### VIKTOR SCRIPT

label vik_1:
    $ vik_scene = 1
    $ renpy.block_rollback()
    scene bg classroom day
    play music "music/bedroom.mp3" fadein 2.0
    "\"Darn\"! slips through my lips as I realize that I left my new HTC phone back at the classroom."
    "I shuffle through the hallway, only getting distracted once: how did a white crow sneak past all the teachers? 
       It's really cute, though!"
    "Its caws are so hushed that the commotion from the other side of the entrance spooks the bird out the opened window."
    voice "voice/viktor/1/vi_scene1_1.ogg"
    cy "... And how do you expect incompetent children to derive a solution 
        for a problem that even a coterie of programming professionals failed to do?"
    voice "voice/viktor/1/vi_zen_scene1_1.ogg"
    z "My observations over the students have led me to believe their capabilities are sufficient to tackle the problem, Cyrus."
    voice "voice/viktor/1/vi_scene1_2B.ogg"
    cy "What benefits does it bring by flailing a bunch of blind monkeys into a virtual world filled with microdelicacies?"
    voice "voice/viktor/1/vi_zen_scene1_2.ogg"
    z "Is there a reason you are particularly oppositional about my decision? 
       I am almost led to believe that there is an ulterior motive behind your antagonistic behavior."
    voice "voice/viktor/1/vi_scene1_3.ogg"
    cy "Tch."
    "Well this is awkward. How am I supposed to go in there, in {i}that{/i} atmosphere?"
    voice "voice/viktor/1/vi_zen_scene1_3.ogg"
    z "I am positive that your assistance would be appreciated in the investigation. 
       However, if I discover that you are impeding any progress made by the club, 
       I will personally ensure consequences will be dealt."
    voice "voice/viktor/1/vi_scene1_4.ogg"
    cy "With what authority?"
    voice "voice/viktor/1/vi_zen_scene1_4.ogg"
    z "I mean as I say."
    "The way they're both talking makes them seem like robots... 
       {i}Gasp{/i}! What if they're AI robots made by Ri-"
    un "Hey, [name]! What are you doing standing outside?"
    mc surprise "!!!!"
    voice "voice/viktor/1/vi_zen_scene1_5.ogg"
    z "[name], welcome. Why don't you come inside?"
    with fade
    show vik flat at left
    show char shen at right
    cy "..."
    voice "voice/viktor/1/vi_zen_scene1_6.ogg"
    z "By any chance, did you stumble upon our conversation?"
    "Looking at Dr. Zen's casual smile, I can't help but feel a bit uneasy. 
       It's like he has a mask - a calm, but merry disguise. Secretive, for sure."
    "And over there by the intercom speakers, Cyrus has his back against the chalkboard and his hands tucked in his red pants. 
       I'm pretty sure he's glaring."
    "With the advisor hovering over the grumpy pupil like a mother catching her son sneaking out at midnight, 
     I can't help but chuckle through my teeth."
    voice "voice/viktor/1/vi_zen_scene1_7.ogg"
    z "Um, [name]?"
    voice "voice/leona/1/le_vi_scene1_1.ogg"
    mc surprise "Oh! Uh, yes. Sorry - I did end up hearing bits of your... debate."
    voice "voice/viktor/1/vi_zen_scene1_8.ogg"
    z "Well, what's been done cannot be undone."
    voice "voice/viktor/1/vi_zen_scene1_9.ogg"
    z "For now, Cyrus will be aiding in your journey of research. The more the merrier, as they say."
    show vik angrymid at left with dissolve
    voice "voice/viktor/1/vi_scene1_5.ogg"
    cy "What? Why would I help this-"
    show vik flatmid at left with dissolve
    voice "voice/viktor/1/vi_zen_scene1_10.ogg"
    z "This is not a request, Cyrus. You {i}will{/i} be helping her."
    "Again with the glare. This time, I know it's directed at Dr. Zen."
    show vik angrymid at left with dissolve
    voice "voice/viktor/1/vi_scene1_6.ogg"
    cy "... If I agree with your absurd shenanigans, 
        will you refrain from encouraging these buffoons to engage in fruitless activities?"
    show vik flat at left with dissolve
    voice "voice/viktor/1/vi_zen_scene1_11.ogg"
    z "I will take that as a confirmation of your cooperation."
    "I can almost hear the outcry of frustration that Cyrus probably wants to let loose right about now."
    "The gaze that he directs at me is filled with a chilling reticence that I find my hands slightly quivering."
    hide vik with dissolve
    show char shen behind vik
    show vik flat at right with dissolve
    voice "voice/viktor/1/vi_scene1_7.ogg"
    cy "If you dare slow me down with needless tasks, I'll be sure to make you face the repercussions of your actions."
    hide vik with easeoutright
    voice "voice/viktor/1/vi_zen_scene1_12.ogg"
    z "Tread carefully going forward, and good luck on the search for the hacker."
    hide char with dissolve
    "With that, both of them head out the room and Dr. Zen flashes me that same deadpan grin."
    "All of this is happening so fast that my mind is spinning like a hamster wheel. 
     Don't I get a say?!"
    $ vik_rp = vik_rp + 3
    stop music fadeout 2.0
    jump events_end_period

label vik_2:
    $ vik_scene = 2
    $ renpy.block_rollback()
    scene bg vr shop
    play music "music/ambient1.mp3" fadein 2.0
    "I'm supposed to be hunting down the hacker, but I'm at a loss as to where I should start."
    "Dr. Zen assigned Cyrus to help me, but I have no idea where that guy hangs out after school. 
     And even if I did find him, he didn't exactly seem overly joyed about working with me."
    "I roam around the fountain trying to collect my thoughts until I reach the shopkeeper. 
     Maybe a shopping spree will clear my mind."
    voice "voice/viktor/2/vi_scene2_1.ogg"
    un "You take up the space of ten elephants and spend eons browsing the store. Stop obstructing my path."
    show vik vr flat with dissolve
    "I turn around, not realizing how long I had been with Doran, the owner. 
     Well, this is convenient. It's the one and only Cyrus."
    "He never talks to anyone and he's always working on his computer, even in class. 
     I didn't realize he got out that often, much less maintained such an... {i}athletic{/i} figure. Or at least his avatar does."
    voice "voice/viktor/2/vi_scene2_2.ogg"
    show vik vr angry with dissolve
    vi "State the purpose of this interruption, now."
    show vik vr flat with dissolve
    voice "voice/leona/2/le_vi_scene2_1.ogg"
    le surprise "Oh! I wasn't expecting to find you here, Cyrus. I see that you like to... play games, and—"
    voice "voice/viktor/2/vi_scene2_3.ogg"
    show vik vr angry with dissolve
    vi "Are people not free to indulge in their own affairs?"
    show vik vr flat with dissolve
    voice "voice/leona/2/le_vi_scene2_2.ogg"
    le surprise "I-I'm just saying that... Everyone says you probably..."
    "It's hard to make words when someone is scrutinizing you with a stony glare."
    voice "voice/viktor/2/vi_scene2_4.ogg"
    vi "I don't share interest in trivial matters such as rumors. 
        The mundane lives of other people deserve none of my attention."
    "Even though I was caught off-guard, I quickly recover my composure in the face of his cold attitude. 
      I'm starting to regret running into Cyrus in the first place."
    voice "voice/leona/2/le_vi_scene2_2.5.ogg"
    le angry "I'm sorry, did I do something wrong? You could have just moved to another lane instead of being a huge jerk!"
    "His expression doesn't change at all."
    voice "voice/leona/2/le_vi_scene2_3.ogg"
    le angry "Geez, what are you? A robot?"
    voice "voice/viktor/2/vi_scene2_5.ogg"
    vi "No."
    "Apparently Cyrus doesn't have a sense of humor."
    show vik vr angrymid with dissolve
    voice "voice/viktor/2/vi_scene2_6.ogg"
    vi "Woman, is there a reason for this unscheduled meeting other than to disrupt my activities?"
    show vik vr flatmid with dissolve
    "Cyrus is quick to snap me out of my thoughts and bring me back to my initial worries."
    voice "voice/leona/2/le_vi_scene2_4.ogg"
    le flat "Mr. Zen said I could ask you for help, right?"
    voice "voice/viktor/2/vi_scene2_7.ogg"
    vi "He didn't actually mean – argh, affirmative. 
        As long as it pertains to the search for the hacker."
    voice "voice/leona/2/le_vi_scene2_5.ogg"
    le flat "Well, I don't really know what to make of all this, 
        so I decided to go inside Summoner's Rift and then I was chatting up a storm with Doran."
    show vik vr angryclose with dissolve
    voice "voice/viktor/2/vi_scene2_8.ogg"
    vi "So you loathe in your own incompetence and seek out help from me as a simple solution?"
    show vik vr flatclose with dissolve
    voice "voice/leona/2/le_vi_scene2_6.ogg"
    le sad "Uh..."
    "He gives me a cold stare without even so much as a notion of breathing. 
     He truly does look inhuman when he becomes like this."
    hide vik with dissolve
    show vik vr flat with dissolve
    voice "voice/viktor/2/vi_scene2_9.ogg"
    vi "The attitude in which you envelop yourself in is unfortunate. 
        You must be -BZZT- ready to set the world on fire." #Viktor - Brand voice
    show vik vr surprised with dissolve
    voice "voice/leona/2/le_vi_scene2_7.ogg"
    le surprise "Wait, what?"
    show vik vr flatmid with dissolve
    voice "voice/viktor/2/vi_scene2_10.ogg"
    vi "Ignorance is fatal, Leona. Only the worthy will survive, 
        and the hacker is making true to this statement." #Zed voice
    show vik vr surprisedmid with dissolve
    voice "voice/leona/2/le_vi_scene2_8.ogg"
    le flat "Uh, Viktor. Your voice..."
    show vik vr angryclose with dissolve
    voice "voice/viktor/2/vi_scene2_11.ogg"
    vi "What?" #Zed voice
    show vik vr surprisedmid with dissolve
    "I cover my mouth as a chuckle breaks through the cracks of my fingers. 
     Viktor's startled face - never saw that coming."
    show vik vr angry with dissolve
    voice "voice/viktor/2/vi_scene2_12.ogg"
    vi "Ugh, that wretched hacker. I hope he writhes, like a worm on a hook." #Thresh voice
    voice "voice/viktor/2/vi_scene2_13.ogg"
    vi "If opportunity befalls me, I will -ZZZ- utterly destroy him." #Thresh - Viktor voice
    voice "voice/leona/2/le_vi_scene2_9.ogg"
    le happy "Ahaha! Now that's what I'd call a punch line... or three!"
    show vik vr angry with dissolve
    voice "voice/viktor/2/vi_scene2_14.ogg"
    vi "Is this amusing for you?"
    voice "voice/leona/2/le_vi_scene2_10.ogg"
    le happy "It was! But anyway, back to nabbing that hacker."
    show vik vr flat
    vi "..."
    voice "voice/viktor/2/vi_scene2_15.ogg"
    vi "As you know, there has been a great deal of modification to the characters, 
        changing not only the gameplay, 
        but the structure of the game itself."
    voice "voice/viktor/2/vi_scene2_16.ogg"
    vi "Obviously, this means that the creator of these alterations is more intelligent than Rito, 
        who cannot defend their simple game from attack."
    voice "voice/viktor/2/vi_scene2_17.ogg"
    vi "The only choice is to see the hacker from a different angle than that of a developer, 
        who only looks at the game in terms of its structural integrity."
    voice "voice/viktor/2/vi_scene2_18.ogg"
    vi "That is why they summoned commoners such as yourself. 
        However, no student here has the proper knowledge to resolve this situation."
    "I'm met with silence once again."
    voice "voice/leona/2/le_vi_scene2_11.ogg"
    le flat "As students we may not have much experience, 
        but that gives us the advantage of perhaps coming up with things that no one has thought of."
    voice "voice/viktor/2/vi_scene2_19.ogg"
    vi "Hah. Don't make me laugh."
    voice "voice/leona/2/le_vi_scene2_12.ogg"
    le angry "I think it's worth a shot."
    voice "voice/viktor/2/vi_scene2_20.ogg"
    vi "It would be a useless endeavor to try."
    voice "voice/leona/2/le_vi_scene2_13.ogg"
    le angry "Have you ever thought about what you would do if you found out you were wrong?"
    voice "voice/leona/2/le_vi_scene2_14.ogg"
    le angry "It sounds like you're more interested in being right than finding out what the truth is."
    hide vik with easeoutright
    "Without another word, Cyrus leaves to continue his battle in the fields, 
     leaving me to appreciate the bright, blue sky of Summoner's Rift... alone."
    "As I watch him circle the fountain, I can't help but feel as if I've fallen behind."
    "I take a deep breath and prepare to wander towards the dragon pit myself, 
     even though I can't comprehend why."
    "I'll progress forward and try to grab onto any clue I scrape up, 
     instead of \"loathing in incompetence,\" as Cyrus would put it."
    $ vik_rp = vik_rp + 10
    stop music fadeout 2.0
    jump events_end_period

label vik_3:
    $ vik_scene = 3
    $ renpy.block_rollback()
    scene bg library
    "I think it's time that I arrange a meeting between me and the lovely textbooks living in the library. 
     Something about hackers is bound to pop up some time today."
    play music "music/ambient2.mp3" fadein 2.0
    "My hands etch a line across the shelves of the history section, the third row down the receptionist desk. 
     \"Runeterra\"... \"Summoner Academy\"... \"Summoner's Rift\"...-"
    with hpunch
    voice "voice/leona/3/le_vi_scene3_1.ogg"
    mc surprise "Oof!"
    voice "voice/viktor/3/vi_scene3_1.ogg"
    show vik angry at left with dissolve
    un "Watch it."
    "You don't even have to tell me who it is. That frigid voice has Cyrus written all over it."
    voice "voice/leona/3/le_vi_scene3_2.ogg"
    mc flat "Sorry. I didn't see you."
    show vik flat at left with dissolve
    voice "voice/viktor/3/vi_scene3_2.ogg"
    cy "Hmph."
    "Tick tock, the clock sings in the empty room, the pulsating beats resonating against the peach colored wallpaper."
    "Where's {i}my{/i} apology? Apparently, my expectant look flies over his head as he waits impatiently for me to move out of the way. 
     His feet tap away as I stand there, arms crossed."
    "Nope, not budging."
    "..."
    "This silence is hopeless. My hand tips the closest book on the shelf out of position so that it lands right in my arms. 
     \"The Building of Summoner's Rift: Virtual Engineering,\" by an anonymous author."
    voice "voice/leona/3/le_vi_scene3_3.ogg"
    mc happy "So~ What brings you to the library, or I guess why here with all the history trivia?"
    voice "voice/viktor/3/vi_scene3_3.ogg"
    cy "Simple: this is the engineering section, my forte. Now, would you hand me the book in your possession?"
    voice "voice/leona/3/le_vi_scene3_4.ogg"
    mc flat "And if I don't want to?"
    voice "voice/viktor/3/vi_scene3_4.ogg"
    cy "The internet will serve its purpose by providing me a copy."
    "I shake my head with a derisive snort."
    
    menu:
        "I'll share it with you.":
            $ renpy.block_rollback()
            $ viktor_confession_pts = 1
            voice "voice/leona/3/le_vi_scene3_5.ogg"
            mc happy "I thought you were the smart one! There's always the option of sharing. Sharing is caring, you know."
            show vik angry at left with dissolve
            voice "voice/viktor/3/vi_scene3_5.ogg"
            cy "Preposterous."
            show vik flat at left with dissolve
            voice "voice/leona/3/le_vi_scene3_6.ogg"
            mc happy "Who even says that these days? 
                And besides, it's not like I'd be holding your hand as we hack away during our reading adventure."
            voice "voice/leona/3/le_vi_scene3_7.ogg"
            mc happy "How about this - I'll take it for now and return it to you the next day with notes. 
                After you get your fair share of reading in, we can compare what we found. Team Summoner Detectives unite!"
            show vik surprised at left with dissolve
            "That was brilliant. Cyrus can't say no to that; I mean, look at him! With his mouth gaping open and his posture so still, 
             he enjoyed that pitch as much as I did."
            show vik flat at left with dissolve
            "...Maybe not."
            voice "voice/leona/3/le_vi_scene3_8.ogg"
            mc happy "Just kidding. You can have the book, just let me copy some pages first."
            voice "voice/viktor/3/vi_scene3_6.ogg"
            cy "Alright. Hurry and complete your task before it gets too late."
            "When his brows lower, his whole face lightens up with relief. I wonder why he's so tense all the time?"
            hide vik with moveoutleft
            "He follows me all the way to the copyroom like a newborn penguin waddling behind its mama... and it's almost adorable.
             After the {i}SHING!{/i} from the copy machine says the job is done, I turn around and again-"
            with hpunch
            mc surprise "Oof!"
            voice "voice/leona/3/le_vi_scene3_9.ogg"
            show vik surprisedclose with easeinright
            mc angry "Why are you standing so close to me?"
            show vik flatmid with dissolve
            voice "voice/viktor/3/vi_scene3_7.ogg"
            cy "To ensure there is no escape."
            voice "voice/leona/3/le_vi_scene3_10.ogg"
            mc surprise "What? Escape to where?"
            voice "voice/viktor/3/vi_scene3_8.ogg"
            cy "I had a mild thought that you would attempt to flee from the premises."
            voice "voice/leona/3/le_vi_scene3_11.ogg"
            mc happy "Wha- ahaha!"
            "For someone who's as uptight as he is, that was pretty funny."
            voice "voice/leona/3/le_vi_scene3_12.ogg"
            mc happy "Well, I won't keep you here anymore. Here you go."
            show vik flat with dissolve
            voice "voice/viktor/3/vi_scene3_9.ogg"
            cy "... I appreciate your cooperation."
            hide vik with dissolve
            $ vik_rp = vik_rp + 5

        "Good going, buddy.":
            $ viktor_confession_pts = 0
            $ renpy.block_rollback()
            voice "voice/leona/3/le_vi_scene3_13.ogg"
            mc happy "Oh, I guess that just means more time for me to hog this book!" #flirt
            voice "voice/viktor/3/vi_scene3_10.ogg"
            cy "Your actions are of no concern to me."
            hide vik with moveoutleft
            "His back says its greetings as Cyrus begins to walk in the direction of anywhere but here."
            voice "voice/leona/3/le_vi_scene3_14.ogg"
            mc flat "Hey! I was just joking with you. No need to ragequit."
            show vik angry with easeinright
            voice "voice/viktor/3/vi_scene3_11.ogg"
            cy "Without the book, you are of no use to me. Obviously, you do not wish to forgo your possession, so I am leaving."
            voice "voice/leona/3/le_vi_scene3_15.ogg"
            mc happy "No, no. You can take it. I don't really need it."
            show vik surprised with dissolve
            pause 1.5
            show vik flat with dissolve
            voice "voice/viktor/3/vi_scene3_12.ogg"
            cy "Then why did you have it?"
            voice "voice/leona/3/le_vi_scene3_16.ogg"
            mc flat "Because it was the first thing I saw."
            pause 2.0
            show vik flatclose
            with hpunch
            pause 0.2
            show vik flat with dissolve
            voice "voice/viktor/3/vi_scene3_13.ogg"
            cy "You perplex me."
            hide vik with easeoutright
            "And with that, he frees my hand of the book and trots away."
    "He heads out past the glass doors, stopping right in front of the checkout station. 
     I never realized how tall he is until his height almost crushes the girl scanning his book ten feet below him."
    "On the other hand, that was almost, kinda pleasant: 
     the whole talking thing, that is. In Cyrus' kind of way."
    "When he \"flees from the premises,\" being the library, 
     a smile sneaks its way on my slightly rosey face. 
     I wonder if he's rubbing off on me?"
    "Another fleeting thought takes hold of my attention - 
     as much as I'd like to think the ice is slowly being chipped away, I wonder what's {i}really{/i} underneath all that mechanic jazz." 
    "A heartfelt side to the oh-so-callous Cyrus. 
     Is he really all that ice cold that people make him out to be, the All-Powerful Frost King Cyrus?"
    "It won't hurt to find out! Hehe~"
    $ vik_rp = vik_rp + 9
    stop music fadeout 2.0
    jump events_end_period
    
label vik_4:
    $ vik_scene = 4
    $ renpy.block_rollback()
    scene bg classroom day
    play music "music/bedroom.mp3"
    "You know, I've been thinking. Cyrus. Talk about an enigma! 
     There's something intriguing about the unknown."
    "Obviously, you have to figure out the obscurity. 
     Otherwise, life would be pretty mundane."
    "There's something about that broody, curt, staunch demeanor he exudes. 
     Not to mention, he is kinda cu—"
    show vik flat at left
    voice "voice/leona/4/le_vi_scene4_1.ogg"
    mc surprise "Oh!"
    "Speak of the devil. He's staring intently at his computer again. Figures. 
     I never noticed how regal his profile is. I wonder if he's busy."
    hide vik with dissolve
    show vik flatclose with dissolve
    voice "voice/leona/4/le_vi_scene4_2.ogg"
    mc flat "Hey, Cyrus."
    "What is he even doing? 
     Day by day, nothing else captivates his attention more than his beloved electronics. 
     I'm going to saunter over and sit on his desk."
    voice "voice/leona/4/le_vi_scene4_3.ogg"
    mc happy "Heeeey. You working hard or hardly working?"
    "Not even a chuckle. In fact, I could have sworn I heard a faint sigh of frustration or annoyance. 
     Maybe he {i}is{/i} doing something important. Oops."
    voice "voice/leona/4/le_vi_scene4_4.ogg"
    mc surprise "S-sorry. I didn't mean to interrupt your work."
    voice "voice/viktor/4/vi_scene4_1.ogg"
    cy "Like you always do?"
    voice "voice/leona/4/le_vi_scene4_5.ogg"
    mc sad "Urgh."
    "Why does he never lighten up?"
    voice "voice/leona/4/le_vi_scene4_6.ogg"
    mc flat "So... what {i}are{/i} you doing?"
    pause 0.5
    voice "voice/viktor/4/vi_scene4_2.ogg"
    cy "Something."
    voice "voice/leona/4/le_vi_scene4_7.ogg"
    mc flat "Oh? What is this \"something\"?"
    pause 0.5
    voice "voice/viktor/4/vi_scene4_3.ogg"
    cy "Work."
    voice "voice/leona/4/le_vi_scene4_8.ogg"
    mc flat "What kind of work?"
    "Seriously, just tell me already! Enough with the dilly daddling."
    voice "voice/viktor/4/vi_scene4_4.ogg"
    cy "It does not concern you."
    "Fine, I'll just look at his screen for myself."
    show vik angryclose
    "As I attempt to huddle over, I see him frantically tapping away at his keyboard, 
     like he's trying to make his work vanish. Was that an alt + f4 right there?"
    show vik flatclose
    voice "voice/leona/4/le_vi_scene4_9.ogg"
    mc happy "Are you afraid of someone finding out your secret appreciation for internet memes? 
        Don't worry, I won't tell anyone." #Flirty
    hide vik with dissolve
    show vik flat with dissolve
    "And again with the sighs. He leans back in his chair and looks up at the ceiling. 
     It's almost like he's trying to convince himself I'm not standing right in front of him."
    "Well, news flash buddy. I'm not giving up that easily!"
    voice "voice/leona/4/le_vi_scene4_10.ogg"
    mc angry "Look, I'm not trying to jeopardize the integrity of your work. 
        I'm just curious. Everyone says you're so distant and aloof; almost robotic even. 
        But something tells me that it's not all true."
    voice "voice/leona/4/le_vi_scene4_11.ogg"
    mc angry "I just want to know... more about you, I guess. Is that so wrong?"
    voice "voice/viktor/4/vi_scene4_5.ogg"
    cy "...Normal people would not understand. 
        Many of my peers remain blissfully ignorant of the world around them, 
        which is why they would not acknowledge my efforts."
    voice "voice/viktor/4/vi_scene4_6.ogg"
    cy "I strive to show the masses they are erroneous in their judgment." #va pronounces erroneous wrong

    menu:
        "What do you mean?":
            $ renpy.block_rollback()
            $ viktor_confession_pts = viktor_confession_pts + 0
            voice "voice/leona/4/le_vi_scene4_12.ogg"
            mc flat "That sounds... complicated, to say the least."
            voice "voice/viktor/4/vi_scene4_7.ogg"
            cy "It is evident in daily routine to see that people's values 
                are placed within themselves and not in others."
            voice "voice/leona/4/le_vi_scene4_13.ogg"
            mc sad "You don't really believe that, do you?"
            show vik flatmid with dissolve
            voice "voice/viktor/4/vi_scene4_8.ogg"
            cy "On the contrary. 
                Anyone who displays such feeble emotions of concern are doing it to gain control; 
                to satiate {i}their{/i} feelings of unrest."
            "My heart pounds against the walls of my chest as Cyrus stares at me. 
             I know he's only doing it to overpower me, but I can't help to find his poise attractive."
            voice "voice/leona/4/le_vi_scene4_14.ogg"
            mc flat "I don't know. Seems like you're grasping at straws to justify why {i}you{/i} 
                isolate yourself from situations. It doesn't hurt to have someone in your corner."
            show vik angry with dissolve
            voice "voice/viktor/4/vi_scene4_9.ogg"
            cy "And it's that kind of reasoning that cause people to remain naive and oblivious. 
                They receive handouts, never doing anything for themselves. Never facing hardships on their own."
            show vik flat with dissolve
            voice "voice/viktor/4/vi_scene4_10.ogg"
            cy "But I wouldn't expect someone like you to understand."
            voice "voice/leona/4/le_vi_scene4_15.ogg"
            mc angry "What's that supposed to mean?!"
            show vik flat at left with dissolve
            "Cyrus goes back to his computer, giving off this aura that the conversation is over."
            voice "voice/viktor/4/vi_scene4_11.ogg"
            cy "I have something to do."
            "I find an empty desk to rest as I face him off. I'm seething at his words, his accusations. 
             How can someone be so cold?"
            voice "voice/leona/4/le_vi_scene4_16.ogg"
            mc angry "So then, how does the stuff you're working on have anything to do with teaching the masses they're wrong?"
            "He's gone back to ignoring me. This is so infuriating."
            voice "voice/leona/4/le_vi_scene4_17.ogg"
            mc angry "Would you at least tell me that much?"
            show vik angry at left with dissolve
            voice "voice/viktor/4/vi_scene4_12.ogg"
            cy "It has nothing to do with you, nor do I wish to involve you in my matters."
            "This is pointless. I want to leave. But I can't. I don't know why, I just can't."
            mc angry "..."
            voice "voice/leona/4/le_vi_scene4_18.ogg"
            mc angry "So, about the hacker. At least help me piece together the clues we have on the hacker so far. 
                What do you think his motive could be?"
            hide vik with dissolve
            show vik angryclose with dissolve
            "I think that struck a nerve. The fumes of his anger seem to emanate from his body. 
             He's staring daggers at me."
            voice "voice/viktor/4/vi_scene4_13.ogg"
            cy "You should know when to quit. 
                That issue is over your head, and the consequences for getting involved will be undesirable."
            "Yep, this is hopeless. I should have left earlier with some of my dignity."
            hide vik with dissolve
            show vik flat at left with dissolve
            voice "voice/leona/4/le_vi_scene4_19.ogg"
            mc angry "So I'm just like everyone else, huh?"
            "At this point, even the silence is better company than him. Maybe another day, Cyrus."
            hide vik with dissolve
            $ vik_rp = vik_rp - 5
            stop music fadeout 2.0
            jump events_end_period

        "Stop being so vague and spit it out!":
            $ renpy.block_rollback()
            $ viktor_confession_pts = viktor_confession_pts + 1
            voice "voice/leona/4/le_vi_scene4_20.ogg"
            mc angry "Enough with the riddles, Cyrus. Tell me what you {i}really{/i} mean."
            voice "voice/viktor/4/vi_scene4_14.ogg"
            cy "My business does not concern you."
            voice "voice/leona/4/le_vi_scene4_21.ogg"
            mc flat "Are there ways I can help?"
            show vik flatmid with dissolve
            voice "voice/viktor/4/vi_scene4_15.ogg"
            cy "Do my comments hold no value? I have clearly stated that I do not wish to involve you in my matters."
            voice "voice/leona/4/le_vi_scene4_22.ogg"
            mc angry "Why? Why are you acting like the next Superman who's destined to hold the weight of the world on your shoulders?"
            "What am I even saying anymore..."
            voice "voice/viktor/4/vi_scene4_16.ogg"
            cy "My issues are mine alone."
            voice "voice/leona/4/le_vi_scene4_23.ogg"
            mc sad "But it doesn't have to be! I can help you, and not just me! There's Dr. Zen, Jason, and -"
            "Clearly Cyrus thinks I'm unworthy. He stomps away towards his desk, back to his computer."
            voice "voice/viktor/4/vi_scene4_17.ogg"
            show vik angryclose with dissolve
            cy "And what abilities do you possess that could possibly assist me?"
            voice "voice/leona/4/le_vi_scene4_24.ogg"
            mc angry "I-I-I don't know! But I want to!"
            show vik surprisedclose with dissolve
            pause 1.0
            show vik flatclose with dissolve
            voice "voice/viktor/4/vi_scene4_18.ogg"
            cy "Why?"
            voice "voice/leona/4/le_vi_scene4_25.ogg"
            mc sad "Because-"
            "There’s a swelling in my throat, giving way to my voice cracking. If I tell him the real reason, he'll blow me off."
            voice "voice/leona/4/le_vi_scene4_26.ogg"
            mc sad "Because... this seems important to you. I mean, we're in this club together. 
                Why not work together on other things?"
            pause 1.0
            hide vik with dissolve
            show vik flat with dissolve
            ## cutoff where kevin stopped doing viktor stuff
            voice "voice/viktor/4/vi_scene4_19.ogg"
            cy "I don't need anyone's help."
            with vpunch
            "Argh! I stamp my foot hard on the floor with enough force that the tables next to us shake a slight dance."
            voice "voice/leona/4/le_vi_scene4_27.ogg"
            mc angry "No one can do everything alone. You have to let someone in."
            voice "voice/viktor/4/vi_scene4_20.ogg"
            cy "So are you saying we should be friends?"
            voice "voice/leona/4/le_vi_scene4_28.ogg"
            mc sad "...Maybe."
            show vik angrymid with dissolve
            voice "voice/viktor/4/vi_scene4_21.ogg"
            cy "How humorous. What do you know about me? Nothing, because if you did-"
            pause 0.2
            show vik flatmid with dissolve
            pause 0.5
            "He's looking straight at me. His piercing glare acts as the ultimate move right before my defeat."
            voice "voice/viktor/4/vi_scene4_22.ogg"
            cy "Your presence would have departed much sooner, along with your annoying demeanor."
            "I'm not sure if there's a feeling beyond crap, but if there is, that's how I'm feeling right now. 
             Except worse - like over 9,000 times worse."
            hide vik with dissolve
            "I slump down the chair closest to me. Any energy I had to argue with Cyrus was zapped away by his contempt. 
             All I can do is stare at my feet."
            show vik flat with dissolve
            voice "voice/viktor/4/vi_scene4_23.ogg"
            cy "Nobody is willing to sacrifice their attention and care if it does not result in their favor. 
                Everyone is engulfed in their own world, never hesitating to destroy others in the process if deemed necessary."
            voice "voice/viktor/4/vi_scene4_24.ogg"
            cy "It's all about self-gratification."
            "Whoa. That came out of nowhere. Maybe I {i}am{/i} getting through to him."
            voice "voice/leona/4/le_vi_scene4_29.ogg"
            mc flat "Not everyone is like that. There are people who fight for what they believe in without losing their friends."
            voice "voice/viktor/4/vi_scene4_25.ogg"
            cy "For what reason would anyone do that?"
            voice "voice/leona/4/le_vi_scene4_30.ogg"
            mc happy "Perhaps because the reward is worth the work."
            voice "voice/viktor/4/vi_scene4_26.ogg"
            cy "That still boils down to self-gratification."
            voice "voice/leona/4/le_vi_scene4_31.ogg"
            mc angry "So, are you saying that we're not supposed to be happy? That we aren't allowed friendship without benefit?"
            pause 1.0
            voice "voice/viktor/4/vi_scene4_27.ogg"
            cy "You are an imbecile. After the novelty of relationships diminish, people cast it aside into oblivion."
            voice "voice/leona/4/le_vi_scene4_32.ogg"
            mc angry "That just sounds lonely."
            voice "voice/viktor/4/vi_scene4_28.ogg"
            cy "Those feelings do not bring about success or progress."
            "This is pointless. I want to leave. But I can't. I don't know why, I just can't."
            mc angry "..."
            voice "voice/leona/4/le_vi_scene4_33.ogg"
            mc angry "So, about the hacker. At least help me piece together the clues we have on the hacker so far. 
                What do you think his motive could be?"
            "I think that struck a nerve. The fumes of his anger seem to emanate from his body. He's staring daggers at me."
            show vik angry
            voice "voice/viktor/4/vi_scene4_29.ogg"
            cy "You should know when to quit. Go back to the world you know and stay out of the one you don't."
            "Yep, this is hopeless. I should have left earlier with some of my dignity."
            voice "voice/leona/4/le_vi_scene4_34.ogg"
            mc angry "So I'm just like everyone else, huh?"
            show vik surprised
            "At this point, even the silence is better company than him. Maybe another day, Cyrus."
            hide vik with dissolve
            $ vik_rp = vik_rp - 8
            stop music fadeout 2.0
            jump events_end_period
        

label vik_5:
    $ vik_scene = 5
    $ renpy.block_rollback()
    scene bg bedroom night
    play music "music/bedroom.mp3" fadein 2.0
    "Why is it that Cyrus has taken control over the pilot seat in my head? I see nothing but him lately; 
     him and those captivating golden crimson eyes."
    "And what was up with his sullen mood? It's a puzzle waiting to be unraveled, but until it does, 
     how do I face him? Should I apologize or stay angry? 
     Maybe I should dart in the other direction when he graces me with his remarkably dashing glare?!"
    "No, no, what am I saying? I can't do that. None of this is me!"
    "\"Arghhh!\" is all I groan as my head buries into the softness of my poofy pillow. 
     At least I've got my reliable bunny cushion to comfort my headache."
    "So I guess it's back to square one? Or maybe even negative square a million?!"
    "When I see all these sides of Cyrus that others don't know - dorky, silly, angry, confused - it's like I'm one step ahead of the game."
    "... Wait. Ahead of the game?"
    "What game...?"
    "UWAHHH! I don't even know what I'm saying anymore!" #blush
    "Face, meet Mrs. Kiki, the Bunny Pillow. \"Shwoop\"! Feathers scamper in all directions as my head crashes against the pillow."
    "..."
    voice "voice/leona/5/le_vi_scene5_1.ogg"
    mc angry "Stupid Cyrus. He's turned me into one of his mindless minions - or maybe mind{i}ful{/i}?"
    "There's no point sitting here and just thinking about it..."
    "Time to hop on Summoner's Rift! was my last thought before I hear the warp sounds and-"
    stop music fadeout 1.0
    #Transition to Fountain BG
    scene bg fountain with fade
    show vik vr angry with dissolve
    voice "voice/viktor/5/vi_scene5_1.ogg"
    vi "Inferior constructs! Your bodies are all frail; relinquish the flesh and join the glorious evolution!"
    "Not exactly the person I want to see right now."
    play music "music/ambient1.mp3" fadein 1.0
    show vik vr happy with dissolve
    voice "voice/viktor/5/vi_scene5_2.ogg"
    vi "Ah, Leona. Have you come to embrace progress?"
    hide vik with easeoutleft
    "My legs carry me far, far away. Away from him. Perhaps the fields of justice will be enough of a distraction."
    "Mindless swinging and slashing partner throughout my hack 'n slash adventure, 
     but not even the sun's ray will sunder my own thoughts."
    show char shen with dissolve
    voice "voice/viktor/5/vi_zen_scene5_1.ogg"
    s "Leona, you look troubled."
    voice "voice/leona/5/le_vi_scene5_2.ogg"
    "Dr. Zen, er, uh, Shen..."
    voice "voice/viktor/5/vi_zen_scene5_2.ogg"
    s "The Radiant Dawn is not looking so sunny this afternoon."
    voice "voice/leona/5/le_vi_scene5_3.ogg"
    le sad "Aha. I guess not."
    voice "voice/viktor/5/vi_zen_scene5_3.ogg"
    s "What occupies your thoughts?"
    voice "voice/leona/5/le_vi_scene5_4.ogg"
    le sad "It's about... a friend."
    voice "voice/leona/5/le_vi_scene5_5.ogg"
    le sad "He keeps to himself a lot. As time goes on, I hope that he opens up to me, but recently, I think I made it worse."
    voice "voice/viktor/5/vi_zen_scene5_4B.ogg"
    s "Hmm."
    voice "voice/leona/5/le_vi_scene5_6.ogg"
    le sad "Maybe I'm prodding too much into his business. But I want him to realize I'm there as support, 
        not to pester him like a useless jungler."
    voice "voice/viktor/5/vi_zen_scene5_5B.ogg"
    s "Mmm."
    voice "voice/leona/5/le_vi_scene5_7.ogg"
    le sad "He hates me, I can feel it. But I don't know why, or how to fix that... if I even can."
    voice "voice/leona/5/le_vi_scene5_8.ogg"
    le happy "I want to learn more about him: what does he like to eat? What's his favorite band? His dreams..."
    pause 0.5
    le flat "..."
    pause 0.5
    voice "voice/leona/5/le_vi_scene5_9.ogg"
    le sad "...Does he ever get lonely..."
    "I don't know why that last statement sent a pang through my heart."
    voice "voice/viktor/5/vi_zen_scene5_6.ogg"
    s "Is this friend more than a friend?"
    
    menu:
        "What?!":
            $ renpy.block_rollback()
            $ viktor_confession_pts = viktor_confession_pts + 0
            voice "voice/leona/5/le_vi_scene5_10.ogg"
            le surprise "What are you saying! Uh, I..."
            "My tongue gets twisted in five hundred knots before I can say another word. Or maybe it's my heart."
            "Huh. My affections for Cyrus might run deeper than I thought."
        
        "I... I'm not sure.":
            $ vik_rp = vik_rp + 3
            $ renpy.block_rollback()
            $ viktor_confession_pts = viktor_confession_pts + 1
            voice "voice/leona/5/le_vi_scene5_11.ogg"
            le surprise "T-that's... No, no. I mean, he obviously doesn't like me. The way he talks to me gives me that much."
            voice "voice/leona/5/le_vi_scene5_12.ogg"
            le sad "I really don't know how I feel."
            "Or do I...?"
    
    voice "voice/viktor/5/vi_zen_scene5_7.ogg"
    s "Perhaps your \"friend\" is unsure of himself. Not everyone opens up so easily."
    voice "voice/viktor/5/vi_zen_scene5_8.ogg"
    s "Give him some time. And space."
    voice "voice/leona/5/le_vi_scene5_13.ogg"
    le sad "But my worries make it hard to leave him alone. I want to show him that he doesn't have to ride solo - 
        that there is someone who cares. Someone who thinks about him. Possibly even -"
    "What great timing, Mr. Hacker. Oh, and there's the wonderful \"Attempting to Reconnect\" pop up."
    voice "voice/leona/5/le_vi_scene5_14.ogg"
    le surprise "Uh, Shen? Are you there?"
    voice "voice/viktor/5/vi_zen_scene5_9.ogg"
    s "Be careful out there, and always be alert."
    hide char with dissolve
    "Wait, you're just going to leave me here while the game is glitching?! Ugh."
    "By the time I approach the fountain, quiet echoes against the hollow structure veer all over the scenery. 
     It almost feels as though a timid gaze haunts my steps."
    "Or maybe the hysteria is getting to me. 
     The dragon pit will probably give me food for thought, since reports of glitches have been occurring there."
    "But on my way, what accompanies me isn't the sound of my own strides but the eerie darkness that engulfs the screen. 
     Screeches of silence emerges from the pits of this black void."
    "Following the stillness is a presence I can feel approaching my very motionless character."
    voice "voice/leona/5/le_vi_scene5_15.ogg"
    le angry "W-who's there?! I know you're out here!"
    "An odd silence, and very ghostly to boot. Why do I get the feeling that I'm the only one trapped here?"
    with vpunch
    "{i}PANG!{/i} W-what was that?!" #shake
    with hpunch
    "{i}SHING!{/i} Someone - or something - is definitely attacking me." #shake
    with hpunch
    "That's enough! I must retaliate before I suffer any more grievous wounds. {i}SWOOSH!{/i}" #shake
    "I reach for my handy dandy sword, but notice that my hands grasp at nothing; both of them! My shield is gone, too."
    "Hopping here and there helps me avoid the impending attacks I hear from all directions. 
     Then suddenly, my feet halt in its tracks. I can't even fall over by the sudden impact of not moving."
    "Am I... dying here? Alone?"
    with hpunch
    pause 0.3
    with hpunch
    pause 0.2
    voice "voice/leona/5/le_vi_scene5_16.ogg"
    le sad "H-help."
    "I can feel the points of my health steadily decreasing by every 30 points. My conscience waning..."
    un "!!!"
    "A soft, radiant glow covers the edges of my golden armor, enrapturing my wounds in a rich light. 
     Small trinkets of glitter disperse into the air as it leaves a healing effect on my avatar."
    show vik vr angrymid with dissolve
    voice "voice/viktor/5/vi_scene5_3.ogg"
    vi "Are you okay?"
    voice "voice/leona/5/le_vi_scene5_17.ogg"
    le surprise "V-viktor?"
    voice "voice/viktor/5/vi_scene5_4.ogg"
    vi "Are you injured?"
    voice "voice/leona/5/le_vi_scene5_18.ogg"
    le flat "I, uh, no. I'm fine, thanks."
    voice "voice/leona/5/le_vi_scene5_19.ogg"
    le surprise "...How did you know where I was? Or rather, how did you do that?"
    pause 0.3
    hide vik with dissolve
    show vik vr flat with dissolve
    vi "..."
    voice "voice/leona/5/le_vi_scene5_20.ogg"
    le surprise "Did you find an exploit?! No! You found the hacker, didn't you?!"
    voice "voice/viktor/5/vi_scene5_5.ogg"
    vi "No. I'm unaware of those details."
    voice "voice/leona/5/le_vi_scene5_21.ogg"
    le flat "Oh. Wait, then how did you get here-"
    voice "voice/viktor/5/vi_scene5_6.ogg"
    vi "Did you mean what you said? That you wanted to be more acquainted with me? To get closer?"
    "I hope Viktor didn't just see the fifty shades of red my face just sped through."
    "Wait a minute..."
    
    menu:
        "How did you know that?":
            $ renpy.block_rollback()
            $ viktor_confession_pts = viktor_confession_pts + 0
            voice "voice/leona/5/le_vi_scene5_22.ogg"
            le angry "What? Were you eavesdropping? Or maybe you're modifying values in the game somehow!"
            show vik vr surprised with dissolve
            pause 0.2
            show vik vr flat with dissolve
            voice "voice/viktor/5/vi_scene5_7.ogg"
            vi "...I must go."
            hide vik with easeoutleft
            voice "voice/leona/5/le_vi_scene5_23.ogg"
            le surprise "Cyrus! Err, Viktor! Wait!"
            "I don't get a chance to catch him before I hear the warp that sends him back to the real world."
            "What was that all about?"
            $ vik_rp = vik_rp + 12
            stop music fadeout 2.0
            jump events_end_period

        "Something's fishy here.":
            $ viktor_confession_pts = viktor_confession_pts + 1
            $ renpy.block_rollback()
            voice "voice/leona/5/le_vi_scene5_24.ogg"
            le flat "This makes no sense. How could you possibly know...? Are you the hacker, Viktor?"
            show vik vr surprised with dissolve
            pause 0.5
            voice "voice/viktor/5/vi_scene5_8.ogg"
            vi "I, uh..."
            hide vik with dissolve
            "{i}*BLIP*{/i}"
            "Did he...? He {i}totally{/i} just logged off. This is not over yet!"
            stop music fadeout 2.0
            jump events_end_period
            $ vik_rp = vik_rp + 16
    
label vik_6:
    $ vik_scene = 6
    $ renpy.block_rollback()
    scene bg classroom day
    play music "music/bedroom.mp3" fadein 2.0
    "{i}-BZZT-{/i}" with hpunch
    "Huh? What's this? A text message?"
    voice "voice/leona/6/le_vi_scene6_1.ogg"
    mc flat "...Park. 4:00PM. And it's from an unknown number. Super weird." #Reading to self
    "Well, it doesn't hurt to snoop around for a bit."
    #Transition to park
    scene bg park day with fade
    "I love this time of year. The gentle warmth from the sun, the crisp blue skies, 
     and the freshness of newly-blossomed flowers permeating the air."
    "Everything feels refreshing, and new. Like the beginnings of a brand new start; a clean slate."
    voice "voice/viktor/6/vi_scene6_1.ogg"
    cy "...[name]. Hello."
    show vik flat at right with dissolve
    voice "voice/leona/6/le_vi_scene6_2.ogg"
    mc surprise "Cyrus."
    "I guess I should have seen this coming, what with how he acted last time."
    voice "voice/viktor/6/vi_scene6_2.ogg"
    cy "A pleasure to see you."
    voice "voice/leona/6/le_vi_scene6_3.ogg"
    mc angry "Not sure I should say likewise."
    voice "voice/viktor/6/vi_scene6_3.ogg"
    cy "I suppose that response was warranted."
    hide vik with dissolve
    show vik flat at center with dissolve
    "He sort of does this awkward gesture to get us to go for a walk. Should I fancy his invitation?"
    "...Gosh, his stoic expression leaves me baffled with curiosity. What harm is there? 
     He does owe me an explanation after all."
    hide vik with dissolve
    "The long, winding path of pebbles and leaflets of flowers stretch out 
     past the puddles of Sakura trees and teal bushes that glint under the sun."
    "Bustling noise catches drift in the air as a cart of students and parents dart off 
     toward the row of food trucks planted right next to the playground haven."
    "Our marches and the charming melodies of the blue jays harmonize together to complement 
     the songs of the sun's affectionate flickers."
    mc flat "..."
    cy "..."
    "Does he expect the air to do all the talking? I mean, I can only do so much scenery narration."
    voice "voice/leona/6/le_vi_scene6_4.ogg"
    mc flat "Uh, Cyrus."
    show vik blush with dissolve
    cy "... ..."
    "I can't believe it! Is he... fidgeting? Is he nervous?! 
     The stereotypical straight man acting like Jason? The world is coming to an end."
    voice "voice/viktor/6/vi_scene6_3.5.ogg"
    cy "We need to discuss the occurrences of our last encounter."
    voice "voice/leona/6/le_vi_scene6_5.ogg"
    mc flat "Okay. Keep going."
    show vik flat
    cy "..."
    
    menu:
        "Omigosh. Stop with your kiddy behavior!":
            $ vik_rp = vik_rp + 2
            $ viktor_confession_pts = viktor_confession_pts + 1
            $ renpy.block_rollback()            
            voice "voice/leona/6/le_vi_scene6_6.ogg"
            mc angry "Will you stop acting like an anxious adolescent wailing in their teenage angst and spit it out already?!"
            show vik angry
            voice "voice/viktor/6/vi_scene6_4.ogg"
            cy "It is difficult to explain my situation."
            voice "voice/leona/6/le_vi_scene6_7.ogg"
            mc angry "Try  me."
            show vik flat
            cy "..."
                    
        "What's holding you back?":
            $ viktor_confession_pts = viktor_confession_pts + 0
            $ renpy.block_rollback()
            voice "voice/leona/6/le_vi_scene6_8.ogg"
            mc flat "I guess this is a delicate issue for you."
            cy "..."
            voice "voice/leona/6/le_vi_scene6_9.ogg"
            mc flat "Will you at least tell me how you found me? Or the hacker?"
            voice "voice/viktor/6/vi_scene6_5.ogg"
            cy "I do not know his identity."
            voice "voice/leona/6/le_vi_scene6_10.ogg"
            mc angry "That's a lie, and we both know it."
            cy "..."
            
    if viktor_confession_pts > 3: # viktor confesses if we have 4 points or more
        $ vik_confessed = True
        voice "voice/viktor/6/vi_scene6_6.ogg"
        cy "Under duress, I came across the teachings of an acclaimed computer engineer and fell victim to his brilliant babbling."
        voice "voice/viktor/6/vi_scene6_7.ogg"
        cy "His TED talks were exceptionally inspirational; he explains the engine of human progress throughout history. 
            In his lectures, countless observations prove true to the idea of evolutionary advancement."
        voice "voice/viktor/6/vi_scene6_8.ogg"
        cy "The collective brain is the essence of an individual's intellectual worth. 
            He advocates the need to rise during our prime stage of genius."
        voice "voice/leona/6/le_vi_scene6_11.ogg"
        mc surprise "Wait. Are you saying...?"
        voice "voice/viktor/6/vi_scene6_9.ogg"
        cy "Yes, your assumptions are correct."
        voice "voice/leona/6/le_vi_scene6_12.ogg"
        mc angry "Spell it out for me; my brain is still swimming in ideas."
        show vik happy with dissolve
        "Did he just crack a chuckle?"
        show vik flat with dissolve
        voice "voice/viktor/6/vi_scene6_10.ogg"
        cy "I came in contact with the programmer who is terminating League of Legends."
        "What the - brainfart."
        mc surprise "...???"
        "Derp."
        voice "voice/leona/6/le_vi_scene6_13.ogg"
        mc flat "Okaaay. So you're like, what, the hacker's protégé?"
        voice "voice/viktor/6/vi_scene6_11.ogg"
        cy "More or less, I suppose."
        voice "voice/leona/6/le_vi_scene6_14.ogg"
        mc flat "Uwahhhh, this is all so mind-blowing... 
            Hold the phone - so that means that {i}you{/i} tried to... kill me?"
        show vik angry
        voice "voice/viktor/6/vi_scene6_12.ogg"
        cy "No, never. That was the hacker. All I did was prevent his acts of insanity."
        show vik flat
        voice "voice/leona/6/le_vi_scene6_15.ogg"
        mc flat "But, why? I don't understand. What benefits are there for you?"
        voice "voice/viktor/6/vi_scene6_13.ogg"
        cy "At the time, I believed it best to rid the community of incompetent fools, 
            but his recent activity makes it difficult to justify those beliefs."
        voice "voice/leona/6/le_vi_scene6_16.ogg"
        mc surprise "Eh? You mean, you were worried?"
        voice "voice/viktor/6/vi_scene6_14.ogg"
        cy "In summation... yes."
        "Wowow. How many times will my face mirror the blaring red flush of an apple?"
        voice "voice/leona/6/le_vi_scene6_17.ogg"
        mc happy "... Thanks, Cyrus. For saving me-"
        show vik happy with dissolve
        "He reciprocates my gratitude with a nonchalant head bob."
        voice "voice/leona/6/le_vi_scene6_18.ogg"
        mc happyblush "-and telling me the truth. I can't imagine how hard that was."
        voice "voice/leona/6/le_vi_scene6_19.ogg"
        mc happyblush "Ahem. Okay! From now on, promise me you won't burden everything on yourself; 
            you'll share your troubles with friends, and people who care."
        show vik flat
        cy "..."
        voice "voice/leona/6/le_vi_scene6_20.ogg"
        mc happy "I'll buy you a crêpe if you say yes!"
        show vik surprised with dissolve
        "Aha! Cyrus just made three expressions back to back - confused, stumped, defeat - that's a first! Score!"
        pause 0.2
        show vik happy with dissolve
        "Again with the nod, but this time in approval."
        $ vik_rp = vik_rp + 8
    else: # viktor does not confess if we have less than 4 points
        voice "voice/viktor/6/vi_scene6_15.ogg"
        cy "I..."
        voice "voice/viktor/6/vi_scene6_16.ogg"
        cy "I was attempting to thwart the hacker in his cybersteps by constructing an engine of my own. That is all."
        voice "voice/leona/6/le_vi_scene6_21.ogg"
        mc angry "That's it? That's all you have to say?"
        pause 1.0
        voice "voice/viktor/6/vi_scene6_17.ogg"
        cy "Affirmative."
        "Ugh, back to where we started! The old, cold Cyrus, never opening up." #angry
        "I almost had him, I swear. Why doesn't he just trust me?" #sad

    voice "voice/leona/6/le_vi_scene6_22.ogg"
    mc happy "Just know that I am your friend, Cyrus. If a cat's got your tongue, I'll be there to slash it away."
    show vik surprised with dissolve
    pause 0.5
    show vik flat with dissolve
    voice "voice/viktor/6/vi_scene6_18.ogg"
    cy "Why would a cat ever approach my mouth?"
    voice "voice/leona/6/le_vi_scene6_23.ogg"
    mc flat "...Nevermind."
    "Well, that was pretty intense and exhausting. I can feel my shoulders sagging against the sunlight."
    voice "voice/leona/6/le_vi_scene6_24.ogg"
    mc happy "Anyways, let's get a crêpe!"
    show vik surprised with dissolve
    pause 0.2
    hide vik with fade
    "I reach out for his hand and drag him through the waterfalls of people crowding the locally famous Crêpe Stop. 
     The world literally stops for a bite of their heavenly pastries."
    show vik happyclose with fade
    "One look at his gleaming eyes tells me he's gloating in bliss as he munches down 
     on his Very Vanilla & Banana Ice Cream Crêpe. As do I."
    hide vik with dissolve
    show vik happymid with dissolve
    voice "voice/viktor/6/vi_scene6_19.ogg"
    cy "Thanks."
    "Hehe. Well, that wasn't too bad of an ending there, was it?"
    call gift_check("Cyrus") from _call_gift_check_16
    $ vik_rp = vik_rp + 4
    stop music fadeout 2.0
    jump events_end_period

label vik_7:
    $ vik_scene = 7
    $ vik_rp = vik_rp + 12
    $ renpy.block_rollback()
    scene bg library
    play music "music/ambient2.mp3" fadein 2.0
    "I have this odd feeling churning in my gut that tells me Cyrus will spectularly appear out of nowhere right at this moment."
    "..."
    "Maybe not. I guess fate isn't as kind as I thou-"
    scene cg vik end with fade
    mc surprise "Cyrus!"
    voice "voice/viktor/7/vi_scene7_1.ogg"
    cy "Oh, it is a surprise to see you here, [name]."
    "Hehe, not really."
    mc surprise "What are you up to?"
    voice "voice/viktor/7/vi_scene7_2.ogg"
    cy "Collecting data to optimize my understanding."
    mc flat "Understanding? Of what?"
    cy "..."
    "Oh no, buddy. We aren't playing the silence game again. You should've learned {i}that{/i} the first time, bub!"
    "Time to take a sneak peek at his precious \"research\" material!"
    "As Cyrus takes no notice of my slow but steady progress toward his side of the table, 
     I come close enough to the nape of his neck that my breath leaves a soft imprint on his silky, smooth skin."
    scene bg library with fade
    with hpunch
    show vik surprisedblush with dissolve
    cy "?!?!?!?" #Angry blush?
    voice "voice/viktor/7/vi_scene7_3.ogg"
    cy "H-Have you turned delusional? What are you doing?!"
    hide vik with dissolve
    "His fumbling around the books leaves them exposed on the ground, tripping over each other. 
     Cyrus' graceful attempt to rummage through them amounts to the most entertaining 5 seconds of my life."
    show vik angrymid with dissolve
    voice "voice/viktor/7/vi_scene7_4.ogg"
    cy "I would appreciate if you would refrain from such unsightly behavior."
    mc happy "Hahaha! I'm the one with unsightly behavior?"
    show vik flatmid
    "Oh? What's this? I notice that the books he gathered didn't contain all the technical jargon that I would expect of him to enjoy."
    mc surprise "Morello's basic guide... to humor? Cyrus, are you..."
    hide vik with dissolve
    show vik surprisedblush with dissolve
    cy "..."
    show vik blush
    "Now Cyrus looks away, ears turning beet red! This has got to be the most enjoyable day of this quarter."
    voice "voice/viktor/7/vi_scene7_5.ogg"
    cy "*Cough* The most efficient way of understanding plebian culture is to attempt to understand some of its most rudimentary forms of language."
    "The ringing of my laughter must have caused a disturbance loud enough for everyone in the library to hear."
    mc flat "So, Cyrus, student of the contemporary culture. What have you been able to grasp from your studies?"
    "Glints of delight in his expression shadows the sunlight's glare against his maroon colored eyes. How cute."
    hide vik with dissolve
    show vik happy with dissolve
    voice "voice/viktor/7/vi_scene7_6.ogg"
    cy "As a matter of fact, I am able to develop even my own humorous \"jabs,\" with the aid of didactic texts."
    voice "voice/viktor/7/vi_scene7_7.ogg"
    cy "What does a child have that an adult doesn't?"
    "Knowing Cyrus, it's probably something pretty crude."
    mc sad "Hmmm. I don't know. An appendix maybe?"
    voice "voice/viktor/7/vi_scene7_8.ogg"
    cy "Negative. You were, however, appropriate in assuming that it pertains to an organ in the digestive system."
    mc flat "... I give up. What is it?"
    pause 1.0
    show vik happyblush with dissolve
    voice "voice/viktor/7/vi_scene7_9.ogg"
    cy "Heh. They are kid-knees."
    mc flat "..."
    "I'm not sure what's cuter - his confidence that the joke is funny or his adorable giggling."
    show vik happyblushmid
    voice "voice/viktor/7/vi_scene7_10.ogg"
    cy "The brilliance and novelty of lower levels of culture is that you are exempt from the laws of logic so long as the humor, 
        in this case the pun, does go across."
    voice "voice/viktor/7/vi_scene7_11.ogg"
    cy "Despite the fact that people of all ages do truly possess a kidney, 
        it is undeniable that an adult's knees are not of similar quality to-"
    mc angry "Hey! You're not supposed to explain it; that defeats the purpose. Giving away the humor of the joke is the equivalent of putting out your own fire."
    "Surprise, surprise! Something that Cyrus failed to know."
    show vik surprisedmid with dissolve
    pause 0.5
    hide vik with dissolve
    show vik flat with dissolve
    voice "voice/viktor/7/vi_scene7_12.ogg"
    cy "I see! That indeed seems to be the crux of the humor, 
        assuming that even with the lack of reasoning that others will come to understand the 
        intention of one's words. I will make sure to keep note."
    show vik happyblush with dissolve
    "And with that newly found information, we take a stroll back to the chairs. 
     He again buries his head in his research like he's trying to find the meaning of existence."
    "His cool eyes draw my attention to his inquisitive gaze. I admire his dedication to the \"pursuit of knowledge.\" 
     To others, that cool exterior is all that there is."
    "But to me, he's just a diligent person that protects himself and others by keeping relationships at a distance because he overthinks too much. 
     Hehe, there's a special side to him that only I know~"
    hide vik with dissolve
    stop music fadeout 2.0
    jump events_end_period