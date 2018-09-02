# cmpe273-lab1
Lab1: Demo of Sync and ASync calls to webhook.site

1. http_call.py: Uses requests library to make 5 blocking sync calls
2. http_async_call.py: Uses grequests library to make 5 non-blocking async calls
3. http_async_asyncio_variant.py: Uses asyncio and aiohttp libraries to make 5 non-blocking

As you notice on python console after running them, there's over 400% time saving on running the async over sync.
