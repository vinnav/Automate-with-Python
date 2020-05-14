
import bs4, requests, os
os.makedirs("batchDownloaded", exist_ok=True)

res = requests.get("https://url/")
url = "https://url/"


res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, "lxml")
elems = soup.select(".main-content-data a")
for i in range(10,len(elems)):
    elem = elems[i].get("href")
    elemUrl = url + elem[2:]
    print("downloading %s..." % elem[2:].replace("%20", " ").replace("%28", "(").replace("%29", ")")) 
    elemName = elem[2:].replace("%20", " ").replace("%28", "(").replace("%29", ")")
    pdf = requests.get(elemUrl)
    pdf.raise_for_status

    pdfFile = open(os.path.join("batchDownloaded", os.path.basename(elemName)), "wb")
    
    for chunk in pdf.iter_content(chunk_size=8192):
        pdfFile.write(chunk)
    pdfFile.close()