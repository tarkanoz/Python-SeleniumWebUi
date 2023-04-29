#PDPTechSpecShareNewProduct
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
import json
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import atexit
from datetime import datetime
import pandas as pd
import xlsxwriter
def initialize_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver
def shutdown_driver():
    print('fail something happened')
    driver.close()
atexit.register(shutdown_driver)
def select_random_element(elements):
    index = random.randint(0, len(elements) - 1)
    return elements[index]
def open_products_menu_item(driver):
    PRODUCTS_MENU_ITEM = driver.find_element_by_css_selector('#header-main > div > nav.menu.main__menu.Menu__root > button.JS-menu-button.subnav-products.NavigationButton__root')
    PRODUCTS_MENU_ITEM.click()
def select_random_product_category_from_header_menu(driver):
     global status,errorDetail
    
     #first
     PRODUCTS_CATEGORY_CONTAINERS = driver.find_elements(by=By.XPATH, value='//*[@id="subnav"]/div[1]/div[2]/div[1]/div[2]/div')
     print('Found', len(PRODUCTS_CATEGORY_CONTAINERS), 'product category containers in header menu', ' ')
     PRODUCTS_CATEGORY_CONTAINER = select_random_element(PRODUCTS_CATEGORY_CONTAINERS)
     webdriver.ActionChains(driver).move_to_element(PRODUCTS_CATEGORY_CONTAINER).perform()
     PRODUCTS_CATEGORY_CONTAINER.click()
     #2th 
     FIRST_CATEGORY_BUTTON_TEXT = PRODUCTS_CATEGORY_CONTAINER.text
     print(FIRST_CATEGORY_BUTTON_TEXT)
     FIRST_CATEGORY_BUTTON_TEXT_PRO = FIRST_CATEGORY_BUTTON_TEXT.lower().replace(' ', '-')
     PRODUCTS_CATEGORY_TWO = driver.find_elements(by=By.XPATH, value='//*[@id="header-big-menu-'+FIRST_CATEGORY_BUTTON_TEXT_PRO+'"]/div[1]/div[2]/div[1]/ul/li')
     print(PRODUCTS_CATEGORY_TWO)
     PRODUCTS_CATEGORY_TWO_CONTAINER = select_random_element(PRODUCTS_CATEGORY_TWO)
     webdriver.ActionChains(driver).move_to_element(PRODUCTS_CATEGORY_TWO_CONTAINER).perform()
     print(PRODUCTS_CATEGORY_TWO_CONTAINER)
     print('Found', len(PRODUCTS_CATEGORY_TWO), 'product category buttons in selected container', ' ')
     PRODUCTS_CATEGORY_TWO_CONTAINER.click()
     PRODDUCT_CATEGORY_TWO_CONTAINER_TEXT = PRODUCTS_CATEGORY_TWO_CONTAINER.text
     print('Selected product category container', PRODDUCT_CATEGORY_TWO_CONTAINER_TEXT)
     PRODUCTS_CATEGORY_TWO_CONTAINER_BUTTON_TEXT = PRODDUCT_CATEGORY_TWO_CONTAINER_TEXT.lower().replace(' ', '-')
     #3th
     PRODUCTS_CATEGORY_THREE = driver.find_elements(by=By.XPATH, value='//div[@id="header-bug-menu-'+FIRST_CATEGORY_BUTTON_TEXT_PRO+'-'+PRODUCTS_CATEGORY_TWO_CONTAINER_BUTTON_TEXT+'"]//a')
     print('Found', len(PRODUCTS_CATEGORY_THREE), 'product category containers in header menu', ' ')
     if len(PRODUCTS_CATEGORY_THREE) == 0:
         CHOOSE_ONE_SUB_CATEGORY = driver.find_element(by=By.XPATH, value='//div[@id="header-bug-menu-'+FIRST_CATEGORY_BUTTON_TEXT_PRO+'-'+PRODUCTS_CATEGORY_TWO_CONTAINER_BUTTON_TEXT+'"]//a')
         webdriver.ActionChains(driver).move_to_element(CHOOSE_ONE_SUB_CATEGORY)
         CHOOSE_ONE_SUB_CATEGORY.click()
         print('go to the PLP')
     else:
         PRODUCTS_CATEGORY_THREE_CONTAINER = select_random_element(PRODUCTS_CATEGORY_THREE)
         webdriver.ActionChains(driver).move_to_element(PRODUCTS_CATEGORY_THREE_CONTAINER).perform()
         PRODUCTS_CATEGORY_THREE_CONTAINER.click()
         print('select random sub category and go to the plp ')
