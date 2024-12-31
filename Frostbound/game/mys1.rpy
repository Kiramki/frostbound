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
    $ listen_count = 0

    menu sneak_menu:
        "Look around first" if looked_around == 0:
            jump sneak_1_look

        "Try to distract them":
            jump sneak_1_distract

        "Make a break for the stairs":
            jump sneak_1_stairs

        "Keep listening":
            if listen_count == 0:
                jump sneak_1_eavesdrop
            elif listen_count == 1:
                jump sneak_1_eavesdrop2
            elif listen_count == 2:
                jump sneak_1_eavesdrop3
            elif listen_count >= 3:
                jump sneak_1_eavesdrop4

label sneak_1_look:
    scene main_deck_right
    narrate "My eyes adjust to the dim light as I squint, scanning the area."
    narrate "Before the blizzard, this place was a bustling thoroughfare for passengers."
    narrate "To the side, there's a humble wooden door. It's probably a storage closet, though I have no clue what's inside."
    narrate "Then, there's the grand staircase. It spirals upwards, its once-pristine brass railing now draped in icicles."
    narrate "At the foot of the stairs, something shiny catches my eye."
    narrate "Wait a minute."
    narrate "That's not the key {i}to{/i} the the upper deck, is it? That's... not a good security measure."
    play sound "audio/clue.mp3"
    narrate "{color=#49D5FF}Item Acquired: Key to upper deck.{/color}"
    $ looked_around = 1
    jump sneak_menu

label sneak_1_distract:
    narrate "I grab the nearest thing around me and throw it into the room, trying to knock something over."
    stop music
    play sound "audio/slam.mp3"
    show main_deck_cg with vpunch
    watchman2 "Shit!"
    narrate "Whatever I threw caused a cascade of icicles to fall around them with unintended destruction."
    narrate "The watchman to the right throws his body protectively over the other, shielding him from the falling debris."
    watchman1 "What was hell that?"
    narrate "Their two hands find each other in the dark and hold on tightly."
    narrate "Well. I'll have time to feel mortified about this later."
    narrate "I bolt, rushing up the staircase."
    play sound "audio/footsteps_near.mp3"
    play music "audio/intense_theme.mp3"
    scene main_deck_right 
    watchman1 "Wait - I see someone. You there, stop!"
    watchman2 "Damn it. I'll take care of this. Wait here."
    narrate "I scramble up the staircase, my heart pounding in my chest to the roaring song of a war drum in accelerando."
    narrate "The gate at the top of the stairs is unguarded."
    jump sneak_1_gate

label sneak_1_stairs:
    play sound "audio/footsteps_near.mp3"
    play music "audio/intense_theme.mp3"
    scene main_deck_right
    with Dissolve(1)
    narrate "I dart toward the stairs, keeping my steps as light as possible. My pulse races, but I focus, forcing myself to stay calm."
    narrate "The gate at the top of the stairs is unguarded."
    watchman1 "Hey, did you hear something?"
    watchman2 "... Someone's here."
    jump sneak_1_gate

label sneak_1_eavesdrop:
    scene main_deck_cg
    with Dissolve(1)
    narrate "They seem engaged in their conversation. Perhaps I'll learn something about the state of the ship."
    watchman1 "Did you run into Mouse during your rounds tonight? Heard he's been missing since breakfast."
    narrate "Mouse... is that the same crew member who replaced my steward this morning? I lean in a bit closer."
    watchman2 "Kid's gone. Probably went off and buried his head in some hole, hidin' like he always does. Don't know how he's made it this far."
    narrate "The words are harsh, but there is a weary edge to them."
    watchman1 "Take it easy on him, will you? He's had a rough couple of days."
    watchman2 "Rough? Everyone here's had it rough, but that kid... he cracks under the smallest pressure."
    narrate "The watchman tilts his head back and looks out at the snowy wasteland."
    narrate "..."
    watchman1 "You alright?"
    watchman2 "Fine. Just, damn this cold. You?"
    narrate "There's a pause."
    watchman1 "Could be worse... Listen, about last night..."
    watchman2 "Not here. Later, alright?"
    play sound "audio/clue.mp3"
    narrate "{color=#49D5FF}Clue Added: Sometime after breakfast—where I may have scared him off—the crew member, Mouse, vanished. It seems he's had a rough few days. {/color}"
    $ listen_count +=1
    jump sneak_menu

