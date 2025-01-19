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
driver.get(
    "https://www.google.com/maps/search/restaurants+near+Dubai+-+UAE/@25.1017088,54.8731616,11z/data=!3m1!4b1?entry=ttu")
link_list = []
end = "You've reached the end of the list."
try:
    print('-----------------------------------------')
    # panel_xpath = '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]'
    scrollable_div = driver.find_element(By.XPATH, '//div[@class="m6QErb DxyBCb kA9KIf dS8AEf ecceSd"]')
    print('--------------------------------')
    # scrolling
    flag = True
    i = 0
    while flag:
        try:
            print(f"Scrolling to page")

            driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', scrollable_div)
            time.sleep(5)

            if "You've reached the end of the list." in driver.page_source:
                flag = False

            links = driver.find_elements(By.XPATH, '//a[@class="hfpxzc"]')
            for i in links:
                jj = i.get_attribute('href')
                link_list.append(jj)
                print(jj,'-----------------------link')
            time.sleep(5)
            # link.append(set(link_list))
            # i =i+1
        except:
            break
except:
    pass

df = pd.DataFrame({'Link': link_list})
df = df.drop_duplicates()
df.to_csv('Resturant_link_dubai.csv', index=False)

# kk = set(link_list)
# Link = list(kk)
# print(len(Link),'----------------------Length of Data---------------------')
# df = pd.DataFrame({'Link':Link})
# df.to_csv('GoogleMap.csv')
