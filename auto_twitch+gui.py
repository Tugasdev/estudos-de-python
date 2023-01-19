import PySimpleGUI as sg
from auto_twitch import auto_twitch

sg.theme ('DarkAmber')
    

layout = [  [sg.Text ('auto twitch!')],
            [sg.Text ('vou te levar pro melhor canal da twitch.')],
            [sg.Button ('clique para iniciar')],
            [sg.Button ('sair')]]

window = sg.Window('auto', layout)

while True:
    event, values = window.read()    
    if event == 'clique para iniciar':
      auto_twitch (iniciar=True)
    elif event == sg.WIN_CLOSED or event == 'sair':
        break


      

window.close()