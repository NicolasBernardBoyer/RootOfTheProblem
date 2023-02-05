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


# Room with Characters D
label main_room:

    scene hq
    show edge computer at edge_position

    # (!)
    "There are bunnies hidden thoughout the game"

    se "This little menage is ShadowEdge12. He refuses to tell us his real name, his age or anything else about him other than his screen name, which he claims is his real name."
    "Edge found this old thing a while back. Not sure how it still works, but if you plug the power cord in one of those damned roots, it turns on. For some reason, the clock is stuck at 11:23 PM."

    mc "what are your working on, Edgy?"
    se "Reading."
    mc "..."
    mc "So what are you reading?"

    show edge smug
    "..."

    show edge computer
    se "It's… Um…"
    se "When Nor came back, before she… Well, you know."
    se "She gave me this relatively intact cell phone she found. It doesn't have much on it, but I found this really cool map of what the old town used to look like."
    mc "What did it look like?"
    se "It was so big. Judging by the houses, there must have been so many people in it."
    se "I haven't even seen another person other than you, Vina and Nor in over two years, but these people must have walked by dozens of people every time they went outside."
    se "It's not like I care or anything. People suck. They're just distractions"
    se "They must have had it so easy. I see grocery stores and pharmacies peppered around everywhere on the map."
    se "Imagine wanting something and you can just leave the house and walk for like 10 minutes and it's yours."
    se "Must've been fun."
    se "You know, we COULD go look for supplies in what's left of those stores. [mc_name] I'm not sure… That sounds dangerous."
    se "I know, but there's something I want to check out while we're there."
    se "The map lists a laboratory near the center of the town."
    se "There must be so much tech inside. Some of it might even be intact enough for me to recover some files from it! I have to check it out!"
    
    mc "Alright then, but you'll have to be very careful when we're out. Promise me that you won't give me any trouble."
    se "Promise!"

    jump abandoned_lab
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