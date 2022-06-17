
from bs4 import BeautifulSoup

file = open("website.html", encoding="utf8")
content = file.read()

soup = BeautifulSoup(content, "html.parser")
all_anchor_tags = soup.find_all(name="a")

for tag in all_anchor_tags:
    pass
    #print(tag)

heading = soup.find(name="h1", id="name")
print(heading)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading.get("class"))

file.close()
