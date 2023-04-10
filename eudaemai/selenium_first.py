from selenium import webdriver

website = 'https://www.adamchoi.co.uk/overs/detailed'
path = 'eudaemai\chromedriver.exe'

driver = webdriver.Chrome(path)
driver.get(website)

driver.quit()
# Thsi is no functional code. It requires Chrome and the chromedriver to be installed in the same directory as the script. 
# The chromedriver can be downloaded from https://chromedriver.chromium.org/downloads