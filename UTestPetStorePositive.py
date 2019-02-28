# -*- coding: utf-8 -*-
import requests
import unittest
import json


class TestPositiveTestsPet(unittest.TestCase):

    # Add a new pet to the store
    # POST /pet
    def testCreatePet(self):

        url = "http://petstore.swagger.io/v2/pet"
        payload = \
            {
                "id": 11,
                "category": {
                    "id": 0,
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

        headers = {'Content-Type': "application/json"}
        # serialize an object to a JSON
        payloadJSON = json.dumps(payload)

        response = requests.post(url, data=payloadJSON, headers=headers)

        self.assertEqual(200, response.status_code, ('Status code should be is 200. Current status code is %d.'
                                                     % response.status_code))

    # Find pet by ID
    # GET /pet/{petId}
    def testGetPetFromId(self):

        url = "http://petstore.swagger.io/v2/pet/"
        id = "11"
        headers = {'Content-Type': "application/json"}
        response = requests.get(url + id, headers=headers)

        # parsing JSON response
        myJSONResponse = json.loads(response.text)

        self.assertEqual(200, response.status_code,
                         ('Status code should be is 200. Current status code is %d.' % response.status_code))
        self.assertEqual(11, myJSONResponse['id'],
                         ('Field value "id" should be is 11. Current status code is %d.' % myJSONResponse['id']))
        self.assertEqual("Tom", myJSONResponse['category']['name'],
                         ('Field value "name" should be is "Tom". Current value is %s.' % myJSONResponse['category'][
                             'name']))
        self.assertEqual("available", myJSONResponse['status'],
                         ('Field value "status" should be is "available". Current value is %s.' % myJSONResponse[
                             'status']))

    # Update an existing pet
    # PUT /pet
    def testUpdatePet(self):

        url = "http://petstore.swagger.io/v2/pet/"
        payload = \
            {
                "id": 11,
                "category": {
                    "id": 0,
                    "name": "Tom"
                },
                "name": "cat",
                "photoUrls": [
                    "string"
                ],
                "tags": [
                    {
                        "id": 1,
                        "name": "wild"
                    }
                ],
                "status": "available"
            }

        headers = {'Content-Type': "application/json"}
        # serialize an object to a JSON
        payloadJSON = json.dumps(payload)

        response = requests.put(url, data=payloadJSON, headers=headers)

        # parsing JSON response
        myJSONResponse = json.loads(response.text)

        self.assertEqual(200, response.status_code,
                         ('Status code should be is 200. Current status code is %d.' % response.status_code))
        self.assertEqual(1, myJSONResponse['tags'][0]['id'],
                         ('Field value "id" should be is 1. Current status code is %d.' % myJSONResponse['tags'][0][
                             'id']))
        self.assertEqual("wild", myJSONResponse['tags'][0]['name'],
                         ('Field value "name" should be is "wild". Current value is %s.' % myJSONResponse['tags'][0][
                             'name']))

    # Finds Pets by status
    # GET /pet/findByStatus
    def testFindPetByStatusAvailable(self):

        url = "http://petstore.swagger.io/v2/pet/findByStatus"
        querystring = {"status": "available"}
        headers = {'Content-Type': "application/json"}

        response = requests.get(url, headers=headers, params=querystring)

        # parsing JSON response
        myJSONResponse = json.loads(response.text)

        n = 0
        for i in range(len(myJSONResponse)):
            if myJSONResponse[i]['id'] == 11:
                n += 1
                print (myJSONResponse[i])

        self.assertEqual(1, n, "No record in database!!!")

    # Updates a pet in the store with form data
    # POST /pet/{petId}
    def testUpdatesAPet(self):

        url = "http://petstore.swagger.io/v2/pet/"
        petId = "11"
        querystring = {"status": "sold"}
        headers = {'Content-Type': "application/x-www-form-urlencoded"}

        response = requests.post(url + petId, headers=headers, params=querystring)

        self.assertEqual(200, response.status_code,
                         ('Status code should be is 200. Current status code is %d.' % response.status_code))


if __name__ == "__main__":
    unittest.main()
