import requests
from datetime import datetime, timedelta
import json
import collections
import pprint
import time


BASE_URL = 'https://api.stackexchange.com'
START = (datetime.now() - timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0)
END = START + timedelta(days=1)
print(f'Start: {START}, end: {END}')
JSON_01 = f'./data/questions_{START.strftime("%Y%m%d")}.json'
SLEEP = 20


def main():

    # Make parameters
    site = 'stackoverflow'
    fromdate = int(START.timestamp())
    todate = int(END.timestamp())
    sort = 'popular'
    order = 'desc'
    pagesize = 100
    page = 1
    has_more = True

    # Make HTTP request
    items = []
    r = requests.get(
        url=f'{BASE_URL}/2.3/tags?'
            f'site={site}'
            f'&fromdate={fromdate}&todate={todate}'
            f'&sort={sort}&order={order}'
            f'&page={page}&pagesize={pagesize}'
    )
    print(f'Status code: {r.status_code}')
    pprint.pprint(r.json())
    print(f'Quota remaining: {r.json()["quota_remaining"]}')


if __name__ == '__main__':
    main()
