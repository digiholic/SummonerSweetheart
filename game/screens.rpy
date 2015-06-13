# This file is in the public domain. Feel free to modify it as a basis
# for your own screens.

# Note that many of these screens may be given additional arguments in the
# future. The use of **kwargs in the parameter list ensures your code will
# work in the future.

######################################### SAY
# Screen that's used to display adv-mode dialogue.
# http://www.renpy.org/doc/html/screen_special.html#say
screen say(who, what, side_image=None, two_window=False):

    # Decide if we want to use the one-window or two-window variant.
    if not two_window:
        # The one window variant.
        window:
            id "window"
            has vbox:
                style "say_vbox"
            if who: # tacky way of doing this, forces rest of text to be one line lower
                text who id "who" ypos -58
            text what id "what"
    else:
        # The two window variant.
        vbox:
            style "say_two_window_vbox"
            if who:
                window:
                    style "say_who_window"
                    text who:
                        id "who"
            window:
                id "window"
                has vbox:
                    style "say_vbox"
                text what id "what"

    if side_image:
        add side_image
    else:
        add SideImage() xalign 0.0 yalign 1.0
    use quick_menu
    use clock

######################################### CHOICE
# Screen that's used to display in-game menus.
# http://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):

    window:
        style "menu_window"
        xalign 0.5
        yalign 0.5

        vbox:
            style "menu"
            spacing 2

            for caption, action, chosen in items:

                if action:

                    button:
                        action action
                        style "menu_choice_button"

                        text caption style "menu_choice"

                else:
                    text caption style "menu_caption"

init -2:
    $ config.narrator_menu = True

    style menu_window is default

    style menu_choice is button_text:
        clear

    style menu_choice_button is button:
        xminimum int(config.screen_width * 0.75)
        xmaximum int(config.screen_width * 0.75)


######################################### INPUT
# Screen that's used to display renpy.input()
# http://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):

    window style "input_window":
        has vbox

        text prompt style "input_prompt"
        input id "input" color "#000000"

    use quick_menu

######################################### NVL
# Screen used for nvl-mode dialogue and menus.
# http://www.renpy.org/doc/html/screen_special.html#nvl

screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            style "nvl_vbox"

        # Display dialogue.
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox:
                    spacing 10

                if who is not None:
                    text who id who_id

                text what id what_id

        # Display a menu, if given.
        if items:

            vbox:
                id "menu"

                for caption, action, chosen in items:

                    if action:

                        button:
                            style "nvl_menu_choice_button"
                            action action

                            text caption style "nvl_menu_choice"

                    else:

                        text caption style "nvl_dialogue"

    add SideImage() xalign 0.0 yalign 1.0

    use quick_menu

######################################### MAIN MENU
# Screen that's used to display the main menu, when Ren'Py first starts
# http://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    # This ensures that any other menu screen is replaced.
    tag menu

    # The background of the main menu.
    window:
        style "mm_root"

    # The main menu buttons.
    imagemap:
        auto "gui/mm_%s.png"
        alpha False # forces everything transparent to be invisible to cursor?
        
        hotspot (626,275,146,41) action Start()
        hotspot (626,326,141,41) action ShowMenu("load")
        hotspot (626,384,175,41) action ShowMenu("preferences")
        hotspot (626,444,130,41) action Help()
        hotspot (626,505,183,41) action OpenURL("http://bigstepsvn.tumblr.com") # change URL to credits screen
        hotspot (874,707,130,41) action Quit(confirm=False)

######################################### NAVIGATION
# Screen that's included in other screens to display the game menu
# navigation and background.
# http://www.renpy.org/doc/html/screen_special.html#navigation
screen navigation():

    # The background of the game menu.
    window:
        style "gm_root"

    # The various buttons.
    frame:
        style_group "gm_nav"
        xalign .98
        yalign .98

        has vbox

        textbutton _("Return") action Return()
        textbutton _("Preferences") action ShowMenu("preferences")
        textbutton _("Save Game") action ShowMenu("save")
        textbutton _("Load Game") action ShowMenu("load")
        textbutton _("Main Menu") action MainMenu()
        textbutton _("Help") action Help()
        textbutton _("Quit") action Quit()

init -2:

    # Make all game menu navigation buttons the same size.
    style gm_nav_button:
        size_group "gm_nav"


