from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
browser = webdriver.Firefox(executable_path='./geckodriver')
print("this script is created by Mazdak Pakaghideh \n")
print("github.com/mazdakpak/whatsapp-spammer \n")
name = str(input("Name => \n"))
msg = str(input("Message => \n"))
num = int(input("Number of messages to send(0 for ultimated) =>"))

browser.get("https://web.whatsapp.com")
time.sleep(15)
def sendMesaage(reciver , number , message):
    num = 1
    group = browser.find_element_by_xpath(f"//span[@title='{reciver}']")
    group.click()
    typech = browser.find_elements_by_class_name("_3FRCZ")

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



sendMesaage(name ,num , msg )



        
        
        
    
