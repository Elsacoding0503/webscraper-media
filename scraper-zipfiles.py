from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from fake_useragent import UserAgent 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import requests, os, time, zipfile

ua = UserAgent()
options = Options() 
# options.add_argument('--headless') 
options.add_argument("user-agent=" + ua.chrome)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.implicitly_wait(3)

url_statistics = 'https://www.twse.com.tw/zh/trading/statistics/list05-225.html'

# 操作網頁的查詢功能
driver.get(url_statistics)

select_year = Select(driver.find_element(By.ID, 'label0'))
select_year.select_by_value('2022')

search_button = driver.find_element(By.CSS_SELECTOR, 'button.search')
search_button.click()
time.sleep(2)

# 下載zip檔
links = driver.find_element(By.CLASS_NAME, 'is-last-page').find_elements(By.TAG_NAME, 'a')

for link in links:
    zip_response = requests.get(link.get_attribute('href'))
    
    if not os.path.exists('zip_files'):
        os.mkdir('zip_files')

    with open(f'zip_files//{link.text}', 'wb') as f:
        f.write(zip_response.content)
    
    # 下載同時解壓縮
    zip_ = zipfile.ZipFile(f'zip_files//{link.text}')
    zip_.extractall('zip_files//.')

driver.quit()
