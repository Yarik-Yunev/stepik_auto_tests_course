import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    # применение алерт окна
    browser = webdriver.Chrome()
    browser.get('https://suninjuly.github.io/alert_accept.html')
    
    firstname = browser.find_element(By.CLASS_NAME, 'btn')
    firstname.click()
    
    alert = browser.switch_to.alert
    alert.accept()
    
    x_element = browser.find_element(By.ID, "input_value")
    x_alpha = int(x_element.text)
    otvet = calc(x_alpha)
    
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(otvet)
    
    button = browser.find_element(By.TAG_NAME, 'button')
    button.click()
    
    # много кнопок)
    # lastname = browser.find_element(By.NAME, 'lastname')
    # lastname.send_keys('Jonson')
    
    # email = browser.find_element(By.NAME, 'email')
    # email.send_keys('Jon@Jon.son')
    
    # file = browser.find_element(By.NAME, 'file')
    # c = os.path.abspath(os.path.dirname(__file__))
    # f = os.path.join(c, 'funcion_for_robot_capch.txt')
    # file.send_keys(f)
    
    # button = browser.find_element(By.TAG_NAME, 'button')
    # button.click()

finally:
    time.sleep(10)
    browser.quit()