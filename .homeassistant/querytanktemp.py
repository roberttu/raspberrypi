#!/usr/bin/python3

from requests import get
print(get('http://192.168.1.189:8000/tanktemp.txt').text)
