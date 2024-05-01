#!/usr/bin/env bash
"""Inserting in mongodb"""


from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """insert item into mongo"""
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id