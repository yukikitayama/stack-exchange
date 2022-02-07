import requests
import pandas as pd
import pprint


CSV_01 = './data/sites.csv'


def main():

    # HTTP GET request to site endpoint
    r = requests.get('https://api.stackexchange.com/2.3/sites')
    print(f'Status code: {r.status_code}')
    # pprint.pprint(r.json())

    # Get site names
    sites = []
    items = r.json()['items']
    for item in items:
        site = item['api_site_parameter']
        sites.append(site)
        print(site)
    sites.sort()

    # Save sites
    df = pd.DataFrame({'site': sites})
    df.to_csv(CSV_01, index=False)


if __name__ == '__main__':
    main()
