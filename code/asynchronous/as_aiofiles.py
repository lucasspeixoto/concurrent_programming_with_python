import asyncio
import aiofiles

text_path: str = "code/asynchronous/text.txt"

async def example_file1():
    async with aiofiles.open(text_path) as file:
        content = await file.read()

    print(content)


async def example_file2():
    async with aiofiles.open(text_path) as file:
        async for line in file:
            print(line)


def main():
    event_loop = asyncio.new_event_loop()
    asyncio.set_event_loop(event_loop)

    event_loop.run_until_complete(example_file2())

    event_loop.close()


if __name__ == "__main__":
    main()
