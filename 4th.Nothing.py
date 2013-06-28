import httplib2

strNothing = ''
lstTemp =[]

h = httplib2.Http('.cache')

for i in range(1, 200):
	if(i/200 *100 % 10 == 0):
		print(i/200*100, '%')

	strURL = \
		"http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + strNothing
	response, content = \
	  h.request(strURL)
	strCont = content.decode('utf-8')
	strNothing = strCont.split()[-1]
	lstTemp.append(strNothing)
	if(strNothing.isdigit() == False):
		break

print('Finished at ', i/200*100, '%')
print(lstTemp)