from selenium import webdriver

## 如果是chrome浏览器的驱动
#driver = webdriver.Chrome("G:\Anaconda3-5.3.0\chromedriver.exe")

##如果是firefox浏览器的驱动
#driver = webdriver.Firefox(executable_path="G:\Anaconda3-5.3.0\geckodriver.exe")

######如果浏览器驱动的目录加入了环境变量的话

## 如果是chrome浏览器的驱动
driver = webdriver.Chrome()
driver.get(url='https://www.baidu.com')
driver.find_element_by_xpath("//select[@id='9560af43bfc949c4826d329c352e4eb6_class']").select_by_index(4)  # 定位公共互联网环境

##如果是firefox浏览器的驱动
#driver = webdriver.Firefox()

driver.find_elemant_by_xpath("//html/body/form/input[1]")

driver.find_element_by_xpath("//form/input")

# 用相对路径和属性进行定位，form标签下的input标签的name值等于username的标签
driver.find_element_by_xpath("//form/input[@name='username']")

driver.find_element_by_xpath("//a[contains(@href,'login')]")

# 切换到指定的iframe框架
driver.switch_to.frame("mainFrame")  # 切换iframe框架
driver.switch_to.default_content()  # 切换到主框架
