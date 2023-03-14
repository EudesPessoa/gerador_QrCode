import PySimpleGUI as sg
import criar_qr
from time import sleep
from threading import Thread




sg.theme('Reddit')

#    ('Arial Baltic', 16),
#     ("Cooper Black", 16),
#     ("Courier New", 16),
#     ("Times New Roman", 16),
#     ("Bookman Old Style", 16),

def pagina_inicial():
    font = (4)
    layout = [
        [sg.Text('Escolha o tipo de QrCode?', font=15)],
        [sg.Text('')],
        [sg.Radio('URL', group_id='tipo_qr', key='url', font=font),
         sg.Radio('VCARD', group_id='tipo_qr', key='vcard', font=font)],
        [sg.Radio('TEXT', group_id='tipo_qr', key='text', font=font),
         sg.Radio('WIFI', group_id='tipo_qr', key='wifi', font=font)],
        [sg.Radio('INSTAGRAM', group_id='tipo_qr', key='instagram', font=font),
         sg.Radio('FACEBOOK', group_id='tipo_qr', key='facebook', font=font)],
        [sg.Text('')],
        [sg.Button('Iniciar', font=25, size=(8, 2))]

    ]
    return sg.Window('Pagina Inicial',icon='qrcode.ico',size=(350,300), element_justification='center', layout=layout, finalize=True)


def pagina_dois(item_escolhido):
    layout = [
        [sg.Text('Escolha o modelo do QrCode?')],
        [sg.Text(f'QrCode para {item_escolhido}')],
        [sg.Text('')],
        [sg.Text('Escolha a Cor externa do QrCode'), sg.Combo(values=['white','black','blue','red'],default_value='white',size=(15,1), key='cor_externa')],
        [sg.Text('')],
        [sg.Text('Escolha a Cor interna do QrCode'), sg.Combo(values=['white','black','blue','red'],default_value='black',size=(15,1), key='cor_interna')],
        [sg.Text('')],
        [sg.Button('Visualizar')],
        [sg.Image('', key='baixar_arquivo')]
    ]
    return sg.Window('Pagina dois',icon='qrcode.ico',size=(350,300), element_justification='center', layout=layout, finalize=True)


def janela_img(cor_exter, cor_inter):
    layout = [
        [sg.Text('QrCode')],
        [sg.Text(f'QrCode para {item_escolhido}')],
        [sg.Image(f'./img/{cor_exter}-{cor_inter}.png')],
        [sg.Button('Voltar'), sg.Button('Próximo')]
    ]
    return sg.Window('Pagina QrCode',icon='qrcode.ico',size=(500,500), element_justification='center', layout=layout, finalize=True)


def janela_baixar_url(cor_exter, cor_inter):
    layout = [
        [sg.Text('Baixar QrCode URL')],
        [sg.Text(f'QrCode para {item_escolhido}')],
        [sg.Text('Insira abaixo o link')],
        [sg.Input(key='link_url')],
        [sg.Image(f'./img/{cor_exter}-{cor_inter}.png')],
        [sg.Button('Voltar'), sg.Button('Baixar')]
    ]
    return sg.Window('Baixar QrCode URL',icon='qrcode.ico',size=(500,500), element_justification='center', layout=layout, finalize=True)


def janela_baixar_vcard(cor_exter, cor_inter):
    layout = [
        [sg.Text('Baixar QrCode Vcard')],
        [sg.Text(f'QrCode para {item_escolhido}')],
        [sg.Text('Insira seu nome completo')],
        [sg.Input(key='link_nome')],
        [sg.Text('Insira seu email')],
        [sg.Input(key='link_email')],
        [sg.Text('Insira seu telefone')],
        [sg.Input(key='link_telefone')],
        [sg.Text('Insira nome da empresa')],
        [sg.Input(key='link_empresa')],
        [sg.Image(f'./img/{cor_exter}-{cor_inter}.png')],
        [sg.Button('Voltar'), sg.Button('Baixar')]
    ]
    return sg.Window('Baixar QrCode Vcard',icon='qrcode.ico',size=(500,500), element_justification='center', layout=layout, finalize=True)


