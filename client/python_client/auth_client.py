#!/usr/bin/env python

import requests


def main():

  endpoint = "http://127.0.0.1:8500"
  input_data = {
      "data": {
          "keys": [[11.0], [2.0]],
          "features": [[1, 1, 1, 1, 1, 1, 1, 1, 1],
                       [1, 1, 1, 1, 1, 1, 1, 1, 1]]
      }
  }
  auth = requests.auth.HTTPBasicAuth("admin", "admin")
  result = requests.post(endpoint, json=input_data, auth=auth)
  print(result.text)


if __name__ == "__main__":
  main()
