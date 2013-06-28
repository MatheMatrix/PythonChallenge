strPath = 'E:\\PythonLearning\\PythonChallenge\\'

listImage = [b'', b'', b'', b'', b'']

with open(strPath + '12th.evil2.gfx', 'rb') as fileEvil:
	data = fileEvil.read()			# 检查这个文件的大小
	fileEvil.seek(0)				# 重新定位到开头
	intLen = len(data)
	for i in range(0, intLen):
		listImage[i % 5] = listImage[i % 5] + fileEvil.read(1)


for i in range(0, 5):
	with open(strPath + '12th.evil2.part{0}.jpg'.format(i), 'wb') as fileTemp:
		fileTemp.write(listImage[i])