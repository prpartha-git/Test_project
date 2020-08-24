#https://thetestingworld.com/
#https://thetestingworld.com/testings/

from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select

path="C:\\Users\\Parthu\\PycharmProjects\\chromedriver.exe"
driver=Chrome(executable_path=path)
driver.get("https://thetestingworld.com/testings/")
driver.maximize_window()

dropdown=Select(driver.find_element_by_name("sex"))
dropdown.select_by_visible_text("Male")
#dropdown.select_by_index(1)
#dropdown.select_by_value("1")