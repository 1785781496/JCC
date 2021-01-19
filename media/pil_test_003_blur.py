from PIL import Image, ImageFilter

if __name__ == '__main__':

    im = Image.open('D:\\images\\Normal\\thumbnail.jpg')

    im2 = im.filter(ImageFilter.BLUR)
    im2.save('D:\\images\\Normal\\blur.jpg', 'jpeg')