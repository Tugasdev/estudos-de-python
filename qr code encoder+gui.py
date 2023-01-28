import PySimpleGUI as psg
import qr_code_encoder

layout = [
    [psg.Text ('CORIFICADOR DE QRCODE!!!')],
    [psg.Text ('Informações do qr:')],
    [psg.InputText(size=(50, 1), key= 'QR_INFO')],
    [psg.Text('Onde vai ser criado:')],
    [psg.Input(key='PASTA_OUTPUT'), psg.FolderBrowse()],
    [psg.Text('Nome do arquivo:'),psg.InputText(size = (30,1), key='NOME_ARQUIVO')],
    [psg.Exit('Sair'), psg.Button('Criar')]
]

janela = psg.Window ('QRCode', layout)

while True:
    event, values = janela.read()
    if event in (psg.WIN_CLOSED, 'Sair'):
        break

    elif event == 'Criar':
        qrinfo = values['QR_INFO']
        nome_arquivo = values ['NOME_ARQUIVO']
        pasta_output = values['PASTA_OUTPUT']
        print (qrinfo, type(qrinfo))
        print (nome_arquivo, type(nome_arquivo))
        print (pasta_output, type(pasta_output))
        qr_code_encoder.qrcodegenerator(qrinfo, nome_arquivo, pasta_output)



janela.close()