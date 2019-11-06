import bs4, requests

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
    }

def getAmazonPrice(productUrl):
    res = requests.get(productUrl, headers = headers)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, "lxml")
    elems = soup.select("#priceblock_ourprice")
    return elems[0].text.strip()

price = getAmazonPrice("https://www.amazon.com/Foamily-Premium-Hypoallergenic-Polyester-Standard/dp/B0106UASB4?pf_rd_p=e20438cc-c728-4474-a9ad-1b99bb034660&pd_rd_wg=9CBg6&pf_rd_r=FCH60C79XY115SJDAQF1&ref_=pd_gw_unk&pd_rd_w=lDqir&pd_rd_r=ee087445-12e4-439f-a032-318e99be95e4")
print("The price is " + price)
