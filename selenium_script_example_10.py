from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

# Файл к уроку 2.1 - Курс "Автоматизация тестирования с помощью Selenium и Python"

try:
    # It's work in Chrome with Windows, Linux and macOS
    options = webdriver.ChromeOptions();
    options.add_argument("--start-maximized");

    browser = webdriver.Chrome();
    browser = webdriver.Chrome(chrome_options=options);
    
    link = "http://suninjuly.github.io/get_attribute.html";
    browser.get(link);

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))));

    chest_element = browser.find_element(By.ID, 'treasure');
    chest_element_int = chest_element.get_attribute('valuex');
    x = chest_element_int;
    y = calc(x);

    t_element = browser.find_element(By.ID, 'answer');
    t_element.send_keys(y);

    check_element = browser.find_element(By.ID, 'robotCheckbox');
    check_element.click();

    radio_element = browser.find_element(By.ID, 'robotsRule');
    radio_element.click();


    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn");
    button.click();

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30);
    # закрываем браузер после всех манипуляций
    browser.quit();

# не забываем оставить пустую строку в конце файла