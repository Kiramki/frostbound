﻿## This file contains some of the options that can be changed to customize
## your Ren'Py game. It only contains the most common options... there
## is quite a bit more customization you can do.
##
## Lines beginning with two '#' marks are comments, and you shouldn't
## uncomment them. Lines beginning with a single '#' mark are
## commented-out code, and you may want to uncomment them when
## appropriate.

init -1 python hide:

    ## These control the width and height of the screen.

    config.screen_width = 1280
    config.screen_height = 720

    ## This controls the title of the window, when Ren'Py is
    ## running in a window.

    config.window_title = u"GUI Tutorial by zishy"

    # These control the name and version of the game, that are reported
    # with tracebacks and other debugging logs.
    config.name = "GUI Tutorial by zishy"
    config.version = "0.0"

    #########################################
    # Themes

    ## We then want to call a theme function. theme.roundrect is
    ## a theme that features the use of rounded rectangles.
    ##
    ## The theme function takes a number of parameters that can
    ## customize the color scheme.

    theme.diamond(
        ## Theme: Diamond
        ## Color scheme: First Valentines

        ## The color of an idle widget face.
        widget = "#F09898",

        ## The color of a focused widget face.
        widget_hover = "#D6C5BB",

        ## The color of the text in a widget.
        widget_text = "#593131",

        ## The color of the text in a selected widget. (For
        ## example, the current value of a preference.)
        widget_selected = "#B31E1E",

        ## The color of a disabled widget face.
        disabled = "#F8F2D0",

        ## The color of disabled widget text.
        disabled_text = "#BFA1A1",

        ## The color of informational labels.
        label = "#5D1010",

        ## The color of a frame containing widgets.
        frame = "#F8F2D0",

        ## The background of the main menu. This can be a color
        ## beginning with '#', or an image filename. The latter
        ## should take up the full height and width of the screen.
        mm_root = "#D98989",

        ## The background of the game menu. This can be a color
        ## beginning with '#', or an image filename. The latter
        ## should take up the full height and width of the screen.
        gm_root = "#D98989",

        ## If this is True, the in-game window is rounded. If False,
        ## the in-game window is square.
        rounded_window = False,

        ## And we're done with the theme. The theme will customize
        ## various styles, so if we want to change them, we should
        ## do so below.
        )


    #########################################
    ## These settings let you customize the window containing the
    ## dialogue and narration, by replacing it with an image.

    ## The background of the window. In a Frame, the two numbers
    ## are the size of the left/right and top/bottom borders,
    ## respectively.

    style.window.background = Frame("gui/textbox.png", 0, 0)

    ## Margin is space surrounding the window, where the background
    ## is not drawn.

    style.window.left_margin = 44
    style.window.right_margin = 44
    style.window.top_margin = 7
    style.window.bottom_margin = 7

    ## Padding is space inside the window, where the background is
    ## drawn.

    style.window.left_padding = 222
    style.window.right_padding = 22
    style.window.top_padding = 44
    style.window.bottom_padding = 7

    ## This is the minimum height of the window, including the margins
    ## and padding.

    style.window.yminimum = 222
    
    #########################################
    
    ## This code is for the namebox.
    
    style.say_who_window.background = Frame("namebox.png", 0, 0) #Background skin
    
    ## This is the position of the namebox
    style.say_who_window.xalign = -111 #leftright
    style.say_who_window.yalign = 266 ##updown ##up300+ ##down300-
    style.say_who_window.xpos = 111
    style.say_who_window.ypos = 322
    
    ## This is the padding and position of the text
    style.say_who_window.left_padding = 77
    style.say_who_window.top_padding = 10
    style.say_who_window.right_padding = 77
    style.say_who_window.bottom_padding = 10
    
    style.say_who_window.xminimum = 333 ##width
    style.say_who_window.yminimum = 7
    style.say_who_window.xfill = False

    #style.nvl_window.background = Image("nvl.png")    


    #########################################
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


    #########################################
    ## These let you customize the default font used for text in Ren'Py.

    ## The file containing the default font.

    style.default.font = "ARLRDBD.ttf"

    ## The default size of text.

    style.default.size = 33

    ## Note that these only change the size of some of the text. Other
    ## buttons have their own styles.
    
    ## This is the game dialogue color
    style.default.color = "#1a000d"



    #########################################
    ## These settings let you change some of the sounds that are used by
    ## Ren'Py.

    ## Set this to False if the game does not have any sound effects.

    config.has_sound = True

    ## Set this to False if the game does not have any music.

    config.has_music = True

    ## Set this to True if the game has voicing.

    config.has_voice = True

    ## Sounds that are used when button and imagemaps are clicked.

    style.button.activate_sound = "click.wav"
    style.imagemap.activate_sound = "click.wav"

    ## Sounds that are used when entering and exiting the game menu.

    # config.enter_sound = "click.wav"
    # config.exit_sound = "click.wav"

    ## A sample sound that can be played to check the sound volume.

    # config.sample_sound = "click.wav"

    ## Music that is played while the user is at the main menu.

    config.main_menu_music = "Happy Alley.mp3"


    #########################################
    ## Transitions.

    ## Used when entering the game menu from the game.
    config.enter_transition = dissolve

    ## Used when exiting the game menu to the game.
    config.exit_transition = dissolve

    ## Used between screens of the game menu.
    config.intra_transition = dissolve

    ## Used when entering the game menu from the main menu.
    config.main_game_transition = dissolve

    ## Used when returning to the main menu from the game.
    config.game_main_transition = dissolve

    ## Used when entering the main menu from the splashscreen.
    config.end_splash_transition = dissolve

    ## Used when entering the main menu after the game has ended.
    config.end_game_transition = dissolve

    ## Used when a game is loaded.
    config.after_load_transition = dissolve

    ## Used when the window is shown.
    config.window_show_transition = dissolve

    ## Used when the window is hidden.
    config.window_hide_transition = dissolve

    ## Used when showing NVL-mode text directly after ADV-mode text.
    config.adv_nvl_transition = dissolve

    ## Used when showing ADV-mode text directly after NVL-mode text.
    config.nvl_adv_transition = dissolve

    ## Used when yesno is shown.
    config.enter_yesno_transition = dissolve

    ## Used when the yesno is hidden.
    config.exit_yesno_transition = dissolve

    ## Used when entering a replay
    config.enter_replay_transition = dissolve

    ## Used when exiting a replay
    config.exit_replay_transition = dissolve

    ## Used when the image is changed by a say statement with image attributes.
    config.say_attribute_transition = dissolve

    #########################################
    ## This is the name of the directory where the game's data is
    ## stored. (It needs to be set early, before any other init code
    ## is run, so the persistent information can be found by the init code.)
    
    
    ### Delete this part so your saves during encoding will be deleted when making a distribution. As for now, I use hashtag. You should also delete the folder.