def excel():
    end_time = time.time()
    finish_time = end_time-start_time
    excelFile = xlsxwriter.Workbook('result.xlsx')
    workSheet = excelFile.add_worksheet('news')
    test_data = {
        'testCode':['PDP TechSpec Share Button'],
        'testScenario':['In the techspec section of the PDP area, the relevant social media icons are randomly selected and clicked.'],
        'end_time':[finish_time],
        'status':[status],
        'ErroDetail':[errorDetail+(driver.current_url)],
        'lastTestDate':[datetime.today],
        'url':[GO_TO_URL],
        'lang':[language]
    }
    dt = pd.DataFrame(test_data)
    writer = pd.ExcelWriter(workSheet)
    writer.book = excelFile
    dt.to_excel(writer,sheet_name='news')
    col_num = writer.sheets['news'].max_row
    for key, value in test_data.items():
        workSheet.write(0,col_num,key)
        workSheet.write_column(1,col_num,value)
        col_num +=1
    writer.close()     
def page_404():
    global status,errorDetail
    TITLE_404 = driver.find_element(By.CSS_SELECTOR,"head > title").get_attribute("textContent")
    print(language," page :",TITLE_404) 
    if str(TITLE_404) == "404":
           print("fail 404 page not found {country_code}")
           status ="fail"
           errorDetail="page is 404"
    elif str(TITLE_404) == "404 Not Found":
           print("fail 404 page {country_code} ")
           status ="fail"
           errorDetail="page is 404"
    elif str(TITLE_404) == "Site Not Found":
           print("fail 404 page  {country_code} ") 
           status ="fail"
           errorDetail="page is 404"
    elif str(TITLE_404) == "Not Found":
           print("fail 404 page  {country_code} ") 
           status ="fail"
           errorDetail="page is 404"
    else:       
           print("pass") 
def chatboxBlocker(driver):
  js_code = driver.execute_script("document.readyState === 'complete'")
  try:
        if js_code == True:
           driver.execute_script("var pop_up_facebook = document.querySelectorAll('.CookiePolicyBanner')[1]; if (c!== null) { c.remove();} ")
           driver.execute_script("var pop_up_location = document.querySelector('.fb_dialog'); if (a!== null) { a.remove();} ")
           driver.execute_script("var pop_up_location_reset =document.querySelector('.fb_reset'); if (b!==null) { b.remove();}")
        else:    
           time.sleep(20)
           driver.execute_script("var pop_up_facebook = document.querySelectorAll('.CookiePolicyBanner')[1]; if (c!== null) { c.remove();} ")
           driver.execute_script("var pop_up_location = document.querySelector('.fb_dialog'); if (a!== null) { a.remove();} ")
           driver.execute_script("var pop_up_location_reset =document.querySelector('.fb_reset'); if (b!==null) { b.remove();}")
           time.sleep(8)
  except NoSuchElementException:
        print("chat box not found")            
with open("country_lang.json") as jsonFile:
    jsonObject = json.load(jsonFile)
