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

df = pd.read_csv('Instagram_data.csv')
data = df['Instagram Url'].to_list()

for i in data[:]:
    driver.get(i)
    time.sleep(5)

    name = ''
    try:
        name = driver.find_element(By.XPATH, '//header/section//h2').text
    except:
        pass
    print('User Name ---->>>>', name)

    follower = ''
    try:
        follower = driver.find_element(By.XPATH, '(//header//section//ul//button//span//span)[2]').text
    except:
        pass
    print('Follower ------->>', follower)

    following = ''
    try:
        following = driver.find_element(By.XPATH, '(//header//section//ul//button//span//span)[3]').text
    except:
        pass
    print('following ------->>', following)

    link = i
    with open('demo_csv.csv', 'a', newline='') as csv_file:

        field_names = ['Instagram Name', 'follower', 'following', 'accountstatus', 'Instagram Url']

        dict = {"Instagram Name": name, "follower": follower, "following": following,'Instagram Url':link}
        dict_object = csv.DictWriter(csv_file, fieldnames=field_names)
        dict_object.writerow(dict)
    print("---->>>>successfully<<<<<<-------------")