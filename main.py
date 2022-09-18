# Code by Shaan Suthar, Maaz Siddiqi, Nick Koenig, Richard Wu

import adhawkapi
import adhawkapi.frontend

def on_connect(error):
    if not error:
        print('Connected to AdHawk Backend Service')

def on_disconnect(error):
    print('Disconnected from AdHawk Backend Service')

api = adhawkapi.frontend.FrontendApi()
api.start(connect_cb=on_connect, disconnect_cb=on_disconnect)
...
# Terminate communication
input()
api.shutdown()