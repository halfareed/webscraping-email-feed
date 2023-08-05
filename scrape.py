import requests
import lxml.html

# html = requests.get('https://store.steampowered.com/explore/new/')
# doc = lxml.html.fromstring(html.content)                            # created an HtmlElement object
# new_releases = doc.xpath('//div[@id="tab_newreleases_content"]')[0] # filter div tags that have newreleases id
# titles = new_releases.xpath('.//div[@class="tab_item_name"]/text()')
# print(titles)

html = requests.get('https://geeksforgeeks.org/trending')
doc = lxml.html.fromstring(html.content)        # created an HtmlElement object
trending_python = doc.xpath('//*[@id="gfg-trending-main-div"]')[0]   # filter div tags that have newreleases id
titles = trending_python.xpath('//*[@id="gfg-trending-main-div"]/div[5]/div[2]/a/p/text()')
print(trending_python)
print(titles)
