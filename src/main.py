## @file main.py
# @brief Main entry point for the application
# @author Timur Kininbayev
##

import eel
from logic.controller import *

eel.init('src/web')

if eel.chrome.find_path():
    mode = 'chrome'
elif eel.edge.find_path():
    mode = 'edge'
else:
    mode ='default' 

eel.start('index.html', mode=mode)