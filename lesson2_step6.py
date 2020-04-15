from selenium import webdriver
import time 
import math

link = "http://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = str(math.log(abs(12*math.sin(int(x)))))
    
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView({block: 'center'});", button)

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    input2 = browser.find_element_by_css_selector("[type='checkbox']")
    input2.click()
    input3 = browser.find_element_by_id("robotsRule")
    input3.click()
    button.click()

finally:
    time.sleep(30)
    browser.quit()
