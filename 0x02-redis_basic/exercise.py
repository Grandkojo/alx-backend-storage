#!/usr/bin/env python3
"""Writing strings to redis"""


import redis
import uuid
import typing
from functools import wraps


def count_calls(method: typing.Callable) -> typing.Callable:
    """count call decorator"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwds):
        self._redis.incr(key)
        return method(self, *args, **kwds)

    return wrapper


def call_history(method: typing.Callable) -> typing.Callable:
    """store input and output history"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwds):
        self._redis.rpush(f"{key}:inputs", str(args))
        result = method(self, *args, **kwds)
        self._redis.rpush(f"{key}:outputs", str(result))
        return result
    return wrapper


class Cache:
    """A cache class in python for redis"""
    def __init__(self):
        """init function constructor"""
        self._redis = redis.Redis()
        self. _redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: typing.Union[str, bytes, float, int]) -> str:
        """store method that returns a string repr of the uuid"""
        rkey = str(uuid.uuid4())
        self._redis.set(rkey, data)
        return rkey

    def get(self, key: str,
            fn: typing.Optional[typing.Callable] = None) -> typing.Union[
                    str, bytes, float, int]:
        """A get function that take a key and returns the value"""
        get_value = self._redis.get(key)
        if fn is not None and get_value is not None:
            return fn(get_value)
        return get_value

    def get_str(self, key: str) -> str:
        """returns str repr of key"""
        value = self.get(key, fn=lambda x: x.decode())
        return value

    def get_int(self, key: str) -> int:
        """return the int rept of key"""
        value = self.get(key, fn=int)
        return value


def replay(method: typing.Callable) -> None:
    """a replay method to display history of calls to a function"""
    key = method.__qualname__
    self = method.__self__
    inputs = self._redis.lrange(f"{key}:inputs", 0, -1)
    outputs = self._redis.lrange(f"{key}:outputs", 0, -1)

    print(f"{key} was called {len(inputs)} times:")
    for _in, _out in zip(inputs, outputs):
        print(f"{key}(*{_in.decode('utf-8')}) -> {_out.decode('utf-8')}")