def janela_baixar_wifi(cor_exter, cor_inter):
    layout = [
        [sg.Text('Baixar QrCode WIFI')],
        [sg.Text(f'QrCode para {item_escolhido}')],
        [sg.Text('Insira abaixo o nome do wifi')],
        [sg.Input(key='link_user')],
        [sg.Text('Insira abaixo a senha do wifi')],
        [sg.Input(key='link_senha')],
        [sg.Image(f'./img/{cor_exter}-{cor_inter}.png')],
        [sg.Button('Voltar'), sg.Button('Baixar')]
    ]
    return sg.Window('Baixar QrCode WIFI',icon='qrcode.ico',size=(500,500), element_justification='center', layout=layout, finalize=True)


pagina_inicial_, pagina_dois_, janela_img_, janela_baixar_url_, janela_baixar_vcard_, janela_baixar_wifi_ = pagina_inicial(), None, None, None, None, None


item_escolhido = ''

while True:
    window, event, values = sg.read_all_windows()
    if event == sg.WIN_CLOSED:
        break
    elif window == pagina_inicial_:
        if event == 'Iniciar':
            for x, y in values.items():
                if y is True:
                    item_escolhido = x
                    pagina_inicial_.close()
                    pagina_dois_ = pagina_dois(item_escolhido)

    elif window == pagina_dois_:
        if event == 'Visualizar':
            cont = 0
            exter = ''
            inter = ''
            for x, y in values.items():
                if cont == 0:
                    exter = y
                    cont += 1
                elif cont == 1:
                    inter = y
                cont == 0
            janela_img_ = janela_img(exter, inter)
            pagina_dois_.hide()

    elif window == janela_img_:
        if event == 'Voltar':
            pagina_dois_.un_hide()
            janela_img_.hide()

        elif event == 'Próximo':
            if item_escolhido == 'url':
                janela_baixar_url_ = janela_baixar_url(exter, inter)
                janela_img_.hide()
            elif item_escolhido == 'text':
                janela_baixar_url_ = janela_baixar_url(exter, inter)
                janela_img_.hide()
            elif item_escolhido == 'instagram':
                janela_baixar_url_ = janela_baixar_url(exter, inter)
                janela_img_.hide()
            elif item_escolhido == 'facebook':
                janela_baixar_url_ = janela_baixar_url(exter, inter)
                janela_img_.hide()

            elif item_escolhido == 'vcard':
                janela_baixar_vcard_ = janela_baixar_vcard(exter, inter)
                janela_img_.hide()
            elif item_escolhido == 'wifi':
                janela_baixar_wifi_ = janela_baixar_wifi(exter, inter)
                janela_img_.hide()

    elif window == janela_baixar_url_:
        if event == 'Voltar':
            janela_img_.un_hide()
            janela_baixar_url_.hide()
        
        elif event == 'Baixar':
            link_passado = values['link_url']
            thread_arquivo1 = Thread(target=criar_qr.qr_basic1,
                                args=(link_passado, exter, inter), daemon=True)
            thread_arquivo1.start()
            sleep(1)
            break
    
    elif window == janela_baixar_vcard_:
        if event == 'Voltar':
            janela_img_.un_hide()
            janela_baixar_vcard_.hide()
        
        elif event == 'Baixar':
            user = values['link_nome']
            email = values['link_email']
            telefone = values['link_telefone']
            empresa = values['link_empresa']
            thread_arquivo3 = Thread(target=criar_qr.qr_vcard,
                                args=(user, email, telefone, empresa, exter, inter), daemon=True)
            thread_arquivo3.start()
            sleep(1)
            break


    elif window == janela_baixar_wifi_:
        if event == 'Voltar':
            janela_img_.un_hide()
            janela_baixar_wifi_.hide()
        
        elif event == 'Baixar':
            user = values['link_user']
            senha = values['link_senha']


            thread_arquivo2 = Thread(target=criar_qr.qr_wifi,
                                args=(user, senha, exter, inter), daemon=True)
            thread_arquivo2.start()
            sleep(1)
            break
