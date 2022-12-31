from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

# Файл к уроку 2.4 - Курс "Автоматизация тестирования с помощью Selenium и Python"

try:
    # It's work in Chrome with Windows, Linux and macOS
    options = webdriver.ChromeOptions();
    options.add_argument("--start-maximized");

    browser = webdriver.Chrome();
    browser = webdriver.Chrome(chrome_options=options);
    
    link = "http://suninjuly.github.io/explicit_wait2.html";
    browser.get(link);

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))));

    btn_book = browser.find_element(By.ID, 'book');
    btn = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'));
    btn_book.click();

    x_element = browser.find_element(By.ID, 'input_value');
    browser.execute_script("return arguments[0].scrollIntoView(true);", x_element)
    x = x_element.text;
    y = calc(x);

    t_element = browser.find_element(By.ID, 'answer');
    t_element.send_keys(y);

    # Отправляем заполненную форму
    button = browser.find_element(By.ID, "solve");
    button.click();

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30);
    # закрываем браузер после всех манипуляций
    browser.quit();

# не забываем оставить пустую строку в конце файла
