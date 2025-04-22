from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_cart_button_accessibility(browser):
    browser.get(link)

    # Ищем все элементы с нужным селектором
    buttons = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")

    # Проверка, что хотя бы один элемент найден
    assert buttons, "Кнопка не найдена на странице"