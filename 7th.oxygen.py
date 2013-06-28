# -*- coding : 'utf-8' -*-

from PIL import Image									# Pillow 2.0.0
import re

path = 'E:\\PythonLearning\\PythonChallenge\\'
im = Image.open(path + '7th.oxygen.png')
strTemp = ''

for i in range(0, 629, 7):
	print(chr(im.getpixel((i, 45))[0]), end = '')		# 0 or 1 or 2 all of them are ok.
	strTemp = strTemp + chr(im.getpixel((i, 45))[0])

print()

for i in re.findall(r'\d{3}', strTemp):
	print(chr(int(i)), end = '')