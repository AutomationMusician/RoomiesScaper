import os
import os.path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from sortedcontainers import SortedSet
from os import path

# Load IDs
id_set = SortedSet()
for filepath in os.listdir('data/id_lists/'):
    with open('data/id_lists/' + filepath) as file:
        line = True
        cnt = 1
        while line:
            line = file.readline().rstrip()
            if line != '':
                id_set.add(int(line))
                cnt += 1

DRIVER_PATH = './chromedriver'
options = Options()
options.add_argument("window-size=500,500")
driver = webdriver.Chrome(chrome_options=options, executable_path=DRIVER_PATH)

# Get ids from the id lists and combine them into one sorted set

# iterate over ids
for id in id_set:
    # first check if there is already an html page for this id
    filepath = 'data/profiles/' + str(id) + '.html'
    # if no html page exists
    if not path.exists(filepath):
        print filepath + ' does not exists'
        # go to page
        driver.get('https://www.roomies.com/profiles/' + str(id))
        with open('data/profiles/' + str(id) + '.html', 'w') as f:
            # download page source
            print(driver.page_source)
            f.write(driver.page_source.encode('ascii', 'ignore'))
    else:
        print filepath + ' exists'

driver.close()
