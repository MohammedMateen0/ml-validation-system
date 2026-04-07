import time
import functools
import logging
from typing import Callable

logging.basicConfig(level=logging.INFO)


def timer(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        logging.info(f"[TIMER] {func.__name__} → {elapsed:.4f}s")
        return result
    return wrapper


def retry(max_attempts: int = 3, delay: float = 1.0):
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts:
                        logging.error(f"All attempts failed: {e}")
                        raise
                    logging.warning(f"Attempt {attempt} failed: {e}. Retrying...")
                    time.sleep(delay * attempt)
        return wrapper
    return decorator