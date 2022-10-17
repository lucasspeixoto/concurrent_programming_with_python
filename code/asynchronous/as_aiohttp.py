import asyncio
import aiofiles
import aiohttp
import bs4

links_path: str = "code/asynchronous/links.txt"


async def get_links() -> list[str]:
    links: list[str] = []

    async with aiofiles.open(links_path) as file:
        async for link in file:
            links.append(link.strip())

    return links


async def get_html(link: str) -> bs4.Doctype:
    print(f"Getting html of course {link}")

    async with aiohttp.ClientSession() as session:
        async with session.get(link) as resp:
            resp.raise_for_status()

            return await resp.text()


def get_page_title(html) -> str:

    soup = bs4.BeautifulSoup(html, "html.parser")

    title = soup.select_one("title")
    
    title = title.text.split("|")[0].strip()

    return title


async def print_titles():
    links = await get_links()
    tasks = []
    for link in links:
        new_task = asyncio.create_task(get_html(link))
        tasks.append(new_task)
    for task in tasks:
        html = await task

        title = get_page_title(html)

        print(f"Course: {title}")


def main():
    event_loop = asyncio.new_event_loop()
    asyncio.set_event_loop(event_loop)

    event_loop.run_until_complete(print_titles())

    event_loop.close()


if __name__ == "__main__":
    main()
