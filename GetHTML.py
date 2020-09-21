from selenium import webdriver
from sortedcontainers import SortedSet

DRIVER_PATH = './chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)

# Get ids from the id lists and combine them into one sorted set

# iterate over ids
    # first check if there is already an html page for this id
    # if no html page exists
        # go to page
        # download page source

profile_num = '843331'
driver.get('https://www.roomies.com/profiles/' + profile_num)

with open('data/' + profile_num + '.html', 'w') as f:
    print(driver.page_source)
    f.write(driver.page_source.encode('ascii', 'ignore'))
