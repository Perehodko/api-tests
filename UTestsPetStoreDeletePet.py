# -*- coding: utf-8 -*-
import requests
import unittest
import json


class TestPositiveTestsPet(unittest.TestCase):


    # Add a new pet to the store
    # POST /pet
    def testCreatePet(self):

        url = "http://petstore.swagger.io/v2/pet"
        payload = "{\n  \"id\": 12,\n  \"category\": {\n    \"id\": 0,\n    \"name\": \"Jerry\"\n  }," \
                  "\n  \"name\": \"mouse\",\n  \"photoUrls\": [\n    \"string\"\n  ],\n  \"tags\": " \
                  "[\n    {\n      \"id\": 0,\n      \"name\": \"string\"\n    }\n  ],\n  \"status\": " \
                  "\"available\"\n}\n\n"
        headers = {'Content-Type': "application/json"}

        response = requests.post(url, data=payload, headers=headers)

        # parsing JSON response
        myJSONResponse = json.loads(response.text)

        self.assertEqual(200, response.status_code,
                         ('Status code should be is 200. Current status code is %d.' % response.status_code))
        self.assertEqual(12, myJSONResponse['id'],
                         ('Field value "id" should be is 12. Current status code is %d.' % myJSONResponse['id']))
        self.assertEqual("Jerry", myJSONResponse['category']['name'],
                         ('Field value "name" should be is "Jerry". Current value is %s.' % myJSONResponse['category']['name']))


    # Deletes a pet
    # DELETE /pet/{petId}
    def testDeletePet(self):

        url = "http://petstore.swagger.io/v2/pet/"
        petId = "12"
        payload = ""
        headers = {'Content-Type': "application/json"}

        response = requests.delete(url+petId, data = payload, headers=headers)

        self.assertEqual(200, response.status_code,
                         ('Status code should be is 200. Current status code is %d.' % response.status_code))


    # Get pet by ID
    # GET /pet/{petId}
    def testGetPet(self):

        url = "http://petstore.swagger.io/v2/pet/"
        petId= "12"
        payload = ""
        headers = {'Content-Type': "application/json"}

        response = requests.get(url+petId, data=payload, headers=headers)

        self.assertEqual(404, response.status_code,
                         ('Status code should be is 404. Current status code is %d.' % response.status_code))



if __name__ == "__main__":
    unittest.main()



