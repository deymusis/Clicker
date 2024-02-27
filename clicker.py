from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Функция открытия сайта и перехода по всем ссылкам на этом сайте
def open_website(url):
    try:
        # Создаем объект опций браузера
        options = webdriver.ChromeOptions()
        # Указываем путь к исполняемому файлу браузера
        options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        # Открываем браузер в полноэкранном режиме
        options.add_argument("--start-maximized")
        # Создаем экземпляр браузера
        driver = webdriver.Chrome(options=options)
        # Переходим на сайт
        driver.get("https://" + url)
        # Ждем, пока страница загрузится (не более 10 секунд)
        driver.implicitly_wait(10)
        # Первоначальная пауза на 5 секунд для демонстрации
        time.sleep(5)
        # Получаем все ссылки на сайте и открываем их в новых вкладках
        links = driver.find_elements(By.TAG_NAME, "a")
        # Перебираем все ссылки на сайте
        for link in links:
            try:
                # Получаем атрибут href ссылки
                href = link.get_attribute("href")
                # Если ссылка ведет на тот же сайт, что и сайт, на котором мы находимся
                if href and url in href:
                    # Открываем ссылку в новой вкладке
                    driver.execute_script("window.open('{}', '_blank');".format(href))
                    # Пауза между открытием ссылок в новых вкладках на 10 секунд
                    time.sleep(10)
            except Exception as e:
                print("Ошибка:", e)
                continue
    # Обработка исключений и закрытие драйвера
    # Обработка исключения при нажатии Ctrl+C
    except KeyboardInterrupt:
        print("Программа остановлена пользователем.")
    except Exception as e:
        print("Ошибка:", e)
    finally:
        driver.quit()

# Запуск программы
if __name__ == "__main__":
    print("""
    Эта программа для запуска на Windows. Проверьте, что у вас установлен браузер Google Chrome и его исполняемый файл находится в папке по пути "C:\Program Files\Google\Chrome\Application".
    Программа в браузере Google Chrome открывает сайт, запрашиваемый пользователем и открывает все ссылки на этом сайте в новых вкладках каждые 10 секунд.
    Для остановки программы используйте комбинацию клавиш Ctrl+C.
    """)
    # Бесконечный цикл для ввода адреса сайта
    while True:
        website = input("Введите адрес сайта, на который хотите перейти: ")
        # Проверка наличия точки в адресе сайта
        if '.' not in website:
            print("Неправильный формат адреса.")
            continue
        # Вызов функции открытия сайта
        open_website(website)
