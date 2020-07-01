from urllib.request import urlretrieve
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver


search = input("SEARCH: ")
url = f'https://www.google.com/search?q={quote_plus(search)}&tbm=isch&ved=2ahUKEwioxZG4yuPpAhWKAd4KHXZqCfwQ2-cCegQIABAA&oq={quote_plus(search)}&gs_lcp=CgNpbWcQAzICCAAyAggAMgIIADICCAAyBAgAEB4yBAgAEB4yBAgAEBgyBggAEAoQGDIGCAAQChAYMgQIABAYOgQIIxAnUKP_AljOoANg4KUDaAFwAHgAgAGwAYgBrQmSAQMwLjiYAQCgAQGqAQtnd3Mtd2l6LWltZw&sclient=img&ei=YoLWXqiMIoqD-Ab21KXgDw&bih=657&biw=1366'

driver = webdriver.Chrome("driver\chromedriver.exe")
driver.get(url)

html = driver.page_source
soup = BeautifulSoup(html, features="html.parser")

img = soup.select('img')
n = 1
imgurl = [ ]

for i in img:
    try:
        imgurl.append(i .attrs["src"])
    except KeyError:
        imgurl.append(i .attrs["data-src"])

for i in imgurl:
    urlretrieve(i, "CrawlingImages/" + search + str(n) + ".jpg" )
    n += 1

driver.close()
