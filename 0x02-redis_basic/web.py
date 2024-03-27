#!/usr/bin/env python3
"""
Web caching implementation using Redis
"""
import redis
import requests
from functools import wraps

# Connect to Redis
rc = redis.Redis()

def cache_page(func):
    """Decorator to cache page response"""
    @wraps(func)
    def wrapper(url: str) -> str:
        """Wrapper function"""
        count_key = f"count:{url}"
        cached_key = f"cached:{url}"
        # Increase count for the URL
        rc.incr(count_key)
        # Check if URL is cached
        if rc.exists(cached_key):
            return rc.get(cached_key).decode('utf-8')
        else:
            # Fetch the page
            resp = func(url)
            # Cache the response with expiration time of 10 seconds
            rc.setex(cached_key, 10, resp)
            return resp
    return wrapper

@cache_page
def get_page(url: str) -> str:
    """Fetches and returns the content of the URL"""
    return requests.get(url).text

if __name__ == "__main__":
    print(get_page('http://slowwly.robertomurray.co.uk'))
