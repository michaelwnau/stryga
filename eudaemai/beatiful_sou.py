from bs4 import BeautifulSoup
import requests

#soup.find(id="specific id")
#soup.find(id='tag', class_="class_name")
# soup.find_all("h2")  # find all h2 tags; returns a list

# This module is hard-coded to get the transcript for Titanic from the website https://subslikescript.com/movie/Titanic-120338
# The same template can be used to get the transcript for any movie on the website.
# To make this into a general purpose module, the website and the movie name can be passed as arguments to the function.
# This module can generalized and integrated into the main app as a pipeline.

website = 'https://subslikescript.com/movie/Titanic-120338'
result = requests.get(website)
content = result.text

soup = BeautifulSoup(content, 'lxml')
#print(soup.prettify())

box = soup.find('article', class_='main-article') # Note the use of class_ instead of class; required in Python
title = box.find('h1').get_text() # Get the text from the h1 tag
transcript = box.find('div', class_='full-script').get_text(strip=True, separator= ' ') # Get the text from the div class

# print(title)
# print(transcript)

with open(f'{title}.txt', 'w', encoding='utf-8') as file:
    file.write(transcript)