label sneak_1_eavesdrop2:
    scene main_deck_cg
    with Dissolve(1)
    narrate "It seems like they'll be talking for a while. Surely it wouldn't hurt to listen some more."
    watchman1 "-and then he dropped the whole wretched thing, guts and all, right into the day's gumbo!"
    watchman2 "Hah! Does he also sprinkle rat droppings in the ale when your back's turned?"
    watchman1 "Ellis! I'm telling it straight. Gave me such a fright, I spent the a whole week eating nothing but hardtack."
    narrate "His companion laughs at this, but not unkindly."
    watchman2 "You coulda told me, I'd have set aside some of my salt beef for you."
    narrate "..."
    narrate "Suddenly, I'm very thankful that father upgraded my cabin afterall."
    $ listen_count +=1
    jump sneak_menu

label sneak_1_eavesdrop3:
    scene main_deck_cg
    with Dissolve(1)
    narrate "... I'll admit - at this point I've been listening in for so long I don't know how to stop myself."
    watchman1 "You don't think Mouse would've... you know?"
    watchman2 "Jumped ship? No point when the whole sea's frozen over. Everything's gone to hell."
    narrate "There's a long pause."
    watchman1 "So the captain is gone, isnt he?"
    narrate "A long sigh."
    watchman2 "It's hard to say. But honestly, death might be a mercy in his case."
    watchman2 "We're screwed too, if we don't get out of this blizzard soon."
    narrate "For reasons unknown, this cues a chortle out of his companion. Soon, they're both laughing quietly."
    watchman1 "You and I can't seem to catch a break, huh?"
    watchman2 "Yeah well, call me a madman but I can't imagine it any other way with you."
    narrate "Their conversation continues on in a low murmur, indecipherable to my ears."
    play sound "audio/clue.mp3"
    narrate "{color=#49D5FF}Clue Added: The captain's fate is uncertain, but he's not the same after the incident. Death may be a relief in his current state. {/color}"
    $ listen_count +=1
    jump sneak_menu

label sneak_1_eavesdrop4:
    scene main_deck_cg
    with Dissolve(1)
    narrate "I know I should retreat now, but an inexplicable force keeps me rooted in place."
    watchman2 "Hey, you remember what I said about last night?"
    narrate "It's the first time Ellis has initiated a conversation, and the sudden shift catches both me and his companion off guard."
    watchman1 "Wh- you mean twenty minutes ago?"
    narrate "Have I truly been eavesdropping on these two for that long?"
    watchman2 "Yeah, didn't think this was the right place for it."
    watchman2 "Imagined I'd do it just off shore, or somewhere that would really wow you but..."
    narrate "There's a rustling of fabric. In the dim light, I can just make out Ellis pressing something small and flat into his companion's palm."
    watchman2 "You're the best of me, Will. I'll be damned if something happens to us before you know."
    narrate "The tenderness in Ellis' voice makes me feel like an intruder in a deeply private moment. I shift uncomfortably."
    watchman1 "Ellis, what..."
    show main_deck_cg with vpunch
    watchman1 "WHAT ARE YOU DOING OVER THERE?"
    narrate "In an instant, both watchmen whirl around, their eyes locking onto me like searchlights."
    narrate "I stand frozen in mortification."
    watchman2 "Goddamnit, how long have you been standing there?"
    watchman2 "You know what, I don't want to know. Come with me."
    narrate "Rough hands seize my arms, and I'm unceremoniously marched back to my quarters."
    narrate "The air between us is thick with shared embarrassment."
    scene black
    with Dissolve(1)
    play sound "audio/door_shut.mp3"
    narrate "The door slams shut behind me, the lock clicking with grim finality. I'm not going anywhere tonight."
    narrate "With nothing left to do, I crawl into my bed, pulling the blanket up to my chin. I'm left alone with my thoughts and the lingering mystery of what I witnessed on deck."
    jump bad_end_1

