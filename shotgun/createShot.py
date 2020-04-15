#!/usr/bin/env python

# --------------------------------------
# Imports
# --------------------------------------
import shotgun_api3
from pprint import pprint # useful for debugging

# --------------------------------------
# Globals
# --------------------------------------
# make sure to change this to match your Shotgun server and auth credentials.
SERVER_PATH = "https://mystudio.shotgunstudio.com"
SCRIPT_NAME = 'my_script'
SCRIPT_KEY = '27b65d7063f46b82e670fe807bd2b6f3fd1676c1'

# --------------------------------------
# Main
# --------------------------------------
if __name__ == '__main__':

    sg = shotgun_api3.Shotgun(SERVER_PATH, SCRIPT_NAME, SCRIPT_KEY)

    # --------------------------------------
    # Create a Shot with data
    # --------------------------------------
    data = {
        'project': {"type":"Project","id": 4},
        'code': '100_010',
        'description': 'Open on a beautiful field with fuzzy bunnies',
        'sg_status_list': 'ip'
    }
    result = sg.create('Shot', data)
    pprint(result)
    print("The id of the {} is {}.".format(result['type'], result['id']))