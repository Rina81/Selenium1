import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('http://localhost/Litecart/admin/login.php');
time.sleep(5)
username = driver.find_element_by_name('username')
username.send_keys('admin')
password = driver.find_element_by_name('password')
password.send_keys('admin')
login = driver.find_element_by_name('login')
login.click()
time.sleep(5)
driver.quit()