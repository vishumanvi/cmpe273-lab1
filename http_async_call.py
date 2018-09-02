import asyncio
import time
import grequests

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
		f.write("\n Date - ASync using grequests: " + dateinHeader)
		f.close()
	except FileNotFoundError:
		print("Caught a file exception")
		pass

# this function uses grequests to invoke async non-blocking requests to the siteURLs
def readDatefromSiteHeader():
	try:
		request = (grequests.get(url) for url in siteURLs)
		responses = grequests.map(request)
	except ConnectionError:
		print("Caught a connection exception")
		pass

	for response in responses:
			writeToFile(response.headers['Date'])


# invoking above functions. check out the time taken. It's a cool saving of over 400%!
startTime = time.time()
readDatefromSiteHeader()
elapsedTime = time.time() - startTime

print("Total time taken for ASync using grequests is : %4.2f " % elapsedTime + "secs")
