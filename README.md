**Скрипт читает файлы с данными о рейтингах товаров и формирует отчеты.**

**Небольшие особенности работы:**

- возможность получения данных из нескольких файлов
- автоматическая подстановка расширения файла (.csv) на случай, если пользователь не указал его
- пустые или поврежденные строки будут проигнорированы, программа продолжит выполнение

**Установка зависимостей:**

`pip install -r requirements.txt`

**Тесты:**

- основной тест парсинга аргументов, переданных через командную строку
- проверка расширений файлов
- проверка сортировки сформированного отчета
- проверка создания отчета с одним брендом

---

**Команды для запуска (мозможно указание пути до файла)**

`python main.py --files products1.csv products2.csv --report average-rating`

`python main.py --files .\files\products1.csv products2.csv --report average-rating`

**Примеры запуска**
<img width="738" height="209" alt="brands_rating" src="https://github.com/user-attachments/assets/48134588-43a5-4756-be84-edc9b8531a0e" />

<img width="743" height="208" alt="brands_rating1" src="https://github.com/user-attachments/assets/3cc86c62-0652-407c-8fea-1e82dd9d8689" />

**Покрытие тестами**
<img width="706" height="317" alt="test_coverage" src="https://github.com/user-attachments/assets/1abd479c-2441-4eb7-9521-69df882fbd1d" />
