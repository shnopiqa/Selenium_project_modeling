import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

link = "http://suninjuly.github.io/find_link_text"
text = str(math.ceil(math.pow(math.pi, math.e) * 10000))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.LINK_TEXT, text).click()
    browser.find_element(By.TAG_NAME, "input").send_keys("Ivan")
    browser.find_element(By.NAME, "last_name").send_keys("Petrov")
    browser.find_element(By.CLASS_NAME, 'form-control.city').send_keys("Smolensk")
    browser.find_element(By.ID, "country").send_keys("Russia")
    browser.find_element(By.CSS_SELECTOR, ".btn.btn-default").click()
    print(browser._switch_to.alert.text)

finally:
    sleep(10)
    browser.quit()