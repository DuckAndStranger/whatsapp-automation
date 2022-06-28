import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from time import sleep
import os

files = os.listdir("spampics")

chromedriver_autoinstaller.install()
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver,600)

sleep(10)
receiver = str(input("\n\n\n\n\nEnter name of group or user: "))
target = "'" + receiver + "'"
x_arg = '//span[contains(@title, ' + target + ')]'
target = wait.until(ec.presence_of_element_located((By.XPATH,x_arg)))
target.click()

i = 1
for st in files:
    #Generating path to picture
    st = os.path.abspath(str("spampics/" + st))
    #Sending picture
    attachment = driver.find_element_by_xpath('//div[@title="Attach"]')
    attachment.click()
    image_box = driver.find_element_by_xpath('//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
    image_box.send_keys(st.strip())
    sleep(1)
    send_btn = driver.find_element_by_xpath('//span[@data-icon="send"]')
    send_btn.click()
    sleep(1)
    print("Picture №", i ,"sent")
    i+=1