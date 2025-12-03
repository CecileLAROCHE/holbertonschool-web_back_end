#!/usr/bin/env python3
"""
Module qui contient une seule fonction : schools_by_topic
"""

from pymongo import MongoClient
client = MongoClient()
db = client.logs
collection = db.nginx
nb_get = collection.count_documents({"method": "GET"})
nb_post = collection.count_documents({"method": "POST"})
nb_put = collection.count_documents({"method": "PUT"})
nb_patch = collection.count_documents({"method": "PATCH"})
nb_delete = collection.count_documents({"method": "DELETE"})
nb_status = collection.count_documents({"method": "GET", "path": "/status"})
total_logs = collection.count_documents({})
print(f"{total_logs} logs")
print("Methods:")
print(f"\tmethod GET: {nb_get}")
print(f"\tmethod POST: {nb_post}")
print(f"\tmethod PUT: {nb_put}")
print(f"\tmethod PATCH: {nb_patch}")
print(f"\tmethod DELETE: {nb_delete}")
print(f"{nb_status} status check")
