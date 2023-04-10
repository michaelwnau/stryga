from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time

options = Options()
options.headless = True
options.add_argument('--window-size=1920x1080')


#web = "https://www.audible.com/search"
web = "https://www.audible.com/adblbestsellers?ref=a_search_t1_navTop_pl0cg1c0r0&pf_rd_p=8a113f1a-dc38-418d-b671-3cca04245da5&pf_rd_r=8RVVZ3KQT0NZRKMHMHCM&pageLoadId=XF1XvlAsfLKq3jEA&creativeId=1642b4d1-12f3-4375-98fa-4938afc1cedc"
path = 'eudaemai\chromedriver.exe'
driver = webdriver.Chrome(path, options=options) #<--Added options=options
driver.get(web)
driver.maximize_window()

# Pagination handling:
pagination = driver.find_element_by_xpath('//ul[contains(@class, "pagingElements")]')
pages = pagination.find_elements_by_tag_name('li')
last_page = int(pages[-2].text) #<-- -2 because the last page is always a "next" button

# Pagination handling using a while loop:
current_page = 1
    # Initializing storage
book_title = []
book_author = []
book_length = []


while current_page <= last_page:
    time.sleep(2)
    # Locating the box that contains all the audiobooks listed in the page
    container = driver.find_element_by_class_name('adbl-impression-container')
    # Getting all the audiobooks listed (the "/" gives immediate child nodes)
    products = container.find_elements_by_xpath('.//li[contains(@class, "productListItem")]')

    # Looping through the products list (each "product" is an audiobook)
    for product in products:
        # We use "contains" to search for web elements that contain a particular text, so we avoid building long XPATH
        book_title.append(product.find_element_by_xpath('.//h3[contains(@class, "bc-heading")]').text)
        book_author.append(product.find_element_by_xpath('.//li[contains(@class, "authorLabel")]').text)
        book_length.append(product.find_element_by_xpath('.//li[contains(@class, "runtimeLabel")]').text)
    
    current_page = current_page + 1
    
    try:
        next_page = driver.find_element_by_class_xpath('//span[contains(@class, "nextButton")]')
        next_page.click()
    except:
        pass
    
# Close the browser
driver.quit()



# Create a DataFrame and export to a csv file 
df_books = pd.DataFrame({'title': book_title, 'author': book_author, 'length': book_length})
df_books.to_csv('books_bestsellers.csv', index=True) # <----Can also be sent to JSON like this: df_books.to_json() OR to a Postgres database like this: df_books.to_sql()