######################################### SAVE/LOAD
# Screens that allow the user to save and load the game.
# http://www.renpy.org/doc/html/screen_special.html#save
# http://www.renpy.org/doc/html/screen_special.html#load

screen save():
    tag menu
    
    imagemap:
        ground "gui/save_ground.png"
        idle "gui/load_idle.png"
        hover "gui/load_hover.png"
        cache False
        
        hotspot(887,223,56,39) clicked FilePagePrevious(max=5,wrap=True)
        hotspot(892,521,51,38) clicked FilePageNext(max=5,wrap=True)
        hotspot(899,272,34,37) clicked FilePage(1)
        hotspot(898,326,35,32) clicked FilePage(2)
        hotspot(897,376,38,33) clicked FilePage(3)
        hotspot(900,425,35,33) clicked FilePage(4)
        hotspot(899,475,34,33) clicked FilePage(5)
        hotspot(853,713,162,40) action Return()
        
        hotspot(279,202,230,155) clicked FileSave(1):
            use load_save_slot(number=1)
        hotspot(590,202,230,155) clicked FileSave(2):
            use load_save_slot(number=2)
        hotspot(279,427,230,155) clicked FileSave(3):
            use load_save_slot(number=3)
        hotspot(590,427,230,155) clicked FileSave(4):
            use load_save_slot(number=4)

screen load():
   tag menu

   imagemap:
        ground "gui/load_ground.png"
        idle "gui/load_idle.png"
        hover "gui/load_hover.png"
        cache False
        
        hotspot(887,223,56,39) clicked FilePagePrevious(max=5,wrap=True) focus_mask None
        hotspot(892,521,51,38) clicked FilePageNext(max=5,wrap=True) focus_mask None
        hotspot(899,272,34,37) clicked FilePage(1) focus_mask None
        hotspot(898,326,35,32) clicked FilePage(2) focus_mask None
        hotspot(897,376,38,33) clicked FilePage(3) focus_mask None
        hotspot(900,425,35,33) clicked FilePage(4) focus_mask None
        hotspot(899,475,34,33) clicked FilePage(5) focus_mask None
        hotspot(853,713,162,40) action Return() focus_mask None
        
        hotspot(279,202,230,155) clicked FileLoad(1):
            use load_save_slot(number=1)
        hotspot(590,202,230,155) clicked FileLoad(2):
            use load_save_slot(number=2)
        hotspot(279,427,230,155) clicked FileLoad(3):
            use load_save_slot(number=3)
        hotspot(590,427,230,155) clicked FileLoad(4):
            use load_save_slot(number=4)

        
        
screen load_save_slot:
    $ file_text = "% 2s. %s\n%s" % (
                        FileSlotName(number, 4),
                        FileTime(number, empty=_("")),
                        FileSaveName(number))

    add FileScreenshot(number) xpos 0 ypos 0
    text file_text xpos 0 ypos 10 size 20 color "#ffffff" outlines [ (2, "#302B54") ] kerning 2 #font "FONT FILE NAME HERE"
    
    key "save_delete" action FileDelete(number)
    

######################################### PREFERENCES
# Screen that allows the user to change the preferences.
# http://www.renpy.org/doc/html/screen_special.html#prefereces

screen preferences():
    tag menu
    
    imagemap:
        auto "gui/settings_%s.png"
        hotbar(320,335,197,21) value Preference("music volume")
        hotbar(320,383,198,23) value Preference("sound volume")
        hotbar(320,434,197,23) value Preference("voice volume")
        hotbar(253,611,203,26) value Preference("text speed")
        hotbar(573,612,200,25) value Preference("auto-forward time") 
        
        hotspot(568,331,31,28) action Preference("skip", "seen") focus_mask None
        hotspot(569,367,26,29) action Preference("skip", "all") focus_mask None
        hotspot(569,469,25,26) action Preference("display", "window") focus_mask None
        hotspot(567,504,27,27) action Preference("display", "fullscreen") focus_mask None
        hotspot(802,334,27,26) action Preference("after choices", "stop") focus_mask None
        hotspot(803,371,25,25) action Preference("after choices", "skip") focus_mask None
        hotspot(807,470,26,26) action Preference("transitions", "all") focus_mask None
        hotspot(807,507,25,26) action Preference("transitions", "none") focus_mask None
        hotspot(848,715,156,35) action Return() focus_mask None

