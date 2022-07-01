# from svglib.svglib import svg2rlg
# from reportlab.graphics import renderPM
import cairosvg
from typing import List
from qrcodegen import QrCode, QrSegment
from ff3 import FF3Cipher

def ff3_encrypt():
	key = "2DE79D232DF5585D68CE47882AE256D6"
	tweak = "CBD09280979564"
	c = FF3Cipher(key, tweak)

	plaintext=input('Input Value : ')



def do_basic_demo() -> None:
    """Creates a single QR Code, then prints it to the console."""
    text = input('Input Value : ')   # User-supplied Unicode text
    errcorlvl = QrCode.Ecc.HIGH  # Error correction level

    # Make and print the QR Code symbol
    qr = QrCode.encode_text(text, errcorlvl)
    # print_qr(qr)
    print(to_svg_str(qr, 4))

def to_svg_png():
	cairosvg.svg2png(url='output/qr.svg',write_to='output/qrcode.png')


def to_svg_str(qr: QrCode, border: int) -> None:
	"""Returns a string of SVG code for an image depicting the given QR Code, with the given number
	of border modules. The string always uses Unix newlines (\n), regardless of the platform."""
	if border < 0:
		raise ValueError("Border must be non-negative")
	parts: List[str] = []
	for y in range(qr.get_size()):
		for x in range(qr.get_size()):
			if qr.get_module(x, y):
				parts.append(f"M{x+border},{y+border}h1v1h-1z")
	f=open('output/qr.svg','w+')
	f.write(f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<svg xmlns="http://www.w3.org/2000/svg" version="1.1" viewBox="0 0  {qr.get_size()+border*2} {qr.get_size()+border*2}" stroke="none">
	<rect width="100%" height="100%" fill="#FFFFFF"/>
	<path d="{" ".join(parts)}" fill="#000000"/>
</svg>
""")
	f.close()
	to_svg_png()
# 	return f"""<?xml version="1.0" encoding="UTF-8"?>
# <!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
# <svg xmlns="http://www.w3.org/2000/svg" version="1.1" viewBox="0 0  {qr.get_size()+border*2} {qr.get_size()+border*2}" stroke="none" style="width: 30em; height: 30em;">
# 	<rect width="100%" height="100%" fill="#FFFFFF"/>
# 	<path d="{" ".join(parts)}" fill="#000000"/>
# </svg>
# """
# <svg xmlns="http://www.w3.org/2000/svg" id="qrcode-svg" style="width: 30em; height: 30em;" stroke="none" viewBox="0 0 29 29">

def print_qr(qrcode: QrCode) -> None:
	"""Prints the given QrCode object to the console."""
	border = 4
	for y in range(-border, qrcode.get_size() + border):
		for x in range(-border, qrcode.get_size() + border):
			print("\u2588 "[1 if qrcode.get_module(x,y) else 0] * 2, end="")
		print()
	print()


if __name__ == "__main__":
    do_basic_demo()