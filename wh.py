from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import platform
import cfonts
import colorama
import os

colorama.init()

cfonts.say("WHATSAPP", colors=["green", "white"])
cfonts.say("PY SPAMMER", colors=["red", "white"])

print(colorama.Fore.GREEN+'''
🔒 - Use at your own risk, we are not responsible for your actions.

☑️ - Made by Mazdak Pakaghideh and OrlatoDev.

📝 - Notes: follow the instructions below and when a Chrome window open, log in Whatsapp Web and return to follow the instructions.

'''+colorama.Fore.RESET)

print(colorama.Fore.RED+"Name of contact or group")
name = str(input("=> "))
print("Message")
msg = str(input("=> "))
print("Number of messages to send (0 for ultimated)")
num = int(input("=> "))
print("Delay beatwean each mesaage (from 0.1)")
delay = float(input("=> "))

os_name = platform.system()
dir_path = os.getcwd()
profile = os.path.join(dir_path, "profile", "wpp")
options = webdriver.ChromeOptions()
options.add_argument(
        r"user-data-dir={}".format(profile))

browser = webdriver.Chrome("./chromedriver.exe", options=options)

browser.get("https://web.whatsapp.com")

time.sleep(6)
#here i'm geting a unknow error, that say that some device is not working, i don´t know how fix this
start = str(input("🔥 - Type ENTER when you log into Whatsapp and you're ready: "))

def sendMessage(reciver, number, msg, delay):
    print("Spamming...")
    group = browser.find_element_by_xpath(f"//span[@title='{reciver}']")
    group.click()
    typech = browser.find_elements_by_class_name("_1awRl")

    if(number == 0):
        while(1):
            typech[1].send_keys(msg)
            typech[1].send_keys(Keys.ENTER)
            time.sleep(delay)
    else:
        for i in range(number):
            typech[1].send_keys(msg)
            typech[1].send_keys(Keys.ENTER)
            time.sleep(delay)

    print(colorama.Fore.GREEN+"\nFinish :)")
    os.system("cls")
    browser.close()

sendMessage(name, num, msg, delay)
