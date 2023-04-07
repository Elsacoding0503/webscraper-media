from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
from fake_useragent import UserAgent 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import requests, os
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.action_chains import ActionChains


ua = UserAgent()
options = Options() 
# options.add_argument('--headless') 
options.add_argument("user-agent=" + ua.chrome)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.implicitly_wait(3)

url_pixabay ='https://pixabay.com/images/search/car/'
driver.get(url_pixabay)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

# for i in range(5):
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
#     time.sleep(2)

lists_all_links = []

for i in range(1,5):
    url_pixabay = f'https://pixabay.com/images/search/car/?pagi={i}'
    driver.get(url_pixabay)
    soup_car = bs(driver.page_source, 'lxml')
    
    images_all = soup_car.find_all('div', {'class':'row-masonry search-results'})
    image = images_all[0].find_all('div', {'class':'item'})
#     print(len(image))
    for i in image:
        lists_all_links.append(i.find('meta')['content'])
    time.sleep(2)
    
    next_page = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/a')
    ActionChains(driver).move_to_element(next_page).click(next_page).perform()
    time.sleep(5)


for index, link in enumerate(lists_all_links):
    if not os.path.exists('images'):
        os.mkdir('images')

    img = requests.get(link)
    
    with open(f'images//{index+1}.jpg', 'wb') as f:
        f.write(img.content)

driver.quit()