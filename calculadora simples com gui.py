import PySimpleGUI as sg

sg.theme ('DarkAmber')

def faça_a_conta(numero1, operador, numero2):
  if operador == '*':
    resultado = numero1*numero2
    return resultado

  elif operador == '/':
    resultado = numero1/numero2
    return resultado

  elif operador == '+':
    resultado = numero1+numero2
    return resultado

  elif operador == '-':
    resultado = numero1-numero2
    return resultado

  else:
    resultado = 'resultado inexistente'
    return resultado
    

layout = [  [sg.Text('insane python calculator')],
            [sg.Text('digite uma conta')],
            [sg.InputText(size = (20,20), key = 'contak')],
            [sg.Button('FAÇA A CONTA'), sg.Button('Cancel')] ]

window = sg.Window('insane', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break

    elif event == 'FAÇA A CONTA':
      conta = values['contak']
      conta = conta.split(' ')
      conta [0] = int(conta [0])
      conta [2] = int(conta [2])
      resultado = faça_a_conta(conta[0], conta[1], conta[2])
      resultadinhos = [[sg.Text('o resultado é:')],
                      [sg.Text(resultado)],
                      [sg.Button('Cancel')]]
      resultadinhos_janela = sg.Window('results', resultadinhos)
      resultadinhos_janela.read()

      

window.close()