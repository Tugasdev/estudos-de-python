import PySimpleGUI as ps

layout = [
    [ps.Text('mano pprt')],
    [ps.Text('dota é horrível.', font = ("Helvetica", 25))],
    [ps.Text('vc n concorda?')],
    [ps.Button('sim'), ps.Button('não')]
    ]


janela = ps.Window ('dota?', layout)


while True:
    event, values = janela.read()
    if event == "sim":
        ps.popup ('vc tem bom gosto. 🍷🗿')
           
    elif event == 'não':
        ps.popup ('ce gosta de dar o boga ne ( ͡° ͜ʖ ͡°).')

    elif event == ps.WIN_CLOSED:
        break


janela.close()