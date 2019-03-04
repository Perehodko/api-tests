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

    # tests
    if response.status_code != 200:
        print('Status code should be is 200. Current status code is %d.' % response.status_code)
    else:
        pass


# Find pet by ID
# GET /pet/{petId}
def testGetPetFromId():
    url = "http://petstore.swagger.io/v2/pet/"
    id = "11"
    headers = {'Content-Type': "application/json"}
    response = requests.get(url + id, headers=headers)

    # parsing JSON response
    myJSONResponse = json.loads(response.text)

    # tests
    if response.status_code != 200:
        print('Status code should be is 200. Current status code is %d.' % response.status_code)
    else:
        pass

    if myJSONResponse['id'] != 11:
        print('Field value "id" should be is 11. Current status code is %d.' % myJSONResponse['id'])
    else:
        pass

    if myJSONResponse['category']['name'] != "Tom":
        print('Field value "id" should be is 11. Current status code is %d.' % myJSONResponse['id'])
    else:
        pass

    if myJSONResponse['category']['name'] != "Tom":
        print('Field value "name" should be is "Tom". Current value is %s.' % myJSONResponse['category']['name'])
    else:
        pass

    if myJSONResponse['status'] != "available":
        print('Field value "status" should be is "available". Current value is %s.' % myJSONResponse['status'])
    else:
        pass


# Update an existing pet
# PUT /pet
def testUpdatePet():
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

    # tests
    if response.status_code != 200:
        print('Status code should be is 200. Current status code is %d.' % response.status_code)
    else:
        pass

    if myJSONResponse['tags'][0]['id'] != 1:
        print('Field value "id" should be is 1. Current status code is %d.' % myJSONResponse['tags'][0]['id'])
    else:
        pass

    if myJSONResponse['tags'][0]['name'] != "wild":
        print('Field value "name" should be is "wild". Current value is %s.' % myJSONResponse['tags'][0]['name'])
    else:
        pass


# Finds Pets by status
# GET /pet/findByStatus
def testFindPetByStatusAvailable():
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
            print(myJSONResponse[i])

    # tests
    if response.status_code != 200:
        print('Status code should be is 200. Current status code is %d.' % response.status_code)
    else:
        pass

    # tests
    if n < 1:
        print("No record in database!!!")
    else:
        pass


# Updates a pet in the store with form data
# POST /pet/{petId}
def testUpdatesAPet():
    url = "http://petstore.swagger.io/v2/pet/"
    petId = "11"
    querystring = {"status": "sold"}
    headers = {'Content-Type': "application/x-www-form-urlencoded"}

    response = requests.post(url + petId, headers=headers, params=querystring)

    # tests
    if response.status_code != 200:
        print('Status code should be is 200. Current status code is %d.' % response.status_code)
    else:
        pass


methods = [testCreatePet, testGetPetFromId, testUpdatePet, testFindPetByStatusAvailable, testUpdatesAPet]


def main():
    for m in methods:
        m()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Выход...')
        sys.exit(0)
