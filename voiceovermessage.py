import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import speech_recognition as sr


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


r = sr.Recognizer()

yourid = str(input("Enter your facebook id:\t"))
yourpassword = str(input("Enter your facebook password:\t"))
reciever = str(input("Enter the facebook username of the person you want to send the message:\t"))

driver = webdriver.Chrome('C:/chromedriver.exe')
driver.get("https://messenger.com/")
idbox = driver.find_element_by_xpath('//*[@id="email"]')
passbox = driver.find_element_by_xpath('//*[@id="pass"]')
idbox.send_keys(yourid)
passbox.send_keys(yourpassword)
passbox.send_keys(Keys.RETURN)
driver.get("https://messenger.com/t/" + reciever)
print('''
 Say the following commands when the program says listening:
     - type/write down/write : to activate typing mode and 
             then speak the whole message you want to send and wait for the program to type on messenger.
             execute enter/send command when the program says Listening...
     - send/enter: to send the message
     - exit: to exit the program
 ''')
time.sleep(5)

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source, duration=1)
    understood = input(bcolors.ENDC+"Press any Enter twice to continue...")
    while True:
        print(bcolors.HEADER+'listening...')
        audio = r.listen(source)
        try:
            command = r.recognize_google(audio)
            if command == 'exit':
                driver.close()
                print(bcolors.UNDERLINE+"Session end!")
                sys.exit(1)
            elif command == 'Type' or command== 'type' or command == 'write down' or command == 'write':
                print(bcolors.OKBLUE+'Typing...')
                messageaudio = r.listen(source)
                yourmessage = r.recognize_google(messageaudio)
                message = ActionChains(driver)
                message.send_keys(yourmessage)
                message.perform()
            elif command == 'Send' or command == 'send' or command == 'enter' or command == 'Enter':
                print(bcolors.OKGREEN+'Message Sent!')
                enter = ActionChains(driver)
                enter.send_keys(Keys.RETURN)
                enter.perform()
            else:
                print("no command exists!")
# TODO: voice calls and video calls
        except sr.UnknownValueError:
            print(bcolors.FAIL+'Failed to recognize! Try again!')
        except sr.RequestError as e:
            print(bcolors.FAIL+'Couldn\'t send request'.format(e))
