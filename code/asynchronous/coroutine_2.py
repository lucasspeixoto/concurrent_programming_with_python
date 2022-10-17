import asyncio
from typing import final

async def wait_say_hello():
    print('Hello')
    
    await asyncio.sleep(2)
    
    print('All')
    
""" 
event_loop = asyncio.new_event_loop()
asyncio.set_event_loop(event_loop)
try:
    asyncio.run(wait_say_hello())
except KeyboardInterrupt:
    pass
finally:
    event_loop.close()
"""
    

event_loop = asyncio.new_event_loop()
asyncio.set_event_loop(event_loop)
event_loop.run_until_complete(wait_say_hello())
event_loop.close()


#asyncio.run(wait_say_hello())  