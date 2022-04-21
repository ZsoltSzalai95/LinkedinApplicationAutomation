from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

EMAIL = "YOUREMAIL"
PASSWORD = "YOURPASS"
PHONE = 000000

chrome_driver_path = "C:/Users/.../chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)
linked_in_URL= "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=104514075&keywords=python%20developer&location=Denmark"
driver.get(linked_in_URL)

sleep(2)
sign_in_button = driver.find_element_by_css_selector(".nav__button-secondary")
sign_in_button.click()

sleep(5)

user_name_field = driver.find_element_by_css_selector("#username")
user_name_field.send_keys(EMAIL)
password_field = driver.find_element_by_css_selector("#password")
password_field.send_keys(PASSWORD)
password_field.send_keys(Keys.ENTER)

sleep(5)

easy_apply = driver.find_element_by_css_selector(".jobs-apply-button--top-card")
easy_apply.click()
phone_nr = driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div/form/div/div[1]/div[3]/div[2]/div/div/input")
phone_nr.send_keys("50193190")