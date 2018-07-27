import time
from datetime import datetime as dt

hosts_path = "/etc/hosts"
redirect = "127.0.0.1"
websites_list = ["www.facebook.com","facebook.com","twitter.com"]
start_time = 8
end_time = 16

while True:
	if dt(dt.now().year,dt.now().month,dt.now().day,start_time)< dt.now()< dt(dt.now().year,dt.now().month,dt.now().day,end_time):
		with open(hosts_path,'r+') as file:
			content = file.read()
			for website in websites_list:
				if website in content:
					pass
				else:
					file.write(redirect + "\t" + website + "\n")
			print("Work Hours")
	else:
		with open(hosts_path,'r+') as file:
			content = file.readline()
			file.seek(0)
			for line in content:
				if not any(website in line for website in websites_list):
					file.write(line)
			file.truncate()
		print("Fun hours")
	time.sleep(5)
