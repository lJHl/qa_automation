from pyzbar.pyzbar import decode
from PIL import Image


class QRReader:
    @staticmethod
    def read_qr(path):
        barcode = decode(Image.open(path))[0]
        return {'data': barcode[0].decode('utf-8'), 'type': barcode[1], 'rect': barcode[2], 'polygon': barcode[3]}
