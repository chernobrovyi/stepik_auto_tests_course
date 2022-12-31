from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

# Файл к уроку 2.2 - Курс "Автоматизация тестирования с помощью Selenium и Python"

try:
    # It's work in Chrome with Windows, Linux and macOS
    options = webdriver.ChromeOptions();
    options.add_argument("--start-maximized");

    browser = webdriver.Chrome();
    browser = webdriver.Chrome(chrome_options=options);
    
    link = "http://suninjuly.github.io/selects1.html";
    browser.get(link);

    def calc(x1_value, x2_value):
        return str(int(x1_value) + int(x2_value));
    
    x1 = browser.find_element(By.ID, 'num1');
    x1_value = x1.text;
    x2 = browser.find_element(By.ID, 'num2');
    x2_value = x2.text;

    y = calc(x1_value, x2_value);

    select = Select(browser.find_element(By.TAG_NAME, 'select'));
    select.select_by_value(y);

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn");
    button.click();

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30);
    # закрываем браузер после всех манипуляций
    browser.quit();

# не забываем оставить пустую строку в конце файла