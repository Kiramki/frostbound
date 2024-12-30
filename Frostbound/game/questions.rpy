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
    crew "Sorry, miss. It's just... I don't usually get the chance to talk to lasses while I'm on duty."
    crew "Apologies if I've given offense, miss. It's not you."
    
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
    narrate "The crew member hesitates. He shifts uncomfortably."
    # play lie sound
    crew "{b}I've taken over his duties for the day, miss. It's just the usual shift rotation.{/b}"
    crew "No need to worry. He's just fine."
    cadence "What? That doesn't make any sense."
    cadence "The same person has been delivering my meals every day until now. Why the sudden change?"

    ## SLAM

    crew "Enough!"
    narrate "He answers with uncharacteristic anger. I blink at him, startled."
    narrate "He looks down at his feet and runs a shaky hand through his hair, taking a deep breath."
    crew "I'm sorry, miss. I'd rather not say - got work to do, you know."

    $ questions_asked += 1
    $ crew_q2_asked = 1
    if questions_asked < 2:
        jump crew_questions
    else:
        jump crew_questions_end


label crew_questions_3:
    cadence "Something's happened to the captain, hasn't it?"
    narrate "The crew member startles, his eyes widening."
    crew "How-"
    
    ## lie
    crew "{b}No, miss. The captain's-{/b}"
    cadence "The captain always made his own quips on the intercom each day, some silly joke or another."
    cadence "Now, all of his announcements have been pre-recorded, ever since the blizzard started. Or, at least, completely absent of his usual charm."
    cadence "What's going on?"
    narrate "The crew member shifts uncomfortably on his feet, glancing once again at the corridor behind me."
    crew "It's been a rough spell for the ship, miss. The captain's been... occupied with matters."
    crew "That's about all I can say, miss. With all due respect, it would be best to leave this to the crew."
    play sound "audio/banging.mp3"
    man "Hey, bastard! Don't think I can't hear you through these walls!"
    man "I demand a refund, do you hear me!? This is unacceptable!"
    narrate "The angry voice of one of my neighbors comes through the wall, muffled but clear."
    crew "I really ought to get back to my duties now, miss."

    $ questions_asked += 1
    $ crew_q3_asked = 1
    if questions_asked < 2:
        jump crew_questions
    else:
        jump crew_questions_end

label crew_questions_4:
    cadence "What's the real reason we're locked in here?"
    narrate "The crew member stiffens."

    crew "We told ya: it's the weather. Not safe to be out in it, miss. Please step aside, yeah?"
    ## lyink
    crew "{b}We ain't locking nobody in here, Miss. You're our passenger, it's just a temporary thing.{/b}"

    play sound "audio/banging.mp3"
    man "You're full of shit!! All of you!"
    narrate "The angry voice of my neighbor comes through the wall, muffled but clear."
    man "Three days — {i}THREE DAYS{/i} — you've kept us locked in our rooms like animals! What kind of treatment is this!? This is outrageous!"

    narrate "For a moment, the crew member looks incredibly tired. I feel a little bad."
    crew "That's all I can say, miss. With all due respect, kindly step away from the door."

    $ questions_asked += 1
    $ crew_q4_asked = 1
    if questions_asked < 2:
        jump crew_questions
    else:
        jump crew_questions_end