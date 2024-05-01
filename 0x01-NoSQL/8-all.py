#!usr/bin/env python3
"""A python function for mongodb"""


def list_all(mongo_collection):
    """
    Args: mono_collection - colection object
    Returns: list of all documents, none if not exists
    """
    if mongo_collection is None:
        return {}

    rlist = mongo_collection.find()
    return [document for document in rlist]
