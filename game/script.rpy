# (!) -> WIP

# Characters
define mc = DynamicCharacter("[mc_name]")
define v = Character("Vina", color="#4b65ad")
define n = Character("Nor", color="#9d471f")
define s = Character("ShadowEdge12", color="#736568")
define s = Character("Superbug", color="#2e8838")
define unknown = Character("???", color="#5195c0")

# music
define music_ambience = "audio/music/AMBIENCE 1.mp3"
define music_character_creation = "audio/music/CHARACTER CREATION THEME.mp3"
define music_final_boss = "audio/music/FINAL BOSS THEME.mp3"

define sound_click_slow = "audio/SFX/Button Slow.mp3"
define sound_click_normal = "audio/SFX/Button Normal.mp3"
define sound_click_fast = "audio/SFX/Button Fast.mp3"
define sound_clicks = [sound_click_slow, sound_click_normal, sound_click_fast]

# Image Effects
define hover_effect = im.Flip("click temp.png", vertical=True)
define scale_effect = im.FactorScale("click temp.png", 1.2)
define tint_effect = im.MatrixColor(
    "click temp.png",
    im.matrix.tint(1, 0.5, 1)
)

# Images
define icon_folder = "computer files.png"
define icon_checker = "file pic.png"
define icon_mug = "mug pic.png"
define icon_mug_egg = "mug easter egg.png"
define icon_paint = "mspaint icon.png"
define icon_text = "txt icon.png"
define icon_solitaire = "solitare icon.png"
define icon_trash = "computer trash.png"
define icon_virus = "virus icon.png"
define icon_webpage = "webpage icon.png"

define app_folder = "file explorer.png"
define app_paint = "mspaint.png"
define app_text = "txt page.png"
define app_web = "webpage.png"

# Transform
transform left_to_right:
    xalign 0.0
    linear 2.0 xalign 1.0
    repeat

transform button_animation():
    linear renpy.random.randint(1, 3) / 10.0 rotate renpy.random.randint(2, 10)
    pause 0.2
    linear renpy.random.randint(1, 3) / 10.0 rotate renpy.random.randint(2, 10) * -1
    pause 0.2
    repeat



# Python Code
init:
    $ mc_name = "placeholder"

    $ is_chosen_intro1 = False
    $ is_chosen_intro2 = False

    python:
        def name_input():
            mc_name = renpy.input("Enter your name", length=32)
            mc_name = mc_name.strip()

            while not mc_name:
                mc_name = renpy.input("Please enter a real name..", length=32)
                mc_name = mc_name.strip()

            return mc_name

        def play_click_sound():
            Play(file=renpy.random.choice(sound_clicks),channel="sound")
            #click = randint(1, 3);
            #if click == 1 return "SFX/Button Fast.wav"


# Screens
# First Computer Screen
screen computer1:
    $ factor_scale = 1.1

    imagebutton: # Folder
        xanchor 0.5
        yanchor 0.5
        xpos 0.32
        ypos 0.23
        idle icon_folder
        hover im.FactorScale(icon_folder, factor_scale)
        action [Play(file=renpy.random.choice(sound_clicks),channel="sound"), ToggleScreen("application_folder")] #(!)
        mouse "computer"

    imagebutton: #Paint
        xanchor 0.5
        yanchor 0.5
        xpos 0.41
        ypos 0.23
        idle icon_paint
        hover im.FactorScale(icon_paint, factor_scale)
        action [Play(file=renpy.random.choice(sound_clicks),channel="sound"), ToggleScreen("application_paint")] #(!)
        mouse "computer"

    imagebutton: #Solitaire
        xanchor 0.5
        yanchor 0.5
        xpos 0.65
        ypos 0.56
        idle icon_solitaire
        hover im.FactorScale(icon_solitaire, factor_scale)
        action [Play(file=renpy.random.choice(sound_clicks),channel="sound"), Jump("final_boss")] #(!)
        mouse "computer"

    imagebutton: #Web
        xanchor 0.5
        yanchor 0.5
        xpos 0.55
        ypos 0.72
        idle icon_webpage
        hover im.FactorScale(icon_webpage, factor_scale)
        action [Play(file=renpy.random.choice(sound_clicks),channel="sound"), ToggleScreen("application_web")] #(!)
        mouse "computer"

    imagebutton: #Trash
        xanchor 0.5
        yanchor 0.5
        xpos 0.65
        ypos 0.72
        idle icon_trash
        hover im.FactorScale(icon_trash, factor_scale)
        action [Play(file=renpy.random.choice(sound_clicks),channel="sound"), ToggleScreen("application_trash")] #(!)
        mouse "computer"


#File Explorer Application
screen application_folder:
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.42
        ypos 0.51
        idle app_folder
        action Hide("application_folder") #(!)

