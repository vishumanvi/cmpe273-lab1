import asyncio
import time
import aiohttp

siteURL = "https://webhook.site/b84e2881-97fb-4d94-bb82-d69d72217536"

# this async function writes response header date field to output.txt file
async def writeToFile(dateinHeader):
	try:
		f = open("output.txt", 'a')
		f.write("\n Date - ASync using asyncio, aiohttp: " + dateinHeader)
		f.close()
	except StopAsyncIteration:
		print("Caught an Async exception")
		pass

# this async function connects to siteURL and reads date field from header
async def readDatefromSiteHeader(task):
	try:
		async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
			response = await session.get(siteURL)
			await writeToFile(response.headers['Date'])
	except StopAsyncIteration:
		print("Caught an Async exception")
		pass

loop = asyncio.get_event_loop()

# each of the requests to the siteURL is created as a task
tasks = [
	asyncio.ensure_future(readDatefromSiteHeader("Task A")),
	asyncio.ensure_future(readDatefromSiteHeader("Task B")),
	asyncio.ensure_future(readDatefromSiteHeader("Task C")),
	asyncio.ensure_future(readDatefromSiteHeader("Task D")),
	asyncio.ensure_future(readDatefromSiteHeader("Task E")),
]

# invoking above functions. check out the time taken. It's a cool saving of over 400%!

startTime = time.time()
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

elapsedTime = time.time() - startTime

print("Total time taken for ASync with asyncio is : %4.2f" % elapsedTime + "secs")
