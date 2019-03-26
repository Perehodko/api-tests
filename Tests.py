# -*- coding: utf-8 -*-
import requests
import json
import sys
from requests.exceptions import ConnectionError


# Add a new pet to the store
# POST /pet
def testCreatePet():
    # --- Входные данные ---
    # Адрес сервиса для отправки JSON-запросов
    url = "http://petstore.swagger.io/v2/pet"

    # Создание HTTP-заголовков запроса
    headers = {'Content-Type': "application/json"}

    # Создание тела запроса
    payload = \
        {
            "id": 11,
            "category": {
                "id": 1,
                "name": "Tom"
            },
            "name": "cat",
            "photoUrls": [
                "string"
            ],
            "tags": [
                {
                    "id": 0,
                    "name": "string"
                }
            ],
            "status": "available"
        }

    # Кодирование тела запроса в JSON
    payloadJSON = json.dumps(payload)

    # Выполнение запроса
    try:
        response = requests.post(url, data=payloadJSON, headers=headers)

        # Отладочная информация
        # print("Заголовки запроса: ", response.headers)
        # print("Запрос: ", response.body)
        # print("Заголовки ответа: ", response.headers)
        # print("Ответ: ", response.text)
        # print("\n")

        # Обработка запроса
        if response.status_code != 200:
            print("Произошла ошибка при обращении к серверу API PetStore")
            print("Код ошибки: ", response.status_code)
            print("Описание ошибки: ", response.reason)
        else:
            print(response.text)

    # Обработка ошибки, если не удалось соединиться с сервером API PetStore
    except ConnectionError:
        # В данном случае рекомендуется повторить запрос позднее
        print("Произошла ошибка соединения с сервером API.")
    # Если возникла какая-либо другая ошибка
    except:
        # В данном случае рекомендуется проанализировать действия приложения
        print("Произошла непредвиденная ошибка.")


# Find pet by ID
# GET /pet/{petId}
def testGetPetFromId():
    # --- Входные данные ---
    # Адрес сервиса для отправки JSON-запросов
    url = "http://petstore.swagger.io/v2/pet/"

    # ID существующего пользователя
    userID = "11"

    # Создание HTTP-заголовков запроса
    headers = {'Content-Type': "application/json"}

    # Выполнение запроса
    try:
        response = requests.get(url + userID, headers=headers)

        # Отладочная информация
        # print("Заголовки запроса: ", response.headers)
        # print("Запрос: ", response.body)
        # print("Заголовки ответа: ",response.headers)
        # print("\n")

        # Кодирование тела запроса в JSON
        myJSONResponse = json.loads(response.text)

        # Обработка запроса
        if response.status_code != 200:
            print("Произошла ошибка при обращении к серверу API PetStore")
            print("Код ошибки: ", response.status_code)
            print("Описание ошибки: ", response.reason)
        else:
            if myJSONResponse['id'] != 11:
                print('Field value "id" should be is 11. Current status code is %d.' % myJSONResponse['id'])
            else:
                pass

            if myJSONResponse['category']['id'] != 1:
                print('Field value "id" should be is 11. Current status code is %d.' % myJSONResponse['id'])
            else:
                pass

            if myJSONResponse['category']['name'] != "Tom":
                print(
                    'Field value "name" should be is "Tom". Current value is %s.' % myJSONResponse['category']['name'])
            else:
                pass

            if myJSONResponse['status'] != "available":
                print('Field value "status" should be is "available". Current value is %s.' % myJSONResponse['status'])
            else:
                pass
    # Обработка ошибки, если не удалось соединиться с сервером API PetStore
    except ConnectionError:
        # В данном случае рекомендуется повторить запрос позднее
        print("Произошла ошибка соединения с сервером API.")
    # Если возникла какая-либо другая ошибка
    except:
        # В данном случае рекомендуется проанализировать действия приложения
        print("Произошла непредвиденная ошибка.")


methods = [testCreatePet, testGetPetFromId]


def main():
    for m in methods:
        m()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Выход...')
        sys.exit(0)
