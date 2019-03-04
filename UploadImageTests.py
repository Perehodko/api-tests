# -*- coding: utf-8 -*-
import requests
import json
import sys


# create user
# POST /task/rest/createuser
def testCreateUser():
    url = "http://users.bugred.ru/tasks/rest/createuser"
    payload = {
        "email": "goldy@mail.com",
        "name": "rest",
        "tasks": [12],
        "companies": [36, 37],
        "hobby": "swimming",
        "adres": "Aquarium",
        "name1": "Goldy Fish",
        "surname1": "-",
        "fathername1": "-",
        "cat": "Tom",
        "dog": "Spike",
        "parrot": "NoName",
        "cavy": "Troy",
        "hamster": "Abed",
        "squirrel": "Squirell",
        "phone": "333 33 33",
        "inn": "123456789012",
        "gender": "f",
        "birthday": "01.01.1900",
        "date_start": "11.11.2000"
    }
    # serialize an object to a JSON
    payloadJSON = json.dumps(payload)

    response = requests.post(url, data=payloadJSON)

    # tests
    if response.status_code != 200:
        print('Status code should be is 200. Current status code is %d.' % response.status_code)
    else:
        pass


# upload image
# POST /task/rest/addavatar/
def testUploadAvatar():
    url = "http://users.bugred.ru/tasks/rest/addavatar/"
    querystring = {"email": "goldy@mail.com"}

    with open('/home/nper/Documents/goldi.jpg', 'rb') as avatar:
        dataAvatar = avatar.read()

    files = {'avatar': (
        'goldi.jpg', dataAvatar, "multipart/form-data", {'Expires': '0'})}

    response = requests.post(url, files=files, params=querystring)

    # tests
    if response.status_code != 200:
        print('Status code should be is 200. Current status code is %d.' % response.status_code)
    else:
        pass


# get user data
# GET /rest/getuser
def testGetUserdata():
    url = "http://users.bugred.ru/tasks/rest/getuser"
    querystring = {"email": "goldy@mail.com"}

    response = requests.get(url, params=querystring)

    # parsing JSON response
    myJSONResponse = json.loads(response.text)

    # tests
    if response.status_code != 200:
        print('Status code should be is 200. Current status code is %d.' % response.status_code)
    else:
        pass

    if myJSONResponse['avatar'] != "http://users.bugred.ru//tmp/files/goldi.jpg":
        print('Field value "avatar" should be is "http://users.bugred.ru//tmp/files/goldi.jpg". '
              'Current status code is %s.' % myJSONResponse['avatar'])
    else:
        pass


methods = [testCreateUser, testUploadAvatar, testGetUserdata]


def main():
    for m in methods:
        m()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Выход...')
        sys.exit(0)
