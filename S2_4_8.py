from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

br = webdriver.Chrome()
br.get('http://suninjuly.github.io/explicit_wait2.html')
button =  br.find_element_by_id('book')
WebDriverWait(br, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '10000'))
button.click()
x = br.find_element_by_id('input_value').text
br.find_element_by_id('answer').send_keys(calc(x))
br.find_element_by_id('solve').click()
print(br.switch_to.alert.text.split()[-1])