# -*- coding: utf-8 -*-
import requests
import unittest
import json


class TestUploadImage(unittest.TestCase):

    # create user
    # POST /task/rest/createuser
    def testCreateUser(self):

        url = "http://users.bugred.ru/tasks/rest/createuser"
        payload = "{\n  \"email\": \"goldy@mail.com\",\n  \"name\": \"rest\",\n  \"tasks\": [12],\n  " \
                  "\"companies\": [36,37],\n  \"hobby\":\"swimming\",\n  \"adres\":\"Aquarium\",\n  " \
                  "\"name1\":\"Goldy Fish\",\n  \"surname1\":\"-\",\n  \"fathername1\":\"-\",\n  " \
                  "\"cat\":\"Tom\",\n  \"dog\":\"Spike\",\n  \"parrot\":\"NoName\",\n  \"cavy\":\"Troy\",\n  " \
                  "\"hamster\":\"Abed\",\n  \"squirrel\":\"Squirell\",\n  \"phone\":\"333 33 33\",\n  " \
                  "\"inn\":\"123456789012\",\n  \"gender\":\"f\",\n  \"birthday\":\"01.01.1900\",\n  " \
                  "\"date_start\":\"11.11.2000\"\n}"
        headers = ""

        response = requests.post(url, data = payload, headers=headers)

        self.assertEqual(200, response.status_code,
                         ('Status code should be is 200. Current status code is %d.' % response.status_code))


    # upload image
    # POST /task/rest/addavatar/
    def testUploadAvatar(self):

        url = "http://users.bugred.ru/tasks/rest/addavatar/"
        querystring = {"email": "goldy@mail.com"}
        payload = payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"avatar\"; " \
                            "filename=\"goldi.jpg\"\r\nContent-Type: image/jpeg\r\n\r\n\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
        headers = {'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW"}

        response = requests.post(url, data = payload, headers = headers, params = querystring)
        self.assertEqual(200, response.status_code,
                         ('Status code should be is 200. Current status code is %d.' % response.status_code))


    # get user data
    # GET /rest/getuser
    def testGetUserdata(self):

        url = "http://users.bugred.ru/tasks/rest/getuser"
        querystring = {"email": "goldy@mail.com"}
        payload = ""
        headers = ""

        response = requests.get(url, data=payload, headers = headers, params = querystring)

        # parsing JSON response
        myJSONResponse = json.loads(response.text)

        self.assertEqual(200, response.status_code,
                         ('Status code should be is 200. Current status code is %d.' % response.status_code))
        self.assertEqual("http://users.bugred.ru//tmp/files/goldi.jpg", myJSONResponse['avatar'],
                         ('Field value "id" should be is 11. Current status code is %s.' % myJSONResponse['avatar']))



if __name__ == "__main__":
    unittest.main()



