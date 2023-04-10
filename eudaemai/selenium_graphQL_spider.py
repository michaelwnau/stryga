from selenium import webdriver
import pandas as pd

web = "https://www.audible.com/search"
path = 'eudaemai\chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get(web)
driver.maximize_window()

container = driver.find_element_by_class_name('adbl-impression-container')
products = container.find_elements_by_xpath('.//li[contains(@class, "productListItem")]')

book_title = []
book_author = []
book_length = []

for product in products:
    book_title.append(product.find_element_by_xpath('.//h3[contains(@class, "bc-heading")]').text)
    book_author.append(product.find_element_by_xpath('.//li[contains(@class, "authorLabel")]').text)
    book_length.append(product.find_element_by_xpath('.//li[contains(@class, "runtimeLabel")]').text)

driver.quit()

df_books = pd.DataFrame({'title': book_title, 'author': book_author, 'length': book_length})

# Create a GraphQL mutation string
graphql_mutations = []
for index, row in df_books.iterrows():
    mutation = f'''
mutation {{
  createBook(input: {{
    title: "{row['title']}"
    author: "{row['author']}"
    length: "{row['length']}"
  }}) {{
    book {{
      id
      title
      author
      length
    }}
  }}
}}
'''
    graphql_mutations.append(mutation)

# Save the GraphQL mutations to a file
with open('books.graphql', 'w', encoding='utf-8') as f:
    for mutation in graphql_mutations:
        f.write(mutation)
