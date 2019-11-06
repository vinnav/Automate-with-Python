#! python3
# downloadXkcd.py - Downloads every single XKCD comic.

import requests, os, bs4, threading

url = "http://xkcd.com"             # starting url
os.makedirs("xkcd", exist_ok=True)  # store comics in ./xkcd

def downloadXkcd(startComic, endComic):
    for urlNumber in range(startComic, endComic):
        # Download the page
        print('Downloading page http://xkcd.com/%s...' % (urlNumber))
        res = requests.get('http://xkcd.com/%s' % (urlNumber))
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text)

        # Find the URL of the comic image
        comicElem = soup.select("#comic img")
        if comicElem == []:
            print("Could not find comic image.")
        else:
            # comicUrl = comicElem[0].get("src")
            comicUrl = "http:" + comicElem[0].get("src")
            # Download the image
            print("downloading image %s..." % (comicUrl))
            res = requests.get(comicUrl)
            res.raise_for_status

            # Save the image to ./xkcd
            imageFile = open(os.path.join("xkcd", os.path.basename(comicUrl)), "wb")
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()

    #Get the Prev button's url.
        prevLink = soup.select('a[rel="prev"]')[0]
        url = "http://xkcd.com" + prevLink.get("href")

    print("Done.")

# Create and start the Thread objects
downloadThreads = []                    # a list of all the Thread objects
for i in range(0, 1400, 100):           # loops 14 times, creates 14 threads
    downloadThread = threading.Thread(target=downloadXkcd, args=(i, i+99))
    downloadThreads.append(downloadThread)
    downloadThread.start()

# Wait for all threads to end
for downloadThread in downloadThreads:
    downloadThread.join()
print("Done.")