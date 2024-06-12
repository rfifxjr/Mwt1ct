from selenium import webdriver

# Инициализация Chrome
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
browser = webdriver.Chrome(options=chrome_options)

# Загрузка страницы
browser.get('https://ya.ru')

# Ожидание ввода перед закрытием браузера
input("Нажмите Enter для завершения работы")

# Закрытие браузера
browser.quit()
