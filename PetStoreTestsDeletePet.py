# -*- coding: utf-8 -*-
import requests
import json
import sys


# Add a new pet to the store
# POST /pet
def testCreatePet():
    url = "http://petstore.swagger.io/v2/pet"
    payload = \
        {
            "id": 12,
            "category": {
                "id": 0,
                "name": "Jerry"
            },
            "name": "mouse",
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

    # parsing JSON response
    myJSONResponse = json.loads(response.text)

    # tests
    if response.status_code != 200:
        print('Status code should be is 200. Current status code is %d.' % response.status_code)
    else:
        pass

    if myJSONResponse['id'] != 12:
        print('Field value "id" should be is 12. Current status code is %d.' % myJSONResponse['id'])
    else:
        pass

    if myJSONResponse['category']['name'] != "Jerry":
        print('Field value "name" should be is "Jerry". Current value is %s.' % myJSONResponse['category']['name'])


# Deletes a pet
# DELETE /pet/{petId}
def testDeletePet():
    url = "http://petstore.swagger.io/v2/pet/"
    petId = "12"
    headers = {'Content-Type': "application/json"}

    response = requests.delete(url + petId, headers=headers)

    # tests
    if response.status_code != 200:
        print('Status code should be is 200. Current status code is %d.' % response.status_code)
    else:
        pass


# Get pet by ID
# GET /pet/{petId}
def testGetPet():
    url = "http://petstore.swagger.io/v2/pet/"
    petId = "12"
    headers = {'Content-Type': "application/json"}

    response = requests.get(url + petId, headers=headers)

    # tests
    if response.status_code != 404:
        print('Status code should be is 404. Current status code is %d.' % response.status_code)
    else:
        pass


methods = [testCreatePet, testDeletePet, testGetPet]


def main():
    for m in methods:
        m()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Выход...')
        sys.exit(0)
