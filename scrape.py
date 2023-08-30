import requests
import lxml.html
import yagmail
import smtplib

# Articles are extracted in a list, assign
html = requests.get('https://geeksforgeeks.org/trending')
doc = lxml.html.fromstring(html.content)  # created an HtmlElement object
trending_python = doc.xpath('//*[@id="gfg-trending-main-div"]')[0]  # filter div tags that have trending id
href_list = []
titles = trending_python.xpath('//*[@id="gfg-trending-main-div"]/div[5]/div[2]/a/p/text()') # extract titles trending tab
hrefs = trending_python.xpath('//*[@id="gfg-trending-main-div"]/div[5]/div[2]/a')
for href in hrefs:
    href_list.append(href.attrib['href'])
merged_list = [(titles[i], href_list[i]) for i in range(0, len(titles))]
filter = ["SQLAlchemy", "binary"] # words of interest
filter_set = set([b for b in map(lambda x: x[0], merged_list) if any(a in b for a in filter)]) # extract the wanted titles to use as a filter as a set
for x in range(len(merged_list) - 1, -1, -1):
    if merged_list[x][0] not in filter_set:
      del merged_list[x]
print((merged_list))

with open("config.txt", "r") as f:
    email = f.readline()
    temp_password = f.readline()

yag = yagmail.SMTP(email, temp_password)
contents = [
    "This is the body, and here is just text ",
]
#yag.send('ninjaspy713@gmail.com', 'subject', contents)
