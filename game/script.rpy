# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# define e = Character("Eileen")

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

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg temp
    call screen clickable_items

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    # show eileen happy

    # These display lines of dialogue.

    # e "You've created a new Ren'Py game."

    # e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return

# End
label end:
    
    "Next Step"

    jump start
    return