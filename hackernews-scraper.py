import requests
from bs4 import BeautifulSoup as bs
import pprint


res = requests.get('https://news.ycombinator.com/')
soup = bs(res.text, 'html.parser')
links = soup.select('.storylink')
subtext = soup.select('.subtext')


def sort_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        votes = subtext[idx].select('.score')
        if len(votes):
            vote_value = votes[0].getText()[:-7]
            if int(vote_value) >= 100:
                hn.append({'title': title, 'href': href, 'votes': vote_value})

    return sort_by_votes(hn)


pprint.pprint(create_custom_hn(links, subtext))
