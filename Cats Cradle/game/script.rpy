# Define images of characters
image player = "images/player.png"
image mrs_kitten = "images/mrs_kitten.png"

# Define characters
define narrator = Character("")
define mrs_kitten = Character("Mrs. Kitten", image="mrs_kitten", color="#9bb8d4")
define player = Character("You", image="player", color="#a5c98d")

# Start of script =====================================
label start:

    # Play music
    play music "darkmusic.mp3"

    # Set background
    scene bg outside with fade

    # Display dialogue
    narrator "As you trudge through the night, the weight of the gold sack pulling at your weary shoulders, you spot a humble cottage nestled in the darkness."
    narrator "The air is crisp, sending shivers down your spine, a reminder of the unforgiving chill of the night."
    narrator "You've been on the road for what feels like an eternity, and the sight of shelter beckons to you like a siren's call."

    # Ask user first choice
    menu:
        "YES (PLAY CAT'S CRADLE)":
            jump mrskitten_intro

        "NO (EXIT GAME)":
            jump end  

# End intro =====================================================================
# Enter Mrs. Kitten ==============================================================

label mrskitten_intro:

    narrator "You summon the last of your strength to approach the cottage, your hand reaching out to knock on the weathered door."
    narrator "After a moment, it creaks open, revealing a figure cloaked in shadow."
    narrator "As the door swings wider, the dim light from within illuminates the face of a woman, her features a curious blend of human and feline."

    # Display Mrs. Kitten
    show mrs_kitten with dissolve
    narrator "Dressed in a simple apron, she exudes an air of motherly warmth, yet her eyes, those piercing orbs, seem devoid of life, as if they hold secrets untold."
    
    menu:
        "GREET HER.":
            hide mrs_kitten
            show player
            player "Madam, I seek shelter for the night. Would you be willing to offer me a place to rest?"
            jump greetings

label greetings:

    hide player
    show mrs_kitten
    narrator "For a moment, she simply stares at you, her expression inscrutable."
    narrator "Then, as if waking from a trance, a smile spreads across her face, transforming her countenance into one of genuine warmth."
    mrs_kitten "Why, of course, dear traveler. Welcome to my humble abode. I am Mrs. Kitten. Please, come in, and make yourself at home."

    hide mrs_kitten
    show player
    narrator "You step across the threshold, feeling Mrs. Kitten's gaze lingering on you, her eyes like twin lanterns in the dimness of the cottage."
    narrator "The weight of your sack of gold feels heavier under her scrutiny, and you shift feet, suddenly conscious of your disheveled appearance."

    menu:
        "TELL HER YOU'RE A MERCENARY.":
            player "The duke put a bounty on another petty thief's head. I tracked and cut him down in less than a day. I don't know which I enjoy more: the sport or the handsome reward."
            hide player
            show mrs_kitten
            narrator "Mrs. Kitten's eyes flare as she bares her teeth and hisses at you."
            mrs_kitten "What know you of bloodshed? And what did you do with the meat?"
            mrs_kitten "How dare you waste fresh meat! You ought to repay what you've stolen from me!"
            hide mrs_kitten
            narrator "Your hunger and exhaustion clouds your instincts, and Mrs. Kitten manages to overtake you. You'll make a delicious tomcat stew."
            jump end

        "LIE.":
            player "Mine own missus sent me out to the market this morning."
            player "Evidently, the weather has not favored me. I much prefer handling our cattle, while she sells our crops."
            hide player
            show mrs_kitten
            mrs_kitten "Oh! What do you grow? Do you have anything leftover in that sack of yours? I ought to see — I was about to start dinner!"
            jump peeking_inside

#scene change =====================


label peeking_inside:

    # Set background
    hide mrs_kitten
    scene bg living room with fade
    
    show player with dissolve
    
    narrator "You follow her further into the cottage, your senses assaulted by the stark contrast between the outward appearance of Mrs. Kitten and the state of her home."
    narrator "Despite her groomed look, the interior of the cottage is a scene of disarray."
    narrator "Broken furniture litters the room, dirt coats every surface, and the walls are marred by patches of mold."
    narrator "An uneasy feeling settles in the pit of your stomach as you realize that things are not as they seem in this superficially idyllic abode."

    menu:
        "STAY ON HIGH ALERT. WHAT IS THIS PLACE...?" :
            narrator "Despite Mrs. Kitten's seemingly kind demeanor, you can't shake off the feeling of unease."
            narrator "You decide to stay on high alert and follow her cautiously as she leads you to your room."
            jump suspicious_route

        "RELAX. YOUR HOSTESS IS BUT A KITTEN.":
            narrator "You decide to trust Mrs. Kitten's kind demeanor and follow her into the kitchen."
            jump relax_route


# STAY ON HIGH ALERT =====================================

label suspicious_route:
    
    hide player
    narrator "The journey through the dimly lit corridors only heightens your suspicions, every creak of the floorboards sending a shiver down your spine."

    # Set background
    scene bg players bedroom with fade

    show player with dissolve
    narrator "You enter the room she gestures towards, keeping your senses sharp."
    player "I..."
    narrator "The room reeks of decay. You fight the grimace forming on your face."
    narrator "At this point, you're curious. Any other 'traveler' would have been far gone by now. Perhaps you should explore this eerie place."
    player "Well... Thank you for your hospitality, madam. This, uh... I am grateful for the warmth."
    hide player
    show mrs_kitten
    mrs_kitten "Of course, dear. Rest a bit, and I will prepare you a bowl of stew."
    hide mrs_kitten with dissolve
    narrator "Mrs. Kitten hurries out of your room."
    jump to_be_cont
 

# RELAX ======================================================

label relax_route:

    hide player
    scene bg kitchen with fade
    
    show mrs_kitten with dissolve
    narrator "Rushing into the kitchen, Mrs. Kitten begins to busy herself around the kitchen, preparing a simple but hearty meal. The aroma of stew fills the air, making your stomach growl in anticipation."

    hide mrs_kitten
    show player
    narrator "Her kitchen, much like the living room, was filthy. It looks as if a violent brawl had taken place here, with shards of glass shattered across the floor and a mess of a rotting meal spilled over the dining table."
    narrator "But at the end of the day, who are you to judge? Your hunger overpowers any sense of caution you may have."
    player "Thank you kindly for your hospitality, madam. I imagine your husband is a lucky man."
    hide player
    show mrs_kitten
    narrator "With her back turned to you, you catch Mrs. Kitten stiffen ever so slightly, her ears perking up."
    narrator "Just as quickly as you caught her, Mrs. Kitten recovers and continues preparing your dinner."
    mrs_kitten "Think nothing of it, dear traveler. It's the least I can do for someone who's been on the road for so long."
    narrator "Soon thereafter, Mrs. Kitten approaches you with a bowl of murky, blackened liquid."
    jump to_be_cont


#===========================
label to_be_cont:

    hide mrs_kitten
    scene black with fade
    narrator "END OF DEMO. GRADE THIS PROJECT AN 'A' TO UNCOVER MRS. KITTEN'S SECRETS."

# End of story=========================================================================
label end:

    scene black with fade
    narrator "GAME OVER."