from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd

options = Options()
options.headless = True
options.add_argument('--window-size=1920x1080')




web = "https://www.audible.com/search"
path = 'eudaemai\chromedriver.exe'
driver = webdriver.Chrome(path, options=options) #<--Added options=options
driver.get(web)
driver.maximize_window()

# Locating the box that contains all the audiobooks listed in the page
container = driver.find_element_by_class_name('adbl-impression-container')
# Getting all the audiobooks listed (the "/" gives immediate child nodes)
products = container.find_elements_by_xpath('.//li[contains(@class, "productListItem")]')

# Initializing storage
book_title = []
book_author = []
book_length = []
# Looping through the products list (each "product" is an audiobook)
for product in products:
    # We use "contains" to search for web elements that contain a particular text, so we avoid building long XPATH
    book_title.append(product.find_element_by_xpath('.//h3[contains(@class, "bc-heading")]').text)
    book_author.append(product.find_element_by_xpath('.//li[contains(@class, "authorLabel")]').text)
    book_length.append(product.find_element_by_xpath('.//li[contains(@class, "runtimeLabel")]').text)
# Close the browser
driver.quit()
# Create a DataFrame and export to a csv file 
df_books = pd.DataFrame({'title': book_title, 'author': book_author, 'length': book_length})
df_books.to_csv('books_headless.csv', index=True) # <----Can also be sent to JSON like this: df_books.to_json() OR to a Postgres database like this: df_books.to_sql()
