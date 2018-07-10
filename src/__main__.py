from PIL import Image


def filter_color( im):
    #(r,g,b) = rgb
    source = im.split()
    R, G, B = 0, 1, 2
    getRed = source[R]
    mask = getRed.point(lambda i: i > 100 and 255)

    print(getRed)
    getGreen = source[G].point(lambda i: 0)
    getBlue = source[B].point(lambda i: 0)

    #getGreen.show()
    #getRed.show()

    res = Image.merge(im.mode, (mask,getGreen,getBlue))
    other = Image.merge(im.mode, (getRed,getGreen,getBlue))
    other.show()
    res.show()


if __name__ == "__main__":
    im = Image.open("../pics/flower.JPG")
    filter_color(im)
