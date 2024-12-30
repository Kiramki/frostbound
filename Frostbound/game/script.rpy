# The script of the game goes in this file.

# Python initialization
init python:
    import clues # Import the clues module
    selected_clue = None # Create a variable to store the selected clue

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define cadence = Character("Cadence")
define narrate = Character(None)
define intercom = Character("Intercom")
define crew = Character("Crew Member")
define man = Character("Man")
define woman = Character("Woman")
define stranger = Character("???")
define watchman1= Character("Watchman 1")
define watchman2= Character("Watchman 2")
define watchman = Character("Watchman")

default looked_around = 0
default watchman_eavesdrop = 0
default player_clues = {}


# The game starts here.

label start:

    # Warning message with a black screen. Play howling wind noise - on loop?
    scene black
    play music "audio/ocean_sounds.wav" fadeout 1.0 fadein 1.0
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

    play music "audio/film_static.wav" fadein 1.0

    # Enable clues.
    show screen clue_button

    narrate "{i}The crackling sound of an intercom coming to life fills the room.{/i}"
    intercom "Attention all passengers! This is your captain speaking."
    intercom "Due to continued severe weather conditions, our cruise will be delayed for another day."
    intercom "Remain in your rooms. We'll be back on course just as soon as the weather clears."
    intercom "Thank you for your patience."
    play sound "audio/intercom_click.wav"
    stop music
    narrate "{i}Click...{/i}"

    scene cadence_room_bed
    with Dissolve(1)

    pause(1)
    play music "audio/hope_chords.mp3" fadein 1.0
    narrate "..."
    narrate "Another prerecorded announcement."
    narrate "I flip open a new page in my journal and dip my pen into the inkpot."
    play sound "audio/writing.wav"
    narrate "{i}Cadence Daycott. Daughter of Yusri Daycott, the world-renowned detective.{/i}"
    narrate "{i}Day 3 locked in my cabin aboard the SS Nimbus. Father would be horrified to know his gift has transformed into solitary confinement.{/i}"
    narrate "{i}Each morning, the intercom blares with cheerful news, but I know better.{/i}"
    narrate "{i}The captain of this ship is already dead.{/i}"
    narrate "I blow on the fresh ink."
    narrate "Lies are easy to spot when you have spent your life around them. The most obvious ones dress in the mundane."
    narrate "Somewhere above me, the essential crew is putting on a show of monitoring the weather and preparing breakfast."
    narrate "Interacting with them feels like tightening a violin string on the verge of snapping."
    scene cadence_room_bed
    play sound "audio/door_knock.mp3"
    crew "Miss Cadence Daycott? I have your meal."
    narrate "Speak of the devil."
    play sound "audio/door_open.mp3"
    scene cadence_room_main
    with Dissolve(1)

    narrate "A crew member I don't recognize steps in, awkwardly balancing a tray of food."
    narrate "He's not my usual steward. "
    narrate "This boy can't be older than 15; he looks one wobble away from sending the expensive cutlery crashing to the floor."

    crew "Good morning, Miss Cadence."
    crew "Today's breakfast is eggs, bacon, and toast. Got some coffee too, if you'd like."
    play sound "audio/book_shut.wav"
    narrate "I snap my journal shut. A twinge of guilt settles in my stomach for what I'm about to do."
    narrate "I need information, and he's just the kind of person who will give it to me."
    narrate  "I may lack my father's skill for details, but I've learned:"
    narrate "Ask the right questions, and {b}people will reveal what I need to know on their own.{/b}"

    menu:
        "Is the captain doing alright?":
            jump rs_captain

        "How much longer until we can leave our rooms?":
            jump rs_leave

        "Thank you.":
            jump rs_thankyou

label rs_captain:

    cadence "Is the captain doing alright?"
    narrate "I test the waters, watching his reaction closely. If something's happened to the captain, he'll slip up."
    narrate "The crew member stiffens, his fingers tightening around the tray. "
    play sound "audio/lying.wav"
    crew "The captain? Uh, yeah, he's {b}up on the bridge, overseeing things. Busy as ever, y'know?{/b}"

    narrate "{color=#49D5FF}(Tutorial: Did you catch that? Cadence can sense when someone isn't being truthful. What part of his words felt off?) {/color}"
    narrate "{color=#49D5FF}(Tutorial: in moments like these Cadence can {b}PRESS{/b} for more information. Not everyone appreciates being pressed, though.) {/color}"

    menu:
        "PRESS":
            jump rs_captain_press
        "Let it go":
            jump crew_leaving

