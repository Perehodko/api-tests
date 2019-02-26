# -*- coding: utf-8 -*-
import requests
import unittest
import json

class TestPositiveTestsPet(unittest.TestCase):

    # Add a new pet to the store
    # POST /pet
    def testCreatePet(self):

        url = "http://petstore.swagger.io/v2/pet"
        payload = "{\n  \"id\": 11,\n  \"category\": {\n    \"id\": 0,\n    \"name\": \"Tom\"\n  }," \
                  "\n  \"name\": \"cat\",\n  \"photoUrls\": [\n    \"string\"\n  ],\n  \"tags\": " \
                  "[\n    {\n      \"id\": 0,\n      \"name\": \"string\"\n    }\n  ],\n  \"status\": " \
                  "\"available\"\n}\n\n"

        headers = {'Content-Type': "application/json"}

        response = requests.post(url, data=payload, headers=headers)
        # print (response.text)

        self.assertEqual(200, response.status_code, \
                 ('Status code should be is 200. Current status code is %d.' % response.status_code))


    # Find pet by ID
    # GET /pet/{petId}
    def testGetPetFromId(self):

        url = "http://petstore.swagger.io/v2/pet/"
        id = "11"
        payload = ""
        headers = {'Content-Type': "application/json"}
        response = requests.get(url + id, data=payload, headers=headers)

        # parsing JSON response
        myJSONResponse = json.loads(response.text)

        self.assertEqual(200, response.status_code, \
                         ('Status code should be is 200. Current status code is %d.' % response.status_code))
        self.assertEqual(11, myJSONResponse['id'], \
                         ('Field value "id" should be is 11. Current status code is %d.' % myJSONResponse['id']))
        self.assertEqual("Tom", myJSONResponse['category']['name'],
                         ('Field value "name" should be is "Tom". Current value is %s.' % myJSONResponse['category']['name']))
        self.assertEqual("available",  myJSONResponse['status'], \
                         ('Field value "status" should be is "avilable". Current value is %s.' % myJSONResponse['status']))


    # Update an existing pet
    # PUT /pet
    def testUpdatePet(self):

        url = "http://petstore.swagger.io/v2/pet/"

        payload = "{\n  \"id\": 11,\n  \"category\": {\n    \"id\": 0,\n    \"name\": \"Tom\"\n  },"\
                  "\n  \"name\": \"cat\",\n  \"photoUrls\": [\n    \"string\"\n  ],\n  \"tags\": "\
                  "[\n    {\n      \"id\": 1,\n      \"name\": \"wild\"\n    }\n  ],\n  \"status\": "\
                  "\"available\"\n}\n\n"

        headers = {'Content-Type': "application/json"}
        response = requests.put(url, data=payload, headers=headers)

        myJSONResponse = json.loads(response.text)
        
        self.assertEqual(200, response.status_code, ('Status code should be is 200. Current status code is %d.'
                                                     % response.status_code))
        self.assertEqual(1, myJSONResponse['tags'][0]['id'], ('Field value "id" should be is 1. Current status code is %d.'
                                                              % myJSONResponse['tags'][0]['id']))
        self.assertEqual("wild", myJSONResponse['tags'][0]['name'], ('Field value "id" should be is 1. Current status code is %s.'
                                                                     % myJSONResponse['tags'][0]['name']))


    # Finds Pets by status
    # GET /pet/findByStatus
    def testFindPetByStatusAvailable(self):

        url = "http://petstore.swagger.io/v2/pet/findByStatus"
        querystring = {"status":"available"}
        payload = ""
        headers = {'Content-Type': "application/json"}

        response = requests.get(url, data=payload, headers=headers, params=querystring)

        myJSONResponse = json.loads(response.text)

        n = 0
        for i in range(len(myJSONResponse)):
            if myJSONResponse[i]['id']==11:
                n += 1
                print (myJSONResponse[i])
        self.assertEqual(1, n, "No record in database!!!")


    # Updates a pet in the store with form data
    # POST /pet/{petId}
    def testUpdatesAPet(self):

        url = "http://petstore.swagger.io/v2/pet/"
        petId = "11"
        querystring = {"status": "sold11"}
        payload = ""
        headers = {'Content-Type': "application/x-www-form-urlencoded"}

        response = requests.post(url+petId, data=payload, headers=headers, params = querystring)

        myJSONResponse = json.loads(response.text)

        self.assertEqual(200, response.status_code, ('Status code should be is 200. Current status code is %d.'
                                                     % response.status_code))
        self.assertEqual("sold", myJSONResponse['available'], ('Field value "available" should be is "sold". '
                                                    'Current status code is %s.' % myJSONResponse['available']))


if __name__ == "__main__":
    unittest.main()