label sneak_1_gate:
    scene main_deck_right
    play sound "audio/footsteps_soft.mp3"
    narrate "Heavy footsteps echo from the bottom of the stairs, heading toward me."
    if looked_around:
        narrate "My heart leaps to my throat as I scramble for the key and jam it into the lock of the gate."
        play sound "audio/door_open.mp3"
        narrate "I press my body weight into the gate and slip into the upper deck - it shuts behind me with a clang."
        jump upper_deck
    else:
        narrate "My heart pounds like a wardrum in my chest as I reach the gate and give it a violent shake. However, it doesn't budge."
        narrate "The watchmen must have {b}locked{/b} it."
        narrate "It must have been somewhere in the room below, it's too late to go back and check now."
        stop music
        play sound "audio/slam.mp3"
        show main_deck_right with vpunch
        watchman "Hey!"
        narrate "A rough hand grabs my arm, yanking me backward. The sudden light of a lantern blinds me."
        watchman "What are you doing out of your room? You're not supposed to be here."
        narrate "I try to explain, but come up short. The watchman drags me back to my room."
        scene black
        with Dissolve(1)
        narrate "I hear the door lock behind me. I'm not going anywhere tonight."
        narrate "With nothing left to do, I crawl back into bed and pull the covers up to my chin."
        jump bad_end_1


label upper_deck:
    play sound "audio/door_rattle.mp3"
    scene infirmary_entrance
    narrate "I twist the lock into place just in time. The gate behind me rattles violently, sending a jolt of panic through my veins."
    watchman2 "Who's in there? You're not allowed out of your rooms!"
    watchman1 "One moment... I'm grabbing the spare."
    narrate "Who do I think I am? My father, gallivanting around the streets of London at night? This was a terrible idea."
    narrate "Time is running out. They'll figure out how to open the door any moment now."
    narrate "My eyes scan the room, frantic, searching for any escape."
    narrate "The infirmary door is the first thing I see, and I dart toward it, my breath quickening."
    play sound "audio/door_open.mp3"
    scene black
    narrate "The cold hits me immediately. I search for somewhere to hide, but a gnawing unease settles over me."
    stop music
    narrate "Then I turn, and I see it."
    scene infirmary
    with Dissolve(1)
    play music "audio/its_snowing.mp3"
    narrate "The woman lies in the corner, her body encased in ice, frozen mid-motion, as though time itself had abandoned her."
    narrate "Her hands are curled tightly around something, but the ice has distorted it, making it impossible to tell if it's a weapon or some forgotten trinket."
    narrate "I step back, my mouth going dry. My mind spins in overdrive. What could possibly do this to a person?"
    narrate "I think about the captain, the rumors I've heard, and my gut tightens. So this isn't just about one person."
    narrate "Something horrible is happening to the passengers of this ship."
    stop music
    stranger "Nice going, detective."
    narrate "I whip around, hands instinctively reaching for the rod at my back, prepared to defend myself."
    narrate "And then I see them. Her eyes."
    narrate "Eyes I've avoided all my life."
    narrate "{b}The eyes of a witch.{/b}"
    stop music fadeout 1
    scene black
    with Dissolve(1)
    narrate "{color=#49D5FF}You have reached the end of the demo, thank you for playing Frostbound! Remember to leave a review and rate our game to support us!{/color}"
    narrate "{color=#49D5FF}Our dream is to have our own studio one day and make many more games. We hope to see you again.{/color}"
    narrate "{b}DEMO ENDING: NAH IMMA DO MY OWN THING{/b}"
    stop music fadeout 1
    scene black
    with Dissolve(1)
    return


label sera_stairs:
    scene stowaway_entrance
    with Dissolve(1)
    narrate "At the bottom, my breath fogs the air."
    narrate "Crates are stacked high against the walls, leaning precariously, their shadows stretching long in the flickering light."
    narrate "It smells of salt, damp wood, and something faintly metallic."
    stranger "About time you showed up."
    narrate "My head jerks up to a figure perched lazily atop a stack of crates, as if they'd been waiting for hours."
    narrate "And then I see them. Her eyes."
    narrate "Eyes I've avoided all my life."
    narrate "{b}The eyes of a witch.{/b}"
    play music "audio/meet_seraphine.mp3"
    narrate "I reel back as she as she glides down the stack of crates, her movement swift and seamless, like a needle threading fabric."
    stranger "You're Cadence?"
    narrate "Tiny golden stars dangle from her ears and tangle in her hair as if the night sky had bent to decorate her."
    narrate "I quickly avert my gaze, fixing on the stitching of her cloak instead."
    narrate "There's an absurdity to it, though: aren't witches supposed to look away from us?"
    narrate "A tense silence follows, then, she snickers."
    stranger "Hah! Nel wasn't kidding when she said you looked Detective Daycott with tits."
    narrate "My eyes snap up at the sheer audacity of the comment and she smirks at my scandalized expression."
    stranger "I can explain what's happening. C'mon. You'll understand when you see it."
    narrate "My thoughts feel smothered by the sheer absurdity of this interaction."
    narrate "She extends her hand towards me expectantly."
    menu:
        "Trust her":
            jump sera_stairs_trust
        "Don't trust her":
            jump sera_stairs_distrust

label sera_stairs_trust:
    narrate "My fingers tremble just enough to betray my nerves as I clasp her hand."
    narrate "Something electric hums through the contact, curling around my chest and tightening my breath."
    cadence "Please, call me Cadence. I'm guessing you were my midnight visitor?"
    narrate "Her pupils morph into smiling crescents akin to way watercolor bleeds across parchment."
    sera "The name's Seraphine."
    narrate "She doesn't release my hand right away. Her touch lingers for a second before I pull back, tucking my hands behind me."
    sera "Right this way, Daycott."
    narrate "The insignia on her cloak glints unmistakably as she throws the door open and steps through."
    narrate "I hesitate, steeling myself before stepping in after her."
    narrate "When you've spent your life hiding, it's easy to forget there are other ways to exist."
    narrate "But seeing someone who wears it all so freely—it's almost jarring."
    narrate "It makes me wonder... what would it be like to stop pretending, even for a moment?"
    play sound "audio/footsteps_soft.mp3"
    stop music fadeout 1
    scene black
    with Dissolve(1)
    jump stowaway_hideout

label sera_stairs_distrust:
    narrate "There's one case my father never talks about."
    narrate "The one where he came home trembling, covered in blood, and sheltered in his room for two days straight."
    narrate "Now, standing in front of this witch, I can't let my guard down."
    narrate "My face must betray my emotions because the witch lowers her hand, her expression darkening."
    stranger "What's that? {i}Oh, Seraphine! Thanks for risking your ass to get me down here tonight!{/i}"
    narrate "The witch - Seraphine - flips her braid behind her back, and scoffs."
    sera "Or are you one of those phonies who can't stay loyal to her own kind?"
    narrate "My lips press into a thin line, determined not to answer her."
    narrate "It's a silent battle of wills, and for a moment, I almost feel like we're both waiting for the other to blink."
    narrate "Then, she lets out a long sigh."
    sera "Look, you don't have to trust me. You can even hold onto that oversized rod of yours if it makes you feel better."
    narrate "Her eyes are like peering into a kaleidoscope held up to the sun."
    sera "We're both on the same side here - stuck on this metal death trap... and I need your help."
    narrate "The last part seems to come out reluctantly, as if the words leave a bad taste in her mouth."
    narrate "Without waiting for my response, she swings the door open and steps through it, not checking to see if I'm following."
    narrate "Despite myself, I do."
    play sound "audio/footsteps_soft.mp3"
    stop music fadeout 1
    scene black
    with Dissolve(1)
    jump stowaway_hideout

label stowaway_hideout:
    play music "audio/emotional_theme.mp3"
    scene stowaway_lower
    with Dissolve(1)
    narrate "I pause to take in the scene around me—soft golden light spills from strings of magical lanterns, casting a warm glow across the cramped hold."
    narrate "Crates are stacked high, forming narrow paths like the aisles of an overstuffed library."
    narrate "A young man lounges atop a stack while a few kids peek out shyly from behind the crates."
    sera "We're all in the same boat down here. If the crew knew, they'd toss us into the ice without a second thought."
    narrate "I don't have a response to that. I wonder how many of the faces I'm seeing are witches like Seraphine."
    narrate "She tosses a wink in greeting at one of the children before motioning me deeper into the hold."
    narrate "As we reach a secluded corner, I stop."
    scene stowaway_body
    with Dissolve(1)
    play music "audio/its_snowing.mp3"
    narrate "A single bed sits at the center, and on it lies a boy, his body encased in an unnatural shroud of frost and flowers."
    narrate "Seraphine lowers herself beside him, her usual restless energy is replaced by something softer."
    narrate "I struggle to process the sight before me."
    sera "He was a crew member. Used to visit us often, before the blizzard. Snuck us food when he could."
    sera "Couple nights ago he came down here and said he was tired. Went to sleep… and froze over like this."
    cadence "How is that possible?"
    narrate "Seraphine doesn't answer me. Instead, she closes her eyes, her head bowing slightly as if in prayer."
    narrate "A pale bluebell blooms into existence in her palms, its delicate petals glowing faintly with magic."
    narrate "With care, she places the flower onto the pile of icy flora already covering him."
    sera "{i}Thank you.{/i}"
    narrate "For a moment, I simply watch as Seraphine kneels in the light, the stars adorning her shimmer like pieces of stained glass."
    narrate "..."
    stop music
    narrate "Beside the bed, something shifts."
    scene stowaway_lower
    play music "audio/intense_theme.mp3"
    cadence "!!!"
    narrate "It's the crew member from this morning. Our eyes meet, and panic floods his face."
    narrate "He wriggles against his bindings, gag muffling his attempts to speak."
    narrate "My thoughts race, questions colliding too fast to catch."
    cadence "You... kidnapped my steward?"
    sera "Kidnapped him?"
    narrate "She lets out a sharp laugh, the gentleness of the last few minutes vanishing in an instant."
    sera "In case you haven't realized, we have bigger things to worry about."
    narrate "She gestures emphatically towards the frozen boy, as if the sight alone proves her point."
    narrate "However, when I meet the crew member's terrified gaze, something twists in my stomach."
    cadence "What are you planning to do with him?"
    sera "God, Daycott. I'm not about to chop him up or toss him in my brew, if that's what you're worried about."
    narrate "She shakes her head, a brief pause hanging in the air before she levels me with a smirk."
    sera "You're the detective's daughter, aren't you? So, go on. Tell me why he's down here."
    stop music fadeout 1
    scene black
    with Dissolve(1)
    narrate "{color=#49D5FF}You have reached the end of the demo, thank you for playing Frostbound! Remember to leave a review and rate our game to support us!{/color}"
    narrate "{color=#49D5FF}Our dream is to have our own studio one day and make many more games. We hope to see you again.{/color}"
    narrate "{b}DEMO ENDING: TRUE{/b}"
    stop music fadeout 1
    scene black
    with Dissolve(1)
    return





