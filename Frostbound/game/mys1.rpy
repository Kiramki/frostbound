default recent_menu = None

label hallway_start:
    stop music fadeout 1
    scene black
    with Dissolve(1)
    cadence "!!"

    scene main_deck_hall
    with Dissolve(1.5)

    play music "audio/main_theme.mp3"
    narrate "I'm hit with a burst of cold air that makes my body recoil like a startled housecat."
    cadence "What in the world happened here?"
    narrate "Frost clings to the walls, weaving icy spiderwebs over gaslit fixtures."
    narrate "This hallway was all but spotless three days ago - now, it looks like the blizzard moved in and redecorated."

    play sound "audio/door_shut.mp3"
    narrate "I pull the door shut behind me, cutting off the light from my cabin."
    narrate "There will be consequences if I'm caught sneaking around like this."

    menu note_intersection:
        "Move left, past the other cabin doors":
            jump note_1

        "Move right, towards the upper deck gate":
            jump sneak_1

        "Give up and return to my cabin":
            jump give_up

label give_up:
    narrate "Nope. Nope nope nope. I'm not doing this."
    narrate "It's cold out here, and this was a stupid idea. I'm going back to my cabin."
    narrate "I turn on my heel and head back to my room, the door shutting behind me with a satisfying click."
    play sound "audio/door_shut.mp3"

    scene black
    with Dissolve(1)

    narrate "I waste no time in getting back into bed, pulling the covers up to my chin."
    jump bad_end_1

label note_1:
    play sound "audio/footsteps_soft.mp3"
    scene main_deck_left
    narrate "I move left, past the other cabin doors."
    narrate "I cautiously count the doors under my breath."
    stop music
    narrate "Wait."
    narrate "A looming figure flickers at the of the corridor holding a lantern. The watchman."
    play music "intense_theme.mp3"
    narrate "I can sense him coming closer, if he catches sight of me it's over."
    play sound "audio/footsteps_near.mp3"
    narrate "I hasten my steps. Hopefully my memory doesn't fail me here, this may be my only chance."
    narrate "Which door did S tell me to go through?"

    menu door_1:
        "Fifth door":
            jump note_1_5

        "Sixth door":
            jump note_1_6

        "Fourth door":
            jump note_1_4
    
label note_1_4:
    narrate "I try the fourth door, my fingers trembling as I twist the knob."
    play sound "audio/door_rattle.mp3"
    narrate "Nothing. The door doesn't budge."
    narrate "I hear a voice from inside."
    stranger "Who's there?"
    stranger "Go away! I'm trying to sleep!"
    stranger "I'll call the watchman if you don't leave me alone!"
    narrate "I quickly back away from the door, my heart pounding. Then-"
    stop music
    play sound "audio/slam.mp3"
    show main_deck_left with vpunch
    watchman "Hey!"
    narrate "A rough hand grabs my arm, yanking me backward. The sudden light of a lantern blinds me."
    watchman "What are you doing out of your room? You're not supposed to be here."
    narrate "I try to explain, but come up short. The watchman drags me back to my room."
    scene black
    with Dissolve(1)
    narrate "I hear the door lock behind me. I'm not going anywhere tonight."
    narrate "With nothing left to do, I crawl back into bed and pull the covers up to my chin."

    jump bad_end_1

label note_1_5:
    narrate "I try the fifth door, my fingers trembling as I twist the knob."
    play sound "audio/door_open.mp3"
    narrate "The door creaks open, revealing a dark room. Thank god."
    narrate "I slip inside, pulling the door shut just as the beam of the lantern sweeps by."
    play sound "audio/door_shut.mp3"
    scene black
    with Dissolve(1)
    narrate "I press my ear against the door, holding my breath."
    watchman "... must've been a flicker... probably nothing..."
    narrate "The light from his lantern sweeps faintly under the door before it recedes again."
    narrate "I let out a sigh of relief, my heart pounding in my chest. I rest my forehead against the door for a moment."
    narrate "The air is colder here, stabbing through my clothes like a thousand tiny needles."
    play sound "audio/footsteps_soft.mp3"
    narrate "I descend."
    jump sera_stairs

