init -1 python hide:
    ## config options
    config.developer = False                     # enables dev tools (shift+D)
    config.automatic_images = [' ', '_', '/']   # enables automatic image declaration
    config.screen_width = 1024                  # screen width
    config.screen_height = 768                  # screen height
    config.window_title = u"Summoner Sweetheart"# name of game window
    config.name = "Summoner Sweetheart"         # config name
    config.version = "0.9"                      # config version
    config.thumbnail_width = 230
    config.thumbnail_height = 155
    config.has_quicksave = False
    config.has_autosave = False
    config.skip_delay = 120
    config.use_cpickle = False

    ######################################### THEMES
    ## Theme: Roundrect
    ## Color scheme: Unrequited Love
    theme.roundrect(
        widget = "#7fa1b3",                     # color of idle widget face
        widget_hover = "#b38698",               # color of focused widget face
        widget_text = "#ffffff",                # text color of widget
        widget_selected = "#fffeed",            # text color of selected widget
        disabled = "#dbe4dd",                   # color of disabled widget face
        disabled_text = "#bd9ca9",              # color of disabled widget text
        label = "#23000e",                      # color of informational labels
        frame = "#fffeed",                      # color of frame containing widgets
        mm_root = "bg/mm_root.png",             # color OR IMAGE of the main menu's background. can be a filename
        gm_root = "#b38698",                    # color OR IMAGE of the game menu's background. can be a filename
        rounded_window = False,                 # should the in-game window be rounded, or square?
        )

    ######################################### STYLES
    ## These settings let you customize the window containing the
    ## dialogue and narration, by replacing it with an image.

    ## The background of the window. In a Frame, the two numbers
    ## are the size of the left/right and top/bottom borders,
    ## respectively.
    style.window.background = "gui/saybox.png"

    ## Margin is space surrounding the window, where the background
    ## is not drawn.
    style.window.left_margin = 0
    style.window.right_margin = 0
    style.window.top_margin = 0
    style.window.bottom_margin = 0

    ## Padding is space inside the window, where the background is
    ## drawn.
    style.window.left_padding = 160
    style.window.right_padding = 110
    style.window.top_padding = 80
    style.window.bottom_padding = 20

    ## This is the minimum height of the window, including the margins
    ## and padding
    style.window.yminimum = 244

    ######################################### MENU PLACEMENT
    ## This lets you change the placement of the main menu.
    ## The way placement works is that we find an anchor point
    ## inside a displayable, and a position (pos) point on the
    ## screen. We then place the displayable so the two points are
    ## at the same place.
    ## An anchor/pos can be given as an integer or a floating point
    ## number. If an integer, the number is interpreted as a number
    ## of pixels from the upper-left corner. If a floating point,
    ## the number is interpreted as a fraction of the size of the
    ## displayable or screen.

    # style.mm_menu_frame.xpos = 0.5
    # style.mm_menu_frame.xanchor = 0.5
    # style.mm_menu_frame.ypos = 0.75
    # style.mm_menu_frame.yanchor = 0.5

    ######################################### FONT
    ## Note that these only change the size of some of the text. Other
    ## buttons have their own styles.
    # style.default.font = "DejaVuSans.ttf"     # file containing the default font
    # style.default.size = 22                   # default text size
    style.default.color = "3a3a3a"

    ######################################### SOUND
    ## These settings let you change some of the sounds that are used by
    ## Ren'Py.
    config.has_sound = True
    config.has_music = True
    config.has_voice = True

    ## Sounds that are used when button and imagemaps are clicked.
    # style.button.activate_sound = "click.wav"
    # style.imagemap.activate_sound = "click.wav"

    ## Sounds that are used when entering and exiting the game menu.
    # config.enter_sound = "click.wav"
    # config.exit_sound = "click.wav"

    ## A sample sound that can be played to check the sound volume.
    # config.sample_sound = "click.wav"

    ## Music that is played while the user is at the main menu.
    config.main_menu_music = "music/upbeat.mp3"

    ######################################### HELP
    ## This lets you configure the help option on the Ren'Py menus.
    ## It may be:
    ## - A label in the script, in which case that label is called to
    ##   show help to the user.
    ## - A file name relative to the base directory, which is opened in a
    ##   web browser.
    ## - None, to disable help.
    config.help = None

    ######################################### TRANSITIONS
    config.enter_transition = None              # entering the game menu from the game
    config.exit_transition = None               # exiting the game menu to the game
    config.intra_transition = None              # in between screens in the game menu
    config.main_game_transition = None          # entering the game menu from the main menu
    config.game_main_transition = None          # returning to main menu from the game
    config.end_splash_transition = None         # entering main menu from the splash screen
    config.end_game_transition = None           # entering the main menu after the game has ended
    config.after_load_transition = None         # used when a game is loaded
    config.window_show_transition = None        # used when a window is shown
    config.window_hide_transition = None        # used when a windiw is hidden
    config.adv_nvl_transition = dissolve        # used when showing NVL mode text directly after ADV text
    config.nvl_adv_transition = dissolve        # used when showing ADV text directly after NVL text
    config.enter_yesno_transition = None        # used when yesno is shown
    config.exit_yesno_transition = None         # used when yesno is hidden
    config.enter_replay_transition = None       # used when entering a replay

    ## Used when exiting a replay
    config.exit_replay_transition = None

    ## Used when the image is changed by a say statement with image attributes.
    config.say_attribute_transition = None

    ######################################### SAVE DIRECTORY
    ## This is the name of the directory where the game's data is
    ## stored. (It needs to be set early, before any other init code
    ## is run, so the persistent information can be found by the init code.)
python early:
    config.save_directory = "Summoner Sweetheart-1425348595"

init -1 python hide:
    ######################################### PREFERENCES
    ## Note: These options are only evaluated the first time a
    ## game is run. To have them run a second time, delete
    ## game/saves/persistent

    config.default_fullscreen = False           # default fullscreen?
    config.default_text_cps = 35                 # default text speed (characters per second)?
    config.default_afm_time = 20                # default auto-forward time?

    ######################################### MISCELLANEOUS OPTIONS


######################################### BUILD
## This section contains information about how to build your project into
## distribution files.
init python:

    build.directory_name = "SummonerSweetheart-0.9"
    build.executable_name = "Summoner Sweetheart v0.9"
    build.archive("data")

    ## If True, Ren'Py will include update information into packages. This
    ## allows the updater to run.
    build.include_update = False

    ## File patterns:
    ##
    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base
    ## directory, with and without a leading /. If multiple patterns match,
    ## the first is used.
    ##
    ##
    ## In a pattern:
    ##
    ## /
    ##     Is the directory separator.
    ## *
    ##     Matches all characters, except the directory separator.
    ## **
    ##     Matches all characters, including the directory separator.
    ##
    ## For example:
    ##
    ## *.txt
    ##     Matches txt files in the base directory.
    ## game/**.ogg
    ##     Matches ogg files in the game directory or any of its subdirectories.
    ## **.psd
    ##    Matches psd files anywhere in the project.

    ## Classify files as None to exclude them from the built distributions.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    ## To archive files, classify them as 'archive'.

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    ## Files matching documentation patterns are duplicated in a mac app
    ## build, so they appear in both the app and the zip file.

    build.documentation('*.html')
    build.documentation('*.txt')
    