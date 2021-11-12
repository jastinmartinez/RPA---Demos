from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui

#Example of data  
EMAIL = ''
PASSWORD = ''


#Execute chrome automation driver
driver = webdriver.Chrome('chromedriver')

#set url
driver.get('https://onedrive.live.com/about/en-us/signin/')



WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='email' and @placeholder='Email, phone, or Skype']"))).send_keys(EMAIL)

WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='submit']"))).click()

WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='password']"))).send_keys(PASSWORD)

WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='submit']"))).click()

WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[@class='ms-ContextualMenu-itemText label-107']"))).click()

pyautogui.write('C:/path_to_file/image.jpg') 

pyautogui.press('enter')