import threading
from pynput import keyboard
from playsound import playsound

BATZ = './batz.m4a'
BLJAD = './bljad.m4a'
SHESH = './shesh.m4a'
OH_SHIT = './oh_shit.m4a'

def play_sound(sound_name):
    playsound(sound_name)


def on_press(key):
    try:
        if key == keyboard.Key.space:
            threading.Thread(target=play_sound, args=(BLJAD,)).start()
        elif key == keyboard.Key.backspace:
            threading.Thread(target=play_sound, args=(OH_SHIT,)).start()
        elif key == keyboard.Key.shift_l or key == keyboard.Key.shift_r:
            threading.Thread(target=play_sound, args=(SHESH,)).start()
        else:
            threading.Thread(target=play_sound, args=(BATZ,)).start()
    except AttributeError:
        threading.Thread(target=play_sound, args=(BLJAD,)).start()

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
    on_press=on_press,
    on_release=on_release
) as listener:
    listener.join()
