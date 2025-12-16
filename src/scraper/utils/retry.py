from functools import wraps
import logging
from typing import Any, Callable

from src.utils.logger import configure_logging 

logger = logging.getLogger(__name__) 
configure_logging()


def retry(attempts: int = 3): 
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]: 
        @wraps(func)
        async def wrapper(*args: Any, **kwargs: Any) -> Any: 
            attempt = 0
            while attempt != attempts:
                try:
                    res = await func(*args, **kwargs)
                    return res
                except Exception as exc: 
                    logger.error(f"Error[{attempt + 1}/{attempts}]: {str(exc)}")
                attempt += 1
        return wrapper 
    return decorator