######################################### YESNO
# Screen that asks the user a yes or no question.
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt

screen yesno_prompt(message, yes_action, no_action):
    modal True

    frame:
        style_group "yesno"

        xfill True
        xmargin .05
        ypos .1
        yanchor 0
        ypadding .05

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(message):
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

            imagebutton auto "gui/yes_%s.png" action yes_action
            imagebutton auto "gui/no_%s.png" action no_action

    # Right-click and escape answer "no".
    key "game_menu" action no_action

init -2:
    style yesno_button:
        size_group "yesno"

    style yesno_label_text:
        text_align 0.5
        layout "subtitle"


######################################### QUICK MENU
# A screen that's included by the default say screen, and adds quick access to
# several useful functions.
screen quick_menu():
    imagebutton auto "gui/quick_back_%s.png" action Rollback() xpos 462 ypos 730
    imagebutton auto "gui/quick_auto_%s.png" action Preference("auto-forward", "toggle") xpos 512 ypos 730
    imagebutton auto "gui/quick_skip_%s.png" action Skip() xpos 562 ypos 730
    imagebutton auto "gui/quick_config_%s.png" action ShowMenu('preferences') xpos 925 ypos 670
    imagebutton auto "gui/quick_save_%s.png" action ShowMenu('save') xpos 925 ypos 610
    imagebutton auto "gui/quick_load_%s.png" action ShowMenu('load') xpos 925 ypos 640
    imagebutton auto "gui/quick_title_%s.png" action MainMenu(confirm=True) xpos 925 ypos 700

######################################### CHARACTER SELECT
screen char_select():
    modal True
    imagemap:
        auto "gui/charselect_%s.png"
        hotspot(335,305,354,139) action Return("Ezreal")
        hotspot(339,463,347,138) action Return("Leona")

