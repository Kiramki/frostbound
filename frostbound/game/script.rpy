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
    narrate "{i}\"When the big bell goes at midnight and the night watch is gone, that's your chance.\"{/i}"
    narrate "{i}\"Count five doors on your left. The next one's got a knob that don't turn right. That's your door.\"{/i}"
    narrate "{i}\"Go down the stairs and listen for the creaky boards. One of 'em's loose - there's a hatch underneath.\"{/i}"
    narrate "{i}\"I'll be waiting for you. Don't get caught, yeah?\"{/i}"
    narrate "{i}\"- S.\"{/i}"
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
    narrate "All of is suspicious. Father would stop at nothing to make sure I knew the depths of my idiocy if he found out about this."
    narrate "I should stay in my room. A mystery isn't worth whatever ill fate I might meet, going out to meet a stranger in the dead of night."
    scene cadence_room_bed
    with Dissolve(1)

    narrate "I set the note down on the table, turning back to my bed."
    narrate "I lay down, waiting for sleep to come." 

    scene black
    with Dissolve(1)
    narrate "The midnight bell rings - I ignore it."

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
    narrate "just kidding im not done lol B) u should look at the stay in part though"

label continuing:
    return
