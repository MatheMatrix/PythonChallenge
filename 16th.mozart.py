# -*- coding : utf-8 -*-

from PIL import Image
from PIL import ImageDraw

def FindColor(imFile, intY, tupleColor, intLength):
	'''Find the Pink bar
	'''

	for i in range(0, imFile.size[0]):
		j = i
		count = 0
		for i in range(j, j + intLength):
			if imFile.getpixel((i, intY)) == tupleColor:
				count += 1
		if count == intLength:
			return (j, i)

def ShiftImage(imFile, imDraw, tupleStart, tupleEnd, intShiftLength):
	'''Shift Image's 1 row to Right with intShiftLength
	'''

	for i in range(tupleStart[0], tupleEnd[0] + 1):
		tupleColor = imFile.getpixel((i, tupleStart[1]))
		if i + intShiftLength > imFile.size[0] - 1:
			imDraw.point((i + intShiftLength - imFile.size[0] - 1, tupleStart[1]), fill = tupleColor)
		else:
			imDraw.point((i + intShiftLength, tupleStart[1]), fill = tupleColor)

strPath = 'E:\\PythonLearning\\PythonChallenge\\'

imOrigin = Image.open(strPath + '16th.mozart.1.bmp')	# gif图片是8位色 用python写入时 8位色总是灰阶 所以我用convert函数把它转成RGB的bmp格式了
imNew = Image.new(imOrigin.mode, imOrigin.size)
imDraw = ImageDraw.Draw(imNew)

tuplePinkColor = imOrigin.getpixel((73, 13))

for y in range(0, imOrigin.size[1]):
	tuplePinkBar = FindColor(imOrigin, y, tuplePinkColor, 5)
	ShiftImage(imOrigin, imDraw, (0, y), (tuplePinkBar[1] + 1, y), imOrigin.size[0] - 1 - tuplePinkBar[1] - 1)
	ShiftImage(imOrigin, imDraw, (tuplePinkBar[1] + 2, y), (imOrigin.size[1] - 1, y), imOrigin.size[0] - 1 - tuplePinkBar[1])

imNew.save('16th.mozart.2.bmp')
