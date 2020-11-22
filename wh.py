from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import platform

os_name = platform.system()

class terminalColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(terminalColors.WARNING+'''
🔥🔥🔥 WHATSAPP SPAMMER 🔥🔥🔥

🔒 - Use at your own risk, we are not responsible for your actions.

☑️  - Made by Mazdak Pakaghideh and  OrlatoDev.

📝 - Notes: a firefox window will open, minimize it and follow the instructions presented in the terminal (right after you will have to log into Whatsapp in that same window)

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


'''+terminalColors.ENDC)

print(terminalColors.OKBLUE+"Name of contact or group"+terminalColors.ENDC)
name = str(input("=> "))
print(terminalColors.OKBLUE+"Message"+terminalColors.ENDC)
msg = str(input("=> "))
print(terminalColors.OKBLUE+"Number of messages to send (0 for ultimated)"+terminalColors.ENDC)
num = int(input("=> "))
print(terminalColors.OKBLUE+"Delay beatwean each mesaage (from 0.1)"+terminalColors.ENDC)
delay = float(input("=> "))
if(os_name == "Linux"):
    browser = webdriver.Firefox(executable_path='./geckodriver')
elif(os_name == "Windows"):
     browser = webdriver.Firefox(executable_path='./geckodriver.exe')


browser.get("https://web.whatsapp.com")

start = str(input(terminalColors.OKGREEN+"🔥 - Type ENTER when you log into Whatsapp and you're ready: ")+terminalColors.ENDC)

def sendMesaage(reciver, number, message , de):
    print(terminalColors.WARNING+"Spamming..."+terminalColors.ENDC)
    group = browser.find_element_by_xpath(f"//span[@title='{reciver}']")
    group.click()
    typech = browser.find_elements_by_class_name("_1awRl")

    if(number == 0):
        while(1):
            typech[1].send_keys(msg)
            typech[1].send_keys(Keys.ENTER)
            time.sleep(de)
    else:
        for i in range(number):
            typech[1].send_keys(msg)
            typech[1].send_keys(Keys.ENTER)
            time.sleep(de)

    print(terminalColors.OKGREEN+"Finish :)"+terminalColors.ENDC)



sendMesaage(name, num, msg  , delay)
