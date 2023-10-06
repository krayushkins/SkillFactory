from test_login_page import valid_email
from test_login_page import valid_password
from test_login_page import time_page
from test_login_page import small_time
from test_login_page import login_page
import time
from selenium.webdriver.common.by import By

name = 'Сергей'
surname = 'Краюшкин'


# test 2
def test_register_with_data_email(selenium):
    """Проверка регистрации пользователя по почте"""

    # Открыть страницу
    selenium.get(login_page)
    time.sleep(time_page)

    # Жмем кнопку "Зарегестрироваться"
    search_button = selenium.find_element(By.ID, 'kc-register').click()
    time.sleep(small_time)

    # Ищем и вводим в поле "Имя" Имя
    search_input = selenium.find_element(By.NAME, 'firstName')
    search_input.send_keys(name)

    # Ищем и вводим в поле "Фамилия" фамилию
    search_input = selenium.find_element(By.NAME, 'lastName')
    search_input.send_keys(surname)

    # Ищем и вводим в поле "email" почту
    search_input = selenium.find_element(By.ID, 'address')
    search_input.send_keys(valid_email)

    # Ищем и вводим в поле "пароль" пароль
    search_input = selenium.find_element(By.ID, 'password')
    search_input.send_keys(valid_password)

    # Ищем и вводим в поле "Подтверждение пароля" пароль
    search_input = selenium.find_element(By.ID, 'password-confirm')
    search_input.send_keys(valid_password)

    # Жмем кнопку "Зарегестрироваться"
    search_button = selenium.find_element(By.NAME, 'register')
    time.sleep(small_time)


# test 2
def test_mask_password_button(selenium):
    """Проверяем работоспособность кнопки маскировчного пароля"""

    # Открыть страницу
    selenium.get(login_page)
    time.sleep(time_page)

    # Жмем кнопку "Зарегестрироваться"
    search_button = selenium.find_element(By.ID, 'kc-register').click()
    time.sleep(small_time)

    # Ищем и вводим в поле "пароль" пароль
    search_input = selenium.find_element(By.ID, 'password')
    search_input.send_keys(valid_password)

    # Ищем и вводим в поле "Подтверждение пароля" пароль
    search_input = selenium.find_element(By.ID, 'password-confirm')
    search_input.send_keys(valid_password)

    # Ищем кнопку закрытого глаза в поле "Пароль" и кликаем.
    search_button = selenium.find_element(By.CLASS_NAME, 'rt-eye-icon').click()

    # Ищем кнопку закрытого глаза в поле "Подтверждение пароля" и кликаем.
    search_button = selenium.find_element(By.XPATH,
                                          '//*[@id="page-right"]/div/div/div/form/div[4]/div[2]/div/div[2]').click()

    # Делаем скрин
    selenium.save_screenshot('test_mask_password_button.png')


# test 3
def test_button_in_body_user_agreement(selenium):
    """Проверка работоспособности кнопки 'Пользовательское соглашение'"""

    # Открыть страницу
    selenium.get(login_page)
    time.sleep(time_page)

    # Жмем кнопку "Зарегестрироваться"
    search_button = selenium.find_element(By.ID, 'kc-register').click()
    time.sleep(small_time)

    # Жмем кнопку.
    search_button = selenium.find_element(By.CSS_SELECTOR, 'div.auth-policy > a.rt-link.rt-link--orange').click()
    time.sleep(small_time)


# test 4
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


# test 5
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


# test 6
def test_button_in_footer_user_agreement(selenium):
    """Проверка работоспособности кнопки 'Cookie' в подвале"""

    # Открыть страницу
    selenium.get(login_page)
    time.sleep(time_page)

    # Жмем кнопку.
    search_button = selenium.find_element(By.ID, 'cookies-tip-open').click()
    time.sleep(small_time)

    # Делаем скрин
    selenium.save_screenshot('test_button_in_footer_user_agreement.png')
