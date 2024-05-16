import functools

def log(filename=None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                log_message = f'{func.__name__} ok'
                if filename:
                    with open(filename, 'a') as file:
                        file.write(log_message + '\n')
                else:
                    print(log_message)
                return result
            except Exception as e:
                error_message = f'{func.__name__} error: {type(e).__name__}. Input {args}, {kwargs}'
                if filename:
                    with open(filename, 'a') as file:
                        file.write(error_message + '\n')
                else:
                    print(error_message)
        return wrapper
    return decorator


@log(filename="mylog.txt")
def my_function(x, y):
    return x + y

my_function(1, 2)