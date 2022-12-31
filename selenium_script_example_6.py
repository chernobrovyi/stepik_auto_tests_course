from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Файл к уроку 1.6 - Курс "Автоматизация тестирования с помощью Selenium и Python"

try:
    browser = webdriver.Chrome();

    # It's work in Chrome with Windows, Linux and macOS
    options = webdriver.ChromeOptions();
    options.add_argument("--start-maximized");

    browser = webdriver.Chrome(chrome_options=options);
    
    browser.get("http://suninjuly.github.io/find_xpath_form");
    elements = browser.find_elements(By.TAG_NAME, 'input');
    for element in elements:
        element.send_keys("Мой ответ");

    button = browser.find_element(By.XPATH, '//button[text()="Submit"]');
    button.click();

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30);
    # закрываем браузер после всех манипуляций
    browser.quit();

# не забываем оставить пустую строку в конце файла