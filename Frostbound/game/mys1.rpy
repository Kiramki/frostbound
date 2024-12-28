default recent_menu = None

label hallway_start:
    stop music fadeout 1
    scene black
    with Dissolve(1)

    narrate "The door creaks as I carefully push it ajar..."
    cadence "!!"

    scene main_deck_hall
    with Dissolve(1.5)

    play music "audio/hope_in_the_cold.mp3"

    narrate "I'm hit with a burst of cold air that makes my body recoil like a startled housecat."
    narrate "My breath clouds the air almost immediately. Frost clings to the walls, weaving icy spiderwebs over gaslit fixtures."
    narrate "I had thought that my room was cold - but this corridor is a different kind of chill."

    cadence "What in the world happened here?"
    narrate "This hallway was all but spotless three days ago - now, it's like a blizzard moved in and redecorated."

    ## play door shutting sound
    narrate "I pull the door shut behind me, cutting off the light from my cabin."
    narrate "The empty corridor beckons before me like a headmaster's door left ajar— there will be consequences if I'm caught sneaking around like this."
    narrate "The note I hid in my pocket is crumpled, but the words are still clear - if I feel the need to check it again."

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

    scene black
    with Dissolve(1)

    narrate "I waste no time in getting back into bed, pulling the covers up to my chin."
    jump bad_end_1

label note_1:
    scene main_deck_left
    narrate "I move left, past the other cabin doors."
    narrate "I cautiously count the doors under my breath."
    narrate "A looming figure appears at the other end of the corridor holding a lantern. I need to hurry."
    narrate "Which door is it?"

    menu door_1:
        "Fifth door":
            jump note_1_5

        "Sixth door":
            jump note_1_6

        "Fourth door":
            jump note_1_4
    
label note_1_4:
    narrate "I try the fourth door, my fingers trembling as I twist the knob."
    narrate "I hear a voice from inside."
    stranger "Who's there?"
    stranger "Go away! I'm trying to sleep!"
    stranger "I'll call the watchman if you don't leave me alone!"
    narrate "I quickly back away from the door, my heart pounding. Then-"
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
    narrate "The door creaks open, revealing a dark room. Thank god."
    narrate "I slip inside, pulling the door shut just as the beam of the lantern sweeps by."
    narrate "I press my ear against the door, holding my breath. I can hear the watchman mutter something before he moves on."
    watchman "... must've been a flicker... probably nothing..."
    narrate "The light from his lantern sweeps faintly under the door before it recedes again."
    narrate "I let out a sigh of relief, my heart pounding in my chest. I rest my forehead against the door for a moment."
    narrate "The air is colder here, stabbing through my clothes like a thousand tiny needles."
    narrate "I scan the room until I find the hidden staircase mentioned in the note."
    narrate "I descend."

    jump sera_stairs

label note_1_6:
    narrate "I try the sixth door, my fingers trembling as I twist the knob."
    narrate "Nothing. The door doesn't budge."
    narrate "I try again, but the knob refuses to turn."
    watchman "Hey!"
    narrate "A rough hand grabs my arm, yanking me backward. The sudden light of a lantern blinds me."
    watchman "What are you doing out of your room? You're not supposed to be here."
    narrate "I try to explain, but come up short. The watchman drags me back to my room."

    scene black
    with Dissolve(1)
    narrate "I hear the door lock behind me. I'm not going anywhere tonight."
    narrate "With nothing left to do, I crawl back into bed and pull the covers up to my chin."

    jump bad_end_1

label sneak_1:
    narrate "I move right, towards the upper deck gate."

    scene main_deck_right
    with Dissolve(1)
    narrate "I hear the conversation of two watchmen - I startle, but they haven't seen me yet."
    watchman1 "Shit, man... I didn't dress for this weather."
    watchman2 "None of us did. Who dresses for a blizzard in the middle of the damn summer?"
    narrate "It looks like they're taking a break. When I look, they seem weary."
    narrate "One of them takes a swig from something that seems suspiciously distinct from water."
    narrate "If I can get past them, I'll be able to get to the upper gate - whatever might be over there. Assuming that it isn't locked."

    $ looked_around = 0

    menu sneak_menu:
        "Look around first" if looked_around == 0:
            jump sneak_1_look

        "Try to distract them":
            jump sneak_1_distract

        "Go straight for the door":
            jump sneak_1_door

        "Keep listening":
            jump sneak_1_eavesdrop

label sneak_1_look:
    narrate "My eyes have been slowly adjusting to the dim light. I squint, looking around."
    narrate "(this is a part where i might describe my surroundings)"
    narrate "When I look closely, I spot a key on the gate."
    narrate "That's not the key to the gate, is it? That's... not a good security measure."
    $ looked_around = 1
    jump sneak_menu

label sneak_1_distract:
    narrate "sh"

label sneak_1_door:
    narrate "shhhhhh"

label sneak_1_eavesdrop:
    narrate "shshshshshhhhh"


label sera_stairs:
    narrate "yo this is a problem for later me"