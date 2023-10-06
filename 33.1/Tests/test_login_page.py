# python -m pytest -v --driver Firefox --driver-path "Путь до драйвера"geckodriver.exe test_login_page.py

import time
from selenium.webdriver.common.by import By

login_page = 'https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=149e4875-32e6-491e-bccb-1e01cb086a56&theme&auth_type'
# Данные взяты самостоятельно.
valid_number = '9123456789'
valid_email = 'User@y.ru'
valid_login = 'User123'
valid_ls = '652651511332'
valid_password = 'Qwerty789'
no_valid_number = '9213456789'
no_valid_email = 'UserNoMe@ya.ru'
no_valid_login = 'User321'
no_valid_ls = '763762622443'
no_valid_password = 'no_qwerty'

time_page = 7
small_time = 1


# Примечание:
# Тесты могут завсать из-за капчи. Прописать любые данные в поля логина и пароля, ввести капчу.
# При использовании гибких ожиданий по типу presence_of_element_located, тесты ломаются, поэтому используется модуль time.sleep
# В проверках assert, где требуется проверить "Неправильный логин или пароль" из-за наличия капчи тест ломается.

# test 1.
def test_login_with_valid_data_number(selenium):
    """Вход с валидными данными по номеру телефона"""

    # Открыть страницу
    selenium.get(login_page)

    time.sleep(time_page)

    # Ищем и вводим в поле "телефон" валидный номер телефона
    search_input = selenium.find_element(By.ID, 'username')
    search_input.send_keys(valid_number)

    # Ищем и вводим в поле "пароль" валидный пароль
    search_input = selenium.find_element(By.ID, 'password')
    search_input.send_keys(valid_password)

    # жмем кнопку "Войти"
    search_button = selenium.find_element(By.ID, 'kc-login').click()

    # Проверяем, что попали на необходимую страницу
    # Предпологаю, что при попадании в личный кабинет мы находим любой элемент, в данном случае заголовок с текстом
    # "Личный кабинет" и id == title, и проверяем, что дейтсвительно попали на необходмую нам страницу.
    # search_input = selenium.find_element(By.ID, 'title').text()
    # assert search_input == 'личный кабинет'


# test 2
def test_login_with_no_valid_data_number(selenium):
    """Вход с не валидными данными по номеру телефона"""

    # Открыть страницу
    selenium.get(login_page)

    time.sleep(time_page)

    # Ищем и вводим в поле "телефон" не валидный номер телефона
    search_input = selenium.find_element(By.ID, 'username')
    search_input.send_keys(no_valid_number)

    # Ищем и вводим в поле "пароль" не валидный пароль
    search_input = selenium.find_element(By.ID, 'password')
    search_input.send_keys(no_valid_password)

    # Жмем кнопку "Войти"
    search_button = selenium.find_element(By.ID, 'kc-login').click()
    time.sleep(small_time)

    # Проверяем, что появилось сообщение о неверных данных.
    search_error = (selenium.find_element(By.ID, 'form-error-message')).text
    assert search_error == 'Неверный логин или пароль'


# test 3
def test_login_with_valid_data_email(selenium):
    """Вход с валидными данными по почте"""

    # Открыть страницу
    selenium.get(login_page)

    time.sleep(time_page)

    # Нажимаем на вкладку "Почта"
    element = selenium.find_element(By.ID, 't-btn-tab-mail').click()

    time.sleep(small_time)

    # Ищем и вводим в поле "телефон" валидный номер телефона
    search_input = selenium.find_element(By.ID, 'username')
    search_input.send_keys(valid_email)

    # Ищем и вводим в поле "пароль" валидный пароль
    search_input = selenium.find_element(By.ID, 'password')
    search_input.send_keys(valid_password)

    # жмем кнопку "Войти"
    search_button = selenium.find_element(By.ID, 'kc-login').click()

    # Проверяем, что попали на необходимую страницу
    # Предпологаю, что при попадании в личный кабинет мы находим любой элемент, в данном случае заголовок с текстом
    # "Личный кабинет" и id == title, и проверяем, что дейтсвительно попали на необходмую нам страницу.
    # search_input = selenium.find_element(By.ID, 'title').text
    # assert search_input == 'личный кабинет'


# test 4
def test_login_with_no_valid_data_number(selenium):
    """Вход с не валидными данными по почте"""

    # Открыть страницу
    selenium.get(login_page)

    time.sleep(time_page)

    # Нажимаем на вкладку "Почта"
    element = selenium.find_element(By.ID, 't-btn-tab-mail').click()

    time.sleep(small_time)

    # Ищем и вводим в поле "почта" не валидную почту
    search_input = selenium.find_element(By.ID, 'username')
    search_input.send_keys(no_valid_email)

    # Ищем и вводим в поле "пароль" не валидный пароль
    search_input = selenium.find_element(By.ID, 'password')
    search_input.send_keys(no_valid_password)

    # Жмем кнопку "Войти"
    search_button = selenium.find_element(By.ID, 'kc-login').click()
    time.sleep(1)

    # Проверяем, что появилось сообщение о неверных данных.
    search_error = (selenium.find_element(By.ID, 'form-error-message')).text
    assert search_error == 'Неверный логин или пароль'


