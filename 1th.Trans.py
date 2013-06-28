# -*- coding : utf-8 -*-

text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
trans = ''

for ch in text:
	if ord(ch) >= ord('a') and ord(ch) <= ord('z'):
		trans = trans + (chr(ord(ch) + 2) if ord(ch) + 2 <= ord('z') else chr(ord(ch) + 2 - 26))
	else:
		trans = trans + ch

print(trans)