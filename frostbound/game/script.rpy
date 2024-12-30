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
    narrate "This boy can't be older than 15; and he looks one wobble away from sending the expensive cutlery crashing to the floor."
    narrate "He's not my usual steward. "

    crew "Good morning, Miss Cadence."
    crew "Today's breakfast is eggs, bacon, and toast. Got some coffee too, if you'd like."
    play sound "audio/book_shut.wav"
    narrate "I snap my journal shut. A twinge of guilt settles in my stomach for what I'm about to do."
    narrate "I need information, and he's just the kind of person who will give it to me."
    narrate  "I may lack my father's skill for the details, but I've learned:"
    narrate "If I ask the right questions, and {b}people will reveal what I need to know on their own.{/b}"

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
    cadence "If the {b}captain's overseeing things{/b}, why have the announcements been prerecorded? Isn't he the one who usually makes them?"
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
    narrate "A tight frustration coils in my stomach. At this point, my first-class cabin resembles a gilded cage more than a sanctuary."
    cadence "Surely we can be let out for some fresh air, or even just a trip to the kitchens?"
    narrate "His smile remains with the carefulness of someone trying not to flub their lines."
    crew "Apologies, Miss. You'll have to wait. We've run into some... unexpected issues on deck."
    play sound "audio/lying.wav"
    crew "{b}We'll have you all out once the weather passes, and you'll be free to stretch your legs.{/b}"
    narrate "{color=#49D5FF}(Tutorial: Did you catch that? Cadence can sense when someone isn't being truthful. What part of his words felt off?) {/color}"
    narrate "{color=#49D5FF}(Tutorial: in moments like these Cadence can {b}PRESS{/b} for more information. Not everyone appreciates being pressed, though.) {/color}"
    menu:
        "PRESS":
            jump rs_leave_press
        "Let it go":
            jump crew_leaving

label rs_leave_press:
    play sound "audio/press.wav"
    cadence "You say {b}we'll be let out when the weather passes{/b}. Who decides when it's safe for us to leave?"
    narrate "His hands tighten around the silver tray as he mulls over my question."
    crew "Well... the room lock was ordered by the captain, Miss. But the senior officers will decide when you can be let out."
    cadence "So it's a group decision, then?"
    narrate "He nods slowly."
    cadence "I see. What has the captain told you about the situation so far?"
    narrate "He shifts his weight from foot to foot."
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
    cadence "You're doing an impressive job managing all of this. It's very brave of you."
    narrate "The crew member straightens at the sudden compliment."
    play sound "audio/press.wav"
    cadence "Is preparing the {b}Captain's prerecorded announcments{/b} part of your duties as well?"
    narrate "At the mention of the announcements, his eyes flicker with a hint of unease, and the lightheartedness from the compliment quickly fades."
    crew "Oh, I don't know nothin' 'bout that, sorry, Miss. I take my orders from someone else."
    play sound "audio/clue.mp3"
    narrate "{color=#49D5FF}Clue Added: The crew member has been reporting to someone other than the captain. {/color}"
    narrate "{color=#49D5FF}(Tutorial: you can view your clues by clicking your {b}JOURNAL{/b} in the top right corner.){/color}"
    jump crew_leaving


