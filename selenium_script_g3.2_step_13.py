from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time


# Файл к уроку 3.2, шаг 13 - Курс "Автоматизация тестирования с помощью Selenium и Python"
class TestAbs(unittest.TestCase):
    def test_abs1(self):
        # It's work in Chrome with Windows, Linux and macOS
        options = webdriver.ChromeOptions();
        options.add_argument("--start-maximized");

        browser = webdriver.Chrome();
        browser = webdriver.Chrome(chrome_options=options);
    
        link = "http://suninjuly.github.io/registration1.html";
        browser.get(link);

        element_1 = browser.find_element(By.CLASS_NAME, 'form-control first');
        element_1.send_keys("Valeriy");
        element_2 = browser.find_element(By.CLASS_NAME, 'form-control second');
        element_2.send_keys("Chernobrovyi");
        element_3 = browser.find_element(By.CLASS_NAME, 'form-control third');
        element_3.send_keys("valerasergeevich@gmail.com");


        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text;

    def test_abs2(self):
        link = "http://suninjuly.github.io/registration2.html";
        browser.get(link);

        element_1 = browser.find_element(By.CLASS_NAME, 'form-control first');
        element_1.send_keys("Valeriy");
        element_2 = browser.find_element(By.CLASS_NAME, 'form-control second');
        element_2.send_keys("Chernobrovyi");
        element_3 = browser.find_element(By.CLASS_NAME, 'form-control third');
        element_3.send_keys("valerasergeevich@gmail.com");


        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text;

if __name__ == "__main__":
    unittest.main();

# не забываем оставить пустую строку в конце файла