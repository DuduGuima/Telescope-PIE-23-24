
from evdev import InputDevice, categorize, ecodes, KeyEvent
gamepad = InputDevice('/dev/input/event1')

for event in gamepad.read_loop():
    print(event)
    if event.type == ecodes.EV_KEY:
        keyevent = categorize(event)
        if keyevent.keystate == KeyEvent.key_down:
            if keyevent.scancode == 304:
                print('Back',keyevent)
            elif keyevent.scancode == 307:
                print ('Left')
            elif keyevent.scancode == 308:
                print ('Forward')
            elif keyevent.scancode == 305:
                print ('Right')