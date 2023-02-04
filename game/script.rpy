# (!) -> WIP

# Character
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
    return


label point_and_click_playground:

    scene bg temp
    call screen clickable_items

    return



# End
label point_and_click_playground_end:
    
    mc "Next Step"

    jump start
    return