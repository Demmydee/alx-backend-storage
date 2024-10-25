#!/usr/bin/env python3
"""
Redis basic project
"""

from functools import wraps
from typing import Any, Callable, Union
import redis
import uuid


class Cache:
    """
    Write strings to Redis
    """

    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    @call_history
    @count_calls
    def store(self, data:  Union[str, bytes, int, float]) -> str:
        """
        take a data argument, generate a random key and return the key.
        """
        data_key = str(uuid.uuid4())
        self._redis.set(data_key, data)
        return data_key