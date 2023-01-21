import PySimpleGUI as psg
import random

psg.theme ('DarkAmber')

with open('caracteres.txt', 'r') as chars:
    caracteres = list(chars.read())

def pegar_senha (num_caracteres):
    contagem = 1
    escolha = []
    while contagem != num_caracteres:
        add = random.choice(caracteres)
        escolha.append (add)
        contagem = contagem+1

    escolha = ''.join(escolha)
    return escolha

senha1 = ''
senha2 = ''
senha3 = ''
senhas = [senha1, senha2, senha3]

layout = [
    [psg.Text ('Gerador de Senhas!', font=('Helvica', 25))],
    [psg.Text ('digite quantos caracteres')], [psg.InputText (size=(2,2), key = 'num_caracteres')],
    [psg.Button ('Clique para gerar')],
    [psg.Text ('Senha 1: '), psg.Text(senha1, key='senha1')],
    [psg.Text ('Senha 2: '), psg.Text(senha2, key='senha2')],
    [psg.Text ('Senha 3: '), psg.Text(senha3, key='senha3')],
    [psg.Button('Fechar')]
]

janela = psg.Window('gerador de senha', layout)

while True:
    event, values = janela.read()
    if event == psg.WIN_CLOSED:
        break
    
    elif event == 'Clique para gerar':
        num_caracteres = int(values['num_caracteres'])
        senhas[0] = pegar_senha(num_caracteres)
        senhas[1] = pegar_senha(num_caracteres)
        senhas[2] = pegar_senha(num_caracteres)
        senha1_element = janela.find_element('senha1')
        senha1_element.update(senhas[0])
        senha2_element = janela.find_element('senha2')
        senha2_element.update(senhas[1])
        senha3_element = janela.find_element('senha3')
        senha3_element.update(senhas[2])
    elif event == 'Fechar':
        janela.close()