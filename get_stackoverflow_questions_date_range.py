import requests
import pandas as pd
from dateutil.relativedelta import relativedelta
from datetime import datetime
import json
import collections
import pprint
import time


BASE_URL = 'https://api.stackexchange.com'
SITE = 'stackoverflow'
JSON_01 = './data/questions.json'
CSV_01 = './data/questions.csv'
START = datetime.now() - relativedelta(months=1)
END = datetime.now()
SLEEP = 20
print(f'Start: {START}, end: {END}')


def main():

    # Make parameters
    fromdate = int(START.timestamp())
    todate = int(END.timestamp())
    sort = 'votes'
    order = 'desc'
    pagesize = 100
    page = 10

    # Make HTTP requests
    items = []
    for i in range(1, page + 1):
        r = requests.get(
            url=f'{BASE_URL}/2.3/questions?site={SITE}'
                f'&fromdate={fromdate}&todate={todate}'
                f'&sort={sort}&order={order}'
                f'&page={i}&pagesize={pagesize}'
        )
        print(f'Status code: {r.status_code}')
        print(r.json())
        print(f'Quota remaining: {r.json()["quota_remaining"]}')
        items.extend(r.json()['items'])
        print(f'Sleeping {SLEEP} seconds...')
        time.sleep(SLEEP)
    data = {'items': items}

    # Save response
    with open(JSON_01, 'w') as f:
        json.dump(data, f)

    # Load data
    with open(JSON_01, 'r') as f:
        data = json.load(f)
    # pprint.pprint(data)
    items = data['items']
    print(len(items))
    tag_to_view = collections.defaultdict(int)
    for item in items:

        tags = item['tags']
        for tag in tags:
            tag_to_view[tag] += item['view_count']

        # creation_date = datetime.fromtimestamp(item['creation_date'])
        # print(creation_date)

    # pprint.pprint(tag_to_view)
    for k, v in sorted(tag_to_view.items(), key=lambda x: x[1], reverse=True):
        print(f'{k}: {v}')


if __name__ == '__main__':
    main()
