import pyautogui as pa
from time import sleep

def auto_twitch (iniciar):
    if iniciar == True:
        pa.click(21,1067, duration=0.2)
        pa.write ('edge')
        pa.press ('enter')
        sleep(1)
        pa.click(274,55, duration=0.1)
        sleep(0.1)
        pa.click(274,55, duration=0.1)
        pa.write('www.twitch.tv/ultrinhanewmew')
        pa.press('enter')