#!/usr/bin/python3
"""
    Python script that takes in a letter and sends
    a POST request to http://0.0.0.0:5000/search_user
"""
from sys import argv
import requests


if __name__ == "__main__":
    data = {'q': ''}
    url = 'http://0.0.0.0:5000/search_user'

    try:
        data['q'] = argv[1]
    except IndexError:
        pass

    r = requests.post(url, data)

    try:
        id, name = r.json().get('id'), r.json().get('name')

        if not id or not name:
            print('No result')
        else:
            print('[{}] {}'.format(id, name))
    except Exception:
        print('Not a valid JSON')
