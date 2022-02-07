# Stack Exchange

- How to use Stack Exchange API

## Getting Started

- Visite [Stack Exchange API](https://api.stackexchange.com/)
- Check [Stack Exchange API docs](https://api.stackexchange.com/docs)
- Check [stackapps tour](https://stackapps.com/tour)
- Register on Stack Apps
  - [http://stackapps.com/apps/oauth/register](http://stackapps.com/apps/oauth/register)
  - What you need
    - Application name
    - Description
    - OAuth domain (I guess redirects to this domain if authentication needs it)
    - Application website

## OAuth 2.0

- [Authentication](https://api.stackexchange.com/docs/authentication)

## Key

- [Throttles](https://api.stackexchange.com/docs/throttle)

## Parameter

- Page and pagesize
  - [Paging](https://api.stackexchange.com/docs/paging)
- Page is 1 by default
- Pagesize is 30 by default, and can be between 0 and 100

### sites

- Use the following API to check what site is available
  - [Usage of /sites GET](http://api.stackexchange.com/docs/sites)

### questions

- By default, return 30 questions
- Parameter


## Python

- [StackAPI](https://stackapi.readthedocs.io/en/latest/)