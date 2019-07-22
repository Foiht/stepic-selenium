from selenium import webdriver
import time

br = webdriver.Chrome()
br.get('http://suninjuly.github.io/wait1.html')
br.implicitly_wait(5)
br.find_element_by_id('check').click()
test = br.find_element_by_id('check_message').text
assert 'успешно' in test