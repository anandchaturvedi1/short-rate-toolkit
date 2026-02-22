from functools import wraps, lru_cache
import time
from typing import Callable, Any

def timeit(func: Callable) -> Callable:
    """timing decorator"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        t0 = time.time()
        res = func(*args, **kwargs)
        t1 = time.time()
        print(f"[timeit] {func.__name__} took {(t1-t0):.4f}s")
        return res
    return wrapper

def cached(maxsize: int = 128):
    """lru_cache-based decorator for instance-less functions (or classmethod)"""
    def deco(func: Callable) -> Callable:
        cache = lru_cache(maxsize=maxsize)(func)
        @wraps(func)
        def wrapper(*args, **kwargs):
            return cache(*args, **kwargs)
        wrapper.cache_clear = cache.cache_clear
        return wrapper
    return deco
