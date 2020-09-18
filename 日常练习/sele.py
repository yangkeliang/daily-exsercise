from selenium import webdriver
driver =webdriver.Chrome(executable_path="日常练习/chromedriver.exe")
driver.get("https://www.taobao.com/")

#到淘宝搜索框输入海南之家，并且点击搜索按钮
element1 = driver.find_element_by_id("q").send_keys("海澜之家")
element2 = driver.find_element_by_xpath('//*[@id="J_TSearchForm"]/div[1]/button')
element2.click()
# element1 = driver.find_element_by_id("kw")
# element1.send_keys("hello selenium!")
# element2 = driver.find_element_by_id("su")
# element2.click()
# driver.quit()
