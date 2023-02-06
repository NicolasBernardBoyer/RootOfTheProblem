label bad_ending:

    scene black
    "If I say this, I'll anger the Mother Tree."
    "I need to rethink how I want to negotiate..."
    # (!) Final Screen

    jump final_boss
    return

label good_ending_attack:

    play music music_attack_ending fadeout 1
    scene black

    "With the Mother Tree dead, the roots stopped growing."
    "They stayed where they were, blocking the way and impeding the reconstruction of anything."
    "And whilst the Mother Tree was defeated, there is no guarantee that it was the only plant controlling the roots."
    "We are not free yet."

    jump credits
    return

label good_ending: #Pacifist

    s "OK I WILL GIVE YOU A CHANCE"
    play music music_good_ending fadeout 1
    scene black

    "With this new friendship established, you went around the world, striking new alliances with every sentient plant you encountered."
    "You taught humans along your way to live in harmony with their vegetal neighbors."
    "Over time, new human civilizations started blossoming."
    "It's a new age of peace."

    jump credits
    return

label credits:
    "Written by Adèlane Desparois, Nicolas Boyer and Aria Tessler"
    "Background Art and UI by Rev Nahabedian"
    "Character Design and Animation by Nicolas Boyer"
    "Audio by Aria Tessler"
    "Programming by Dominic Emond and Nicolas Boyer"

    return