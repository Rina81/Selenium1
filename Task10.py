from selenium import webdriver
driver = webdriver.Chrome()
#driver = webdriver.Edge()
#driver = webdriver.Firefox(capabilities={"marionette": True})
driver.get('http://localhost/Litecart/en/')
driver.implicitly_wait(10)
# *** remember and check data from the main page ***
name = driver.find_element_by_css_selector("div#box-campaigns a:nth-child(1)")
m_name = name.get_attribute('title')
m_rprice = driver.find_element_by_css_selector("div#box-campaigns a:nth-child(1) .regular-price").get_attribute('innerText')
m_cprice = driver.find_element_by_css_selector("div#box-campaigns a:nth-child(1) .campaign-price").get_attribute('innerText')
A = [m_name,m_rprice,m_cprice]
m_r_size = driver.find_element_by_css_selector("div#box-campaigns a:nth-child(1) .regular-price").value_of_css_property("font-size")
m_c_size = driver.find_element_by_css_selector("div#box-campaigns a:nth-child(1) .campaign-price").value_of_css_property("font-size")
if m_r_size < m_c_size:
    print('Regular Price font size is smaller than Campaign Price font size')
else:
    print('Error: Campaign Price font size is smaller than Regular Price font size')
colorR = driver.find_element_by_css_selector("div#box-campaigns a:nth-child(1) .regular-price").value_of_css_property("color")
RGB = colorR[5:-2].split(', ')     #Chrome, Edge
#RGB = colorR[4:-1].split(', ')  #FF
if RGB[0] != RGB[1] or RGB[1] != RGB[2]:
    print('Error: Regular Price Color is not grey')
else:
    print('Regular Price Color is grey')
line = driver.find_element_by_css_selector("div#box-campaigns a:nth-child(1) .regular-price").value_of_css_property('text-decoration')
if "line-through" not in line:
    print('Error: Regular Price is not through-lined')
else:
    print('Regular Price is through-lined')
colorC = driver.find_element_by_css_selector("div#box-campaigns a:nth-child(1) .campaign-price").value_of_css_property("color")
RGBc = colorC[5:-2].split(', ')
#RGBc = colorC[4:-1].split(', ')  #FF
#print(RGBc[1], RGBc[2])
if int(RGBc[1]) == 0 and int(RGBc[2]) == 0:
    print('Campaign Price color is red')
else:
    print('Error: Campaign Price color is not red')
lineC = driver.find_element_by_css_selector("div#box-campaigns a:nth-child(1) .campaign-price").value_of_css_property('font-weight')
#print(lineC)
if lineC == 'bold':      #Chrome
#if lineC < '700':      #Edge, FF
    print('Campaign Price text is bold')
else:
    print('Error: Campaign Price text is not bold')
product_link = driver.find_element_by_css_selector("div#box-campaigns a:nth-child(1)").get_attribute('href')
#   *** check data on the product page and compare with appropriate from the main page
driver.get(product_link)
driver.implicitly_wait(10)
p_name = driver.find_element_by_css_selector('#box-product div h1.title').get_attribute('innerText')
p_rprice = driver.find_element_by_css_selector('s.regular-price').get_attribute('innerText')
p_cprice = driver.find_element_by_css_selector('strong.campaign-price').get_attribute('innerText')
B = [p_name, p_rprice, p_cprice]
for i in range(0, 3):
    if A[i] != B[i]:
        print('Error: %s should be equal %s' % (A[i], B[i]))
    else:
        print('Data on the main page and on the product page are equal')
# regular price fonts check
p_r_size = driver.find_element_by_css_selector('s.regular-price').value_of_css_property("font-size")
p_c_size = driver.find_element_by_css_selector('strong.campaign-price').value_of_css_property("font-size")
if p_r_size < p_c_size:
    print('Product page:Regular Price font size is smaller than Campaign Price font size')
else:
    print('Product page:Error: Campaign Price font size is smaller than Regular Price font size')
p_colorR = driver.find_element_by_css_selector('s.regular-price').value_of_css_property("color")
p_RGB = p_colorR[5:-2].split(', ')     #Chrome, Edge
#p_RGB = colorR[4:-1].split(', ')  #FF
if p_RGB[0] != p_RGB[1] or p_RGB[1] != p_RGB[2]:
    print('Product page:Error: Regular Price Color is not grey')
else:
    print('Product page:Regular Price Color is grey')
p_line = driver.find_element_by_css_selector('s.regular-price').value_of_css_property('text-decoration')
if "line-through" not in p_line:
    print('Product page:Error: Regular Price is not through-lined')
else:
    print('Product page:Regular Price is through-lined')
p_colorC = driver.find_element_by_css_selector('strong.campaign-price').value_of_css_property("color")
p_RGBc = p_colorC[5:-2].split(', ')
#p_RGBc = p_colorC[4:-1].split(', ')  #FF
#print(p_RGBc[1], p_RGBc[2])
if int(p_RGBc[1]) == 0 and int(p_RGBc[2]) == 0:
    print('Product page:Campaign Price color is red')
else:
    print('Product Page: Error: Campaign Price color is not red')
p_lineC = driver.find_element_by_css_selector('strong.campaign-price').value_of_css_property('font-weight')
#print(lineC)
if p_lineC == 'bold':      #Chrome
    #if p_lineC < '700':      #Edge, FF
    print('Product page:Campaign Price text is bold')
else:
    print('Product page:Error: Campaign Price text is not bold')
driver.close()