######################################### SCHOOL MAP
screen school_map():
    modal True
    add "gui/schoolmap_bg.png"
    imagebutton auto "gui/home_%s.png" action Return("vr") xpos 808 ypos 446 focus_mask True
    imagebutton auto "gui/library_%s.png" action Return("library") xpos 130 ypos 261 focus_mask True
    imagebutton auto "gui/soccer_%s.png" action Return("soccer") xpos 176 ypos 449 focus_mask True
    imagebutton auto "gui/museum_%s.png" action Return("museum") xpos 323 ypos 276 focus_mask True
    imagebutton auto "gui/park_%s.png" action Return("park") xpos 624 ypos 426 focus_mask True
    imagebutton auto "gui/class_%s.png" action Return("class") xpos 219 ypos 128 focus_mask True
    if day < 7 or (day == 7 and period == 1):
            imagebutton auto "gui/dungeon_%s.png" action Return("dungeon") xpos 703 ypos 384 focus_mask True
    if whois_vr != "None":
        $ vr_x = 895
        $ vr_y = 415
        if route == "Ezreal":
            if whois_vr == "Ahri":
                add "gui/map_ahri_hover.png" xpos vr_x ypos vr_y
            elif whois_vr == "Soraka":
                add "gui/map_soraka_hover.png" xpos vr_x ypos vr_y
            elif whois_vr == "Rengar":
                add "gui/map_rengar_hover.png" xpos vr_x ypos vr_y
        elif route == "Leona":
            if whois_vr == "Jayce":
                add "gui/map_jayce_hover.png" xpos vr_x ypos vr_y
            elif whois_vr == "Rumble":
                add "gui/map_rumble_hover.png" xpos vr_x ypos vr_y
            elif whois_vr == "Viktor":
                add "gui/map_viktor_hover.png" xpos vr_x ypos vr_y
    if whois_library != "None":
        $ lib_x = 221
        $ lib_y = 336
        if route == "Ezreal":
            if whois_library == "Ahri":
                add "gui/map_ahri_hover.png" xpos lib_x ypos lib_y
            elif whois_library == "Soraka":
                add "gui/map_soraka_hover.png" xpos lib_x ypos lib_y
            elif whois_library == "Rengar":
                add "gui/map_rengar_hover.png" xpos lib_x ypos lib_y
        elif route == "Leona":
            if whois_library == "Jayce":
                add "gui/map_jayce_hover.png" xpos lib_x ypos lib_y
            elif whois_library == "Rumble":
                add "gui/map_rumble_hover.png" xpos lib_x ypos lib_y
            elif whois_library == "Viktor":
                add "gui/map_viktor_hover.png" xpos lib_x ypos lib_y
    if whois_soccer != "None":
        $ soc_x = 228
        $ soc_y = 541
        if route == "Ezreal":
            if whois_soccer == "Ahri":
                add "gui/map_ahri_hover.png" xpos soc_x ypos soc_y
            elif whois_soccer == "Soraka":
                add "gui/map_soraka_hover.png" xpos soc_x ypos soc_y
            elif whois_soccer == "Rengar":
                add "gui/map_rengar_hover.png" xpos soc_x ypos soc_y
        elif route == "Leona":
            if whois_soccer == "Jayce":
                add "gui/map_jayce_hover.png" xpos soc_x ypos soc_y
            elif whois_soccer == "Rumble":
                add "gui/map_rumble_hover.png" xpos soc_x ypos soc_y
            elif whois_soccer == "Viktor":
                add "gui/map_viktor_hover.png" xpos soc_x ypos soc_y
    if whois_museum != "None":
        $ mus_x = 381
        $ mus_y = 445
        if route == "Ezreal":
            if whois_museum == "Ahri":
                add "gui/map_ahri_hover.png" xpos mus_x ypos mus_y
            elif whois_museum == "Soraka":
                add "gui/map_soraka_hover.png" xpos mus_x ypos mus_y
            elif whois_museum == "Rengar":
                add "gui/map_rengar_hover.png" xpos mus_x ypos mus_y
        elif route == "Leona":
            if whois_museum == "Jayce":
                add "gui/map_jayce_hover.png" xpos mus_x ypos mus_y
            elif whois_museum == "Rumble":
                add "gui/map_rumble_hover.png" xpos mus_x ypos mus_y
            elif whois_museum == "Viktor":
                add "gui/map_viktor_hover.png" xpos mus_x ypos mus_y
    if whois_park != "None":
        $ park_x = 791
        $ park_y = 562
        if route == "Ezreal":
            if whois_park == "Ahri":
                add "gui/map_ahri_hover.png" xpos park_x ypos park_y
            elif whois_park == "Soraka":
                add "gui/map_soraka_hover.png" xpos park_x ypos park_y
            elif whois_park == "Rengar":
                add "gui/map_rengar_hover.png" xpos park_x ypos park_y
        elif route == "Leona":
            if whois_park == "Jayce":
                add "gui/map_jayce_hover.png" xpos park_x ypos park_y
            elif whois_park == "Rumble":
                add "gui/map_rumble_hover.png" xpos park_x ypos park_y
            elif whois_park == "Viktor":
                add "gui/map_viktor_hover.png" xpos park_x ypos park_y
    if whois_class != "None":
        $ class_x = 309
        $ class_y = 171
        if route == "Ezreal":
            if whois_class == "Ahri":
                add "gui/map_ahri_hover.png" xpos class_x ypos class_y
            elif whois_class == "Soraka":
                add "gui/map_soraka_hover.png" xpos class_x ypos class_y
            elif whois_class == "Rengar":
                add "gui/map_rengar_hover.png" xpos class_x ypos class_y
        elif route == "Leona":
            if whois_class == "Jayce":
                add "gui/map_jayce_hover.png" xpos class_x ypos class_y
            elif whois_class == "Rumble":
                add "gui/map_rumble_hover.png" xpos class_x ypos class_y
            elif whois_class == "Viktor":
                add "gui/map_viktor_hover.png" xpos class_x ypos class_y
    
#####
screen dungeon_run(blocked):
  if blocked:
    modal True
  if current_battle:
    add current_battle xpos 0.0 ypos 0.0
    
