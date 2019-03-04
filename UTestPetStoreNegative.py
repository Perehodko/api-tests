# -*- coding: utf-8 -*-
import requests
import unittest


class TestNegativePet(unittest.TestCase):

    # Add a double separator in path
    # GET /pet//11
    def testDoubleSeparator(self):

        url = "https://petstore.swagger.io/v2/pet//11"
        headers = {"Accept": "application/json"}

        response = requests.post(url, headers=headers)

        self.assertEqual(404, response.status_code,
                         ('Status code should be is 404. Current status code is %d.'% response.status_code))


    # Method not allowed
    # GET /pet/
    def testMethodNotAllowed(self):

        url = "https://petstore.swagger.io/v2/pet"
        headers = {"Accept": "application/json"}

        response = requests.get(url, headers=headers)

        self.assertEqual(405, response.status_code,
                         ('Status code should be is 405. Current status code is %d.' % response.status_code))


    # Nonexistent user id
    # POST /pet/69869
    def testInvalidId(self):

        url = "https://petstore.swagger.io/v2/pet/69869"
        headers = {"Accept": "application/json"}

        response = requests.post(url, headers=headers)

        self.assertEqual(404, response.status_code,
                         ('Status code should be is 404. Current status code is %d.' % response.status_code))


    # Space in path
    # POST /  pet/
    def testSpaceInPath(self):

        url = "https://petstore.swagger.io/v2/  pet"
        headers = {"Accept": "application/json"}

        response = requests.post(url, headers=headers)

        self.assertEqual(400, response.status_code,
                         ('Status code should be is 400. Current status code is %d.' % response.status_code))


if __name__ == "__main__":
    unittest.main()