label rs_captain_press:
    play sound "audio/press.wav"
    cadence "If the captain's overseeing things, {b}why have the announcements been prerecorded{/b}? Isn't he the one who usually makes them?"
    narrate "His eyes flicker with wary recognition at the mention of the announcements. He thinks for a moment."
    crew "I don't report to him directly, Miss, so I can't help much. I'm just following orders, that's all I can say."
    narrate "His tone is clipped now, clearly eager to close the conversation."
    crew "Look, just sit tight 'til the storm blows through, alright? We're all workin' hard to keep you folks safe."
    play sound "audio/clue.mp3"

    narrate "{color=#49D5FF}Clue Added: The crew member has been reporting to someone other than the captain. {/color}"
    narrate "{color=#49D5FF}(Tutorial: you can view your clues by clicking your {b}JOURNAL{/b} in the top right corner.){/color}"

    jump crew_leaving

label rs_leave:
    cadence "How much longer until we can leave our rooms?"
    narrate "He offers me a barely perceptible smile, stiff and polite."
    crew "Just a bit longer 'til the weather clears up, Miss. Ain't safe for you lot out in that cold."
    narrate "A tight frustration coils in my stomach. The weather's not improving, and my first-class cabin feels more like a gilded cage than a sanctuary."
    cadence "Surely we can be let out for some fresh air, or even just a trip to the kitchens?"
    narrate "His smile remains with the carefulness of someone trying not to flub a performance on stage."
    crew "Apologies, Miss. You'll have to wait. We've run into some... unexpected issues on deck."
    play sound "audio/lying.wav"
    crew "{b}We'll have you all out on deck once the weather passes, and you'll be free to stretch your legs.{/b}"
    narrate "{color=#49D5FF}(Tutorial: Did you catch that? Cadence can sense when someone isn't being truthful. What part of his words felt off?) {/color}"
    narrate "{color=#49D5FF}(Tutorial: in moments like these Cadence can {b}PRESS{/b} for more information. Not everyone appreciates being pressed, though.) {/color}"
    menu:
        "PRESS":
            jump rs_leave_press
        "Let it go":
            jump crew_leaving

label rs_leave_press:
    cadence "Strange. We used to get announcements from the captain about issues, but I haven't heard anything."
    play sound "audio/press.wav"
    cadence "Is there a reason that the {b}announcements have been the same{/b} these past few days?"
    narrate "His eyes flicker with wary recognition at the mention of the announcements. His hands tighten around the silver tray."
    crew "Well.. my guess is 'cause the prerecorded ones are easier to manage for the crew."
    cadence "I see. But it seems odd. You'd think the captain would want to keep everyone in the loop?"
    narrate "His face takes on the expression of someone trying to close a book during a tense scene."
    crew "I don't report to him directly, Miss, so I can't help much. I'm just followin' orders. That's all I can say."
    crew "Just sit tight 'til the storm blows through, alright? We're all workin' hard to keep you folks safe."
    play sound "audio/clue.mp3"
    narrate "{color=#49D5FF}Clue Added: The crew member has been reporting to someone other than the captain. {/color}"
    narrate "{color=#49D5FF}(Tutorial: you can view your clues by clicking your {b}JOURNAL{/b} in the top right corner.){/color}"
    jump crew_leaving

label rs_thankyou:
    cadence "Thank you, I'd love some coffee."
    narrate "He nods and pours my coffee into a porcelain cup, handling it with all the grace of an elderly woman."
    cadence "You know, I didn't expect it aboard a ship, but the brew here is splendid."
    narrate "Something flickers across his face."
    crew "Well, that's probably because we make it fresh before servin', Miss. Can't guarantee it'll taste as good now that it's my turn."
    cadence "Oh? I didn't think coffee was part of the crew's usual duties."
    narrate "He pauses, eyes darting around briefly, before he sighs."
    crew "Yeah, we've been up to a lot... more than usual, that's for sure."
    play sound "audio/lying.wav"
    crew "But you know, we're just doing our jobs—It's worth it in the end. {b}Coffee's gotta be served, after all.{/b}"
    narrate "{color=#49D5FF}(Tutorial: Did you catch that? Cadence can sense when someone isn't being truthful. What part of his words felt off?) {/color}"
    narrate "{color=#49D5FF}(Tutorial: in moments like these Cadence can {b}PRESS{/b} for more information. Not everyone appreciates being pressed, though.) {/color}"
    menu:
        "PRESS":
            jump rs_thankyou_press
        "Let it go":
            jump crew_leaving

