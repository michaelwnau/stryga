from bs4 import BeautifulSoup
import requests

#####################################################
# Pagination with BeautifulSoup
#####################################################
# Modified from app\2.bs4-multiple-movies.py
#####################################################

# How to get the HTML
root = 'https://subslikescript.com/'
website = f'{root}/movies_letter-A'
result = requests.get(website)
content = result.text
soup = BeautifulSoup(content, 'lxml')
#print(soup.prettify()) # prints the HTML of the website

# Pagination

pagination = soup.find('ul', class_='pagination')
pages = pagination.find_all('li', class_='page-item')
last_page = pages[-2].text

links = []
for page in range(1, int(last_page)+1)[:2]: # range(1, 132+1) ALSO NOTE THAT THE `[:2]` IS FOR TESTING PURPOSES ONLY!!!
    # https://subslikescript.com/movies_letter-A?page=1
    result = requests.get(f'{website}?page={page}')
    content = result.text
    soup = BeautifulSoup(content, 'lxml')

    # Locate the box that tains a list of movies
    box = soup.find('article', class_='main-article') # Note the use of class_
    #print(box)  # Add this print statement

    # Store each link in "links" list (href doesn't consider root aka "homepage", so we have to concatenate it later)
    for link in box.find_all('a', href=True): # find_all returns a list
        links.append(link['href'])

    print(links)  # Add this print statement

    #################################################
    # Extracting the movie transcript
    #################################################

    # Loop through the "links" list and sending a request to each link
    for link in links:
        try:
            print(link)
            result = requests.get(f'{root}/{link}')
            content = result.text
            soup = BeautifulSoup(content, 'lxml')
            
            # Locate the box that contains title and transcript
            box = soup.find('article', class_='main-article')
            # Locate title and transcript
            title = box.find('h1').get_text()
            title = ''.join(title.split('/'))
            transcript = box.find('div', class_='full-script').get_text(strip=True, separator=' ')
            # Exporting data in a text file with the "title" name
            with open(f'{title}.txt', 'w', encoding='utf-8') as file:
                file.write(transcript)
        except:
            print("--------------Link not working--------------")
            print(link)
            pass
