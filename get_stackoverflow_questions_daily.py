import requests
from dateutil.relativedelta import relativedelta
from datetime import datetime, timedelta
import json
import collections
import pprint
import time


BASE_URL = 'https://api.stackexchange.com'
SITE = 'stackoverflow'
START = (datetime.now() - timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0)
END = START + timedelta(days=1)
print(f'Start: {START}, end: {END}')
JSON_01 = f'./data/questions_{START.strftime("%Y%m%d")}.json'
SLEEP = 20
KEY = '###'


def main():

    # Make parameters
    fromdate = int(START.timestamp())
    todate = int(END.timestamp())
    sort = 'votes'
    order = 'desc'
    pagesize = 100
    page = 1
    has_more = True

    # Make HTTP requests
    # items = []
    # while has_more:
    #     print(f'Page: {page}')
    #     r = requests.get(
    #         url=f'{BASE_URL}/2.3/questions?site={SITE}'
    #             f'&fromdate={fromdate}&todate={todate}'
    #             f'&sort={sort}&order={order}'
    #             f'&page={page}&pagesize={pagesize}'
    #             f'&key={KEY}'
    #     )
    #     print(f'Status code: {r.status_code}')
    #     # print(r.json())
    #     print(f'Quota remaining: {r.json()["quota_remaining"]}')
    #     items.extend(r.json()['items'])
    #
    #     data = {'items': items}
    #     # Save response
    #     with open(JSON_01, 'w') as f:
    #         json.dump(data, f)
    #
    #     has_more = r.json()['has_more']
    #     page += 1
    #     print(f'Sleeping {SLEEP} seconds...')
    #     time.sleep(SLEEP)
    #     print()

    # Load data
    with open(JSON_01, 'r') as f:
        data = json.load(f)
    items = data['items']
    print(f'Number of questions on {START.strftime("%Y-%m-%d")}: {len(items)}')
    tag_to_count = collections.defaultdict(int)
    tag_to_view = collections.defaultdict(int)
    for item in items:

        tags = item['tags']
        for tag in tags:
            tag_to_count[tag] += 1
            tag_to_view[tag] += item['view_count']
        # creation_date = datetime.fromtimestamp(item['creation_date'])
        # print(creation_date)

    print('Count by tag')
    i = 0
    for k, v in sorted(tag_to_count.items(), key=lambda x: x[1], reverse=True):
        print(f'{k}: {v}')
        i += 1
        if i == 10:
            break
    print()

    print('View count by tag')
    i = 0
    for k, v in sorted(tag_to_view.items(), key=lambda x: x[1], reverse=True):
        print(f'{k}: {v}')
        i += 1
        if i == 10:
            break
    print()


if __name__ == '__main__':
    main()
