# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define cadence = Character("Cadence")
define narrate = Character(None)
define intercom = Character("Intercom")
define crew = Character("Crew Member")
define man = Character("Man")
define woman = Character("Woman")
define stranger = Character("???")


# The game starts here.

label start:

    # Warning message with a black screen. Play howling wind noise - on loop?
    scene black

    ## play music "howling wind lol"
    narrate "{i}A word of warning to those who embark on this journey:{/i}"
    narrate "{i}Within this tale, you may encounter unsettling scenes, including themes of death, murder, and other forms of distress. The story you are about to experience is not for the faint of heart.{/i}"
    narrate "{i}Proceed with caution, for once you step further, there is no turning back.{/i}"
    narrate "Do you understand?"
    menu:
        narrate "Do you understand?"
        "Yes.":
            jump introduction
            
label introduction:
    #[INTERCOM MOMENT]

    ## play sound "static"
    narrate "{i}The crackling sound of an intercom coming to life fills the room.{/i}"
    intercom "Attention all passengers! This is your captain speaking."
    intercom "Due to continued severe weather conditions, our cruise will be delayed for another day."
    intercom "Remain in your rooms. We'll be back on course just as soon as the weather clears."
    intercom "Thank you for your patience."
    narrate "{i}Click...{/i}"

    scene cadence_room_bed
    with Dissolve(1)

    pause(1)

    cadence "Hm..."
    narrate "I sit cross-legged on the narrow bed of my cabin, scribbling a quick tally in my journal."
    cadence "Another pre-recorded announcement, is it?"

    play music "audio/hope_chords.mp3"

    ## zoom in on the window of cadence_room_bed.png
    narrate "The luxury of first class on a cargo ship grants me one of the few cabins with a window."
    narrate "It's useless now, though. Frost creeps up the sides of my window, and everything outside is a blur of white. I can't see a thing."
    narrate "I boarded this ship a week ago, courtesy of my father. It was a gift for finishing women's boarding school."
    narrate "He's probably not too pleased with me right now. I've been stuck in this cabin for days - I've barely seen a soul outside of the crew providing room service."

    ## knock knock
    crew "Room service!"
    narrate "Speak of the devil."
    cadence "Come in!"

    ## play sound "door opening"
    scene cadence_room_main
    with Dissolve(1)

    narrate "The door creaks open, and a crew member steps inside with a tray of food."
    narrate "It's not the usual crew member who delivers my meals. I don't recognize him."
    crew "Good morning, Miss Cadence."
    crew "Today's breakfast is eggs, bacon, and toast. Got some coffee too, if you'd like."


    menu:
        "Is the captain doing alright?":
            jump rs_captain

        "How much longer until we can leave our rooms?":
            jump rs_leave

        "Thank you.":
            jump rs_thankyou

label rs_captain:

    cadence "Is the captain doing alright?"
    narrate "It's been a while since I've heard anything from the captain that wasn't pre-recorded. Just what is going on out there?"
    narrate "The crew member stiffens, his eyes darting to the door."
    ## play sound "lie"
    crew "{b}Captain's keeping busy, but he's managing just fine. No need to worry, miss.{/b}"
    crew "Just hang tight 'til the weather clears, alright? Won't be long now."

    jump crew_leaving

label rs_leave:
    
    cadence "How much longer until we can leave our rooms?"
    narrate "I'm going to lose my mind if I have to stay in this room for another day without any answers."
    crew "Just a bit longer 'til the weather clears up, miss. Ain't safe for you lot out in that cold."
    narrate "He offers me a polite smile."
    ## lie moment
    crew "{b}No need to fret, miss. The captain's got it all in hand. You're in good company.{/b}"
    crew "We'll be back on course soon enough. Just hang tight, alright?"

    jump crew_leaving

label rs_thankyou:

    cadence "Thank you. I'd love some coffee."
    narrate "The crew member nods, adding a cup of coffee to the tray."

    jump crew_leaving


