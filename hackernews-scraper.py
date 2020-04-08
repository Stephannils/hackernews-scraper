import requests
from bs4 import BeautifulSoup as bs

res = requests.get('https://news.ycombinator.com/')
soup = bs(res.text, 'html.parser')
links = soup.select('.storylink')
votes = soup.select('.score')


def create_custom_hn(links, votes):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href', None)
        points = votes[idx].getText()[:-7]
        if int(points) >= 100:
            hn.append({'title': title, 'href': href, 'votes': points})

    return hn

print((create_custom_hn(links, votes)))