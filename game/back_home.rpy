# Room with Characters D
label back_home:

    hide screen computer1
    hide screen application_folder
    hide screen application_paint
    hide screen application_web
    hide screen application_trash
    hide screen screen_mug
    hide screen screen_virus

    play music music_infirmary fadeout 1
    scene infirmary

    "I returned home after making my shocking discovery, eager to ask Vina for help."
  
    show vina neutral at left

    v "So you two found an old lab report hidden in a computer that told you that the plants are sentient and that they fused with computers, huh?"

    show vina sad

    v "Your story sounds utterly ridiculous."

    show edge surprised at right

    se "I swear, it's true! I saw it all!"

    show vina smile

    v "Calm down, man. I believe you."

    show edge neutral
    show vina neutral

    v "If we want to take down the threat, we'll need to eradicate the source."
    v "You mentioned that the report said it started out small in a basement. If you find that basement, all we'd have left to figure out is how to kill it."

    show vina smile

    v "I don't think weed spray would cut it."
    mc "But how would we find the right basement?"

    show vina neutral

    v "It must be where the roots are the thickest. But we still need a plan to kill it."

    show edge smug

    se "Well, guess it's my time to shine."
    v "What are you talking about? [mc_name] can go in there, but I won't let you go. You're too young to attempt such a stunt."
    se "There's no need for that. I don't need to actually be there to take down the threat."
    v "What are you talking about?"
    se "Do I really need to spell it out for you? The plants are fused with computers."
    se "If you wanna kill a computer, you're gonna need a bug."
    se "Give me an hour or something. I need to make something."

    scene black
    "two hours later..."
    scene infirmary
    
    show edge smug at right
    show vina neutral at left

    se "Alright, partner. It took me a little longer than I expected, but I've finally done it."
    se "This baby contains some of the worst malware out there. It all culminates together to create my masterpiece: the Superbug."
    se "That name is trademarked, by the way."
    se "With this, you'll be able to destroy any computer simply by running it."
    
    "Edge hands me a usb stick."

    se "You better put it to good use."

    show vina smile

    v "Good luck out there, and don't die. If you do, you'll never figure out Edgy's real name."

    show edge surprised

    se "I already told you! My real name is ShadowEdge12!"

    jump cave
    return