from PIL import Image
import imagehash


class CheckImage:

    @staticmethod
    def compare_two_pictures(img_1, img_2):
        im_1 = Image.open(img_1)
        im_2 = Image.open(img_2)
        hash = imagehash.average_hash(im_1)
        another_hash = imagehash.average_hash(im_2)
        if hash - another_hash == 0:
            return True
        else:
            return False