label crew_leaving:
    narrate "The crew member hurries to my table and sets the tray down with a clang. He's eager to leave."
    crew "Stay in your room for now, Miss. I'll bring your supper later."
    play sound "audio/door_open.mp3"
    narrate "A chill pushes in as he opens my door."
    cadence "Wait—!"
    narrate "I spring from my bed and rush to plant myself in front his path before he can exit."
    play sound "audio/clang.wav"
    narrate "The crew member jumps back. His arm knocks the tray, sending coffee spilling over my toast."
    narrate "He only just manages to stop the rest of it from splashing onto the floor."
    cadence "I have a few questions, if you could spare a moment."
    narrate "His gaze flicks nervously to the corridor behind me."
    crew "Apologies, but I've got to get back to my duties now."
    narrate " I'm not going to let him get away that easily. If he leaves, I'll be stuck in this room with no leads."
    cadence "Please, just for a moment. I promise I won't keep you long."
    narrate " He's clearly in a rush. I'll only have time for a few questions before he's gone."
    play music "audio/hope_in_the_cold.mp3" fadein 1.0

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
    cadence "Could you at least tell me what's truly going on?"
    cadence "None of this adds up, and you know it."
    narrate "I take a deliberate step forward, but falter as he shrinks back, his shoulders hunching like a cornered animal."
    crew "I... I don't know! Just — please, step back!"
    narrate "He buries his head in his hands, fingers clutching his hair as he breathes heavily."
    cadence "Um..."

    narrate "Oh dear. It seems I pressed him too hard. Father would surely disapprove—or worse, commend my tactics. The thought is hardly comforting."
    narrate "For a moment, I simply watch, unsure whether to console him."
    cadence "Excuse me... are you alright?"

    narrate "I try to soften my words and reach out in an attempt to comfort him."
    narrate "My fingers brush against his arm."
    stop music
    play sound "audio/slam.mp3"
    show cadence_room_main with vpunch
    crew "{i}GET OFF ME!{/i}"
    narrate "He shoves me aside with startling force. My body hits the wall, the breath knocked out of me."
    play sound "audio/door_shut.mp3"
    narrate "The door locks with a sharp click as he bolts."
    narrate "My neighbors are not amused."
    play sound "audio/banging.mp3"
    woman "Excuse me! You forgot our food! Oh, dear god, my baby needs food - she's starving! Please, we need it now!"
    play sound "audio/banging.mp3"
    man "Those bastards! I'm kicking down this door! I'M KICKING DOWN THIS DOOR, YOU HEAR ME?!"
    narrate "... Is that all we can do? Just wait for the blizzard to pass?"
    narrate "I glance at my ruined meal and push the tray aside, my appetite gone."

    menu:
        "Wait.":
            jump intro_note

label intro_note:
    play music "audio/hope_chords.mp3" fadein 1.0 fadeout 1.0
    narrate "I return to my bed in the corner of the room and pull out my journal once more."
    ## !!!!! ##
    narrate "{color=#49D5FF}(Tutorial: solve the mystery alongside Cadence by viewing clues in your {b}JOURNAL{/b} in the top right corner.){/color}"
    narrate "{color=#49D5FF}(Not everyone is going to be as forthcoming with information so be sure to {b}PRESS{/b} strategically.){/color}"
    narrate "{color=#49D5FF}(If a character reacts poorly to your choices, it's not always a bad thing. Good luck.){/color}"
    ###########
    play sound "audio/writing.wav"
    narrate "Time passes as I work. When I spare a moment to glance at the clock, I find that hours have passed."
    
    play sound "audio/door_knock.mp3"
    narrate "A knock at the door. The crew member must have been shaken if he's this late with my supper."
    narrate "..."
    cadence "... Hello? You can come in."
    narrate "..."
    narrate "I frown, setting my pen down."
    narrate "Then, I notice something, a note slid under the crack of my door."

    narrate "{i}\"I know why they're locking people in their rooms. We don't have much time left.\"{/i}"
    narrate "{i}\"When the big bell tolls at midnight and the night watch is gone, that's your chance.\"{/i}"
    narrate "{i}\"Count five doors to your left—there's a hidden staircase there.\"{/i}"
    narrate "{i}\"I'll be waiting for you at the bottom.\"{/i}"
    narrate "{i}\"Don't get caught.\"{/i}"
    narrate "{i}\"- S.\"{/i}"
    narrate "The words are aggressively scribbled out, whoever wrote this was in a rush."
    narrate "The penmanship style doesn't match that of a crew member."
    narrate "...Could it be?"
    narrate "I grip the door handle, and my heart skips when it turns without resistance."
    cadence "Looks like my visitor unlocked the door for me."
    narrate "Midnight is only a few minutes away. I have to decide: do I stay, or do I sneak out?"
    narrate "I'm not familiar enough with the layout of the ship to know where this note will lead me."
    narrate "It's hard to say if my visitor comes with good intentions. Not that the crew has been any better about that."
    narrate "I could also try going my own way, ignoring the note's instructions. But the risk of getting caught is a very real threat."
    menu:
        narrate "Sneak out, or stay in?"

        "Sneak out.":
            jump intro_sneak_out
        
        "Stay in.":
            jump intro_stay_in

