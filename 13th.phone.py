import xmlrpc.client

proxy = xmlrpc.client.ServerProxy('http://www.pythonchallenge.com/pc/phonebook.php')

proxy.system.listMethods()
proxy.system.methodHelp('phone')

try:
	proxy.phone('Bert')
except xmlrpc.client.Fault as err:
	print("A fault occurred")
	print("Fault code: %d" % err.faultCode)
	print("Fault string: %s" % err.faultString)