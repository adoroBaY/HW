import functools
from collections import OrderedDict
import requests

def cache(max_limit=64):
    """A decorator for caching with deleting elements by LFU algorithm after going beyond the limit"""

    def internal(func):
        @functools.wraps(func)
        def deco(*args, **kwargs):
            cache_key = (args, tuple(kwargs.items()))
            if cache_key in deco._cache:
                # move to the end of the list
                if cache_key in counter:
                    counter[cache_key] += 1
                return deco._cache[cache_key]

            result = func(*args, **kwargs)

            # delete when the limit is reached
            if len(deco._cache) >= max_limit:
                min_key = min(counter, key=counter.get)
                # delete the first element
                deco._cache.pop(min_key)
                counter.pop(min_key)

            deco._cache[cache_key] = result
            counter[cache_key] = 1
            return result

        deco._cache = OrderedDict()
        counter = {}
        return deco

    return internal


@cache()
def fetch_url(url, first_n=100):
    """Fetch a given url"""
    res = requests.get(url)
    return res.content[:first_n] if first_n else res.content


print(fetch_url('https://lms.ithillel.ua'))
print(fetch_url('https://twitter.com'))
print(fetch_url('https://www.reddit.com'))
print(fetch_url('https://www.dtek-oem.com.ua'))
print(fetch_url('https://youtube.com'))
