## Dict of all clues
clue_dict = {
    # Severe Weather
    "severe_weather": {
        "id":"severe_weather",
        "name": "Severe Weather",
        "description": "The SS Nimbus has been experiencing severe weather conditions for the past few days.\
        This has caused the ship's journey to be delayed significantly.\n\n\
When I look out the window, I can see frost creeping up the glass. The ship has been getting colder by the day. This is highly unusual weather for the season."
    },

    # Lockdown
    "lockdown": {
        "id":"lockdown",
        "name": "Lockdown",
        "description": "The SS Nimbus has been placed under a strict lockdown. No passengers are allowed to leave their cabins.\
 It seems that the crew has been instructed to keep the passengers confined to their rooms. They claim that it is for our safety.\n \n\
Three times a day, the crew delivers meals to the passengers' rooms. The food is good, as would be expected from a luxury experience, but the crew seems to be on edge. \
\n\nIt's hardly any kind of social interaction, though - solation is taking its toll on the passengers. I can hear them arguing with the crew through the walls."
    },

    # Pre-recorded Announcements
    "pre_recorded_announcements": {
        "id":"pre_recorded_announcements",
        "name": "Pre-recorded Announcements",
        "description": "I've noticed something strange. About a day after the lockdown was put in place, all of the ship's announcements have been pre-recorded.\
\n\nI believe that something is amiss. The crew has been avoiding my questions about the captain. Why hasn't the captain been making the announcements? He seemed to take great joy in it."
    },

    # Captain's Whereabouts
    "captains_whereabouts": {
        "id":"captains_whereabouts",
        "name": "Captain's Whereabouts",
        "description": "The crew member that served me breakfast this morning has been reporting to someone other than the captain."
    },

    # Missing Steward
    "missing_steward": {
        "id":"missing_steward",
        "name": "Missing Steward",
        "description": "The steward that usually serves my meals failed to show up this morning. Allegedly, he has been 'moved'. The crew is reluctant to discuss him."

    },

    # Mysterious Note
    "mysterious_note": {
        "id":"mysterious_note",
        "name": "Mysterious Note",
        "description": "\"I found a note slipped under my door this evening. It reads:\
\n\nI know why they're locking people in their rooms. We don't have much time left.\
\nWhen the big bell tolls at midnight and the night watch is gone, that's your chance.\
\nCount five doors to your left—there's a hidden staircase there.\
\nI'll be waiting for you at the bottom.\
\nDon't get caught.\
\n- S.\"\
\n\nThe writing is hasty, words aggressively scribbled out - as if the person writing it were in a rush. The penmanship style does not match that of a crew member."
    }



}

## Dict of all possible updates for clues
clue_updates = {
    # Captain's Whereabouts
    "captains_whereabouts": {
        "first_mate": "The first mate of the ship has taken over command. The crew of the SS Nimbus now reports to him, indicating a shift of leadership.",
    },
}

# get a new clue
def get_clue(clue, dict = clue_dict):
    # Returns a copy of a clue, default from the clue_dict defined here.

    ### How to use this function to update player_clues: ########
    #
    # player_clues['clue_id'] = clues.get_clue('clue_dict_id')
    #
    # clue_dict_id = the required id from clue_dict
    # clue_id = the id you want to store the clue as in player_id
    # I prefer to make the player_clues id and the clue_dict id match.
    #############################################################

    return dict[clue].copy()

def update_clue(clue, flag, id="description"):
    # Updates the given clue's description by consulting the flag in the clue_updates dictionary

    ### How to use this function to update player_clues: ########
    #
    # player_clues['description'] = clues.update_clue('id','flag_name')
    #
    # Flag name is listed in the clue updates.
    # Use the desired update id listed under the matching clue id.
    #############################################################


    clue[id] = clue_updates[clue['id']][flag]
    return None