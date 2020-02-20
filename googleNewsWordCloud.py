#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import feedparser
from wordcloud import WordCloud
import re
import unicodedata

# stop words
stop_words = open('stop-words_brazil_1_br.txt').read().splitlines()

d = feedparser.parse('https://news.google.com/rss?hl=pt-BR&gl=BR&ceid=BR:pt-419')

news = []

def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  cleantext = cleantext.replace("nbsp", "")
  noticias = "Notícias".decode("utf-8")
  cleantext = cleantext.replace(noticias, "")
  insensitive_case = re.compile(re.escape('Google'), re.IGNORECASE)
  cleantext = insensitive_case.sub("", cleantext)
  insensitive_case = re.compile(re.escape('Jornal'), re.IGNORECASE)
  cleantext = insensitive_case.sub("", cleantext)
  insensitive_case = re.compile(re.escape('Veja'), re.IGNORECASE)
  cleantext = insensitive_case.sub("", cleantext)
  insensitive_case = re.compile(re.escape('Folha'), re.IGNORECASE)
  cleantext = insensitive_case.sub("", cleantext)
  insensitive_case = re.compile(re.escape('Cobertura'), re.IGNORECASE)
  cleantext = insensitive_case.sub("", cleantext)
  insensitive_case = re.compile(re.escape('Completa'), re.IGNORECASE)
  cleantext = insensitive_case.sub("", cleantext)
  return cleantext

for post in d.entries:
  post_list = cleanhtml(post.title).split()
  for word in post_list:
    word = unicodedata.normalize('NFKD', word).encode('ascii','ignore') 
    if (len(word)) >= 4 and not (word in stop_words):
      news.append(word)
  post_list = cleanhtml(post.summary).split()
  for word in post_list:
    word = unicodedata.normalize('NFKD', word).encode('ascii','ignore')    
    if (len(word)) >= 4 and not (word in stop_words):
      news.append(word)

text = ' '.join(news)

# Generate a word cloud image
wordcloud = WordCloud().generate(text)

# Display the generated image:
# the matplotlib way:
import matplotlib.pyplot as plt

# lower max_font_size
wordcloud = WordCloud(max_font_size=40).generate(text)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
