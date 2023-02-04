# (!) -> WIP

# Characters
define mc = DynamicCharacter("[mc_name]")
define v = Character("Vina", color="#5195c0")
define n = Character("Nor", color="#9d471f")
define s = Character("ShadowEdge12", color="#6d176d")
define s = Character("Superbug", color="#2e8838")
define unknown = Character("???", color="#5195c0")

# music
define music_final_boss = "audio/music/FINAL BOSS THEME.mp3"

define sound_click_slow = "audio/SFX/Button Slow.mp3"
define sound_click_normal = "audio/SFX/Button Normal.mp3"
define sound_click_fast = "audio/SFX/Button Fast.mp3"
define sound_clicks = [sound_click_slow, sound_click_normal, sound_click_fast]

#Images
define mouse_cursor = "computer trash.png"

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
        action [Play(file=renpy.random.choice(sound_clicks),channel="sound"), Show("application")] #(!)
        mouse "computer"

    imagebutton: #Paint
        xanchor 0.5
        yanchor 0.5
        xpos 0.41
        ypos 0.23
        idle icon_paint
        hover im.FactorScale(icon_paint, factor_scale)
        action [Play(file=renpy.random.choice(sound_clicks),channel="sound"), Show("application_paint")] #(!)
        mouse "computer"

    imagebutton: #Trash
        xanchor 0.5
        yanchor 0.5
        xpos 0.65
        ypos 0.72
        idle "computer trash.png"
        hover im.FactorScale("computer trash.png", factor_scale)
        action [Play(file=renpy.random.choice(sound_clicks),channel="sound")] #(!)
        mouse "computer"


#Paint Application
screen application_paint:
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.5
        ypos 0.5
        idle "mspaint.png"
        action Hide("application_paint") #(!)


#Test Application Window
screen application:
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.5
        ypos 0.5
        idle "webpage.png"
        action Hide("application") #(!)



# __ _             _   
#/ _\ |_ __ _ _ __| |_ 
#\ \| __/ _` | '__| __|
#_\ \ || (_| | |  | |_ 
#\__/\__\__,_|_|   \__|

label start:
    $ mc_name = name_input()
    jump intro
    return

label intro:
    unknown "[mc_name], follow the roots."
    unknown "Follow the roots and come find me."

    # Scene Infirmary
    v "Ah, you're awake"
    v "Tell me you haven't been here all night, you're going to get a crick in your neck."
    v "I bet you haven't eaten either."

    # (!) Vina Sad Face
    v "I know you're worried about Nor, but you have to keep taking care of yourself."
    v "We have to stay strong and keep going until she wakes up."

    # (!) Vina Small smile
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
    "Final Boss Time (!)"
    return


# Deprecated. Use as reference
label point_and_click_playground:

    scene bg temp
    call screen clickable_items

    return



# Deprecated. Use as reference
label point_and_click_playground_end:
    
    mc "Next Step"

    jump start
    return