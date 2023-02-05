# Room with Characters D
label main_room:

    scene hq
    show edge computer at edge_position

    # (!)
    "This little menace is ShadowEdge12. He refuses to tell us his real name, age or anything else about him other than his screen name, which he claims is his real name."
    "Edge found an old computer a while back. Not sure how it still works, but if you plug the power cord in one of those damned roots, it turns on. For some reason, the computer's clock is stuck at 11:23 PM."

    mc "What are your working on, Edge?"
    se "Reading."
    mc "..."
    mc "So what are you reading?"

    se "When Nor came back, before she… Well, you know."
    se "She gave me this pretty intact cell phone she found. It doesn't have much on it, but I found this really cool map of what the old town used to look like."
    mc "What did it look like?"
    se "It was so big. Judging by the houses, there must have been so many people in it."
    se "I haven't even seen another person other than you, Vina or Nor in over two years, but these people must have walked by dozens of people every day."
    se "It's not like I care or anything. People suck. They're just distractions."

    show edge neutral at center

    se "They must have had it so easy. I see grocery stores and pharmacies peppered around everywhere on the map."
    se "Imagine wanting something and you can just leave the house and walk for like 10 minutes and it's yours."
    se "Must've been fun."
    se "You know, we COULD go look for supplies in what's left of those stores."
    mc "I'm not sure… That sounds dangerous."

    show edge smug

    se "I know, but there's something I REALLY want to check out while we're there."
    se "The map lists a laboratory near the center of the town."
    se "There must be so much tech inside. Some of it might even be intact enough for me to recover some files from it! I have to check it out!"
    
    mc "Alright then, but you'll have to be very careful when we're out. Promise me that you won't give me any trouble."

    se "Promise!"

    jump abandoned_lab
    return