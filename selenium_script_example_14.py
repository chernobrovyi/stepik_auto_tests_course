from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math
import os

# Файл к уроку 2.2 - Курс "Автоматизация тестирования с помощью Selenium и Python"

try:
    # It's work in Chrome with Windows, Linux and macOS
    options = webdriver.ChromeOptions();
    options.add_argument("--start-maximized");

    browser = webdriver.Chrome();
    browser = webdriver.Chrome(chrome_options=options);
    
    link = "http://suninjuly.github.io/file_input.html";
    browser.get(link);

    # Заполняем данные форм
    first_name_input = browser.find_element(By.NAME, 'firstname');
    first_name_input.send_keys('Valeriy');
    last_name_input = browser.find_element(By.NAME, 'lastname');
    last_name_input.send_keys('Chernobrovyi');
    email_input = browser.find_element(By.NAME, 'email');
    email_input.send_keys('valerasergeevich@gmail.com');

    add_btn_input = browser.find_element(By.NAME, 'file');
    # add_btn_input.click();

    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
    add_btn_input.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn");
    button.click();

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30);
    # закрываем браузер после всех манипуляций
    browser.quit();

# не забываем оставить пустую строку в конце файла