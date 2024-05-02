#!/usr/bin/env python3
""" a python script to dislplay some messages on a dataabase"""

from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginxstuff = client.logs.nginx
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']

    print(f'{nginxstuff.count_documents({})} logs')

    print("Methods:")
    for method in methods:
        number = nginxstuff.count_documents({"method": method})
        print(f'    method {method}: {number}')

    number = nginxstuff.count_documents({"method": "GET", "path": "/status"})
    print(f'{number} status check')