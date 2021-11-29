from PIL import Image

image = Image.open(imageLocation)
pixels = image.load()
size_w, size_h = image.size

def rgb_to_hsv(r, g, b):
    r, g, b = r/255.0, g/255.0, b/255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx-mn
    if mx == mn:
        h = 0
    elif mx == r:
        h = (60 * ((g-b)/df) + 360) % 360
    elif mx == g:
        h = (60 * ((b-r)/df) + 120) % 360
    elif mx == b:
        h = (60 * ((r-g)/df) + 240) % 360
    if mx == 0:
        s = 0
    else:
        s = (df/mx)*100
    v = mx*100
    return h, s

colors = []
for h in range(size_h):
    for w in range(size_w):
        try:
            r, g, b = image.getpixel((h, w))
        except:
            pass
        hue = rgb_to_hsv(r, g, b)[0]
        saturation = rgb_to_hsv(r, g, b)[1]
        brightness = sum([r, b, g]) // 3
        colors.append(((hue, saturation, brightness), (r, g, b)))

def make_hue():
    global colors

    color_index = len(colors)
    colors1 = sorted(colors, key=lambda x: (x[0][0]))
    for h in range(size_h):
        for w in range(size_w):
            pixels[w, h] = colors1[color_index-1][1]
            color_index -= 1
    image.save(hueSaveLocation)

def make_saturation():
    global colors

    color_index = len(colors)
    colors1 = sorted(colors, key=lambda x: (x[0][1]))
    for h in range(size_h):
        for w in range(size_w):
            pixels[w, h] = colors1[color_index-1][1]
            color_index -= 1
    image.save(saturationSaveLocation)

def make_brightness():
    global colors

    color_index = len(colors)
    colors3 = sorted(colors, key=lambda x: (x[0][2]))
    for h in range(size_h):
        for w in range(size_w):
            pixels[w, h] = colors3[color_index-1][1]
            color_index -= 1
    image.save(brightnessSaveLocation)

make_hue()
make_saturation()
make_brightness()
