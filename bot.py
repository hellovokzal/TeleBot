import requests as r

url = os.environ['URL']

while True:

    load = r.get(url)
