from wordcloud import WordCloud
import MeCab

stopwords = ["の"]

f = open("messages.txt", "r")
text = f.read()
t = MeCab.Tagger()
node = t.parseToNode(text)

words = []
while (node):
    word_type = node.feature.split(",")[0]
    if node.surface == "の":
        print(node.feature)
    if word_type in["名詞"] and node.surface not in stopwords:
        words.append(node.surface)
    node = node.next

wordcloud = WordCloud(font_path=r"./font.ttc", width=1000, height=1000, background_color="white").generate(text=" ".join(words))
wordcloud.to_file("out.png")