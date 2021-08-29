from pynput import keyboard
import ClipImageToText as citt
# -- Testing purposes --
# import os
# clear = lambda: os.system('cls')
# --


# Importing Combination from ClipImageToText.py
COMBINATIONS = citt.COMBINATIONS

current = set()

detectionCount = 0

def parse_text():
  # global detectionCount 
  # detectionCount += 1
  # clear()
  # print("Capture #" + str(detectionCount))
  citt.clipboardToText()


def on_press(key):
  if any([key in COMBO for COMBO in COMBINATIONS]):
    current.add(key)
    if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS):
      parse_text()

def on_release(key):
  if any([key in COMBO for COMBO in COMBINATIONS]):
    try:
      current.remove(key)
    except:
      pass
    
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
  listener.join()