label rs_thankyou_press:
    cadence "You're doing an impressive job managing all of this. I'm sure the crew really appreciates someone so young stepping up—very brave of you."
    narrate "The crew member straightens up a bit at the sudden compliment."
    crew "Ah, well... thanks, Miss. Appreciate it, but I'm just keepin' things moving along. Same as the rest."
    narrate "He offers a casual shrug, but his face betrays a flush of warmth."
    play sound "audio/press.wav"
    cadence "Has the captain mentioned why {b}the announcements are prerecorded{/b}? Is that part of your duties as well?"
    narrate "At the mention of the announcements, his eyes flicker with a hint of unease, and the lightheartedness from the compliment quickly fades."
    crew "Oh, I don't know nothin' 'bout that, sorry, Miss. I get my orders from someone else. You probably know as much as I do on that."
    play sound "audio/clue.mp3"
    narrate "{color=#49D5FF}Clue Added: The crew member has been reporting to someone other than the captain. {/color}"
    narrate "{color=#49D5FF}(Tutorial: you can view your clues by clicking your {b}JOURNAL{/b} in the top right corner.){/color}"
    jump crew_leaving


label crew_leaving:

    narrate "The crew member hurries toward the table, setting the tray down with a quick, almost nervous motion. He's eager to leave."
    crew "That'll be all, Miss. Stay in your room for now. I'll bring your supper later and see to anything else you need."
    cadence "Wait—!"
    narrate "I spring from my bed, rushing to the door and standing in front of it, blocking his way."
    narrate "The crew member jumps back. His arm knocks the tray, sending coffee spilling over my toast."
    narrate "He only just manages to stop the rest of it from splashing onto the floor."
    cadence "Oh, my apologies! I didn't mean to startle you, it's just..."
    cadence "I have a few questions. If you could spare a moment."
    narrate "His gaze flicks nervously to the corridor behind me."
    crew "Apologies, miss, but I've got to get back to my duties now."
    crew "Plenty of work to do, you know. Other passengers to attend to."
    narrate " I'm not going to let him get away that easily. If he leaves, I'll be stuck in this room for who knows how long with no leads."
    cadence "Please, just for a moment. I promise I won't keep you long."
    narrate " He's clearly in a rush. I'll only have time for a few questions before he's gone."

    $ questions_asked = 0
    $ crew_q1_asked = 0
    $ crew_q2_asked = 0
    $ crew_q3_asked = 0
    $ crew_q4_asked = 0

    jump crew_questions

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
    show cadence_room_main with vpunch
    ## AUGHGHGHGHGHGH
    crew "{i}DON'T TOUCH ME!{/i}"
    narrate "With startling force - likely more than he intended to use - he shoves me aside. My body hits the wall, knocking the breath out of me."

    ## lock click
    narrate "The door locks with a sharp click as he bolts, his footsteps retreating frantically down the corridor."
    narrate "My neighbors are not amused."
    play sound "audio/banging.wav"
    woman "Excuse me! You forgot our food! Oh, dear god, my baby needs food - she's starving! Please, we need it now!"
    play sound "audio/banging.wav"
    man "Those bastards! I'm kicking down this door! I'M KICKING DOWN THIS DOOR, YOU HEAR ME?!"

    narrate "... Is that all we can do? Just wait for the blizzard to pass?"
    narrate "I glance at my ruined meal. The coffee has soaked into the toast, making it inedible."
    narrate "I push the tray aside, my appetite gone."

    menu:
        "Wait.":
            jump intro_note

label intro_note:
    narrate "I return to my bed in the corner of the room and pull out my journal once more."

    ## !!!!! ##
    narrate "{i}(WOW THIS IS A REALLY GOOD SPOT TO INCLUDE A TUTORIAL ABOUT CLUES AND GATHERING INFORMATION){/i}"
    narrate "{i}(WOW ITD BE SO COOL IF THE PEOPLE WRITING THIS IMPLEMENTED SOMETHING ABOUT THAT WOW){/i}"
    ###########

    narrate "As words fill the pages, the chaos from earlier fades, sinking to the back of my mind."
    narrate "Time passes, slipping by me as I work. When I spare a moment to glance at the clock, I find that hours have passed."
    narrate "The time for supper comes and goes. The crew member that I had scared off before doesn't come back."
    narrate "I am given my meals by someone who has no time for entertaining my questions, who doesn't even walk into my room all the way."
    narrate "By the time night falls, I'm writing in my journal just to have something to do."

    ## knock knock knock
    narrate "A knock rings through the air. I glance up, expecting to hear a crew member declare their business."
    narrate "I hear nothing."
    cadence "... Hello?"
    narrate "Nothing. I frown, setting my pen down."
    cadence "You can come in."
    narrate "Still, nothing. I rise from my bed, crossing the room to the door."
    narrate "There, I notice something that I couldn't see from my bed. A note, slid under the door. I pick it up, unfolding it."

    narrate "{i}\"I know why they're locking people in their rooms. We don't have much time left.\"{/i}"
    narrate "{i}\"When the big bell tolls at midnight and the night watch is gone, that's your chance.\"{/i}"
    narrate "{i}\"Count five doors to your left—there's a hidden staircase there.\"{/i}"
    narrate "{i}\"I'll be waiting for you at the bottom.\"{/i}"
    narrate "{i}\"Don't get caught.\"{/i}"
    narrate "{i}\"- S.\"{/i}"
    narrate "The note is written in a hasty scrawl, words aggressively scribbled out - hinting that whoever was writing it was in a rush."
    narrate "The penmanship style doesn't match that of a crew member."

    narrate "I blink at the note, reading it over again. Could it be?"
    narrate "I touch the handle of the door, attempting to turn it."
    narrate "In previous days, it had been locked - to ensure that I, and the other passengers, stayed in our rooms."
    narrate "Now, it turns easily in my hand. I hold back from opening it, glancing at the note once more."
    narrate "Who could have written this? Why did they give it to me?"

    cadence "Let's think..."
    narrate "Ultimately, I have two choices. Stay in my room, or sneak out."
    narrate "This note is obviously suspicious. Any sane person would be wary of sneaking out of their room at midnight to meet a stranger."
    narrate "I'm not familiar enough with the layout of the ship to have any idea of where these instructions would be leading me."
    narrate "It could be dangerous. A trap."
    narrate "But... it's a mystery. I'm already itching to solve it."
    narrate "Of course, I could also just try to sneak out without following the note's instructions."
    narrate "That's an option too - though I wouldn't get far, since I have no idea where I'm going, nor do I know the crew's schedule."
    
    menu:
        narrate "Sneak out, or stay in?"

        "Sneak out.":
            jump intro_sneak_out
        
        "Stay in.":
            jump intro_stay_in

