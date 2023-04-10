from selenium import webdriver

website = 'https://www.adamchoi.co.uk/overs/detailed'
path = 'eudaemai\chromedriver.exe'

driver = webdriver.Chrome(path)
driver.get(website)

all_matches_button = driver.find_element_by_xpath('//label[@analytics-event="All matches"]')
all_matches_button.click()

#driver.quit()  <-- Only uncomment this line when you are ready to close the browser or have an autmated scraper.