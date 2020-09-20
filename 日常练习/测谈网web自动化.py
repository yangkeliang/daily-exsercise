from selenium import webdriver
import time
# def login():
driver = webdriver.Chrome("daily-exsercise\日常练习\chromedriver.exe")
driver.get("http://118.24.105.78:8080/ljindex/index.html")
element1 = driver.find_element_by_xpath('//*[@id="unlogin"]/div[1]/a')
element1.click()
time.sleep(3)
elementname = driver.find_element_by_xpath('//*[@id="username"]')
elementname.send_keys("yangkeliang")
elementpasswd = driver.find_element_by_id("password")
elementpasswd.send_keys("a1234567")
elementlogin = driver.find_element_by_id("userLogin")
elementlogin.click()
time.sleep(3)
elementarticle = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[2]/div/div[1]/div[1]/span")
elementarticle.click()
element_article_title = driver.find_element_by_id("user_article_title")
element_article_title.send_keys("yann")
element_article_content = driver.find_element_by_class_name("w-e-text")
element_article_content.send_keys("挺牛逼呗")
element_tj = driver.find_element_by_id("allcommit")
element_tj.click()
time.sleep(100)


# if __name__=="__main__":
#     login()