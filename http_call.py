import requests
import time

siteURLs = ["https://webhook.site/b84e2881-97fb-4d94-bb82-d69d72217536",
			"https://webhook.site/b84e2881-97fb-4d94-bb82-d69d72217536",
			"https://webhook.site/b84e2881-97fb-4d94-bb82-d69d72217536",
			"https://webhook.site/b84e2881-97fb-4d94-bb82-d69d72217536",
			"https://webhook.site/b84e2881-97fb-4d94-bb82-d69d72217536"
		]

# this function writes response header date field to output.txt file
def writeToFile(dateinHeader):
	try:
		f = open("output.txt", 'a')
		f.write("\n Date - Sync using requests: " + dateinHeader)
		f.close()
	except FileNotFoundError:
		print("Caught a file exception")
		pass

# this function uses requests to invoke sync blocking requests to the siteURLs
def readDatefromSiteHeader():
	try:
		for siteURL in siteURLs:
			r = requests.get(siteURL)
			writeToFile(r.headers['Date'])
	except ConnectionError:
		print("Caught a connection exception")
		pass

'''
invoke above functions to connect to siteURLs and write to output.txt file.
Check out the time taken
'''

startTime = time.time()
readDatefromSiteHeader()
elapsedTime = time.time() - startTime

print("Total time taken for Sync calls is : %4.2f" % elapsedTime + "secs")
