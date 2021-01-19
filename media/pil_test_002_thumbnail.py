from PIL import Image


if __name__ == '__main__':

    im = Image.open('D:\\images\\Normal\\default.jpg')
    w, h = im.size
    print('Original image size: %sx%s' % (w, h))
    im.thumbnail((w//4, h//4))
    print('Resize image to: %sx%s' % (w//4, h//4))
    im.save('D:\\images\\Normal\\thumbnail.jpg', 'jpeg')
