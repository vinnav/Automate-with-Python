import requests
res = requests.get("https://automatetheboringstuff.com/files/rj.txt")

try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))

type(res)

res.status_code == requests.codes.ok
len(res.text)
print(res.text[:250])

# Download the file to RomeoAndJuliet.txt in cwd

playFile = open('RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)

playFile.close()