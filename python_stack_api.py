from stackapi import StackAPI
from datetime import datetime
import pprint


def main():
    site = StackAPI('stackoverflow')

    # max_pages is the number of API calls
    # Total number of data is max_pages * page_size
    site.max_pages = 1
    site.page_size = 10
    from_date = datetime(2022, 1, 1).timestamp()
    to_date = datetime(2022, 2, 1).timestamp()
    print(f'From: {datetime.fromtimestamp(from_date)}, to: {datetime.fromtimestamp(to_date)}')

    comments = site.fetch(
        'questions',
        fromdate=int(from_date),
        todate=int(to_date)
    )
    print(type(comments))
    print(comments.keys())
    print(len(comments['items']))
    pprint.pprint(comments)


if __name__ == '__main__':
    main()
