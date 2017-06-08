from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://localhost/Litecart/admin/login.php')
driver.implicitly_wait(10)
username = driver.find_element_by_name('username')
username.send_keys('admin')
driver.implicitly_wait(10)
password = driver.find_element_by_name('password')
password.send_keys('admin')
login = driver.find_element_by_name('login')
login.click()
driver.implicitly_wait(10)
# main menu check
lv1 = driver.find_elements_by_css_selector('#box-apps-menu li#app-')
for i in range(len(lv1)):
    lv1[i].click()
    driver.implicitly_wait(5)
    if not driver.find_elements_by_css_selector("h1"):    # headers check
        print('Error: The header is missing')
    lv1 = driver.find_elements_by_css_selector('#box-apps-menu li#app-')
    lv2 = driver.find_elements_by_css_selector(".docs li")
    #submenu check
    if len(lv2) > 0:
        for j in range(len(lv2)):
            lv2[j].click()
            driver.implicitly_wait(5)
            lv1 = driver.find_elements_by_css_selector('#box-apps-menu li#app-')
            lv2 = driver.find_elements_by_css_selector(".docs li")
            if not driver.find_elements_by_css_selector("h1"): # headers check
                print('Error: The header is missing')
driver.close()
