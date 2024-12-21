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
    scene black-screen

    ## play music "howling wind lol"
    narrate "A word of warning to those who embark on this journey:"
    narrate "Within this tale, you may encounter unsettling scenes, including themes of death, murder, and other forms of distress. The story you are about to experience is not for the faint of heart."
    narrate "Proceed with caution, for once you step further, there is no turning back."

    ## stop music fadeout 1.0

    #[INTERCOM MOMENT]

    ## play sound "static"
    intercom "Attention all passengers! This is your captain speaking."
    intercom "Due to continued severe weather conditions, our cruise will be delayed for another day."
    intercom "Remain in your rooms. We'll be back on course just as soon as the weather clears."
    intercom "Thank you for your patience."
    narrate "{i}Click...{/i}"

    # oooooo scene fades innnn OOOOOO
    narrate "(imagine a REALLY COOL scene transition here)"
    cadence "Hm..."
    narrate "I sit cross-legged on the narrow bed of my cabin, scribbling a quick tally in my journal."
    cadence "Another pre-recorded announcement, is it?"

    play music "audio/hope_chords.mp3"
    narrate "The luxury of first class on a cargo ship grants me one of the few cabins with a window."
    narrate "It's useless now, though. Frost creeps up the sides of my window, and everything outside is a blur of white. I can't see a thing."
    narrate "I boarded this ship a week ago, courtesy of my father. It was a gift for finishing women's boarding school."
    narrate "He's probably not too pleased with me now. I've been stuck in this cabin for days - I've barely seen a soul outside of the crew providing room service."

    



    return
