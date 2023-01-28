import qrcode

def qrcodegenerator(valor, nome, pasta_output):
    imagem = qrcode.make(valor)
    caminho_completo = pasta_output + '\\' + nome + '.png'
    print (caminho_completo)
    imagem.save(caminho_completo)

qrcodegenerator('www.youtube.com', 'teste', 'C:\\Users\\Mk Academy 11\\Downloads')