## 1 uzduotis ###
from PIL import Image

img = Image.open("/DaysgoBy/logo.png")

width, height = img.size
left = (width - 128) // 2
top = (height - 72) // 2
right = left + 128
bottom = top + 72

line = (left, top, right, bottom)
region = img.crop(line)
region.show()

new_filename = "/DaysgoBy/naujaslogis.png"
region.save(new_filename)
##### 2 uzduotis
from PIL import Image, ImageFilter, ImageEnhance


def redaguoti_paveiksleli(paveikslas, kontrastas, spalvingumas, astrumas, ryskumas, issaugoti=False):
    img = Image.open(paveikslas)

    img.show()

    img_edited = img.copy()
    img_edited = ImageEnhance.Contrast(img_edited).enhance(kontrastas)
    img_edited = ImageEnhance.Color(img_edited).enhance(spalvingumas)
    img_edited = img_edited.filter(ImageFilter.SHARPEN)
    img_edited = ImageEnhance.Sharpness(img_edited).enhance(ryskumas)

    img_edited.show()

    if issaugoti:
        naujas_pavadinimas = paveikslas.split(".")[0] + "_modified." + paveikslas.split(".")[1]
        img_edited.save(naujas_pavadinimas)


paveikslelio_pavadinimas = "wolfas.jpg"
kontrastas = 1.5
spalvingumas = 1.2
astrumas = 1.0
ryskumas = 1.2

redaguoti_paveiksleli(paveikslelio_pavadinimas, kontrastas, spalvingumas, astrumas, ryskumas, issaugoti=True)
### 3 uzduotis #####
from PIL import Image
import os


def prideti_logo(nuotrauka, logotipas, aukstis):
    img = Image.open(nuotrauka)
    width, height = img.size
    naujas_plotis = int(width * (aukstis / height))
    img = img.resize((naujas_plotis, aukstis), Image.LANCZOS)
    logo = Image.open(logotipas)
    logo_width, logo_height = logo.size
    x = img.width - logo_width - 10
    y = img.height - logo_height - 10
    img.paste(logo, (x, y), logo)
    pavadinimas = os.path.splitext(nuotrauka)[0] + "_modified.jpg"
    img.save(pavadinimas, quality=90)


katalogas = "/Users/giedriuspranevicius/Desktop/Nuotrk"
logotipas = "/Users/giedriuspranevicius/mainbase/treciadienis/logo.png"
aukstis = 300

for failas in os.listdir(katalogas):
    if failas.endswith(".jpg") or failas.endswith(".jpeg") or failas.endswith(".png"):
        nuotrauka = os.path.join(katalogas, failas)
        prideti_logo(nuotrauka, logotipas, aukstis)

#### 4 uzduotis ####
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
r_korekcija = 50
g_korekcija = -20
b_korekcija = 30

koreguoti_nuotrauka(nuotrauka, r_korekcija, g_korekcija, b_korekcija)
##### 5 uzduotis #########
from PIL import Image


def pakeisti_spalvas(nuotrauka, r_riba, g_riba, b_riba):
    img = Image.open(nuotrauka).convert("RGB")
    width, height = img.size
    for x in range(width):
        for y in range(height):
            r, g, b = img.getpixel((x, y))
            if r > r_riba or g > g_riba or b > b_riba:
                img.putpixel((x, y), (0, 0, 0))
            else:
                img.putpixel((x, y), (255, 255, 255))
    img.save("pakeistariba_nuotrauka.jpg")


nuotrauka = "/Users/giedriuspranevicius/mainbase/treciadienis/wolfas.jpg"
r_riba = 150
g_riba = 120
b_riba = 180

pakeisti_spalvas(nuotrauka, r_riba, g_riba, b_riba)
