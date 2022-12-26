import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:\\Users\\Igor_Vasiliev.EPAM\\AppData\\Local\\Google\\Chrome\\User Data\\Default")

service = Service(executable_path="C:/Users/Igor_Vasiliev.EPAM/Desktop/Drivers/71/chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)
chat_id = ["243856482", "5508457168"]
text_msg = 'тест тест'
delay = 10


def getElem(id):
    driver.refresh()
    driver.get("https://web.telegram.org/k/#" + id)
    time.sleep(1)
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, 'input-message-input')))
    return driver.find_element(By.CLASS_NAME, 'input-message-input')


def main():
    for id in chat_id:
        inputElement = getElem(id)
        while not inputElement.is_displayed():
            inputElement = getElem(id)
        time.sleep(1)
        inputElement.click()
        inputElement.send_keys(text_msg)
        inputElement.send_keys(Keys.ENTER)
        time.sleep(1)


while 1:
    main()
    time.sleep(delay)
    print("new sending...")
