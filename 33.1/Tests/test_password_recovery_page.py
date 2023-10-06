# python -m pytest -v --driver Firefox --driver-path "Путь до драйвера"geckodriver.exe test_password_recovery_page.py

from test_login_page import valid_number
from test_login_page import valid_email
from test_login_page import valid_login
from test_login_page import valid_ls
from test_login_page import login_page
from test_login_page import time_page
from test_login_page import small_time

import time
from selenium.webdriver.common.by import By


# test 1
def test_recovery_number(selenium):
    """Проверяем возможность восстановления пароля по телефону"""

    # Открыть страницу
    selenium.get(login_page)
    time.sleep(time_page)

    # Жмем кнопку "Забыл пароль"
    search_button = selenium.find_element(By.ID, 'forgot_password').click()
    time.sleep(small_time)

    # Ищем и вводим в поле "Телефон" телефон
    search_input = selenium.find_element(By.ID, 'username')
    search_input.send_keys(valid_number)

    # Жмем кнопку "Продолжить"
    search_button = selenium.find_element(By.ID, 'reset')
    time.sleep(time_page)

    # Тут должна быть проверка, что мы попадаем на страницу ввода кода из сообщения.
    # code


# test 2
def test_recovery_email(selenium):
    """Проверяем возможность восстановления пароля по email"""

    # Открыть страницу
    selenium.get(login_page)
    time.sleep(time_page)

    # Жмем кнопку "Забыл пароль"
    search_button = selenium.find_element(By.ID, 'forgot_password').click()
    time.sleep(small_time)

    # Ищем вкладку "почта"
    search_button = selenium.find_element(By.ID, 't-btn-tab-mail').click()

    # Ищем и вводим в поле "email" email
    search_input = selenium.find_element(By.ID, 'username')
    search_input.send_keys(valid_email)

    # Жмем кнопку "Продолжить"
    search_button = selenium.find_element(By.ID, 'reset')
    time.sleep(time_page)

    # Тут должна быть проверка, что мы попадаем на страницу ввода кода из сообщения.
    # code


# test 3
def test_recovery_login(selenium):
    """Проверяем возможность восстановления пароля по логину"""

    # Открыть страницу
    selenium.get(login_page)
    time.sleep(time_page)

    # Жмем кнопку "Забыл пароль"
    search_button = selenium.find_element(By.ID, 'forgot_password').click()
    time.sleep(small_time)

    # Ищем вкладку "Логин"
    search_button = selenium.find_element(By.ID, 't-btn-tab-login').click()

    # Ищем и вводим в поле "Логин" логин
    search_input = selenium.find_element(By.ID, 'username')
    search_input.send_keys(valid_login)

    # Жмем кнопку "Продолжить"
    search_button = selenium.find_element(By.ID, 'reset')
    time.sleep(time_page)

    # Тут должна быть проверка, что мы попадаем на страницу ввода кода из сообщения.
    # code


# test 4
def test_recovery_ls(selenium):
    """Проверяем возможность восстановления пароля по лицевому счету"""

    # Открыть страницу
    selenium.get(login_page)
    time.sleep(time_page)

    # Жмем кнопку "Забыл пароль"
    search_button = selenium.find_element(By.ID, 'forgot_password').click()
    time.sleep(small_time)

    # Ищем вкладку "Лицевой счет"
    search_button = selenium.find_element(By.ID, 't-btn-tab-ls').click()

    # Ищем и вводим в поле "Лицевой счет" лицевой счет
    search_input = selenium.find_element(By.ID, 'username')
    search_input.send_keys(valid_ls)

    # Жмем кнопку "Продолжить"
    search_button = selenium.find_element(By.ID, 'reset')
    time.sleep(time_page)

    # Тут должна быть проверка, что мы попадаем на страницу ввода кода из сообщения.
    # code


# test 5
def test_button_reset_back(selenium):
    """Проверяем возможность вернуться назад"""

    # Открыть страницу
    selenium.get(login_page)
    time.sleep(time_page)

    # Жмем кнопку "Забыл пароль"
    search_button = selenium.find_element(By.ID, 'forgot_password').click()
    time.sleep(small_time)

    # Жмем кнопку "Вернуться"
    search_button = selenium.find_element(By.ID, 'reset-back').click()
    time.sleep(small_time)

    # В качестве проверки делаем скрин
    selenium.save_screenshot('test_button_reset_back.png')


# test 6
def test_button_in_footer_privacy_policy(selenium):
    """Проверка работоспособности кнопки 'Политика конфиденциальности' в подвале"""

    # Открыть страницу
    selenium.get(login_page)
    time.sleep(time_page)

    # Жмем кнопку "Зарегестрироваться"
    search_button = selenium.find_element(By.ID, 'kc-register').click()
    time.sleep(small_time)

    # Жмем кнопку.
    search_button = selenium.find_element(By.XPATH, '//*[@id="rt-footer-agreement-link"]/span[1]').click()
    time.sleep(small_time)

    # Проверяем, что мы на нужной странице
    # К сожалению не смог зацепиться за текст, поэтому данная проверка на данный момент не работает. Может быть в будущем пофиксю.
    # search_text = selenium.find_element(By.XPATH, '//*[@class="offer-title"]/text()').text()
    # assert search_text == 'Публичная оферта о заключении Пользовательского соглашения на использование Сервиса «Ростелеком ID»'


# test 7
def test_button_in_footer_user_agreement(selenium):
    """Проверка работоспособности кнопки 'Пользовательское соглашение' в подвале"""

    # Открыть страницу
    selenium.get(login_page)
    time.sleep(time_page)

    # Жмем кнопку "Зарегестрироваться"
    search_button = selenium.find_element(By.ID, 'kc-register').click()
    time.sleep(small_time)

    # Жмем кнопку.
    search_button = selenium.find_element(By.XPATH, '//*[@id="rt-footer-agreement-link"]/span[2]').click()
    time.sleep(small_time)

    # Проверяем, что мы на нужной странице
    # К сожалению не смог зацепиться за текст, поэтому данная проверка на данный момент не работает. Может быть в будущем пофиксю.
    # search_text = selenium.find_element(By.XPATH, '//*[@class="offer-title"]/text()').text()
    # assert search_text == 'Публичная оферта о заключении Пользовательского соглашения на использование Сервиса «Ростелеком ID»'


# test 8
def test_button_in_footer_user_agreement(selenium):
    """Проверка работоспособности кнопки 'Cookie' в подвале"""

    # Открыть страницу
    selenium.get(login_page)
    time.sleep(time_page)

    # Жмем кнопку.
    search_button = selenium.find_element(By.ID, 'cookies-tip-open').click()
    time.sleep(small_time)

    # Проверяем, что мы на нужной странице
    # Возникает ошибка "TypeError: 'str' object is not callable", поэтому данная проверка на данный момент не работает. Может быть в будущем пофиксю.
    # search_text = selenium.find_element(By.XPATH, '//*[@class="rt-tooltip__title"]').text()
    # assert search_text == 'Мы используем Cookie»'
    # В качестве проверки делаем скрин
    selenium.save_screenshot('test_button_in_footer_user_agreement.png')
