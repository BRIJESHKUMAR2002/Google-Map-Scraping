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

df = pd.read_csv('Resturant_link_dubai.csv')
data = df['Link'].to_list()

for i in data[:]:
    driver.get(i)
    time.sleep(2)
    type = ''
    name = ''
    web = ''
    addr = ''
    rating = ''
    phone = ''
    menu = ''
    live = i

    try:
        try:
            name = driver.find_element(By.XPATH,'//div[@class="lMbq3e"]//h1').text
        except:
            pass
        print('Name--------------->',name)

        try:
            web = driver.find_element(By.XPATH,'(//div[@class="m6QErb "])//a[@data-tooltip="Open website"]').get_attribute('href')
        except:
            pass
        print('website------------>',web)

        try:
            addr = driver.find_element(By.XPATH,'((//div[@class="m6QErb "])[1]//button[@data-tooltip="Copy address"])[1]').text
        except:
            pass
        print('address------------>',addr)

        try:
            rating = driver.find_element(By.XPATH,'(//div[@class="lMbq3e"]//span[@aria-hidden="true"])[1]').text
        except:
            pass
        print('Rating------------->',rating)

        try:
            phone = driver.find_element(By.XPATH,'((//div[@class="m6QErb "])[1]//button[@data-tooltip="Copy phone number"])[1]').text
        except:
            pass
        print('phone-------------->',phone)

        try:
            menu = driver.find_element(By.XPATH,'(//div[@class="m6QErb "])//a[@data-tooltip="Open menu link"]').get_attribute('href')
        except:
            pass
        print('menu--------------->',menu)


        try:
            type = driver.find_element(By.XPATH,'//button[@jsaction="pane.rating.category"]').text
        except:
            pass
        print('Type-------------->',type)

    except:
        pass

    print('-----------------------------------------------------------------------------------------')

    with open('Resturant_data_dubai.csv','a+',newline='',encoding='utf-8') as file:
        fields = ['Name','Type','Address','Contact','Rating','Menu Url','Live Location','Website Url']
        dictwriter_object = csv.DictWriter(file, fieldnames=fields)
        dict = {'Name': name,'Type':type,'Address':addr,'Contact':phone,'Rating':rating,'Menu Url':menu,'Live Location':live,'Website Url':web}
        # Pass the dictionary as an argument to the Writerow()
        dictwriter_object.writerow(dict)