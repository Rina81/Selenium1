from selenium import webdriver
driver = webdriver.Chrome()
driver.get('http://localhost/Litecart/admin/login.php')
# *** LOGIN ***
driver.implicitly_wait(10)
username = driver.find_element_by_name('username')
username.send_keys('admin')
password = driver.find_element_by_name('password')
password.send_keys('admin')
login = driver.find_element_by_name('login')
login.click()
driver.implicitly_wait(10)
# *** CHECK COUNTRIES SORTING ***
driver.get('http://localhost/Litecart/admin/?app=countries&doc=countries')
driver.implicitly_wait(10)
table = driver.find_element_by_css_selector('form>table.dataTable')
sorted_countries = []
for country in table.find_elements_by_xpath('.//tr/td[5]/a'):    #check countries sorting
    if country.text != '':
        sorted_countries.append(country.text)
countries_unsorted = sorted_countries
sorted_countries.sort()
if countries_unsorted == sorted_countries:
    print("Countries are sorted")
else:
    print("Countries are not sorted")
# *** CHECK ZONES SORTING ON COUNTRY PAGE ***
hrefs = []
zones = driver.find_elements_by_xpath('//form/table/tbody/tr/td[6]')
for zone in zones:
    if zone.text != "0":
        mm = zone.find_element_by_xpath('../td[5]/a').get_attribute('href')
        hrefs.append(mm)
print(hrefs)
for href in hrefs:
    driver.get(href)
    driver.implicitly_wait(20)
    country_value = driver.find_element_by_xpath("//tbody/tr//td//input[@name='name']").get_attribute('value')
    print(country_value)
    table = driver.find_element_by_css_selector('.dataTable')
    zone_list = table.find_elements_by_xpath('..//tr/td[3]')
    zone_names = []
    if zone_list != []:
        for zone_1 in zone_list:
            zone_names.append(zone_1.text)
        zone_sorted = zone_names
        zone_sorted.sort()
        print(zone_sorted)
        if zone_sorted == zone_names:
            print("Zones are sorted")
        else:
            print("Zones are not sorted")
    driver.get('http://localhost/Litecart/admin/?app=countries&doc=countries')
    driver.implicitly_wait(10)
  # *** CHECK ZONES SORTING FROM GEOZONES PAGE ***
driver.get('http://localhost/Litecart/admin/?app=geo_zones&doc=geo_zones')
driver.implicitly_wait(10)
#table = driver.find_element_by_class_name('dataTable')
geolinks = []
for geo_country in driver.find_elements_by_css_selector('td:nth-child(3)>a'):
    ll = geo_country.get_attribute('href')
    geolinks.append(ll)
print(geolinks)
for geolink in geolinks:
    driver.get(geolink)
    driver.implicitly_wait(10)
    countryname = driver.find_element_by_css_selector('[name=name]').get_attribute('value')
    print(countryname)
    table = driver.find_element_by_class_name('dataTable')
    zones = table.find_elements_by_css_selector('td:nth-child(3) > select > [selected=selected]')
    zone_values = []
    if len(zones) > 1:
        for zone in zones:
            zone_values.append(zone.text)
        zone_values_sorted = zone_values
        zone_values_sorted.sort()
        if zone_values_sorted == zone_values:
            print('Geozones are sorted')
        else:
            print('Geozones are not sorted')
        driver.get('http://localhost/Litecart/admin/?app=geo_zones&doc=geo_zones')
        driver.implicitly_wait(10)
driver.close()


