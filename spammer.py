from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import platform
import cfonts
import colorama
import os


os_name = platform.system()

colorama.init()

cfonts.say("WHATSAPP", colors=["green", "white"])
cfonts.say("SPAMMER", colors=["red", "white"])

print(colorama.Fore.BLUE+'''
🔒 - Use at your own risk, we are not responsible for your actions.


☑️ - Made by Mazdak Pakaghideh and OrlatoDev.


📝 - Notes: follow the instructions below and when a Chrome window open, log in Whatsapp Web and return to follow the instructions.


'''+colorama.Fore.RESET)

print(colorama.Fore.GREEN+'''
=======
📝 - Instructions:
--------------------------------------------------------
|1-) Type the name of the contact or group             |
|                                                      |
|2-) Type the message you want to send                 |
|                                                      |
|3-) Enter how many times you want to send the message |                                               |
|                                                      |
|4-) Delay beatwean each message                       |
|                                                      |
|5-) Log in to your Whatsapp                           |
|                                                      |
|6-) Type Enter after logging in and you are ready     |
|                                                      |   
|                                                      | 
-------------------------------------------------------|


''')

print(colorama.Fore.BLUE+"Name of contact or group")
name = str(input("=> "))
print( colorama.Fore.CYAN+"Message")
msg = str(input("=> "))
print(colorama.Fore.YELLOW+"Number of messages to send (0 for ultimated)")
num = int(input("=> "))

print(colorama.Fore.GREEN+"Delay beatwean each mesaage (from 0.1)")
delay = float(input("=> "))

#Load driver based on detected os
if(os_name == "Linux"):
    browser = webdriver.Firefox(executable_path='./geckodriver')

elif(os_name == "Windows"):
     browser = webdriver.Firefox(executable_path='./geckodriver.exe')

elif(os_name == "Darwin"):
     browser = webdriver.Firefox(executable_path='./geckodriver')


browser.get("https://web.whatsapp.com")

time.sleep(6)


start = str(input("🔥 - Type ENTER when you log into Whatsapp and you're ready: "))


def sendMesaage(reciver, number, message , delay):
    print(colorama.Fore.GREEN+"Spamming...")

    group = browser.find_element_by_xpath(f"//span[@title='{reciver}']")
    group.click()
    input_box = browser.find_elements_by_class_name("_13NKt")

    if(number == 0):
        while(1):
            input_box[1].send_keys(message)
            input_box[1].send_keys(Keys.ENTER)

            time.sleep(delay)

    else:
        for i in range(number):
            input_box[1].send_keys(message)
            input_box[1].send_keys(Keys.ENTER)


            time.sleep(delay)

    
    print(colorama.Fore.GREEN+"\Spamming Finshed :)")
    os.system("clear")
    browser.close()

sendMesaage(name, num, msg  , delay)

