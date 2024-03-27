#!/usr/bin/env python3

"""
This module implements a get_page function with caching functionality and expiration time.
"""

import requests
import time
from typing import Callable

# Import Cache class and relevant decorators from web.py
from web import Cache, count_calls


# Initialize the Cache object
cache = Cache()


# Define decorator for caching with expiration time
def cache_with_expiry(expiration_time: int) -> Callable:
    """
    Decorator function to cache function results with expiration time.

    Args:
        expiration_time (int): Expiration time for cache in seconds.

    Returns:
        Callable: Decorator function.
    """
    def decorator(func: Callable) -> Callable:
        """
        Decorator function to cache function results with expiration time.

        Args:
            func (Callable): Function to be decorated.

        Returns:
            Callable: Wrapper function.
        """
        @wraps(func)
        def wrapper(url: str) -> str:
            """
            Wrapper function to cache function results with expiration time.

            Args:
                url (str): URL to fetch.

            Returns:
                str: HTML content of the page.
            """
            # Generate cache key
            cache_key = f"page:{url}"
            # Check if cached data exists and is not expired
            cached_data = cache.get(cache_key)
            if cached_data:
                return cached_data
            # If not cached or expired, fetch the page content
            page_content = requests.get(url).text
            # Cache the page content with expiration time
            cache.store(cache_key, page_content, expiration_time)
            return page_content
        return wrapper
    return decorator


# Apply cache decorator with expiry time of 10 seconds
@cache_with_expiry(10)
def get_page(url: str) -> str:
    """
    Fetches the HTML content of a page and caches it with expiration time.

    Args:
        url (str): URL of the page.

    Returns:
        str: HTML content of the page.
    """
    return requests.get(url).text


# Test the function
if __name__ == "__main__":
    url = "http://slowwly.robertomurray.co.uk/delay/1000/url/http://www.google.com"
    for _ in range(3):
        print(get_page(url))
        time.sleep(5)  # Wait for cache to expire