######################################### CLOCK
screen clock():
    if period == 0:
        add "gui/clock_day.png" xpos 0 ypos 0
    elif period == 1:
        add "gui/clock_day.png" xpos 0 ypos 0
    elif period == 2:
        add "gui/clock_night.png" xpos 0 ypos 0
        
    $ date_x = 130
    $ date_y = 45
    if day == 1:
        add "gui/clock_day1.png" xpos date_x ypos date_y
    elif day == 2:
        add "gui/clock_day2.png" xpos date_x ypos date_y
    elif day == 3:
        add "gui/clock_day3.png" xpos date_x ypos date_y
    elif day == 4:
        add "gui/clock_day4.png" xpos date_x ypos date_y
    elif day == 5:
        add "gui/clock_day5.png" xpos date_x ypos date_y
    elif day == 6:
        add "gui/clock_day6.png" xpos date_x ypos date_y
    elif day == 7:
        add "gui/clock_day7.png" xpos date_x ypos date_y
        
    imagebutton auto "gui/clockbutton_%s.png" xpos 29 ypos 123 action ShowTransient("bio_select")
        
######################################### BIO SELECT AND BIO PAGES
screen bio(champ):
    modal True
    add "gui/bio_bg.png"
    if champ == "ahri":
        add "gui/bio_ahri_sprite.png" xpos 512 ypos 0
        add "gui/bio_ahri_pix.png" xpos 441 ypos 593
        $ champion = "Ahri"
        $ bio_name = "Ami Kaminoka"
        $ spiel = "Daughter of the well known Kaminoka household, Ami strives to succeed the family business. She does not associate well with \"commoners\" and only seeks out fellow elitists. Rumors say she dislikes Rengar out of envy of her free and wild nature."
        $ quote = "Mercy is a human luxury... and a responsibility." #wat
    elif champ == "raka":
        add "gui/bio_raka_sprite.png" xpos 512 ypos 0
        add "gui/bio_raka_pix.png" xpos 441 ypos 593
        $ champion = "Soraka"
        $ bio_name = "Sharon May"
        $ spiel = "Sharon is often a calm and quiet schoolgirl who keeps to herself, stowed away in the library. Her appreciation of the night sky is characterisitc of her aloof and almost absentminded demeanor. Rarely does she speak to others first, keeping conversations short."
        $ quote = "For peace of mind."
    elif champ == "rango":
        add "gui/bio_rango_sprite.png" xpos 512 ypos 0
        add "gui/bio/rango_pix.png" xpos 441 ypos 593
        $ champion = "Rengar"
        $ bio_name = "Gwen Leon"
        $ spiel = "The tough kid around the block. Raised by a father who dwelled in action-packed glory, this tomboy is constantly on the lookout for challenges, unafraid to stir up trouble along the way. She doesn't mingle well with other girls."
        $ quote = "Prey on the weak and you will survive.\nPrey on the strong and you will live."
    elif champ == "vik":
        add "gui/bio_vik_sprite.png" xpos 512 ypos 0
        add "gui/bio_vik_pix.png" xpos 441 ypos 593
        $ champion = "Viktor"
        $ bio_name = "Cyrus Ivanov"
        $ spiel = "A technology  junkie and wizard, Cyrus knows no bounds when it comes to information and information acquisition. He dedicates his life to one thing: progression. As a result, he rarely joins the social circles that others typically would. Instead, he constantly hunts for ways to improve, hungry for personal betterment."
        $ quote = "Embrace progress."
    elif champ == "rumble":
        add "gui/bio_rumble_sprite.png" xpos 512 ypos 0
        add "gui/bio_rumble_pix.png" xpos 441 ypos 593
        $ champion = "Rumble"
        $ bio_name = "Daniel Fletcher"
        $ spiel = "Often seen in the library sketching away or browsing the latest art, Daniel has more to say with his drawings than with his words. As they say, a picture is worth a thousand words, and this diligent artist sticks true to its meaning. His virtual persona may be quite different, though..."
        $ quote = "..."
    elif champ == "jayce":
        add "gui/bio_jayce_sprite.png" xpos 512 ypos 0
        add "gui/bio_jayce_pix.png" xpos 441 ypos 593
        $ champion = "Jayce"
        $ bio_name = "Jason White"
        $ spiel = "Who wouldn't know about the All Star winner, Jason? He is one of the key players of the soccer team at Summoner's Academy who led many to see victory at the national competition. His academics are none too shabby either. It's no wonder that he has so many fans fawning over his skills and good looks."
        $ quote = "I fight for a brighter tomorrow."
        
    text "[champion]" xpos 258 ypos 97 font "MyriadProBold.ttf" size 40 color "#586f94"
    text "[bio_name]" xpos 12 ypos 180 font "MyriadPro.ttf" size 65 color "#ffffff"
    text "[spiel]" xpos 60 ypos 262 xsize 363 ysize 327 font "abeatbykai.ttf" size 22 color "#83e0d8"
    text "[quote]" xpos 50 ypos 683 font "MyriadPro.ttf" size 20 color "#83e0d8"
    
    add "gui/return_triangle.png" xpos 724 ypos 623
    imagebutton auto "gui/bio_return_%s.png" xpos 840 ypos 700 action Hide("bio")

