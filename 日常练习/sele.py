from selenium import webdriver
from seleniumtools import find_element
driver = webdriver.Chrome(executable_path="daily-exsercise\日常练习\chromedriver.exe")
driver.maximize_window()

driver.get("http://www.hfut.edu.cn/")
locator = ("link text", "学校概况")
find_element(driver,locator).click()
driver.switch_to_window(driver.window_handles[-1])
locator = [("link text","历史沿革"),("link text","现任领导"),("link text","历任领导"),("link text","学校章程"),("link text","工大标识")]
for i in locator:
    find_element(driver,i).click()


#弹窗点击确定按钮driver.switch_to_alert().accept()
# 弹窗点击取消按钮driver.switch_to_alert.dismiss()



# from selenium import webdriver
# import time
# # import seleniumtools as setol
# driver =webdriver.Chrome(executable_path="daily-exsercise\日常练习\chromedriver.exe")
# driver.get("https://www.taobao.com/")
# driver.maximize_window()
# # setol.find_element(driver, ("id", "q"), timeout=60).send_keys("hh")
# time.sleep(4)
# # driver.find_element_by_css_selector("#q").send_keys("hhh")
# a = driver.find_element_by_xpath('//*[@id="J_TSearchForm"]/div[1]/button')
# assert a.text  == "搜索"
# # assert a. ==
# #到淘宝搜索框输入海南之家，并且点击搜索按钮
# # element1 = driver.find_element_by_id("q").send_keys("海澜之家")
# # element2 = driver.find_element_by_xpath('//*[@id="J_TSearchForm"]/div[1]/button')
# # element2.click()
# # element1 = driver.find_element_by_id("kw")
# # element1.send_keys("hello selenium!")
# # element2 = driver.find_element_by_id("su")
# # element2.click()
# # driver.quit()
