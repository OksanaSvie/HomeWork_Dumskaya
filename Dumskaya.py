# Домашнее задание
# Закончить регистрацию на сайте 'https://dumskaya.net/' с использованием ожиданий которые рассматривали на паре.

import time

import random
import string

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://dumskaya.net/')
driver.maximize_window()


def generate_email(length):  # Создание рандомных email,ников и паролей
    letters_and_digits = string.ascii_letters + string.digits
    rand_string = ''.join(random.sample(letters_and_digits, length))
    return rand_string


email = generate_email(10)


def generate_nick(length):
    letters_and_digits_2 = string.ascii_letters + string.digits
    random_string = ''.join(random.sample(letters_and_digits_2, length))
    return random_string


nick = generate_nick(10)


def generate_password(length):
    letters_and_digits_3 = string.ascii_letters + string.digits
    random_string_password = ''.join(random.sample(letters_and_digits_3, length))
    return random_string_password


password1 = generate_password(8)

password2 = password1
#
#
id_start = 'pp'
button_start = WebDriverWait(driver, 30).until(EC.presence_of_element_located(('id', id_start)))
button_start.click()
xpath_registration_button = '//a[@href="/register/"]'
registration_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable(('xpath', xpath_registration_button)))
registration_button.click()

xpath_field_email = '//td/input[@name="email"]'
field_email = WebDriverWait(driver, 30).until(EC.element_to_be_clickable(('xpath', xpath_field_email)))
field_email.send_keys(email)

xpath_field_nick = '//td/input[@name="nick"]'
field_email = WebDriverWait(driver, 30).until(EC.element_to_be_clickable(('xpath', xpath_field_nick)))
field_email.send_keys(nick)

xpath_field_password1 = '//td/input[@name="password1"]'
field_email = WebDriverWait(driver, 30).until(EC.element_to_be_clickable(('xpath', xpath_field_password1)))
field_email.send_keys(password1)

xpath_field_password2 = '//td/input[@name="password2"]'
field_email = WebDriverWait(driver, 30).until(EC.element_to_be_clickable(('xpath', xpath_field_password2)))
field_email.send_keys(password2)

xpath_field_gender = '//td/input[@type="radio" and @value="f"]'
button_gender = WebDriverWait(driver, 30).until(EC.element_to_be_clickable(('xpath', xpath_field_gender)))
button_gender.click()

xpath_field_register = '//td/input[@value="Зарегистрироваться"]'
button_register = WebDriverWait(driver, 30).until(EC.element_to_be_clickable(('xpath', xpath_field_register)))
button_register.click()

xpath_field_arrow = '//a [@href="javascript:showuserinfo()" and @class="celldtrif"]'
button_arrow = WebDriverWait(driver, 30).until(EC.element_to_be_clickable(('xpath', xpath_field_arrow)))
button_arrow.click()

xpath_field_exit = '//a [@href="/exit/"]'
button_exit = WebDriverWait(driver, 30).until(EC.element_to_be_clickable(('xpath', xpath_field_exit)))
button_exit.click()

time.sleep(500)