init -2 python:
    style.bio_bar.left_bar = "gui/bioselect_bar_full.png"
    style.bio_bar.right_bar = "gui/bioselect_bar_empty.png"
    style.bio_bar.xsize = 175
    style.bio_bar.ysize = 25
    style.bio_bar.thumb = None

screen bio_select():
    modal True
    add "gui/bioselect_ground.png"
    if route == "Ezreal":
        imagebutton auto "gui/bioselect_ahri_%s.png" xpos 549 ypos 186 action ShowTransient("bio", champ="ahri")
        text "Ami Kaminoka" xpos 122 ypos 215 font "MyriadPro.ttf" size 50 color "#ed6b55"
        text "champion: AHRI" xpos 122 ypos 262 font "OratorStd.ttf" size 30 color "#6b6b6b"
        imagebutton auto "gui/bioselect_raka_%s.png" xpos 549 ypos 366 action ShowTransient("bio", champ="raka")
        text "Sharon May" xpos 122 ypos 395 font "MyriadPro.ttf" size 50 color "#6e7a90"
        text "champion: SORAKA" xpos 122 ypos 443 font "OratorStd.ttf" size 30 color "#6b6b6b"
        if rango_scene > 1:
            imagebutton auto "gui/bioselect_ren_%s.png" action ShowTransient("bio", None, champ="rango") xpos 122 ypos 568
            text "Gwen Leon" xpos 122 ypos 568 size 50 color "#71bb62"
            text "champion: RENGAR" xpos 122 ypos 621 font "OratorStd.ttf" size 30 color "#6b6b6b"
        else:
            add "gui/bioselect_missing2.png" xpos 549 ypos 546
            text "?????????" xpos 122 ypos 568 size 50 color "#71bb62"
        bar value ahri_rp range 100 xpos 817 ypos 237 style "bio_bar"
        bar value raka_rp range 100 xpos 817 ypos 417 style "bio_bar"
        bar value rango_rp range 100 xpos 817 ypos 597 style "bio_bar"
    if route == "Leona":
        imagebutton auto "gui/bioselect_vik_%s.png" xpos 549 ypos 186 action ShowTransient("bio", champ="vik")
        text "Cyrus Ivanov" xpos 122 ypos 215 font "MyriadPro.ttf" size 50 color "#ed6b55"
        text "champion: VIKTOR" xpos 122 ypos 262 font "OratorStd.ttf" size 30 color "#6b6b6b"
        imagebutton auto "gui/bioselect_rum_%s.png" xpos 549 ypos 366 action ShowTransient("bio", champ="rumble")
        text "Daniel Fletcher" xpos 122 ypos 395 font "MyriadPro.ttf" size 50 color "#6e7a90"
        text "champion: RUMBLE" xpos 122 ypos 443 font "OratorStd.ttf" size 30 color "#6b6b6b"
        imagebutton auto "gui/bioselect_jayce_%s.png" xpos 549 ypos 546 action ShowTransient("bio", champ="jayce")
        text "Jason White" xpos 122 ypos 568 size 50 color "#71bb62"
        text "champion: JAYCE" xpos 122 ypos 621 font "OratorStd.ttf" size 30 color "#6b6b6b"
        bar value vik_rp range 100 xpos 817 ypos 237 style "bio_bar"
        bar value rumble_rp range 100 xpos 817 ypos 417 style "bio_bar"
        bar value jayce_rp range 100 xpos 817 ypos 597 style "bio_bar"
    imagebutton auto "gui/bio_return_%s.png" xpos 840 ypos 700 action Hide("bio_select")
