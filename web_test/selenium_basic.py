from selenium import webdriver  #导入Selenium的webdriver
from selenium.webdriver.common.keys import Keys  #导入Keys

driver = webdriver.Chrome()  #指定使用的浏览器，初始化webdriver
# driver.get("https://www.baidu.com")  #请求网页地址
url="http://114.55.234.161:8080/uim/loginPage.jsp?returnURL=%2Fportal%2Findex.jsp&logoutURL=%2Fportal%2Faction%2FfpSSOExit.action"
driver.get(url)
assert "登录" in driver.title  #看看Python关键字是否在网页title中，如果在则继续，如果不在，程序跳出。
print("当前页面：",driver.current_url)

elem_user=driver.find_element_by_id("loginName")
# print(elem_user)
elem_user.clear()
elem_user.send_keys('admin')
elem_pwd = driver.find_element_by_id("password")
elem_pwd.clear()
elem_pwd.send_keys('888888')
elem_pwd.send_keys(Keys.RETURN)
# driver.close()  #关闭webdriver

# def login(browser,username,password):
#     # 登录测试
#     browser.get("http://114.55.234.161:8080/portal")
#     try:
#         elem_user=browser.find_element_by_id("loginName")
#         elem_user.clear()
#         elem_user.send_keys('username')
#         elem_pwd=browser.find_element_by_id("password")
#         elem_pwd.clear()
#         elem_pwd.send_keys('password')
#         elem_pwd.send_keys(Keys.RETURN)
#         return username^"login successfully \n"
#     except:
#         return username^"login failed \n"
#     pass
#
#     login(driver,admin,888888)