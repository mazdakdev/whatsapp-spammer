from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Firefox(executable_path='./geckodriver.exe')

name = str(input("Name of contact => "))
msg = str(input("Message => "))
num = int(input("Number of messages to send (0 for ultimated) => "))

browser.get("https://web.whatsapp.com")
start = str(input("Type ENTER when you log into Whatsapp and you're ready: "))

def sendMesaage(reciver, number, message):
    print("Spamming...")
    group = browser.find_element_by_xpath(f"//span[@title='{reciver}']")
    group.click()
    typech = browser.find_elements_by_class_name("_1awRl")

    if(number == 0):
        while(1):
            typech[1].send_keys(msg)
            typech[1].send_keys(Keys.ENTER)
            time.sleep(0.1)
    else:
        for i in range(number):
            typech[1].send_keys(msg)
            typech[1].send_keys(Keys.ENTER)
            time.sleep(0.1)

    print("Finish :)")



sendMesaage(name, num, msg )
