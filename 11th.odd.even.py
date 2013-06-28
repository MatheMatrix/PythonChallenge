# -*- coding : 'utf-8' -*-

from PIL import Image
from PIL import ImageDraw

strImagePath = 'E:\\PythonLearning\\PythonChallenge\\11th.cave.jpg'

imOrigin = Image.open(strImagePath)
tupleSize = (int(imOrigin.size[0] / 2), int(imOrigin.size[1] / 2))
imNew = Image.new(imOrigin.mode, tupleSize)
imDraw = ImageDraw.Draw(imNew)

for i in range(0, imOrigin.size[0], 2):
	for j in range(0, imOrigin.size[1], 2):
		tuplePoint = (i, j)
		tupleColor = imOrigin.getpixel(tuplePoint)
		tuplePointFix  = (i / 2, j / 2)
		imDraw.point(tuplePointFix, fill = tupleColor)

imNew.save('11th.cave.even.even.jpg')

for i in range(1, imOrigin.size[0], 2):
	for j in range(1, imOrigin.size[1], 2):
		tuplePoint = (i, j)
		tupleColor = imOrigin.getpixel(tuplePoint)
		tuplePointFix  = (int((i - 1) / 2), int((j - 1) / 2))
		imDraw.point(tuplePointFix, fill = tupleColor)

imNew.save('11th.cave.odd.odd.jpg')

for i in range(0, imOrigin.size[0], 2):
	for j in range(1, imOrigin.size[1], 2):
		tuplePoint = (i, j)
		tupleColor = imOrigin.getpixel(tuplePoint)
		tuplePointFix  = (i / 2, int((j - 1) / 2))
		imDraw.point(tuplePointFix, fill = tupleColor)

imNew.save('11th.cave.even.odd.jpg')

for i in range(1, imOrigin.size[0], 2):
	for j in range(0, imOrigin.size[1], 2):
		tuplePoint = (i, j)
		tupleColor = imOrigin.getpixel(tuplePoint)
		tuplePointFix  = (int((i - 1) / 2), j / 2)
		imDraw.point(tuplePointFix, fill = tupleColor)

imNew.save('11th.cave.odd.even.jpg')