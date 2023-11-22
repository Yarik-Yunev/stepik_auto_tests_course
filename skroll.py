from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

link = "https://suninjuly.github.io/execute_script.html"
browser.get(link)

try:
    x_element = browser.find_element(By.ID, "input_value")
    x_alpha = int(x_element.text)
    otvet = calc(x_alpha)
    
    browser.execute_script('window.scrollBy(0, 120);')

    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(otvet)
    
    check = browser.find_element(By.ID, 'robotCheckbox')
    check.click()
    
    radio = browser.find_element(By.ID, 'robotsRule')
    radio.click()
    
    button = browser.find_element(By.TAG_NAME, 'button')
    button.click()
    
finally:
    time.sleep(7)
    browser.quit()

# browser.execute_script("document.title='Script executing'; alert('Robots at work');")
# time.sleep(2)

#browser.execute_script("alert('Robots at work');")
#time.sleep(2)
