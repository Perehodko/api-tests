# -*- coding: utf-8 -*-
import requests
import sys
import inspect


# Add a double separator in path
# GET /pet//11
def testDoubleSeparator():
    url = "https://petstore.swagger.io/v2/pet//11"

    headers = {"Accept": "application/json"}

    response = requests.post(url, headers=headers)

    if response.status_code != 404:
        print('Status code should be is 404. Current status code is %d.' % response.status_code)
        print("The method name is", inspect.stack()[0][3])
    else:
        pass


# Method not allowed
# GET /pet/
def testMethodNotAllowed():
    url = "https://petstore.swagger.io/v2/pet"

    headers = {"Accept": "application/json"}

    response = requests.get(url, headers=headers)

    if response.status_code != 405:
        print('Status code should be is 405. Current status code is %d.' % response.status_code)
        print("The method name is", inspect.stack()[0][3])
    else:
        pass


# Nonexistent user id
# POST /pet/69869
def testInvalidId():
    url = "https://petstore.swagger.io/v2/pet/69869"

    headers = {"Accept": "application/json"}

    response = requests.post(url, headers=headers)

    if response.status_code != 404:
        print('Status code should be is 404. Current status code is %d.' % response.status_code)
        print("The method name is", inspect.stack()[0][3])
    else:
        pass


# Space in path
# POST /  pet/
def testSpaceInPath():
    url = "https://petstore.swagger.io/v2/  pet"
    headers = {"Accept": "application/json"}

    response = requests.post(url, headers=headers)

    if response.status_code != 400:
        print('Status code should be is 400. Current status code is %d.' % response.status_code)
        print("The method name is", inspect.stack()[0][3])
    else:
        pass


methods = [testDoubleSeparator, testMethodNotAllowed, testInvalidId, testSpaceInPath]


def main():
    for m in methods:
        m()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Выход...')
        sys.exit(0)
