# -*- encoding: utf8-*-
from bs4 import BeautifulSoup
import requests
import re

res = requests.get('https://www.ntpu.edu.tw/college/e4/')
res.encoding = 'big5'


soup = BeautifulSoup(res.text, 'html.parser')
tag_name = 'a.news'
tag_date = 'tr td.news'
date = soup.select(tag_date)

date = date[1].text


articles = soup.select(tag_name)
for art in articles:
    path = art['href']
    title = art.text
    break

webid = path[-3:]


pathE = "https://www.ntpu.edu.tw/college/e4/%s" % path
title = title.strip()
title = title[6:]

date = date.strip()


res2 = requests.get(pathE)
res2.encoding = 'big5'
soup2 = BeautifulSoup(res2.text, 'html.parser')
tag2_name = 'tr td.ch'
strong = soup2.select(tag2_name)
content = strong[1].text

content = content.strip()


for i in range(len(content)):
    if content[i] == '》':
        tag = content[1:i]
        break
for i in range(len(content)):
    if content[i] == '\n':
        des = content[(i + 3):][:50]
        content = content[(i + 3):]
        break


reg_img = re.compile('http[s]?://i.imgur.com/\w+\.(?:jpg|png|gif)')
images = reg_img.findall(res2.text)
reg_vid = re.compile('http[s]?://www.youtube.com/embed/\S+')
videos = reg_vid.findall(res2.text)
for i in range(len(videos)):
    videos[i] = videos[i][30:-1]


images1 = images[0]
images2 = images[1:]


vidd = ""
for i in range(len(videos)):
    vid = "    - src: %s%s" % (videos[i], "\n")
    vidd += vid


imgg = ""
for i in range(len(images2)):
    img = "    - src: %s%s" % (images2[i], "\n")
    imgg += img