label note_1_6:
    narrate "I try the sixth door, my fingers trembling as I twist the knob."
    play sound "audio/door_rattle.mp3"
    narrate "Nothing. The door doesn't budge."
    play sound "audio/door_rattle.mp3"
    narrate "I try again, but the knob refuses to turn."
    stop music
    play sound "audio/slam.mp3"
    show main_deck_left with vpunch
    watchman "Hey!"
    narrate "A rough hand grabs my arm, yanking me backward. The sudden light of a lantern blinds me."
    watchman "What are you doing out of your room? You're not supposed to be here."
    narrate "I try to explain, but come up short. The watchman drags me back to my room."

    scene black
    with Dissolve(1)
    play sound "audio/door_shut.mp3"
    narrate "I hear the door lock behind me. I'm not going anywhere tonight."
    narrate "With nothing left to do, I crawl back into bed and pull the covers up to my chin."

    jump bad_end_1

label sneak_1:
    play sound "audio/footsteps_soft.mp3"
    narrate "I move right, towards the upper deck gate."

    scene main_deck_right
    with Dissolve(1)
    narrate "I hear the murmur of two watchmen. My heart jumps to my throat, but it doesn't seem like they've heard me."
    narrate "Holding my breath, I risk a glance into the room they're occupying."
    play music "audio/emotional_theme.mp3"
    scene main_deck_cg
    with Dissolve(1)
    narrate "For a moment, it feels like I've glimpsed something I wasn't meant to see. They seem... weary."
    watchman1 "Shit, man... I didn't dress for this weather."
    watchman2 "None of us did. Who dresses for a blizzard in the middle of the damn summer?"
    narrate "One of them takes a swig from something that seems suspiciously distinct from water."
    scene main_deck_right
    with Dissolve(1)
    narrate "If I can get past them, I'll be able to get to the upper gate - whatever might be over there. Assuming that it isn't locked."

    $ looked_around = 0

    menu sneak_menu:
        "Look around first" if looked_around == 0:
            jump sneak_1_look

        "Try to distract them":
            jump sneak_1_distract

        "Make a break for the stairs":
            jump sneak_1_door

        "Keep listening":
            jump sneak_1_eavesdrop

label sneak_1_look:
    narrate "My eyes have been slowly adjusting to the dim light. I squint, looking around."
    narrate "(this is a part where i might describe my surroundings)"
    narrate "When I look closely, I spot a key on the gate."
    narrate "That's not the key {i}to{/i} the gate, is it? That's... not a good security measure."
    $ looked_around = 1
    jump sneak_menu

label sneak_1_distract:
    narrate "sh"

label sneak_1_stairs:
    narrate "shhhhhh"

label sneak_1_eavesdrop:
    scene main_deck_cg
    with Dissolve(1)
    narrate "They seem engaged in their conversation. Perhaps I'll learn something about the state of the ship."
    watchman1 "Seen Mouse lately? Kid's been missing since breakfast."
    narrate "Mouse... is that the same crew member who replaced my steward this morning? I lean in a bit closer."
    watchman2 "Probably hiding somewhere like he always does. Don't understand how he made it this far."
    watchman1 "Hey, go easy on the kid. He's had a rough couple of days."
    narrate "The other man laughs and looks out at the snowy wasteland."
    watchman2 "Rough? Everyone here's had it rough, but that kid... he cracks under the smallest pressure."
    narrate "The words are harsh, but there is an edge to it that betrays a deeper weariness."
    narrate "..."
    watchman1 "You alright?"
    narrate "A sigh."
    watchman2 "Fine. Just damn this cold. You?"
    watchman1 "Could be worse... Listen, about last night..."
    watchman2 "Not here. Later, alright?"
    play sound "audio/clue.mp3"
    narrate "{color=#49D5FF}Clue Added: Sometime after breakfast—where I may have scared him off—the crew member, Mouse, vanished. It seems he's had a rough few days. {/color}"




label sera_stairs:
    scene stowaway_entrance
    with Dissolve(1)
    narrate "yo this is a problem for later me"