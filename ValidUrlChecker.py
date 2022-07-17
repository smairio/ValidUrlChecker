
#Usage : python checker.py file.txt
import sys
import requests
from bs4 import BeautifulSoup
r = open(sys.argv[1],"r")
urls = r.readlines()

for url in urls:
	url=url[:-1]
	try:
		reqs=requests.get(url,timeout=3)
	except requests.Timeout as err:
		print(url+": time out")
	except Exception as err:
		print("ignoring failed URL")
	else:
		if(reqs.status_code == 200):
			soup = BeautifulSoup(reqs.text,'html.parser')
			for title in soup.find_all('title'):
				print(url+": "+title.get_text())
				with open("result.txt","a",encoding="utf-8") as f:
					f.write(url+": "+str(reqs.status_code)+" |"+title.get_text())
					f.write('\n')
					f.close()
		else:
			print(url+": "+ str(reqs.status_code))
