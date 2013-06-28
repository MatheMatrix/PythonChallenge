# -*- coding: utf-8 -*-

import pickle

with open('E:\\PythonLearning\\PythonChallenge\\3th.banner.p', 'rb') as f:
	banner = pickle.load(f)
	
for lstTemp in banner:
	for tupTemp in lstTemp:
		print(tupTemp[0] * tupTemp[-1], end = '')
	print()