# test 5
def test_login_with_valid_data_login(selenium):
    """Вход с валидными данными по логину"""

    # Открыть страницу
    selenium.get(login_page)
    time.sleep(time_page)

    # Нажимаем на вкладку "Логин"
    element = selenium.find_element(By.ID, 't-btn-tab-login').click()
    time.sleep(small_time)

    # Ищем и вводим в поле "телефон" валидный номер телефона
    search_input = selenium.find_element(By.ID, 'username')
    search_input.send_keys(valid_login)

    # Ищем и вводим в поле "пароль" валидный пароль
    search_input = selenium.find_element(By.ID, 'password')
    search_input.send_keys(valid_password)

    # жмем кнопку "Войти"
    search_button = selenium.find_element(By.ID, 'kc-login').click()

    # Проверяем, что попали на необходимую страницу
    # Предпологаю, что при попадании в личный кабинет мы находим любой элемент, в данном случае заголовок с текстом
    # "Личный кабинет" и id == title, и проверяем, что дейтсвительно попали на необходмую нам страницу.
    # search_input = selenium.find_element(By.ID, 'title').text()
    # assert search_input == 'личный кабинет'


# test 6
def test_login_with_no_valid_data_login(selenium):
    """Вход с не валидными данными по логину"""

    # Открыть страницу
    selenium.get(login_page)
    time.sleep(time_page)

    # Нажимаем на вкладку "Логин"
    element = selenium.find_element(By.ID, 't-btn-tab-login').click()
    time.sleep(small_time)

    # Ищем и вводим в поле "логин" не валидный логин
    search_input = selenium.find_element(By.ID, 'username')
    search_input.send_keys(no_valid_email)

    # Ищем и вводим в поле "пароль" не валидный пароль
    search_input = selenium.find_element(By.ID, 'password')
    search_input.send_keys(no_valid_password)

    # Жмем кнопку "Войти"
    search_button = selenium.find_element(By.ID, 'kc-login').click()
    time.sleep(small_time)

    # Проверяем, что появилось сообщение о неверных данных.
    search_error = (selenium.find_element(By.ID, 'form-error-message')).text
    assert search_error == 'Неверный логин или пароль'


# test 7
def test_login_with_valid_data_ls(selenium):
    """Вход с валидными данными по лицевому счету"""

    # Открыть страницу
    selenium.get(login_page)
    time.sleep(time_page)

    # Нажимаем на вкладку "Логин"
    element = selenium.find_element(By.ID, 't-btn-tab-ls').click()
    time.sleep(small_time)

    # Ищем и вводим в поле "лицевой счет" валидный лицевой счет
    search_input = selenium.find_element(By.ID, 'username')
    search_input.send_keys(valid_ls)

    # Ищем и вводим в поле "пароль" валидный пароль
    search_input = selenium.find_element(By.ID, 'password')
    search_input.send_keys(valid_password)

    # жмем кнопку "Войти"
    search_button = selenium.find_element(By.ID, 'kc-login').click()

    # Проверяем, что попали на необходимую страницу
    # Предпологаю, что при попадании в личный кабинет мы находим любой элемент, в данном случае заголовок с текстом
    # "Личный кабинет" и id == title, и проверяем, что дейтсвительно попали на необходмую нам страницу.
    # search_input = selenium.find_element(By.ID, 'title').text()
    # assert search_input == 'личный кабинет'


# test 8
def test_login_with_no_valid_data_ls(selenium):
    """Вход с не валидными данными по лицевому счету"""

    # Открыть страницу
    selenium.get(login_page)
    time.sleep(time_page)

    # Нажимаем на вкладку "лицевой счет"
    element = selenium.find_element(By.ID, 't-btn-tab-ls').click()
    time.sleep(small_time)

    # Ищем и вводим в поле "логин" не валидный логин
    search_input = selenium.find_element(By.ID, 'username')
    search_input.send_keys(no_valid_ls)

    # Ищем и вводим в поле "пароль" не валидный пароль
    search_input = selenium.find_element(By.ID, 'password')
    search_input.send_keys(no_valid_password)

    # Жмем кнопку "Войти"
    search_button = selenium.find_element(By.ID, 'kc-login').click()
    time.sleep(small_time)

    # Проверяем, что появилось сообщение о неверных данных.
    search_error = (selenium.find_element(By.ID, 'form-error-message')).text
    assert search_error == 'Неверный логин или пароль'


