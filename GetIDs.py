from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from sortedcontainers import SortedSet

start_page = 1
end_page = 50
location = 'king-of-prussia-pa'

DRIVER_PATH = './chromedriver'
options = Options()
options.add_argument("window-size=500,500")
driver = webdriver.Chrome(chrome_options=options, executable_path=DRIVER_PATH)

js = """
var articles = document.getElementsByTagName('article');
var ids = [];
articles.forEach(article => {
    const href = article.children[0].href;
    index = href.lastIndexOf('/');
    ids.push(href.substring(index+1));
});
return ids;
"""
id_set = SortedSet()
page_num = start_page
while (page_num <= end_page):
    print "page number = " + str(page_num)
    driver.get('https://www.roomies.com/profiles/' + location + '?page=' + str(page_num))
    ids = driver.execute_script(js)
    for id in ids:
        id_set.add(int(id))

    with open('data/id_lists/' + str(start_page) + '-' + str(page_num) + '.txt', 'w') as f:
        for id in id_set:
            f.write(str(id) + '\n')

    page_num += 1

driver.close()
