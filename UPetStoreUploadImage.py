# -*- coding: utf-8 -*-
import requests
import unittest
import json


class TestUploadImage(unittest.TestCase):

    # create user
    # POST /task/rest/createuser
    def testCreateUser(self):
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

        self.assertEqual(200, response.status_code,
                         ('Status code should be is 200. Current status code is %d.' % response.status_code))

    # upload image
    # POST /task/rest/addavatar/
    def testUploadAvatar(self):
        url = "http://users.bugred.ru/tasks/rest/addavatar/"
        querystring = {"email": "goldy@mail.com"}

        with open('/home/nper/Documents/goldi.jpg', 'rb') as avatar:
            dataAvatar = avatar.read()

        files = {'avatar': (
            'goldi.jpg', dataAvatar, "multipart/form-data", {'Expires': '0'})}

        response = requests.post(url, files=files, params=querystring)

        self.assertEqual(200, response.status_code,
                         ('Status code should be is 200. Current status code is %d.' % response.status_code))

    # get user data
    # GET /rest/getuser
    def testGetUserdata(self):
        url = "http://users.bugred.ru/tasks/rest/getuser"
        querystring = {"email": "goldy@mail.com"}

        response = requests.get(url, data=payload, headers=headers, params=querystring)

        # parsing JSON response
        myJSONResponse = json.loads(response.text)

        self.assertEqual(200, response.status_code,
                         ('Status code should be is 200. Current status code is %d.' % response.status_code))
        self.assertEqual("http://users.bugred.ru//tmp/files/goldi.jpg", myJSONResponse['avatar'],
                         ('Field value "id" should be is 11. Current status code is %s.' % myJSONResponse['avatar']))


if __name__ == "__main__":
    unittest.main()
