from selenium import webdriver
import pandas as pd

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
    score.append(match.find_element_by_xpath('./td[3]').text)
    away_team.append(match.find_element_by_xpath('./td[4]').text)
driver.quit()

df = pd.DataFrame({'date': date, 'home_team': home_team, 'score': score, 'away_team': away_team})
df.to_csv('football_data.csv', index=True)
print(df)




#driver.quit()  <-- Only uncomment this line when you are ready to close the browser or have an autmated scraper.