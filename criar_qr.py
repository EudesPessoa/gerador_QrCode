import io
import segno
from PIL import Image
from segno import helpers
from qrcode_artistic import write_artistic
from urllib.request import urlopen
import os as sistema
import os


def qr_basic1(link, cor_externa, cor_interna):

    usuario = sistema.getlogin()
    qrcode = segno.make(link)

    os.chdir(os.path.join(os.path.expanduser('~'),'desktop'))

    if(os.path.exists('qrcode.png')):
            
        x = 0
        while True:
            if(os.path.exists(f'qrcode{x}.png')):
                x += 1
            else:
                arquivo1 = (f'qrcode{x}.png')
                break

        print(f"O arquivo {arquivo1} não existe")
        qrcode.save(arquivo1, scale=10, dark=cor_interna, light=cor_externa)
        ba = (f'C:/Users/{usuario}/Desktop/{arquivo1}')

    else:
        print("O arquivo não existe")
        qrcode.save(f"qrcode.png", scale=10, dark=cor_interna, light=cor_externa)
        ba = (f'C:/Users/{usuario}/Desktop/qrcode.png')


def qr_wifi(user, senha, cor_externa, cor_interna):
    wifi_setings = {
        'ssid': user,
        'password': senha,
        'security': 'WPA'
    }
    usuario = sistema.getlogin()
    wifi = helpers.make_wifi(**wifi_setings)

    os.chdir(os.path.join(os.path.expanduser('~'),'desktop'))

    if(os.path.exists('qrcode.png')):
            
        x = 0
        while True:
            if(os.path.exists(f'qrcode{x}.png')):
                x += 1
            else:
                arquivo1 = (f'qrcode{x}.png')
                break

        print(f"O arquivo {arquivo1} não existe")
        wifi.save(arquivo1, scale=10, dark=cor_interna, light=cor_externa)
        ba = (f'C:/Users/{usuario}/Desktop/{arquivo1}')

    else:
        print("O arquivo não existe")
        wifi.save(f"qrcode.png", scale=10, dark=cor_interna, light=cor_externa)
        ba = (f'C:/Users/{usuario}/Desktop/qrcode.png')


def qr_vcard(user, email, telefone, empresa, cor_externa, cor_interna):
    contato = {
        'name': user,
        'email': email,
        'telefone': telefone,
        'empresa' : empresa
}
    usuario = sistema.getlogin()
    vcard = helpers.make_mecard(contato)

    os.chdir(os.path.join(os.path.expanduser('~'),'desktop'))

    if(os.path.exists('qrcode.png')):
            
        x = 0
        while True:
            if(os.path.exists(f'qrcode{x}.png')):
                x += 1
            else:
                arquivo1 = (f'qrcode{x}.png')
                break

        print(f"O arquivo {arquivo1} não existe")
        vcard.save(arquivo1, scale=10, dark=cor_interna, light=cor_externa)
        ba = (f'C:/Users/{usuario}/Desktop/{arquivo1}')

    else:
        print("O arquivo não existe")
        vcard.save(f"qrcode.png", scale=10, dark=cor_interna, light=cor_externa)
        ba = (f'C:/Users/{usuario}/Desktop/qrcode.png')