label intro_stay_in:
    narrate "I've always been scolded for being reckless. Do I really need to prove them right?"
    narrate "All of this is suspicious. Father would stop at nothing to make sure I knew the depths of my idiocy if he found out about this."
    narrate "I should stay in my room. A mystery isn't worth whatever ill fate I might meet, going out to meet a stranger in the dead of night."
    scene cadence_room_bed
    with Dissolve(1)

    narrate "I set the note down on the table, turning back to my bed."
    narrate "I lay down, waiting for sleep to come to me."

    scene black
    with Dissolve(1)
    ## bell sound effect
    narrate "The midnight bell rings - I ignore it."

    jump bad_end_1

label bad_end_1:
    scene cadence_room_bed
    with Dissolve(1)
    narrate "When I wake up the next day, it's cold. Another pre-recorded announcement plays over the intercom. I can see my breath in the air."
    narrate "When I look out my window, the blizzard is worse than ever. I can't see a thing."
    narrate "I didn't pack a coat - it's summer, definitely not the season for such weather. Why would I need one?"
    narrate "I shiver, pulling the blankets up to my chin."

    ##play a knocking noise
    narrate "There is a knock at the door."
    crew "Breakfast, madam."
    cadence "Come in."
    narrate "A crew member enters. I don't recognize them. They set a tray down on the table, and leave without a word."
    narrate "I eat my breakfast in silence. When I'm done, I try the door - it's been locked once again."
    narrate "I'm stuck in my room for another day."

    narrate "..."

    narrate "It's cold. I spend the rest of the day huddled up in bed, trying to keep warm. I hear the complaints of my neighbors through the walls."

    man "Excuse me!? What's wrong with the heating in this place? It's freezing in here!"
    man "I'll have you know that this entire trip has been utterly unacceptable! Do you know who I am!?"
    man "I'll have everyone on this ship fired the moment we dock, do you hear me!? {i}EVERYONE!{/i}"

    woman "Can't you do something about the heating? My child has been shivering all night - at least give us some extra blankets!"

    narrate "I lay in bed, pulling the blankets over my head. I wish they would shut up - the cold is making me miserable."
    narrate "I close my eyes. It's too cold to think."
    scene black
    with Dissolve(1)
    stop music

    narrate "At some point, I drift off to sleep. I dream of a great white blanket, swallowing me whole."
    narrate "It grows larger and larger, until it eventually wraps around the entire earth."
    narrate "I'm freezing. I can't move. I can't breathe."
    narrate "..."
    narrate "I don't wake up."
    jump ending1

label intro_sneak_out:
    narrate "How could I live with myself if I didn't take this opportunity? It might be dangerous, but it's a mystery to solve - something to do, if nothing else."
    narrate "I hide the note in my pocket, then turn back to my bed."
    scene cadence_room_bed
    with Dissolve(1)
    narrate "I sit down, waiting for the night to fall."

    scene black
    with Dissolve(1)
    narrate "I rest my head on my hands. I close my eyes, intending to take a short nap in preparation for the midnight bell."

    ## bell sound effect
    narrate "The midnight bell rings."
    scene cadence_room_bed
    with Dissolve(1)
    narrate "It's time to go."

    scene cadence_room_main
    with Dissolve(1)
    narrate "I listen for the sound of footsteps when I approach my door."
    narrate "I hear none. Cautiously, I turn the handle."
    jump hallway_start

    
label continuing:
    return
