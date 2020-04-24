import os
import os.path
import requests
import time
from selenium import webdriver
from shutil import which
from credentials import username, password
from productUrls import urls

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

if os.path.exists('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe'):
    options.binary_location = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe'
elif os.path.exists('C:/Program Files/Google/Chrome/Application/chrome.exe'):
    options.binary_location = 'C:/Program Files/Google/Chrome/Application/chrome.exe'

chrome_driver_binary = which('chromedriver') or "/usr/local/bin/chromedriver"
driver = webdriver.Chrome(chrome_driver_binary, options=options)

driver.get('https://www.samsclub.com/sams/account/signin/login.jsp?redirectURL=%2F')
time.sleep(10)
usernamebox = driver.find_element_by_xpath('//*[@id="email"]')
usernamebox.send_keys(username)
passwordbox = driver.find_element_by_xpath('//*[@id="password"]')
passwordbox.send_keys(password)
signinbutton = driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/form/button')
signinbutton.click()
time.sleep(5)
done = False

while(done != True):
    try:
        robottextfield = driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/div/span')
        robottext = driver.execute_script("return arguments[0].innerText;", robottextfield)
        time.sleep(10)
    except:
        done = True

done = False
while(done != True):
    i = 0
    urls_temp = urls.copy()
    for url in urls_temp:  
        driver.get(url)
        time.sleep(10)
        try:
            shipbutton = driver.find_element_by_xpath('//*[@id="main"]/div/div/div[2]/div[2]/div[1]/div/div/div[4]/div/div/div/form/button')
            shipbutton_isenabled = shipbutton.is_enabled()
        except:
            shipbutton_isenabled = False
        if(shipbutton_isenabled):
            shipbutton.click()
            time.sleep(10)
            gotocartbutton = driver.find_element_by_xpath('//*[@id="main"]/div/div/div[2]/div[2]/div[3]/div/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/button')
            gotocartbutton.click()
            time.sleep(10)
            try:
                begincheckoutbutton = driver.find_element_by_xpath('//*[@id="nc-cart-items"]/div[9]/div[3]/a')
                begincheckoutbutton.click()
            except:
                begincheckoutbutton = driver.find_element_by_xpath('//*[@id="main"]/div/div[3]/div[2]/div/section[1]/div[4]/button')
                begincheckoutbutton.click()
            time.sleep(10)
            placeorderbutton = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div/button')
            del urls[i]
            print('ordered:' + url)
            placeorderbutton.click()
        else:
            time.sleep(1)
            i = i + 1
    if(len(urls) == 0):
        done = True
    else:
        time.sleep(30)
driver.quit()
