# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define cadence = Character("Cadence")
define narrate = Character(None)
define intercom = Character("Intercom")
define crew = Character("Crew Member")


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
    narrate "The crackling sound of an intercom coming to life fills the room."
    intercom "Attention all passengers! This is your captain speaking."
    intercom "Due to continued severe weather conditions, our cruise will be delayed for another day."
    intercom "Remain in your rooms. We'll be back on course just as soon as the weather clears."
    intercom "Thank you for your patience."
    narrate "{i}Click...{/i}"

    # cadence_room_bed.png scene
    narrate "(imagine a REALLY COOL scene transition here)"
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
    ## cadence_room_main.png scene
    narrate "The door creaks open, and a crew member steps inside with a tray of food."
    crew "Good morning, Miss Cadence."
    crew "Today's breakfast is eggs, bacon, and toast. Got some coffee too, if you'd like."


    #menu:
       # "Is the captain doing alright?":

        #"How much longer until we can leave our rooms?":

        #"Thank you.":







    return
