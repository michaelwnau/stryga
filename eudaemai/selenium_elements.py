from selenium import webdriver

website = 'https://www.adamchoi.co.uk/overs/detailed'
path = 'eudaemai\chromedriver.exe'

driver = webdriver.Chrome(path)
driver.get(website)

driver.quit()
# This is now functional code. It requires Chrome and the chromedriver to be installed in the same directory as the script. 
# The chromedriver can be downloaded from https://chromedriver.chromium.org/downloads

'''
Finding elements on a page with Selenium.

Example syntax using CSS selectors:
    driver.find_element_by_tag_name('h1')
    driver.find_element_by_tag_name('p')
    driver.find_element_by_tag_name('div')

Example syntax using XPath:
    driver.find_element_by_xpath('//h1')
    driver.find_element_by_xpath('//p')
    driver.find_element_by_xpath('//div')
    driver.find_element_by_xpath('//div[@class="container"]')
    driver.find_element_by_xpath('//div[@class="container"]/p')
    driver.find_element_by_xpath('//div[@class="container"]/p[1]')
    driver.find_element_by_xpath(xpath='//div[@class="container"]/div')
    driver.find_element_by_xpath(xpath='//div[@class="container"]/div[1]')
    driver.find_element_by_xpath(xpath='//tag[@AttributeName="Value"]')
    
Example syntax using name, or text:
    driver.find_element_by_name('name')
    driver.find_element_by_name('text')
    


- Dropdowns
- Logins
- Waits
'''