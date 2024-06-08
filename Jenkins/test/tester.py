
from selenium import webdriver
from time import sleep



cService = webdriver.ChromeService(executable_path='/usr/bin/chromedriver')
driver = webdriver.Chrome(service = cService)

driver.get("http://seleniumdemo.com/")
sleep(5)