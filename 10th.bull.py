# -*- coding : 'UTF-8' -*-

def calElement(preivous):
	'''Calculate Sequence Element'''

	i = 0
	now = preivous[0]
	listTemp = [[preivous[0], 0]]
	strResult = ''

	for ch in preivous:
		#print(listTemp)
		if(ch == now):
			listTemp[i][1] = listTemp[i][1] + 1
		else:
			listTemp.append([ch, 1])
			now = ch
			i = i + 1

	for l in listTemp:
		strResult = strResult + str(l[1]) + l[0]

	return(strResult)
	

if __name__ == '__main__':

	strInit = '1'

	for i in range(1, 31):
		print(strInit)
		strInit = calElement(strInit)

	print(strInit)
	print(len(strInit))