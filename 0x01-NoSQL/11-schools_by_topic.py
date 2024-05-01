#!/usr/bin/env python3
"""Return schools by topic"""


from pymongo import MongoClient


def schools_by_topic(mongo_collection, topic):
    """Return schools by topic"""
    search_result = mongo_collection.find( {"topics": topic})
    return [school for school in search_result]

