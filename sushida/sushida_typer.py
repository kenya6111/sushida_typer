
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui

import os
from PIL import Image
import pyocr
import pyocr.builders
from time import sleep

path = "C:\\Program Files\\Tesseract-OCR"
os.environ["PATH"] = os.environ["PATH"] + path
os.environ["TESSDATA_PREFIX"] = "C:\\Program Files\\Tesseract-OCR\\tessdata"

tools = pyocr.get_available_tools()
print(tools)
tool=tools[0]
builder =pyocr.builders.TextBuilder(tesseract_layout=6)


driver = webdriver.Chrome()
driver.get('https://sushida.net/play.html')
driver.maximize_window()
sleep(15)
print(pyautogui.size())
#スタートをクリック
pyautogui.moveTo(x=1284,y=502)
pyautogui.click()
sleep(3)
#
print(pyautogui.position())
pyautogui.moveTo(x=1267,y=567)
pyautogui.click()
sleep(3)
pyautogui.press("enter")
sleep(5)
print(pyautogui.position())

while True:
    sc= pyautogui.screenshot(region=(1119,440,300,70))
    txt=tool.image_to_string(sc, lang="eng",builder=builder)
    pyautogui.write(txt,interval=0.01)

# sleep(5)

# sleep(20)
# actions = ActionChains(driver)
# actions.send_keys(Keys.ENTER).perform()
# sleep(3)
# while True:
#     actions.send_keys("abcdefghijklmnopqrstuvwxyz-,.!?").perform()

#product1--------------------------------------------------------
# driver = webdriver.Chrome()
# driver.get('https://sushida.net/play.html')
# driver.maximize_window()
# sleep(20)
# actions = ActionChains(driver)
# actions.send_keys(Keys.ENTER).perform()
# sleep(3)

# while True:
#     actions.send_keys("abcdefghijklmnopqrstuvwxyz-,.!?").perform()
#--------------------------------------------------------------------

# sleep(20)
# body =  driver.find_element(By.TAG_NAME, "body")
# print(body)
# actions = webdriver.ActionChains(driver)
# print(actions)
# actions.move_to_element_with_offset(body, 939, 370)
# sleep(5)
# actions.click().perform()
# #driver.quit()
# input()