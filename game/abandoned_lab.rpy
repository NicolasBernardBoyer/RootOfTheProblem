label abandoned_lab:

    # (!) Nature Music Sounds
    scene lab
    play music music_ambience fadeout 1
    "We went to a couple of stores and filled our bags as much as possible."
    "After, we stopped at the old lab that Edge was interested in."

    # (!) Inside abandoned lab 
    show edge neutral at center
    se "This is it, the lab."
    se "Do you think the scientists that worked here are the ones who created the calamity?"

    menu:
        "There is no doubt!":
            jump abandoned_lab_choice1
        "No way!":
            jump abandoned_lab_choice2
        "I don't really know.":
            jump abandoned_lab_choice3

    return

label abandoned_lab_choice1:
    se "I think the same. I'm convinced that these scientists didn't know what they were messing with and created a monster in the process."
    jump abandoned_lab_part2
    return

label abandoned_lab_choice2:
    show edge smug
    se "What? You think the plants just appeared outta nowhere? Cmon, don't be such a simpleton, [mc_name]. Someone must have created them."
    jump abandoned_lab_part2
    return

label abandoned_lab_choice3:
    show edge smug
    se "You and Vina sure are lucky to have me, 'cause I know everything."
    se "Well, maybe not EVERYTHING, but I know a lot of things. There's no way these plants came outta nowhere. Someone must've been meddling with something."
    jump abandoned_lab_part2
    return

label abandoned_lab_part2:
    show edge neutral
    se "Anyways, let's go look at the computer."
    jump computer_screen1
    return