#python early:
    #config.save_directory = "GUI Tutorial by zishy-1494491597"
    
    ##Delete til here!

init -1 python hide:
    #########################################
    ## Default values of Preferences.

    ## Note: These options are only evaluated the first time a
    ## game is run. To have them run a second time, delete
    ## game/saves/persistent

    ## Should we start in fullscreen mode?

    config.default_fullscreen = False

    ## The default text speed in characters per second. 0 is infinite.

    config.default_text_cps = 77

    ## The default auto-forward time setting.

    config.default_afm_time = 77

    #########################################
    #########################################
    
    ##### This is the code for the NameBox
style say_label:
        font "WakeUpHoney.TTF"    
        size 37
        bold True
        #drop_shadow [(1, 1)] 
        #drop_shadow_color "#660033"
        #outlines [(1, "#000000", 1, 1)]  # black 
    
## Icon
## ########################################################################'

## The icon displayed on the taskbar or dock.
## Favicon

define config.window_icon = "icon.png"     
    
    
    
    
    
    
    
    
    
    
    
    
    ## You hide the files by using this code as you distribute them. Remove the hashtag kudasai~!
    #build.classify('**~', None)
    #build.classify('**.bak', None)
    #build.classify('**/.**', None)
    #build.classify('**/#**', None)
    #build.classify('**/thumbs.db', None)
    #build.classify('game/**.png', 'archive')
    #build.classify('game/**.jpg', 'archive')
    #build.classify('game/**.mp3', 'archive')
    #build.classify('game/**.ogg', 'archive')
    #build.classify('game/**.wav', 'archive')
    #build.classify('game/**.rpy', 'archive')
    #build.classify('game/**.rpt', 'archive')
    
    #build.classify('game/**.png', 'archive')
    #build.classify('game/**.jpg', 'archive')
    
    #build.documentation('*.html')
    #build.documentation('*.txt')

    
    
    
    
    
    
    
    
    
    
    


## This section contains information about how to build your project into
## distribution files.
init python:

    ## The name that's used for directories and archive files. For example, if
    ## this is 'mygame-1.0', the windows distribution will be in the
    ## directory 'mygame-1.0-win', in the 'mygame-1.0-win.zip' file.
    build.directory_name = "GUI_Tutorial_by_zishy-1.0"

    ## The name that's uses for executables - the program that users will run
    ## to start the game. For example, if this is 'mygame', then on Windows,
    ## users can click 'mygame.exe' to start the game.
    build.executable_name = "GUI_Tutorial_by_zishy"

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
    