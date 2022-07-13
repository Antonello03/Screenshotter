import pyautogui
from pynput import keyboard
from PIL import Image
  
# This method will show image in any image viewer 

c=0

def on_press(key):
    global c
    if key == keyboard.Key.esc:
        return False  # stop listener
    try:
        k = key.char  # single-char keys
    except:
        k = key.name  # other keys
    if k in ['m']:  # keys of interest
        # self.keys.append(k)  # store it in global-like variable
        print('Key pressed: ' + k)
        myScreenshot = pyautogui.screenshot()
        c = c + 1
        myScreenshot.save('.\\file name'+ str(c) +'.png')
        im = Image.open('.\\file name'+ str(c) +'.png') 
        im.show() 

listener = keyboard.Listener(on_press=on_press)
listener.start()  # start to listen on a separate thread
listener.join()  # remove if main thread is polling self.key
