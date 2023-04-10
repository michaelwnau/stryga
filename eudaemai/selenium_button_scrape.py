from selenium import webdriver

website = 'https://www.adamchoi.co.uk/overs/detailed'
path = 'eudaemai\chromedriver.exe'

driver = webdriver.Chrome(path)
driver.get(website)

all_matches_button = driver.find_element_by_xpath('//label[@analytics-event="All matches"]')
all_matches_button.click()

matches = driver.find_elements_by_tag_name('tr')

date = []
home_team = []
score = []
away_team = []

for match in matches:
    date.append(match.find_element_by_xpath('./td[1]').text) #<-- This is the firt column with the td tag and the index of 1
    home = match.find_element_by_xpath('./td[2]').text
    home_team.append(home)
    print(home)
    home_team.append(match.find_element_by_xpath('./td[2]').text)
    score.append(match.find_element_by_xpath('./td[3]').text)
    away_team.append(match.find_element_by_xpath('./td[4]').text)







#driver.quit()  <-- Only uncomment this line when you are ready to close the browser or have an autmated scraper.