label crew_leaving:

    narrate "The crew member walks to the table in my room and sets the tray down. His steps are hurried - he's eager to leave."
    crew "If you need anything else, just give us a call. Enjoy your breakfast."

    cadence "Ah - wait!"
    narrate "I jump up from my bed, hurrying to the door. I plant myself in front of it, blocking his exit."
    narrate "The crew member startles - bad. His arm knocks against the tray, and coffee spills onto my toast."
    narrate "It would have spilled onto the floor too, if he hadn't hurried to catch it."
    cadence "Oh, I do beg your pardon. It's just..."

    cadence "I have a few questions. If you could spare a moment, that would be most appreciated."
    crew "Apologies, miss, but I've got to get back to my duties now."
    crew "Plenty of work to do, you know. Other passengers to attend to."
    narrate "His eyes dart nervously to the corridor behind me."

    narrate "I need answers - if he leaves now, I'll be stuck in this room for another day with nothing to do but twiddle my thumbs."
    cadence "Please, just for a moment. I promise I won't keep you long."
    narrate "He's really busy, I realize. I'll probably only have time to ask a couple questions before he really has to go."

    $ questions_asked = 0
    $ crew_q1_asked = 0
    $ crew_q2_asked = 0
    $ crew_q3_asked = 0
    $ crew_q4_asked = 0

    jump crew_questions

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
    
    ## play banging
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
    crew "I've taken over his duties for the day, miss. It's just the usual shift rotation."
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
    crew "No, miss. The captain's-"
    cadence "The captain always made his own quips on the intercom each day, some silly joke or another."
    cadence "Now, all of his announcements have been pre-recorded, ever since the blizzard started. Or, at least, completely absent of his usual charm."
    cadence "What's going on?"
    narrate "The crew member shifts uncomfortably on his feet, glancing once again at the corridor behind me."
    crew "It's been a rough spell for the ship, miss. The captain's been... occupied with matters."
    crew "That's about all I can say, miss. With all due respect, it would be best to leave this to the crew."

    ## BANG BANG

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

    ##BANGBANG
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

label crew_questions_end:
    menu:
        narrate "The crew member looks a step away from simply shoving me aside and bolting out the door."
        "Wait! Just one more question, please.":
            jump crew_questions_end2

label crew_questions_end2:
    cadence "This doesn't add up, and you know it. Could you at least tell me what's really going on?"

    narrate "I take a step closer to him. He visibly cowers, making me pause."
    crew "I... I don't know! Just — please, step back!"
    narrate "He puts his head in his hands and starts tugging at his hair, taking deep breaths and muttering to himself."
    cadence "Oh my."

    narrate "It seems like I've pushed him too far. Father won't be pleased to hear I've already caused trouble on the trip that he so generously funded for me."
    narrate "If this keeps up, I'll need to find a way to make up for playing detective — again."

    cadence "Excuse me... are you alright?"

    narrate "I try to soften my words, reaching out in an attempt to comfort him."
    narrate "My fingers brush against his arm."

    ## SLAM
    ## SHAKE
    ## AUGHGHGHGHGHGH
    crew "{i}DON'T TOUCH ME!{/i}"
    narrate "With startling force - likely more than he intended to use - he shoves me aside. My body hits the wall, breath knocked out of me."

    ## lock click
    narrate "The door locks with a sharp click as he bolts, his footsteps retreating frantically down the corridor."
    narrate "My neighbors are not amused."

    woman "Excuse me! You forgot our food! Oh, dear god, my baby needs food - she's starving! Please, we need it now!"
    man "Those bastards! I'm kicking down this door! I'M KICKING DOWN THIS DOOR, YOU HEAR ME?!"

    stranger "Will you all shut up?! The doors are metal, ain't no way we're gettin' out 'less someone unlocks 'em for us."

    narrate "... Is that all we can do? Just wait for the blizzard to pass?"
    narrate "I glance at my ruined meal. The coffee has soaked into the toast, making it inedible."
    narrate "I push the tray aside, my appetite gone."

    return
