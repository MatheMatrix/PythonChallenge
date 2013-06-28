import httplib2

strNothing = ''
lstTemp =[]

h = httplib2.Http('.cache')

for i in range(1, 500):
	if(i/500 *100 % 10 == 0):
		print(i/500*100, '%')

	strURL = \
		"http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=" + strNothing
	response, content = \
	  h.request(strURL)
	strCont = content.decode('utf-8')
	strNothing = strCont.split()[-1]

	if strNothing in lstTemp:
		lstTemp.append(strNothing)
		break

	lstTemp.append(strNothing)
	
	if(strNothing.isdigit() == False):
		break

print('Finished')
print(lstTemp)