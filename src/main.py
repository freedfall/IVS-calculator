import eel
from logic.controller import *

eel.init('src/web')

if eel.chrome.find_path():
    mode = 'chrome'
elif eel.edge.find_path():
    mode = 'edge'
else:
    mode ='default' 

eel.start('index.html', mode=mode, size=(1000, 600))