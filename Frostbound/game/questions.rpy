label crew_questions:
    if questions_asked == 0:
        menu:
            narrate "The crew member shifts on his feet, glancing at the door."

            "You're afraid of me. Why?":
                jump crew_questions_1

            "Where's the other person who brings our food?":
                jump crew_questions_2

            "Something's happened to the captain, hasn't it?":
                jump crew_questions_3

            "What's the real reason we're locked in here?":
                jump crew_questions_4

    if questions_asked == 1:
        menu:
            narrate "The crew member looks increasingly uncomfortable. He's clearly eager to leave."

            "You're afraid of me. Why?" if crew_q1_asked < 1:
                jump crew_questions_1

            "Where's the other person who brings our food?" if crew_q2_asked < 1:
                jump crew_questions_2

            "Something's happened to the captain, hasn't it?" if crew_q3_asked < 1:
                jump crew_questions_3

            "What's the real reason we're locked in here?" if crew_q4_asked < 1:
                jump crew_questions_4

label crew_questions_1:
    
    cadence "You're afraid of me. Why?"
    narrate "The crew member's eyes widen, and he laughs nervously."
    crew "Sorry, Miss. It's just... I don't usually get the chance to talk to lasses while I'm on duty."
    cadence "That doesn't answer my question."
    narrate "He shifts uncomfortably, his face reddening, but he presses on."
    crew "Apologies if I've given offense. Truly, it's not you."
    narrate "His earnest tone catches me off guard. It's not fear, exactly, but something else I can't quite place."
    
    play sound "audio/banging.mp3"
    narrate "The sound of banging on the wall startles us both. It's coming from the room next door."
    woman "Excuse me! Is that a crew member?"
    woman "Please, my child is suffering dreadfully from motion sickness! She's so pale, she can barely sit up!"
    woman "She needs fresh air - just let us out for a moment, please!"
    narrate "The frantic voice of my neighbor comes through the wall, muffled but clear."
    crew "I best be getting back to my duties now. If you'd kindly step aside."

    $ questions_asked += 1
    $ crew_q1_asked = 1
    if questions_asked < 2:
        jump crew_questions
    else:
        jump crew_questions_end


label crew_questions_2:
    
    cadence "Where's the other person who brings our food?"
    narrate "I rather liked my steward. He had this windswept look about him, and always wore a smile."
    narrate "For a split second, something dangerous flashes behind the crew member's eyes."
    play sound "audio/lying.wav"
    crew "{b}I've taken over his duties for the day, miss. It's just the usual shift rotation.{/b}"
    menu:
        "PRESS":
            jump crew_questions_2_press
        "Let it go":
            $ questions_asked += 1
            $ crew_q2_asked = 1
            if questions_asked < 2:
                jump crew_questions
            else:
                jump crew_questions_end

label crew_questions_2_press:
    play sound "audio/press.wav"
    cadence "But the same steward has been delivering my meals until today. {b}Why the sudden change?{/b}"
    narrate "A muscle in his jaw twitches. He's uncomfortable with this line of questioning."
    crew "He ain't on duty today, Miss. Looks like you'll have to put up with me. Sorry to disappoint."
    cadence "I see. Do crew members get to choose to be off duty? Or is it decided for them?"
    narrate "His expression is replaced with something unreadable."
    crew "I wouldn't know."
    cadence "But you said you're taking over for him. Surely you were told why."
    play sound "audio/slam.mp3"
    show cadence_room_main with vpunch
    crew "That's enough! I'm done talking about him, alright?"
    narrate "His voice cracks with barely controlled anger. I recoil slightly, startled by the force of it."
    narrate "He takes a sharp breath, looking almost ashamed of himself, and runs a hand through his hair."
    crew "I'm sorry, miss. I'd rather not say. Just... please, don't ask about him again."
    play sound "audio/clue.mp3"
    narrate "{color=#49D5FF}Clue Added: The steward's unexpected absence, along with the crew's reluctance to discuss him, may be linked to the ship's current state.{/color}"
    $ questions_asked += 1
    $ crew_q2_asked = 1
    if questions_asked < 2:
        jump crew_questions
    else:
        jump crew_questions_end



