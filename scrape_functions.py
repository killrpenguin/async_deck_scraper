import asyncio
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import EdgeOptions


VALID_STATUSES = [200, 301, 302, 307, 404]

async def scrape_moxfield(*, session, proxy, web_link):
    try:
        async with session.get(web_link, proxy=proxy, ssl=False, timeout=600) as resp:
            a = await resp.text()
            if resp.status in VALID_STATUSES:

    except Exception as e:
        print("Exception: ", e)


async def scrape_tappedout(*, session, proxy, web_link):
    try:
        async with session.get(web_link, proxy=proxy, ssl=False, timeout=600) as resp:
            await resp.text()
            if resp.status in VALID_STATUSES:
                print('Status Code: ' + str(resp.status))
                set_working(proxy)
    except Exception as e:
        print("Exception: ", e)