label intro_stay_in:
    play sound "audio/paper_rustle.wav"
    play music "audio/its_snowing.mp3" fadein 3.0 fadeout 1.0
    narrate "I shake my head and set the note down on the table, turning back to my bed."
    narrate "By now my father is waiting at the dock for me, anxiously marking each day this trip is delayed."
    narrate "I should let the crew to sort this out. It's time to stop chasing adventures, I'm not a child anymore."
    narrate "The storm will pass — like all storms do."
    scene cadence_room_bed
    with Dissolve(1)
    scene black
    with Dissolve(1)
    stop music
    play sound "audio/bell.wav"
    narrate "The midnight bell rings - I ignore it."
    jump bad_end_1

label bad_end_1:
    scene cadence_room_bed
    play music "audio/its_snowing.mp3" fadein 3.0
    with Dissolve(1)
    narrate "When I wake the next day, a cold chill hangs in the air. The same placating announcement plays over the intercom."
    narrate "Outside my window, the storm has frosted everything, painting the world in a blur of white."
    play sound "audio/door_knock.mp3"
    crew "Breakfast, madam."
    play sound "audio/door_open.mp3"
    narrate "A crew member enters, their face unfamiliar."
    play sound "audio/door_shut.mp3"
    narrate "They set a tray on the table and leave without a word."
    narrate "I spend the rest of the day huddled beneath the blankets, trying to stave off the chill. "
    narrate "Meanwhile, my neighbors bang frantically against the walls like trapped creatures, pacing endlessly."
    play sound "audio/banging.mp3"
    man "Excuse me!? What's wrong with the heating in here? It's freezing!"
    man "This whole trip has been a disaster! Do you know who I am?"
    man "I'll have everyone on this ship fired when we dock, do you hear me!? {i}EVERYONE!{/i}"
    play sound "audio/banging.mp3"
    woman "Can't you do something about the heating? My child's been shivering all night—please, some extra blankets!"

    narrate "I think of my father's face the day I left home. The way he cradled me in his arms like a keepsake being cast to water."
    narrate "I close my eyes."

    scene black
    with Dissolve(1)
    stop music

    narrate "At some point, I drift off to sleep. I dream of a great white blanket, swallowing me whole."
    narrate "It grows larger and larger, until it eventually wraps around the entire earth."
    narrate "..."
    narrate "I don't wake up."
    jump ending1

label intro_sneak_out:
    narrate "If there's one thing about being a Daycott, it's that we don't let others decide our fates."
    narrate "I'd rather take control of the situation than wait around... and the captain's fate does intrigue me. Father doesn't need to know."
    narrate "I fold the note carefully and slip it into my pocket, its weight feeling heavier than paper should."

    scene cadence_room_bed
    with Dissolve(1)
    narrate "I sit down, waiting for the night to fall."

    scene black
    with Dissolve(1)
    stop music
    play sound "audio/bell.wav"
    narrate "The midnight bell rings."
    scene cadence_room_bed
    with Dissolve(1)
    narrate "It's time to go."

    scene cadence_room_main
    with Dissolve(1)
    narrate "I listen for the sound of footsteps when I approach my door."
    narrate "I hear none. Cautiously, I turn the handle."
    play sound "audio/door_open.mp3"
    jump hallway_start

    
label continuing:
    return
