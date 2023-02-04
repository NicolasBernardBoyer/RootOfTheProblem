# (!) -> WIP

# Characters
define mc = DynamicCharacter("[mc_name]")
define v = Character("Vina")
define n = Character("Nor")
define g = Character("Grandpa")
define h = Character("Hal")
define s = Character("Superbug")
define unknown = Character("???")


# Image Effects
define hover_effect = im.Flip("click temp.png", vertical=True)
define scale_effect = im.FactorScale("click temp.png", 1.2)
define tint_effect = im.MatrixColor(
    "click temp.png",
    im.matrix.tint(1, 0.5, 1)
)

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

# Screens
screen clickable_items:
    imagebutton:
        xpos 0.5
        ypos 0.5
        idle "click temp.png"
        hover tint_effect
        action Jump("end")

    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.2
        ypos 0.2
        idle "click temp.png"
        hover scale_effect
        action Jump("end")


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
    return

label intro_choice1:

    $ is_chosen_intro1 = True

    v "I really don't know. She came back yesterday while you were out checking the rabbit traps with Gramps and she just collapsed to the ground without warning."
    v "She started screaming incoherent things and fell asleep after calming down. She hasn't woken up since."
    v "If it wasn't for the fever, I'd think it was just a nervous breakdown."
    v "Anyways, what matters right now is doing whatever we can to keep her fever down."

    jump intro_choices
    return

label intro_choice2:

    $ is_chosen_intro2 = True
    v "There's an old town a few kilometers east from here."
    v "Grandpa found it and said it didn't look like it had been plundered."
    v "I need you to go there to see if you can find any supplies."
    v "Bring back anything you can."

    jump intro_choices
    return




# Deprecated. Use as reference
label point_and_click_playground:

    scene bg temp
    call screen clickable_items

    return



# End
label point_and_click_playground_end:
    
    mc "Next Step"

    jump start
    return