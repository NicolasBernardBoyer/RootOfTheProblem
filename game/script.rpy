# (!) -> WIP


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