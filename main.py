import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image
qr =pyqrcode.create("Shakhin Coder")
qr.png("MeinCode.png", scale=8)