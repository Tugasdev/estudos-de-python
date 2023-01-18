import pyautogui as pa
from time import sleep

pa.click(21,1067, duration=0.2)
pa.write ('edge')
pa.press ('enter')
sleep(1)
pa.click(274,55, duration=0.1)
sleep(0.1)
pa.click(274,55, duration=0.1)
pa.write('https://docs.google.com/spreadsheets/d/1MVrAsz-fpIXaC3mAS32eM7CtKs9lVv_67W5-pRV30UE/edit#gid=1886895500')
pa.press('enter')