# (!) -> WIP

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


# Room with Characters (!)
label main_room:
    jump point_and_click_playground
    return

# Computer Screen 1
label computer_screen1:

    play music music_ambience2 fadeout 2
    scene computer 1

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

    $ font = "fonts/PressStart2P-Regular.ttf"
    "Super Bug wants to Fight!"

    call screen rpg_battle

    return