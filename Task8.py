from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://localhost/Litecart/')
lst = driver.find_elements_by_css_selector('div.image-wrapper')
if len(lst) > 0:
    for i in range(len(lst)):
        st = lst[i].find_elements_by_class_name('sticker')
        a = len(st)
        if a != 1:
            print("Error: there is %s stickers. Each product should have 1 sticker" %a)
driver.implicitly_wait(10)
driver.close()

