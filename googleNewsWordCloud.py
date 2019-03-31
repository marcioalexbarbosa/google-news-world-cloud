import feedparser
from wordcloud import WordCloud

d = feedparser.parse('https://news.google.com/rss?hl=pt-BR&gl=BR&ceid=BR:pt-419')

news = []

for post in d.entries:
  news.append(post.title)

text = ' '.join(news)

# Generate a word cloud image
wordcloud = WordCloud().generate(text)

# Display the generated image:
# the matplotlib way:
import matplotlib.pyplot as plt
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")

# lower max_font_size
wordcloud = WordCloud(max_font_size=40).generate(text)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()