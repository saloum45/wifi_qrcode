import pyqrcode
from pyqrcode import QRCode
ssid="put your wifi password"
security="WPA2"
password="put your password"

qr=pyqrcode.create(f'WIFI:S:{ssid};T:{security};P:{password};;')
qr.png('FALLBOX_QR_CODE.png', scale=6, module_color='#954567')