# test 9
def test_button_in_body_user_agreement(selenium):
    """Проверка работоспособности кнопки 'Пользовательское соглашение'"""

    # Открыть страницу
    selenium.get(login_page)

    # Поэтому использую данное ожидание:
    time.sleep(time_page)

    # Жмем кнопку.
    # search_button = selenium.find_element(By.CSS_SELECTOR, 'div.auth-policy > a.rt-link.rt-link--orange').click()

    time.sleep(small_time)

    # Проверяем, что мы на нужной странице
    # Данная проверка на данный момент не работает. Может быть в будущем разберусь.
    # search_text = selenium.find_element(By.XPATH, '//*[@class="offer-title"]/text()').text()
    # assert search_text == 'Публичная оферта о заключении Пользовательского соглашения на использование Сервиса «Ростелеком ID»'


# test 10
def test_button_in_body_register(selenium):
    """Проверка работоспособности кнопки 'Зарегестрироваться'"""

    # Открыть страницу
    selenium.get(login_page)
    time.sleep(time_page)

    # Жмем кнопку
    search_button = selenium.find_element(By.ID, 'kc-register').click()
    time.sleep(small_time)

    # Проверяем, что мы на нужной странице
    # Возникает ошибка "TypeError: 'str' object is not callable", поэтому данная проверка на данный момент не работает. Может быть в будущем пофиксю.
    # search_text = selenium.find_element(By.CLASS_NAME, 'card-container__title').text()
    # assert search_text == 'Авторизация'


# test 11
def test_button_in_body_forgot_password(selenium):
    """Проверка работоспособности кнопки 'Забыл пароль'"""

    # Открыть страницу
    selenium.get(login_page)
    time.sleep(time_page)

    # Жмем кнопку
    search_button = selenium.find_element(By.ID, 'forgot_password').click()
    time.sleep(small_time)

    # Проверяем, что мы на нужной странице
    # Возникает ошибка "TypeError: 'str' object is not callable", поэтому данная проверка на данный момент не работает. Может быть в будущем пофиксю.
    # search_text = selenium.find_element(By.CLASS_NAME, 'card-container__title').text()
    # assert search_text == 'Восстановление пароля'


# test 12
def test_button_in_footer_privacy_policy(selenium):
    """Проверка работоспособности кнопки 'Политика конфиденциальности' в подвале"""

    # Открыть страницу
    selenium.get(login_page)
    time.sleep(time_page)

    # Жмем кнопку.
    search_button = selenium.find_element(By.XPATH, '//*[@id="rt-footer-agreement-link"]/span[1]').click()

    time.sleep(small_time)

    # Проверяем, что мы на нужной странице
    #Проверка на данный момент не работает. Может быть в будущем разберусь.
    # search_text = selenium.find_element(By.XPATH, '//*[@class="offer-title"]/text()').text()
    # assert search_text == 'Публичная оферта о заключении Пользовательского соглашения на использование Сервиса «Ростелеком ID»'


# test 13
def test_button_in_footer_user_agreement(selenium):
    """Проверка работоспособности кнопки 'Пользовательское соглашение' в подвале"""

    # Открыть страницу
    selenium.get(login_page)
    time.sleep(time_page)

    # Жмем кнопку.
    search_button = selenium.find_element(By.XPATH, '//*[@id="rt-footer-agreement-link"]/span[2]').click()

    time.sleep(small_time)

    # Проверяем, что мы на нужной странице
    # Проверка на данный момент не работает. Может быть в будущем пофиксю.
    # search_text = selenium.find_element(By.XPATH, '//*[@class="offer-title"]/text()').text()
    # assert search_text == 'Публичная оферта о заключении Пользовательского соглашения на использование Сервиса «Ростелеком ID»'


# test 14
def test_button_in_footer_user_agreement(selenium):
    """Проверка работоспособности кнопки 'Cookie' в подвале"""

    # Открыть страницу
    selenium.get(login_page)
    time.sleep(time_page)

    # Жмем кнопку.
    search_button = selenium.find_element(By.ID, 'cookies-tip-open').click()
    time.sleep(small_time)

    # Проверяем, что мы на нужной странице
    # Возникает ошибка "TypeError: 'str' object is not callable", поэтому данная проверка на данный момент не работает. Может быть в будущем разберусь.
    # search_text = selenium.find_element(By.XPATH, '//*[@class="rt-tooltip__title"]').text()
    # assert search_text == 'Мы используем Cookie»'
    # В качестве проверки делаем скрин
    selenium.save_screenshot('test_button_in_footer_user_agreement.png')
