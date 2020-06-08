import sys
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

yourid = str(input("Enter your facebook id:\t"))
yourpassword = str(input("Enter your facebook password:\t"))
reciever = str(input("Enter the facebook username of the person you want to send the message:\t"))
yourmessage = str(input("Enter your message:\t"))
yourtime = int(input("Enter the hour(24-hours format) you want to send:\t"))
while True:
    times = datetime.now()
    if times.hour == yourtime:
        driver = webdriver.Chrome('C:/chromedriver.exe')
        driver.get("https://messenger.com/")
        idbox = driver.find_element_by_xpath('//*[@id="email"]')
        passbox = driver.find_element_by_xpath('//*[@id="pass"]')
        idbox.send_keys(yourid)
        passbox.send_keys(yourpassword)
        passbox.send_keys(Keys.RETURN)
        if driver.current_url == 'https://messenger.com/login/password/':
            print('Something went wrong! Either username or password is wrong!\a')
            sys.exit(1)
        else:
            driver.get("https://messenger.com/t/"+reciever)
            time.sleep(5)
            message = ActionChains(driver)
            message.send_keys(yourmessage)
            message.send_keys(Keys.RETURN)
            message.perform()
            time.sleep(5)
            driver.close()
            sys.exit(1)