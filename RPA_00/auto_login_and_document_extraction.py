from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 

#Example of data
USERNAME = ''
PASSWORD = ''
SUBJECT = '1914-ISO800-GESTION DE CALIDAD DE SOFTWARE-VIR'
SUBJECT_TOPIC = 'Módulo 1 - Conceptos Básicos'
SUBJECT_TOPIC_FILE = 'Download Módulo 1-1.1 -Conceptos Básicos.pptx'
DOWNLOAD_PATH = ''
CHROME_DRIVER = ''

#Chrome settings to set custom path
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("prefs", {
  "download.default_directory": DOWNLOAD_PATH,
  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
  "safebrowsing.enabled": True
})

#Execute chrome automation driver
driver = webdriver.Chrome(executable_path=CHROME_DRIVER,chrome_options=chrome_options)

#set url
driver.get('https://canvas.unapec.edu.do/login/saml')

#path test
WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "i0116"))).send_keys(USERNAME)

WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "idSIButton9"))).click()

WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "i0118"))).send_keys(PASSWORD)

WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "idSIButton9"))).click()

WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "idBtn_Back"))).click()

WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, SUBJECT))).click()

WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, SUBJECT_TOPIC))).click()

WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, SUBJECT_TOPIC_FILE))).click()

#Wait until document is downloaded
time.sleep(3)



