# Label
# Computer Screen 1
define suspicious_email_read = False
define bunny_email = False
define official_report_read = False
define redacted_report_read = False


label computer_screen1:

    play music music_ambience2 fadeout 2
    scene computer 1
    show screen computer1
    call screen logout_hack_screen

    return


label bunny_email:
    $ bunny_email = True


    "Welcome to the number one online newsletter, The Read! As promised, here are three fun facts about your favorite fluffy creatures.{p=1.5}{nw}"
    "Number one: Everyone knows that carrots are the bunny's food of choice… or is it? As it turns out, this happens to be a myth! As root vegetables like carrots have high amounts of sugar, they prove to be quite bad for the health of the rabbit. Instead, they tend to prefer hay and other kinds of veggies!{p=1.5}{nw}"
    "Number two: Bunnies may seem cute and cuddly, but in reality, they have an unexpected dark side. Did you know that they love to drink the blood of their enemies? This can be explained scientifically through consuming the blood of other bunnies can lengthen their lifespan.{p=1.5}{nw}"
    "Number three: Despite their small appearance, bunnies can never get enough of a good feast. They are known to have near endless stomachs, to the point that if they are not willing to eat, you should take them to a veterinarian center as soon as possible.{p=1.5}{nw}"
    "Thank you so much for reading this month's report! See you next month for a story on The Couchening..{p=1.5}{nw}"

    hide screen screen_open_email
    call screen logout_hack_screen
    return



# "{p=1.5}{nw}"
label suspicious_email:
    $ suspicious_email_read = True
    "Good evening. I'm sure at this point you all noticed the worrying behavior of Mx Jekan. Their fraternizing with the asset could jeopardize our operations. {p=1.5}{nw}"
    "This needs to be taken care of. I want them gone.{p=1.5}{nw}"
    "Signed, Management{p=1.5}{nw}"


    hide screen screen_close_email
    call screen logout_hack_screen
    return


label official_report:
    $ official_report_read = True

    "Report on the G-GJ-23 Growth, Date: February 5th 2023{p=1.5}{nw}"
    "Description: A 6ft tall growth was discovered 23 days ago. The species of the plant is unknown, but our tests show it has poisonous properties, causing hallucinations, a fever and death.{p=1.5}{nw}"
    "Conclusions: This substance having no known antidote, it could be used as a bioweapon.{p=1.5}{nw}"

    hide screen screen_official_report
    call screen logout_hack_screen
    return

label redacted_report:
    $ redacted_report_read = True

    "(REDACTED){p=1.5}{nw}"
    se "Give me a second, I think I can recover the original file.{p=1.5}{nw}"
    "Report of Dr Jekan on the sentient plant, Date: February 3rd 2023{p=1.5}{nw}"
    "Description: Locals have found an unknown plant growing in a basement. I was unable to specify its species.{p=1.5}{nw}"
    "As I was studying it, the undiscovered plant grew a vine that wrapped itself around me. I have never seen such a fast and localized growth in all my years of research.{p=1.5}{nw}"
    "The plant was reacting to my presence. After several tests listed below, I determined that this plant is sentient and has human-level intelligence. It also seems to display a human-like emotional range.{p=1.5}{nw}"
    "Conclusions: We must form good relations with this new intelligent species to ensure the continued peace.{p=1.5}{nw}"
    
    hide screen screen_redacted_report
    call screen logout_hack_screen
    return


label closing_screen:

    if not redacted_report_read:
        "You can't logout yet! {p=1.5}{nw}"
        call screen logout_hack_screen
    else:
        jump back_home
    
    return



# Python
init python:
    def logout():
        renpy.say("ss", "You can't logout yet!")

# Screens
# First Computer Screen
screen logout_hack_screen:
    imagebutton: # (!) Logout Button
        xanchor 0.5
        yanchor 0.5
        xpos 0.695
        ypos 0.90
        idle im.FactorScale(icon_close, 1.05)
        hover im.FactorScale(icon_close, 1.15)
        action [Play(file=renpy.random.choice(sound_clicks),channel="sound"), Jump("closing_screen")] #(!)
        mouse "computer"


