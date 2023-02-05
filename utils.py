import re
import time
from datetime import datetime, timedelta

from bs4 import NavigableString, Tag


def convert_date(full_date: str) -> int:
    '''
    Конвертируем дату в unix time. В часовом поясе UTC.
    :param full_date: str: ex '02.02.2023-01:20'
    :return: int
    '''
    local_date = time.strptime(full_date, '%d.%m.%Y-%H:%M')
    local_ts = time.mktime(local_date)
    utc_date = time.gmtime(local_ts)
    unix_created = int(time.mktime(utc_date))
    return unix_created


def prepare_datetime(date_str: str | None, time_str: NavigableString | None) -> str:
    """
    собираем дату и время воедино. Дата соответствует локальному времени.
    :param date_str: str | None
    :param time_str: str | None
    :return: str: ex '02.02.2023-01:20'
    """
    date_pattern = r'\d{2}.\d{2}.\d{4}'
    time_pattern = r'\d{2}:\d{2}'
    if date_str is None:
        date_str = datetime.now().strftime('%d.%m.%Y')
    if time_str is None or isinstance(time_str, Tag):
        time_str = '00:00'
    date_str = re.search(date_pattern, date_str)
    time_str = re.search(time_pattern, time_str)
    if time_str is None:
        time_str = '00:00'
    else:
        time_str = time_str.group()
    if date_str:
        return date_str.group() + '-' + time_str
    return datetime.now().strftime('%d.%m.%Y') + '-' + time_str


def get_unixtime(day: int) -> int:
    '''
    высчитывает дату согласно указаному лиммиту, колиество дней назад
    возвращает unix time в локальном поясе.
    :param day: int
    :return: int
    '''
    delta = timedelta(days=day)
    prev_day = datetime.today() - delta
    rounded_day = prev_day.replace(hour=0, minute=0, second=0,microsecond=0)
    ts_prev_day = int(rounded_day.timestamp())
    return ts_prev_day
