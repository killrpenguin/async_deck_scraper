import asyncio
import aiohttp
from scrape_functions import scrape_moxfield, scrape_tappedout
import pandas as pd
from service_functions import log_scrape


def deck_scraper_main():
    tcp_connection = aiohttp.TCPConnector(limit=10)
    header = {"Authorization": "Basic bG9naW46cGFzcw=="}
    async with aiohttp.ClientSession(connector=tcp_connection, headers=header, trust_env=True) as session:
        try:
            tasks = [asyncio.create_task(scrape_moxfield(session=session, proxy=i web_link=i)) for i in proxy_list]
            for task in tasks:
                await task
        except Exception as e:
            print(e)
        try:
            tasks = [asyncio.create_task(scrape_tappedout(session=session, web_link=i)) for i in proxy_list]
            for task in tasks:
                await task
        except Exception as e:
            print(e)
        await asyncio.sleep(0)