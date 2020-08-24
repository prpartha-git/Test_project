import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

path="C:\\Users\\Parthu\\PycharmProjects\\chromedriver.exe"
driver=Chrome(executable_path=path)
driver.get("https://thetestingworld.com/testings/")
driver.maximize_window()
driver.find_element_by_name("fld_username").send_keys("Rama")
act=ActionChains(driver)
#act.send_keys(Keys.TAB).perform()
#driver.find_element_by_name("fld_email").send_keys("abc@gmail.com")
act.key_down(Keys.CONTROL).send_keys('a').perform()
time.sleep(10)

#act.key_down(Keys.CONTROL).key_down(Keys.ALT).send_keys(Keys.DELETE).perform()

