import asyncio

async def say_hello():
    print('Hello')
    

event_loop = asyncio.new_event_loop()
asyncio.set_event_loop(event_loop)
event_loop.run_until_complete(say_hello())
event_loop.close()



# OR

#asyncio.run(say_hello())  