import feedparser
from wordcloud import WordCloud

d = feedparser.parse('https://news.google.com/rss?hl=pt-BR&gl=BR&ceid=BR:pt-419')

news = []

for post in d.entries:
  post_list = post.title.split()
  for word in post_list:
    if (len(word)) >= 4:
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