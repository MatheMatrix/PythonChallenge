# -*- coding : 'utf-8' -*-

import zipfile

lstTemp = []
lstComments = []

path = 'E:\\PythonLearning\\PythonChallenge\\6th.Channel.zip\\'
strTemp2 = '90052'

for i in range(1, 910):

	if( i / 909 * 100 % 10 < 0.1):
		print('============ Now procession: ', i / 910 * 100 , '% ============')

	zipFile = zipfile.ZipFile(path + 'channel.zip')

	strPath = path + strTemp2 + '.txt'

	with open(strPath, 'r') as fileNothing:
		strTemp1 = fileNothing.readline()
		strTemp2 = strTemp1.split()[-1]
		lstTemp.append(strTemp2)

		if(strTemp2.isdigit() == False):
			break
		lstComments.append(zipFile.getinfo(strTemp2 + '.txt').comment.decode('utf-8'))


print('===========Finished===========')
print(lstTemp)
print()
for ch in lstComments:
	print(ch, end = '')