screen computer1:
    $ factor_scale = 1.1


    imagebutton: # Background
        xanchor 0.5
        yanchor 0.5
        xalign 0.5
        yalign 0.5
        idle "computer_screen1.png"
        action Play(file=renpy.random.choice(sound_clicks), channel="sound")
        mouse "computer"

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
        action Play(file=renpy.random.choice(sound_clicks),channel="sound") #(!)
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
        action Hide("application_folder")
        mouse "computer"

    imagebutton: #Official Report
        xanchor 0.5
        yanchor 0.5
        xpos 0.38
        ypos 0.46
        idle im.FactorScale(icon_text, 0.60)
        hover im.FactorScale(icon_text, 0.9)
        action [Play(file=renpy.random.choice(sound_clicks),channel="sound"), Show("screen_official_report")]
        mouse "computer"

    imagebutton: #Dr Jekans Report
        xanchor 0.5
        yanchor 0.5
        xpos 0.44
        ypos 0.46
        idle im.FactorScale(icon_text, 0.60)
        hover im.FactorScale(icon_text, 0.9)
        action [Play(file=renpy.random.choice(sound_clicks),channel="sound"), Show("screen_redacted_report")]
        mouse "computer"

    

#Paint Application
screen application_paint:
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.52
        ypos 0.38
        idle app_paint
        action Hide("application_paint")
        mouse "computer"


#Web Application
screen application_web:
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.42
        ypos 0.57
        idle app_web
        action Hide("application_web")
        mouse "computer"


# Application Window
screen application_trash:
    imagebutton: #App
        xanchor 0.5
        yanchor 0.5
        xpos 0.55
        ypos 0.46
        idle app_folder
        action Hide("application_trash")
        mouse "computer"

    imagebutton: #Mug
        xanchor 0.5
        yanchor 0.5
        xpos 0.51
        ypos 0.41
        idle im.FactorScale(icon_mug, 0.70)
        hover im.FactorScale(icon_mug, 1)
        action [Play(file=renpy.random.choice(sound_clicks),channel="sound"), ToggleScreen("screen_mug")] #(!)
        mouse "computer"

    imagebutton: #Virus
        xanchor 0.5
        yanchor 0.5
        xpos 0.57
        ypos 0.41
        idle im.FactorScale(icon_virus, 0.70)
        hover im.FactorScale(icon_virus, 1)
        action [Play(file=renpy.random.choice(sound_clicks),channel="sound"), ToggleScreen("screen_virus")] #(!)
        mouse "computer"

    imagebutton: #Email Close
        xanchor 0.5
        yanchor 0.5
        xpos 0.52
        ypos 0.53
        idle im.FactorScale(icon_close_mail, 0.60)
        hover im.FactorScale(icon_close_mail, 0.9)
        action [Play(file=renpy.random.choice(sound_clicks),channel="sound"), Show("screen_close_email")] #(!)
        mouse "computer"

    imagebutton: #Email Open
        xanchor 0.5
        yanchor 0.5
        xpos 0.58
        ypos 0.53
        idle im.FactorScale(icon_open_mail, 0.60)
        hover im.FactorScale(icon_open_mail, 0.9)
        action [Play(file=renpy.random.choice(sound_clicks),channel="sound"), Show("screen_open_email")] #(!)
        mouse "computer"
    
    add im.FactorScale(icon_text, 0.70) xpos 0.63 ypos 0.41 xanchor 0.5 yanchor 0.5


# Email 1
screen screen_close_email:
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.48
        ypos 0.48
        idle app_report_redacted
        action Jump("suspicious_email")
        mouse "computer"

# Bunny Email
screen screen_open_email:
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.48
        ypos 0.48
        idle app_report
        action Jump("bunny_email")
        mouse "computer"

# Offical Report
screen screen_official_report:
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.48
        ypos 0.48
        idle app_report
        action Jump("official_report")
        mouse "computer"

# Redacted Report
screen screen_redacted_report:
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.48
        ypos 0.48
        idle app_report_redacted
        action Jump("redacted_report")
        mouse "computer"


# Mug Screen
screen screen_mug:
    imagebutton: #Mug
        xanchor 0.5
        yanchor 0.5
        xpos 0.48
        ypos 0.48
        idle icon_mug_egg
        action Hide("screen_mug")
        mouse "computer"

# Virus Screen
screen screen_virus:
    imagebutton: #Virus
        xanchor 0.5
        yanchor 0.5
        xpos 0.48
        ypos 0.48
        idle app_real
        action Hide("screen_virus") #(!)
        mouse "computer"
