import driver as driver
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
import time
import csv

options = Options()
options.add_experimental_option("detach", True)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://icopify.co/#viewPricing")
driver.find_element(By.XPATH,'//a[@class="btn  fs-0 rounded btn-lg mr-2 mt-3 btn-primary"]').click()

count=1
# while count<4:
time.sleep(3)
data = driver.find_element(By.XPATH,'//div[@class="table-responsive"]//tbody/tr[1]')
print(data.text)
# for i in data:
#     # print('DATA--------->>',i.text)
#     i.find_element(By.XPATH,'')
# count+=1
# time.sleep(4)
print('---------------------------------------------------------------')