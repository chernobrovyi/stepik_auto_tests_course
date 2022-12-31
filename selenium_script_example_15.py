from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math
import os

# Файл к уроку 2.3 - Курс "Автоматизация тестирования с помощью Selenium и Python"

try:
    # It's work in Chrome with Windows, Linux and macOS
    options = webdriver.ChromeOptions();
    options.add_argument("--start-maximized");

    browser = webdriver.Chrome();
    browser = webdriver.Chrome(chrome_options=options);
    
    link = "http://suninjuly.github.io/alert_accept.html";
    browser.get(link);

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))));

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn");
    button.click();

    alert = browser.switch_to.alert;
    alert.accept();

    x_element = browser.find_element(By.ID, 'input_value');
    x = x_element.text;
    y = calc(x);

    t_element = browser.find_element(By.ID, 'answer');
    t_element.send_keys(y);

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn");
    button.click();

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30);
    # закрываем браузер после всех манипуляций
    browser.quit();

# не забываем оставить пустую строку в конце файла