import datetime
import asyncio


async def data_generator(quantity: int, data: asyncio.Queue):
    print(f"Wait for data generation of {quantity} data....")
    for index in range(1, quantity + 1):
        item = index * index
        await data.put((item, datetime.datetime.now()))
        await asyncio.sleep(0.0001)

    print(f"{quantity } data successfully generate")


async def process_data(quantity: int, data: asyncio.Queue):
    print(f"Wait for data process of {quantity} data!")
    processed = 0
    while processed < quantity:
        await data.get()
        processed += 1
        await asyncio.sleep(0.0001)

    print(f"Where successfully processed {quantity } items!")


def main():

    total = 300

    data = asyncio.Queue()
    
    print(f"Computing {total * 2:.2f} data")

    event_loop = asyncio.new_event_loop()
    asyncio.set_event_loop(event_loop)

    

    event_loop.run_until_complete(data_generator(total, data))
    event_loop.run_until_complete(data_generator(total, data))
    event_loop.run_until_complete(process_data(total * 2, data))

    event_loop.close()


if __name__ == "__main__":

    main()