for language in jsonObject['languages']:
    start_time = time.time()
    URL = "https://www.*******.com/"
    driver = initialize_driver()
    GO_TO_URL =  driver.get(URL + (language))
    time.sleep(4)
    # page_404()
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="onetrust-accept-btn-handler"]')))
    except TimeoutException as ex:
        print("time out")
    try:
        ACCEPPT_COOKIE = driver.find_element(By.XPATH,'//*[@id="onetrust-accept-btn-handler"]')
        ACCEPPT_COOKIE.click()
        time.sleep(2)
    except :
        print('cookie not found')
    
    chatboxBlocker(driver)
    try:
        open_products_menu_item(driver)
        select_random_product_category_from_header_menu(driver)
    except:
        print("fail product landing page not found")
        status = "fail"
        errorDetail = " product landing page not found"
        excel()
        driver.close()
        continue
    chatboxBlocker(driver)
    page_404()
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH,'//*[@id="onetrust-accept-btn-handler"]')))
    except TimeoutException as ex:
        print("time out")
    try:
        ACCEPPT_COOKIE = driver.find_element(By.XPATH,'//*[@id="onetrust-accept-btn-handler"]')
        ACCEPPT_COOKIE.click()
        time.sleep(2)
    except :
        print('second cookie not found')
    driver.execute_script("window.scrollBy(0.,document.body.scrollHeight)")
    time.sleep(4)
    #scroll Page
    driver.execute_script("var i = 1;   function myLoop() {  var btn_text = document.querySelector('button#loadMoreProductButton');{ setTimeout(function() { document.querySelector('button#loadMoreProductButton').click(); i++;    if (i < 50) { myLoop(); }}, 50);}} myLoop();")
    time.sleep(8)
    driver.execute_script("window.scrollBy(0.,document.body.scrollHeight)")
    PRODUCTS = driver.find_elements(By.CSS_SELECTOR, '#productCardContainer > div > div > div.ProductCardPLP__productBody > a')
    print('product:', len(PRODUCTS))
    time.sleep(3)
    if PRODUCTS == 0:
            print("fail product not found ")
            status ='fail '
            errorDetail ="product not found"
    else:  
        print("too many products")
        status="succesful"
        errorDetail=" "
        RANDOM_PRODUCT = random.randint(0, len(PRODUCTS) - 1)  
        print('product selected: ', RANDOM_PRODUCT) 
        SELECT_PRODUCT = PRODUCTS[RANDOM_PRODUCT].click()
        # driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div/div[4]/div[3]/div[1]/div[2]/div/section/div/div[{0}]'.format(random_product)).click()
        print('The product has been clicked')
        time.sleep(3)
        page_404()
        time.sleep(4)
        chatboxBlocker(driver)
    driver.execute_script("window.scrollBy(0.,document.body.scrollHeight)")
    time.sleep(3)
    GO_TO_TECHSPECS = driver.find_element(By.CSS_SELECTOR,"#app > div.root.responsivegrid > div > div.responsivegrid.aem-GridColumn.aem-GridColumn--default--12 > div > div.productdetail.parbase.aem-GridColumn.aem-GridColumn--default--12 > div.pageContent > div.Pb\(90px\).Pb\(70px\)--sm.PdpPage__content > div.Ov\(h\).W\(100\%\).Bgc\(\$white\).Z\(2\).PdpPage__content > div.Py\(90px\).Pt\(70px\)--sm.Bgc\(\$pink-lavanda-gray\) > section > div > div:nth-child(1) > div > div.D\(f\).Mx\(a\).Jc\(sb\)--sm.Pos\(r\).DocumentIconBtns__root.DocumentIconBtns__hideMobile > button.JS-share-button.Mend\(45px\)--md.IconBtn__root.aos-init.aos-animate")
    driver.execute_script("arguments[0].click();", GO_TO_TECHSPECS)
    # GO_TO_TECHSPECS.click()
    time.sleep(3)
    
    try:

        ICONS_LEN = len(driver.find_elements(By.CSS_SELECTOR,'div.active a.ButtonIcon__white div.buttonInner svg.Icon__root'))
        RANDOM_VALUE = random.randint(0,ICONS_LEN-2)
        print(RANDOM_VALUE)
        driver.execute_script("window.scrollTo(0, window.scrollY -200)")
        driver.implicitly_wait(10)
        array = ["Fb","Tw","Pr","Mail"]
        # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH," (//div[contains(@class,'ShareBlock__root active')])/a[{}]".format(RANDOM_VALUE))))
        # ICON = driver.find_element(By.XPATH," (//div[contains(@class,'ShareBlock__root active')])/a[{}]/div".format(RANDOM_VALUE)).click
        print(array[RANDOM_VALUE])
        ICON = driver.find_element(By.XPATH,"(//a[contains(@class,'ButtonIcon__share{}')])[3]".format(array[RANDOM_VALUE]))
        # ICON.click()
        time.sleep(3)
        if ICON.is_displayed:
            driver.execute_script("arguments[0].click();", ICON)
            # ICON.click()
            # ICON = driver.find_element(By.XPATH," (//div[contains(@class,'ShareBlock__root active')])/a[{}]".format(RANDOM_VALUE)).click
            time.sleep(2)
            print("pass")
            time.sleep(5)
            status ="successfull" 
            errorDetail =""
        else:
            print("fail") 
            status ='fail '
            errorDetail ="product not found" 
            
    except NoSuchElementException:
        print("N/A Icon Not Found")
        status="N/A"
        errorDetail="This field is opsiyonel and not avaliable" 
       
        
    # excel()           
    driver.close()
driver.quit()