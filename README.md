## **Скрипт для формирования таблицы с рейтингом брендов**

**Небольшие особенности работы**

- возможность получения данных из нескольких файлов
- получение данных из каталога с использованием аргумента `--dir <dir_name>`
- автоматическая подстановка расширения файла (.csv) на случай, если пользователь не указал его
- пустые или поврежденные строки будут проигнорированы, программа продолжит выполнение

---

**Установка зависимостей**

`pip install -r requirements.txt`

---

**Тесты**

- основной тест парсинга аргументов, переданных через командную строку
- проверка расширений файлов
- проверка сортировки сформированного отчета
- проверка создания отчета с одним брендом
- проверка чтения файлов из каталога
- проверка названия директории с файлами отчетов

---

**Примеры команд для запуска**

`python main.py --files products1.csv products2.csv --report average-rating`

`python main.py --files .\files\products1.csv products2.csv --report average-rating`

`python main.py --dir files --report average-rating`

---

**Примеры запуска**

<img width="738" height="209" alt="brands_rating" src="https://github.com/user-attachments/assets/48134588-43a5-4756-be84-edc9b8531a0e" />

<img width="743" height="208" alt="brands_rating1" src="https://github.com/user-attachments/assets/3cc86c62-0652-407c-8fea-1e82dd9d8689" />

---

**Получение данных из директории**

<img width="736" height="211" alt="brands_rating2" src="https://github.com/user-attachments/assets/3d225362-27f7-4e37-937a-7a55a489527f" />

---

**Покрытие тестами**

<img width="699" height="296" alt="test_coverage" src="https://github.com/user-attachments/assets/4c5828a6-bd10-43ee-b98d-5dd41865fa36" />
