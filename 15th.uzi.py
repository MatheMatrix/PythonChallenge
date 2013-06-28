# -*- coding : 'utf-8' -*-

# Gauss Formula

def CalWeekNumber(strDate): 		#strDate:'YYYYMMDD'
	intDate = int(strDate[-2] + strDate[-1])
	intMonth = int(strDate[-4] + strDate[-3]) - 2
	intYear = int(strDate[2] + strDate[3])
	intCentury = int(strDate[0] + strDate[1])

	if intMonth < 1:
		intMonth = 12 + intMonth
		intYear = intYear - 1

	intWeek = (intDate + int(2.6 * intMonth - 0.2) + \
		5 * (intYear % 4) + 3 * intYear + 5 * (intCentury % 4)) % 7

	return intWeek


def IsLeapYear(strYear):
	if (strYear % 400 == 0):
		return 1
	elif (strYear % 4 == 0) and (strYear % 100 != 0):
		return 1
	else:
		return 0


for i in range(1006, 2000, 10):
	strDate = str(i) + '0127'
	if (CalWeekNumber(strDate) == 2) and (IsLeapYear(i) == 1):
		print(strDate)