# No. 17: Decode a web page: this prints out all article titles on NYT homepage

import requests  #programmatically makes HTTP requests
from bs4 import BeautifulSoup  #gives structure to HTML, allows us to sort through HTML easily

url = 'https://www.nytimes.com'
r = requests.get(url) #loads webpage through python
r_html = r.text

soup = BeautifulSoup(r_html, 'lxml') #sorts the site's HTML
print(soup.prettify()) #prints sorted HTML

article_titles = []

#find and loop through all elements on page with class name 'story-heading'
for story_heading in soup.find_all(class_='story-heading') :

      if story_heading.a : #for story headings that are links - prints out link text, formats it nicely
            article_titles.append(story_heading.a.text.replace('\n',' ').strip())
      else : #for others, takes out contents, formats it nicely
            article_titles.append(story_heading.contents[0].strip())
            
print(article_titles)
