import asyncio
import multiprocessing
from datetime import datetime

import aiohttp
from bs4 import BeautifulSoup as bs

from const import URI, URL, finder_attrs
from sql_app.crud import creat_rows
from utils import convert_date, prepare_datetime


class Parser:
    @staticmethod
    def parse_html(text: str) -> list:
        soup = bs(text, 'html.parser')
        tr_tag = soup.find('table', attrs=finder_attrs).find_all('tr')
        # news_tr_tag XPath: /html/body/table[2]/tbody/tr/td[3]/table/tbody/tr/td/font/center/table[2]
        news_tr_tags = [{'preview_tr_tag': elem.contents[0], 'content_tr_tag': elem.contents[1]} for elem in tr_tag]
        return news_tr_tags

    @staticmethod
    def parse_content(news_tr_tags: list) -> list:
        result = list()
        for tr_tags in news_tr_tags:
            uri = None
            if tr_tags['preview_tr_tag'].contents:
                img_tag = tr_tags['preview_tr_tag'].contents[0].find('img')
                uri = URL + img_tag['src']

            content = tr_tags['content_tr_tag']
            a_tag = content.find('a')
            b_tag = content.find('b')

            title = a_tag.b.text
            date_str = b_tag.text
            time_str = b_tag.next_sibling
            full_date = prepare_datetime(date_str, time_str)
            unix_created = convert_date(full_date)
            href = a_tag.attrs['href'].strip()
            actual_ts = int(datetime.utcnow().timestamp())
            result.append({
                'title': title,
                'uri_picture': uri,
                'posted': unix_created,
                'uri_post': URL + href,
                'parsed': actual_ts})
        return result


async def run_parser():
    while True:
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False)) as session:
            try:
                async with session.get(URI) as response:
                    text = await response.text()
                    news_tr_tags = Parser.parse_html(text)
                    result = Parser.parse_content(news_tr_tags)
                    await creat_rows(result)
            except aiohttp.ClientConnectorError as error:
                print(f'Connection error {error}')
        await asyncio.sleep(600)


def runner_parser():
    print(multiprocessing.current_process())
    asyncio.run(run_parser())
