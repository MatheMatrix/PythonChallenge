# -*- coding : 'utf-8' -*-

from PIL import Image
from PIL import ImageDraw

def GetPointCoord(tupleLastPoint, intOrient):
	'''
	输入描绘的上一个点的坐标(tuple)和下面要描绘的方向(int)，
	返回下一个要描绘的点的坐标(tuple)
	'''

	if intOrient == 0:
		tupleTargetPoint = (tupleLastPoint[0] + 1, tupleLastPoint[1])
	elif intOrient == 1:
		tupleTargetPoint = (tupleLastPoint[0], tupleLastPoint[1] + 1)
	elif intOrient == 2:
		tupleTargetPoint = (tupleLastPoint[0] - 1, tupleLastPoint[1])
	elif intOrient ==3:
		tupleTargetPoint = (tupleLastPoint[0], tupleLastPoint[1] - 1)

	return tupleTargetPoint


listTemp = []
intSum = 0
strPath = 'E:\\PythonLearning\\PythonChallenge\\'

for i in range(98, -1, -2):
	listTemp.append([i+2, i+1, i+1, i])

for l in listTemp:
	for i in l:
		intSum = intSum + i 		#验证下这个和是不是确实是10000

print(listTemp)
print(intSum)

imOrigin = Image.open(strPath + '14th.wire.png')
imNew = Image.new(imOrigin.mode, (100, 100))
imDraw = ImageDraw.Draw(imNew)

listPoint = [0, 0]
k = 0
m = 1

for l in listTemp:
	for i in range(0, 4):
		for j in range(0, l[i]):
			tupleColor = imOrigin.getpixel((k, 0))
			imDraw.point((listPoint[0], listPoint[1]), fill = tupleColor)
			tuplePoint = GetPointCoord((listPoint[0], listPoint[1]), i)
			listPoint = [tuplePoint[0], tuplePoint[1]]
			k = k + 1
	imNew.save(strPath + '14th.wire.new\\' + '14.wire.new.part{0}.png'.format(m))
	m = m + 1

imNew.save('14th.wire.new.png')