#Paint Application
screen application_paint:
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.52
        ypos 0.38
        idle app_paint
        action Hide("application_paint") #(!)


#Web Application
screen application_web:
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.42
        ypos 0.57
        idle app_web
        action Hide("application_web") #(!)
        mouse "computer"


# Application Window
screen application_trash:
    imagebutton: #App
        xanchor 0.5
        yanchor 0.5
        xpos 0.55
        ypos 0.46
        idle app_folder
        action Hide("application_trash") #(!)

    imagebutton: #Mug
        xanchor 0.5
        yanchor 0.5
        xpos 0.51
        ypos 0.41
        idle im.FactorScale(icon_mug, 0.70)
        hover im.FactorScale(icon_mug, 1)
        action [Play(file=renpy.random.choice(sound_clicks),channel="sound"), ToggleScreen("screen_mug")] #(!)
        mouse "computer"
    
    add im.FactorScale(icon_virus, 0.70) xpos 0.57 ypos 0.41 xanchor 0.5 yanchor 0.5
    add im.FactorScale(icon_text, 0.70) xpos 0.63 ypos 0.41 xanchor 0.5 yanchor 0.5


# Mug Screen
screen screen_mug:
    imagebutton: #Mug
        xanchor 0.5
        yanchor 0.5
        xpos 0.48
        ypos 0.48
        idle icon_mug_egg
        action Hide("screen_mug") #(!)
        mouse "computer"


# Final Battle
screen rpg_battle:
    imagebutton: # Button 1
        xanchor 0.5
        yanchor 0.5
        xpos 0.30
        ypos 0.80
        idle "temp button.png" at button_animation()

    imagebutton: # Button 2
        xanchor 0.5
        yanchor 0.5
        xpos 0.50
        ypos 0.80
        idle "temp button.png" at button_animation()

    imagebutton: # Button 3
        xanchor 0.5
        yanchor 0.5
        xpos 0.70
        ypos 0.80
        idle "temp button.png" at button_animation()
        hover 


# __ _             _   
#/ _\ |_ __ _ _ __| |_ 
#\ \| __/ _` | '__| __|
#_\ \ || (_| | |  | |_ 
#\__/\__\__,_|_|   \__|

label start:
    play music music_character_creation fadeout 1
    $ mc_name = name_input()
    jump intro
    return

label intro:
    unknown "[mc_name], follow the roots."
    unknown "Follow the roots and come find me."

    # Scene Infirmary
    play music music_ambience fadeout 1
    show vina smile at right
    v "Ah, you're awake"
    v "Tell me you haven't been here all night, you're going to get a crick in your neck."
    v "I bet you haven't eaten either."

    # (!) Vina Sad Face
    show edge surprised at left
    v "I know you're worried about Nor, but you have to keep taking care of yourself."
    show edge smug
    v "We have to stay strong and keep going until she wakes up."

    # (!) Vina Small smile
    hide edge
    v "Or else, when she wakes up, the first thing she'll see is your eyebags and the first thing she'll hear is your growing stomach."
    v "We don't want that now, do we?"

    jump intro_choices
    return



# Intro choices
label intro_choices:

    menu:
        "What happened to her?" if not is_chosen_intro1:
            jump intro_choice1
        
        "How can I help?" if not is_chosen_intro2:
            jump intro_choice2

    hide vina
    "Continue Here (!)"
    jump computer_screen1
    return

label intro_choice1:

    $ is_chosen_intro1 = True
    $ renpy.fix_rollback()
    v "I really don't know. She came back yesterday while you were out checking the rabbit traps with Gramps and she just collapsed to the ground without warning."
    v "She started screaming incoherent things and fell asleep after calming down. She hasn't woken up since."
    v "If it wasn't for the fever, I'd think it was just a nervous breakdown."
    v "Anyways, what matters right now is doing whatever we can to keep her fever down."

    jump intro_choices
    return

label intro_choice2:

    $ is_chosen_intro2 = True
    $ renpy.fix_rollback()

    v "There's an old town a few kilometers east from here."
    v "Grandpa found it and said it didn't look like it had been plundered."
    v "I need you to go there to see if you can find any supplies."
    v "Bring back anything you can."

    jump intro_choices
    return


# Room with Characters (!)
label main_room:
    jump point_and_click_playground
    return

# Computer Screen 1
label computer_screen1:
    scene bg computer1

    show computer_screen1:
        xanchor 0.5
        yanchor 0.5
        xalign 0.5
        yalign 0.5


    call screen computer1 
    return

# Final Boss
label final_boss:

    play music music_final_boss

    show edge surprised at right
    show vina smile at left
    "Super Bug wants to Fight!"

    call screen rpg_battle

    return