from selenium.webdriver import Chrome
path="C:\\Users\\Parthu\\PycharmProjects\\chromedriver.exe"
driver=Chrome(executable_path=path)
driver.get("https://www.google.com/")
driver.maximize_window()
driver.find_element_by_xpath("//input[@name='q']").send_keys("Python Learning..")
