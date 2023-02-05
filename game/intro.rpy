label intro:
    play music music_ambience fadeout 1 fadein 3

    "There are bunnies hidden thoughout the game. Try to find them all!"

    unknown "[mc_name], follow the roots."
    unknown "Follow the roots and come find me."

    # Scene Infirmary
    scene hq
    show vina neutral at right
    v "You're finally awake."
    v "Please tell me you haven't been here all night. You're gonna get a crick in the neck. You probably haven't eaten either…"
    
    show vina sad
    v "I know you're worried about Nor, but you gotta take care of yourself, too."
    v "We have to stay strong until she wakes up."

    show vina smile
    v "If not, the first thing she'll see when she wakes up will be your eyebags."
    v "We don't want that, do we?"

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
    jump main_room
    return

label intro_choice1:

    $ is_chosen_intro1 = True
    $ renpy.fix_rollback()

    show vina sad
    v "I really don't know. She came back yesterday while you were out checking the rabbit traps and she just collapsed to the ground without warning."
    v "She started screaming incoherent things and fell asleep after calming down. She hasn't woken up since."
    v "If it wasn't for the fever, I'd think it was just a nervous breakdown."
    
    show vina neutral
    v "Anyways, what matters right now is doing whatever we can to keep her fever down."

    jump intro_choices
    return

label intro_choice2:

    $ is_chosen_intro2 = True
    $ renpy.fix_rollback()

    v "There's an old town a few kilometers east from here."
    v "I noticed it and it didn't look like it had been plundered. Too bad I had too much stuff to carry at the time."
    v "I need you to go there to see if you can find any supplies."

    show vina smile
    v "Bring back anything you can."

    jump intro_choices
    return