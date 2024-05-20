import functools
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """Декоратор для логирования вызовов функций"""

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                log_message = f"{func.__name__} ok"
                if filename:
                    with open(filename, "a") as file:
                        file.write(log_message + "\n")
                else:
                    print(log_message)
                return result
            except Exception as e:
                error_message = f"{func.__name__} error: {type(e).__name__}. Input {args}, {kwargs}"
                if filename:
                    with open(filename, "a") as file:
                        file.write(error_message + "\n")
                else:
                    print(error_message)

        return wrapper

    return decorator
