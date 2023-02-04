# (!) -> WIP

# Character
define mc = Character("Main Character Name Here (!)")

# Image Effects
define hover_effect = im.Flip("click temp.png", vertical=True)
define scale_effect = im.FactorScale("click temp.png", 1.2)
define tint_effect = im.MatrixColor(
    "click temp.png",
    im.matrix.tint(1, 0.5, 1)
)

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

# The game starts here.

label start:

    scene bg temp
    call screen clickable_items

    return



# End
label end:
    
    mc "Next Step"

    jump start
    return