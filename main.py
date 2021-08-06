import rstr
import requests
from concurrent.futures import ThreadPoolExecutor
import datetime

generated_urls = []

date_time = datetime.datetime.now()

ext = str(input("Extension (jpg,gif,png) : "))
filename = f"[VALID Imgur {ext}] {date_time.strftime('%d-%m-%y %I-%M-%S-%p')}.txt"


def gen_url(ex):
    img_id = rstr.xeger(r'[A-Za-z0-9]{5}')
    url = f"https://i.imgur.com/{img_id}.{ex}"
    return url


def check_url(url):
    response = requests.get(url).url
    if "removed" not in response:
        print(f"[*] Good ----> {url}")
        open(f"Results\\{filename}", "a").write(f"{url}\n")


for i in range(10000):
    generated_urls.append(gen_url(ext))

with ThreadPoolExecutor(max_workers=50) as executor:
    futures = [executor.submit(check_url, url) for url in generated_urls]
    executor.shutdown(wait=True)
