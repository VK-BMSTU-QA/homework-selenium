# Предварительно необходимо установить chromedriver
## Инструкция для macOS

1. Скачиваем версию, совместимую с вашим браузером Chrome:
    ```
    https://chromedriver.storage.googleapis.com/index.html
    ```
2. Копируем:
    ```
    cp chromedriver /usr/local/bin/chromedriver
    ```
3. Навешиваем необходимые атрибуты:
    ```
    sudo xattr -d com.apple.quarantine /usr/local/bin/chromedriver
    ```
4. Все готово для запуска тестов


# Сборка
1. Настройка virtual enviroment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
    
2. Установка зависимостей:
    ```bash
   pip install -r requirements.txt
   ```
    
# Запуск

* Запуск всех тестов проекта:

    ```bash
    bash runner_tests.sh
    ```