# Cave before computer 2.

label cave:

    # (!) Hide all other screens too
    hide screen computer1
    hide screen application_folder
    hide screen application_paint
    hide screen application_web
    hide screen application_trash
    hide screen screen_mug
    hide screen screen_virus

    play music music_ambience2 fadeout 1
    scene black

    "I left Vina and Edge to their banter and left for the core."

    scene cave

    mc "Hello, calamity. It's just you and me. I know you can understand me."
    mc "However, I can't understand you. Do you know what we could do to communicate better?"
    "Plant" "{i}Makes weird noises{/i}"

    mc "Perfect. Just don't stab me while I let my guard down."
    "I plug the usb stick that Edge gave me into the computer."
    "The computer bluescreens and displays a strange app named Superbug.exe."
    "The computer warns me that this app may harm it."

    jump computer_final_scene
    return