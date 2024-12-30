## Dict of all clues
clue_dict = {
    # Severe Weather
    "severe_weather": {
        "id":"severe_weather",
        "name": "Severe Weather",
        "description": "The SS Nimbus has been experiencing severe weather conditions for the past few days.\
        This has caused the ship's journey to be delayed significantly. \n \n\
When I look out the window, I can see frost creeping up the glass. The ship has been getting colder by the day. This is highly unusual weather for the season."
    },

    # Lockdown


    # Pre-recorded Announcements


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



}

## Dict of all possible updates for clues
clue_updates = {
    # Captain's Whereabouts
    "captains_whereabouts": {
        "first_mate": "The first mate of the ship has taken over command. The crew now reports to him, indicating a shift of leadership.",
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

def update_clue(clue, flag):
    # Updates the given clue's description by consulting the flag in the clue_updates dictionary

    ### How to use this function to update player_clues: ########
    #
    # player_clues['description'] = clues.update_clue('id','flag_name')
    #
    # Flag name is listed in the clue updates.
    # Use the desired update id listed under the matching clue id.
    #############################################################


    clue["description"] = clue_updates[clue['id']][flag]
    return None