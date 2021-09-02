# from os import name
from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")


article_texts = [
    article_tag.getText()
    for article_tag in soup.findAll(name="a", class_="storylink")
]
article_links = [
    article_tag.get("href")
    for article_tag in soup.findAll(name="a", class_="storylink")
]
article_upvotes = [
    int(score.getText().split(" ")[0])
    for score in soup.findAll(name="span", class_="score")
]

print(article_texts)
print(article_links)
print(article_upvotes)

index = article_upvotes.index(max(article_upvotes))

print(
    f"{article_texts[index]}\n{article_links[index]}\n{article_upvotes[index]}"
)

with open("./website.html") as html_file:
    contents = html_file.read()

soup = BeautifulSoup(contents, "html.parser")
print(soup.title)
print(soup.title.string)

print(soup.prettify())

all_anchor = soup.find_all(name="a")
print(all_anchor)

for tag in all_anchor:
    print(tag.get("href"))

heading = soup.find(name="h1", id="name")
print(heading)

soup.select(".heading")
