from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://twitter.com")

time.sleep(3)

loginHome = driver.find_element_by_link_text('Log in')
loginHome.click()

time.sleep(2)

username = driver.find_element_by_name("session[username_or_email]")
username.send_keys("isi dengan id atau username twitter")

password = driver.find_element_by_name("session[password]")
password.send_keys("isi dengan password dari username yang ditulis diatas")
password.send_keys(Keys.RETURN)

time.sleep(1)

home = driver.find_element_by_link_text('Home').click()

time.sleep(2)

text = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
text.send_keys("Tulis apa saja")

time.sleep(2)

uploadImage = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div[1]/input')
uploadImage.send_keys("isi dengan lokasi file yang akan di upload")

time.sleep(2)

submit = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div[2]/div[3]').click()

# driver.quit()

