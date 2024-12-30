## Dict of all clues
clue_dict = {}

## Dict of all possible updates for clues
clue_updates = {
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