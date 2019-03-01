API тестируемых сервисов:
- http://petstore.swagger.io/
- https://testbase.atlassian.net/wiki/spaces/USERS/overview

Тестирование организованно с помошью:
- Язык написания тестовых сценраиев Python3.5;
- Для выполняет HTTP-запросов используется бибилиотека Python Requests;
- Для проверки результатов используется модуль для написания юнит-тестов Unittest;
- Для кодирования и декодирования данных используется модуль JSON.

Методы:
- GET
- POST
- PUT 
- DELETE

Установка библиотеки Requests:
```
pip install requests
```
Установка модуля Unittest:
```
pip install unittest
```
Запуск тестов из консоли Linux:
1) Перейти в директорию, где хранятся ваши тесты:
```
cd /path-to-tests/
```
2) Запустить весь набор тестов с выводом результатов в консоль:
```
python UTestPetStorePositive.py; 
python UTestsPetStoreDeletePet.py; 
python UTestUploadImage.py; 
python UTestPetStoreNegative.py
```
