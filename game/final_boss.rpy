# Final Boss
# Variables

# Font for fight. Use Style instead...
define pixel_font = "fonts/PressStart2P-Regular.ttf"

# Text Style for buttons. Deprecated
style button_style is text:
    size 40
    font pixel_font



#  Labels
# template: "{font=[pixel_font]}{/font}"
label final_boss:
    scene fight bg
    play music music_final_boss fadeout 1


    show superbug idle
    show mothertree idle

    "{font=[pixel_font]}The Mother Tree blocks your path!{/font}"
    "{font=[pixel_font]}The Mother Tree lashes out with roots!{/font}"
    
    show mothertree attack
    show slash
    pause 0.2
    hide slash
    pause 0.25
    show mothertree idle

    "{font=[pixel_font]}It's ineffective against Superbug!”{/font}"

    call screen rpg_battle

    return

define attackLeft = 1
# (!) Not used
label attack:

    if attackLeft > 0:
        $ attackLeft = attackLeft - 1
        "{font=[pixel_font]}You are too scared of the mother tree!{/font}"
        call screen rpg_battle

    
    "{font=[pixel_font]}Superbug unloads a rain of bullets!{/font}"
    # (!) Attack
    show superbug shoot
    show bullets
    pause 1.0
    hide bullets
    show superbug idle
    show mothertree idle

    "{font=[pixel_font]}The Mother Tree is weak to Superbug's attack!{/font}"
    show mothertree death
    
    "{font=[pixel_font]}The Mother Tree has perished…{/font}"
    hide mothertree

    "{font=[pixel_font]}You won! You gained 10708 exp and 450 Gold.{/font}"
    
    call screen rpg_battle
    return

label talk_mothertree:

    return

label fight_items:
    "{font=[pixel_font]}You do no have an inventory!{/font}"
    call screen rpg_battle

    return

label fight_run:
    s "{font=[pixel_font]}Superbug does not run away!{/font}"
    call screen rpg_battle

    return


# Final Battle
screen rpg_battle:

    textbutton "Attack" at button_animation:
        xanchor 0.5
        yanchor 0.5
        xpos 0.20
        ypos 0.80
        text_font pixel_font
        text_size 40
        text_color '#ffffff'
        action Jump("attack")

    textbutton "Talk" at button_animation:
        xanchor 0.5
        yanchor 0.5
        xpos 0.40
        ypos 0.80
        text_font pixel_font
        text_color '#ffffff'
        action Jump("attack")

    textbutton "Items" at button_animation:
        xanchor 0.5
        yanchor 0.5
        xpos 0.60
        ypos 0.80
        text_font pixel_font
        text_color '#ffffff'
        action Jump("fight_items")

    textbutton "Run!" at button_animation:
        xanchor 0.5
        yanchor 0.5
        xpos 0.80
        ypos 0.80
        text_font pixel_font
        text_color '#ffffff'
        action Jump("fight_run")


# Animations
# Superbug
define superbug_x = 0.25
define superbug_y = 0.5

image superbug idle:
    xanchor 0.5
    yanchor 0.5
    xpos superbug_x
    ypos superbug_y
    im.FactorScale("bug idle/bug idle1.png", 1)
    pause 0.5
    im.FactorScale("bug idle/bug idle2.png", 1)
    pause 0.5
    repeat


image superbug shoot:
    xanchor 0.5
    yanchor 0.5
    xpos superbug_x
    ypos superbug_y
    im.FactorScale("bug shoot/bug shoot1.png", 1)
    pause 0.1
    im.FactorScale("bug shoot/bug shoot2.png", 1)
    pause 0.1
    repeat 5


image slash:
    xanchor 0.5
    yanchor 0.5
    xpos superbug_x - 0.01
    ypos superbug_y + 0.05
    im.FactorScale("slash/slash1.png", 1)
    pause 0.1
    im.FactorScale("slash/slash2.png", 1)
    pause 0.1


#Mother tree
define mothertree_x = 0.75
define mothertree_y = 0.4

image mothertree attack:
    xanchor 0.5
    yanchor 0.5
    xpos mothertree_x
    ypos mothertree_y
    im.FactorScale("mother tree attack/mothertree attack1.png", 1)
    pause 0.06
    im.FactorScale("mother tree attack/mothertree attack2.png", 1)
    pause 0.06
    im.FactorScale("mother tree attack/mothertree attack3.png", 1)
    pause 0.06
    im.FactorScale("mother tree attack/mothertree attack4.png", 1)
    pause 0.06
    im.FactorScale("mother tree attack/mothertree attack5.png", 1)
    pause 0.06
    im.FactorScale("mother tree attack/mothertree attack6.png", 1)
    pause 0.06
    im.FactorScale("mother tree attack/mothertree attack7.png", 1)
    pause 0.06

image mothertree death:
    xanchor 0.5
    yanchor 0.5
    xpos mothertree_x
    ypos mothertree_y
    im.FactorScale("mother tree death/mothertree death1.png", 1)
    pause 0.1
    im.FactorScale("mother tree death/mothertree death2.png", 1)
    pause 0.1
    im.FactorScale("mother tree death/mothertree death3.png", 1)
    pause 0.1
    im.FactorScale("mother tree death/mothertree death4.png", 1)
    pause 0.1
    im.FactorScale("mother tree death/mothertree death5.png", 1)
    pause 0.1
    im.FactorScale("mother tree death/mothertree death6.png", 1)
    pause 0.1
    im.FactorScale("mother tree death/mothertree death7.png", 1)
    pause 0.1
    im.FactorScale("mother tree death/mothertree death8.png", 1)
    pause 0.1
    im.FactorScale("mother tree death/mothertree death9.png", 1)
    pause 0.1

image mothertree idle:
    xanchor 0.5
    yanchor 0.5
    xpos mothertree_x
    ypos mothertree_y
    im.FactorScale("mother tree idle/mothertree idle1.png", 1)
    pause 0.5
    im.FactorScale("mother tree idle/mothertree idle2.png", 1)
    pause 0.5
    repeat


# Bullets
image bullets:
    xanchor 0.5
    yanchor 0.5
    xpos 0.75
    ypos 0.4
    im.FactorScale("bullets/bullets1.png", 1)
    pause 0.1
    im.FactorScale("bullets/bullets2.png", 1)
    pause 0.1
    repeat 5
    





transform button_animation():
    linear renpy.random.randint(1, 3) / 10.0 rotate renpy.random.randint(2, 10) / 20
    pause 0.2
    linear renpy.random.randint(1, 3) / 10.0 rotate renpy.random.randint(2, 10) * -1 / 20
    pause 0.2
    repeat 







# Python for animation (not working!)
init python:
    def shoot(st, at):
        if st > 5.0:
            return "bug idle/bug idle1.png", None
        elif st % 0.2 == 0:
            return im.FactorScale("bug shoot/bug shoot1.png", 5), 0.1
        else:
            return im.FactorScale("bug shoot/bug shoot2.png", 5), 0.1
