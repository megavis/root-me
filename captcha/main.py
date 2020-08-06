#!/usr/bin/env python3

import pytesseract

import requests
import io, base64
from PIL import Image

flag_phrase = "retente ta chance."

def get_img_bounds(text):
   start = r.text.find("data:image/png;base64,") 
   end = r.text.find("\" /><br><br>")
   return [start, end]

with requests.Session() as session:
    url = "http://challenge01.root-me.org/programmation/ch8/"

    for retry in range(30):
        r=session.get(url)

        start, end = get_img_bounds(r.text)
        img64 = r.text[start+22:end]

        buf = io.BytesIO(base64.b64decode(img64))
        img = Image.open(buf)
        img.show()
        img.save("captcha.png")

        num = pytesseract.image_to_string(img)
        for c in "()[]\'\"{}~=-: .":
            num = num.replace(c, "")

        print(f"[+] trying '{num}'")
        r = session.post(url, data={ "cametu" : num})

        start, end = get_img_bounds(r.text)
        if r.text.find(flag_phrase) < 0:
            print(r.text[:start], r.text[end:])

