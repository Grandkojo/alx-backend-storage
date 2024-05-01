#!/usr/bin/env python3
"""Update a collection"""


from pymongo import MongoClient


def update_topics(mongo_collection, name, topics):
    """Update topics based on name"""
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics } })
