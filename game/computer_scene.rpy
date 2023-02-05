# Screens
# First Computer Screen
screen computer1:
    $ factor_scale = 1.1

    imagebutton: # Folder
        xanchor 0.5
        yanchor 0.5
        xpos 0.32
        ypos 0.23
        idle icon_folder
        hover im.FactorScale(icon_folder, factor_scale)
        action [Play(file=renpy.random.choice(sound_clicks),channel="sound"), ToggleScreen("application_folder")] #(!)
        mouse "computer"

    imagebutton: #Paint
        xanchor 0.5
        yanchor 0.5
        xpos 0.41
        ypos 0.23
        idle icon_paint
        hover im.FactorScale(icon_paint, factor_scale)
        action [Play(file=renpy.random.choice(sound_clicks),channel="sound"), ToggleScreen("application_paint")] #(!)
        mouse "computer"

    imagebutton: #Solitaire
        xanchor 0.5
        yanchor 0.5
        xpos 0.65
        ypos 0.56
        idle icon_solitaire
        hover im.FactorScale(icon_solitaire, factor_scale)
        action [Play(file=renpy.random.choice(sound_clicks),channel="sound"), Jump("final_boss")] #(!)
        mouse "computer"

    imagebutton: #Web
        xanchor 0.5
        yanchor 0.5
        xpos 0.55
        ypos 0.72
        idle icon_webpage
        hover im.FactorScale(icon_webpage, factor_scale)
        action [Play(file=renpy.random.choice(sound_clicks),channel="sound"), ToggleScreen("application_web")] #(!)
        mouse "computer"

    imagebutton: #Trash
        xanchor 0.5
        yanchor 0.5
        xpos 0.65
        ypos 0.72
        idle icon_trash
        hover im.FactorScale(icon_trash, factor_scale)
        action [Play(file=renpy.random.choice(sound_clicks),channel="sound"), ToggleScreen("application_trash")] #(!)
        mouse "computer"


#File Explorer Application
screen application_folder:
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.42
        ypos 0.51
        idle app_folder
        action Hide("application_folder") #(!)

#Paint Application
screen application_paint:
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.52
        ypos 0.38
        idle app_paint
        action Hide("application_paint") #(!)


#Web Application
screen application_web:
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.42
        ypos 0.57
        idle app_web
        action Hide("application_web") #(!)
        mouse "computer"


# Application Window
screen application_trash:
    imagebutton: #App
        xanchor 0.5
        yanchor 0.5
        xpos 0.55
        ypos 0.46
        idle app_folder
        action Hide("application_trash") #(!)

    imagebutton: #Mug
        xanchor 0.5
        yanchor 0.5
        xpos 0.51
        ypos 0.41
        idle im.FactorScale(icon_mug, 0.70)
        hover im.FactorScale(icon_mug, 1)
        action [Play(file=renpy.random.choice(sound_clicks),channel="sound"), ToggleScreen("screen_mug")] #(!)
        mouse "computer"
    
    add im.FactorScale(icon_virus, 0.70) xpos 0.57 ypos 0.41 xanchor 0.5 yanchor 0.5
    add im.FactorScale(icon_text, 0.70) xpos 0.63 ypos 0.41 xanchor 0.5 yanchor 0.5


# Mug Screen
screen screen_mug:
    imagebutton: #Mug
        xanchor 0.5
        yanchor 0.5
        xpos 0.48
        ypos 0.48
        idle icon_mug_egg
        action Hide("screen_mug") #(!)
        mouse "computer"