label crew_questions_3:
    cadence "Something's happened to the captain, hasn't it?"
    narrate "The crew member startles, his eyes widening."
    crew "How... how do you mean, Miss?"
    cadence "The prerecorded announcements, the hushed reactions when his name comes up... it doesn't add up. What's really going on?"
    narrate "He shifts on his feet, glancing over his shoulder like he expects someone to be listening."
    play sound "audio/lying.wav"
    crew "It's been a rough spell for the ship, Miss. The captain's been... {b}tied up with other matters.{/b}"
    menu:
        "PRESS":
            jump crew_questions_3_press
        "Let it go":
            jump crew_questions_3_letgo
        



label crew_questions_3_letgo:
    narrate "I nod sagely and let the matter drop."
    narrate "He seems adamant about not sharing the captain's current state. But why?"
    play sound "audio/banging.mp3"
    man "Hey, bastard! Don't think I can't hear you through these walls!"
    man "I demand a refund, do you hear me!? This is unacceptable!"
    narrate "The angry voice of one of my neighbors comes through the wall, muffled but clear."
    crew "That's about all I can say, Miss. With all due respect, it would be best to leave this to the crew."

    $ questions_asked += 1
    $ crew_q3_asked = 1
    if questions_asked < 2:
        jump crew_questions
    else:
        jump crew_questions_end

label crew_questions_3_press:
    play sound "audio/press.wav"
    cadence "{b}Tied up{/b} with what, exactly?"
    narrate "His jaw tightens, and he rubs the back of his neck."
    play sound "audio/lying.wav"
    crew "{b}Ship's upkeep. Been workin' with the engineers. That's all I know, miss.{/b}"
    narrate "He seems adamant about keeping the captain's current state a secret from me. But why?"
    play sound "audio/banging.mp3"
    man "Hey, bastard! Don't think I can't hear you through these walls!"
    man "I demand a refund, do you hear me!? This is unacceptable!"
    narrate "The angry voice of one of my neighbors comes through the wall, muffled but clear."
    crew "That's about all I can say, Miss. With all due respect, it would be best to leave this to the crew."

    $ questions_asked += 1
    $ crew_q3_asked = 1
    if questions_asked < 2:
        jump crew_questions
    else:
        jump crew_questions_end


label crew_questions_4:
    cadence "What's the real reason we're locked in here?"
    narrate "The crew member stiffens as if he were bracing for a pitch."
    crew "It's as the captain says. It's not safe for you all to be out with the storm, Miss. Please step aside, yeah?"
    narrate "His face betrays some emotion. Guilt? I press him harder."
    cadence "The weather? You expect me to believe this storm requires locking passengers in their rooms?"
    cadence "If news gets out about this, the entire crew could land themselves in serious trouble."
    narrate "His eyes widen and for a moment, it looks like he's about to say something, but then he swallows it down."
    play sound "audio/lying.wav"
    crew "{b}We ain't locking nobody in here, Miss.{/b} You're our passenger, we're doing what's best for everyone."
    play sound "audio/banging.mp3"
    man "You're full of shit!! All of you!"
    narrate "The angry voice of my neighbor filters through the wall, abruptly cutting off our conversation."
    man "Three days — {i}THREE DAYS{/i} — you've kept us locked in our rooms like animals! What kind of treatment is this!? This is outrageous!"

    narrate "For a moment, the crew member looks incredibly tired. I feel a little bad."
    crew "That's all I can say, Miss. With all due respect, kindly step away from the door."

    $ questions_asked += 1
    $ crew_q4_asked = 1
    if questions_asked < 2:
        jump crew_questions
    else:
        jump crew_questions_end