from bs4 import Tag

import pytest
from freezegun import freeze_time
from core_parser import convert_date
from utils import prepare_datetime

from utils import get_unixtime


@freeze_time('2023-02-03', tz_offset=3)
@pytest.mark.parametrize(
    'value, expected', [
        ({'date_str': '  02.03.2023  ', 'time_str': '12:34'}, '02.03.2023-12:34'),
        ({'date_str': '<tr>02.03.2023</tr>', 'time_str': '<p> 02:34 </p>'}, '02.03.2023-02:34'),
        ({'date_str': '<br>', 'time_str': '01:00'}, '03.02.2023-01:00'),
        ({'date_str': None, 'time_str': None}, '03.02.2023-00:00'),
        ({'date_str': '02.03.2023', 'time_str': '<br>'}, '02.03.2023-00:00'),
        ({'date_str': '<br>', 'time_str': '<br>'}, '03.02.2023-00:00'),
        ({'date_str': '<br>', 'time_str': Tag(name='<br>')}, '03.02.2023-00:00'),
    ],
)
def test_prepare_datetime(value, expected):
    result = prepare_datetime(**value)
    assert result == expected


@freeze_time('2023-02-02', tz_offset=3)
@pytest.mark.parametrize(
    'value, expected', [
        ('02.02.2023-13:34', 1675323240),
        ('02.02.2023-00:00', 1675274400),
        ('02.02.2023-01:00', 1675278000),
        ('02.02.2023-01:00', 1675278000),
    ],
)
def test_convert_date(value, expected):
    '''Проверяем возращаемый timestamp. С учетомм UTC'''
    result = convert_date(value)
    assert result == expected

@freeze_time('2023-02-06 10:17:00', tz_offset=3)
@pytest.mark.parametrize(
    'day, expected', [(5, 1675198800), (4, 1675285200)])
def test_get_unixtime(day, expected):
    '''
    Проверяем определение предыдущей даты согласно заданому лимиту.
    day количество дней назад.
    '''
    result = get_unixtime(day)
    assert result == expected
