#! python3
# lucky.py - Opens several Google search results.

import requests, sys, webbrowser, bs4

print('Googling...')    # display text while dowloading the Google page
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()


# TODO: Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, "lxml")
# print(soup.select("a"))
# TODO: Open a browser tab for each result.
linkElems = soup.select(".r a")

numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))
    