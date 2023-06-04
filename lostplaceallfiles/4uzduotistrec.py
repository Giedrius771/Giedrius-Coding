from PIL import Image


def koreguoti_nuotrauka(nuotrauka, r_korekcija, g_korekcija, b_korekcija):
    img = Image.open(nuotrauka)
    width, height = img.size
    for x in range(width):
        for y in range(height):
            r, g, b = img.getpixel((x, y))
            r = max(0, min(r + r_korekcija, 255))
            g = max(0, min(g + g_korekcija, 255))
            b = max(0, min(b + b_korekcija, 255))
            img.putpixel((x, y), (r, g, b))
    img.save("pakeista_nuotrauka.jpg")


nuotrauka = "/Users/giedriuspranevicius/mainbase/treciadienis/wolfas.jpg"
r_korekcija = 20
g_korekcija = -10
b_korekcija = 90

koreguoti_nuotrauka(nuotrauka, r_korekcija, g_korekcija, b_korekcija)
