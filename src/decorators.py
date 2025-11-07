from time import time


def log(filename=None):
    """Создан декоратор log, который будет автоматически логировать начало и конец выполнения функции,
    а также ее результаты или возникшие ошибки.  Декоратор должен принимать необязательный аргумент filename,
    который определяет, куда будут записываться логи (в файл или в консоль):
    Если filename задан, логи записываются в указанный файл.
    Если filename не задан, логи выводятся в консоль."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            if filename is None:
                try:
                    start_time = time()
                    result = func(*args, **kwargs)
                    end_time = time()
                    print(f'{func.__name__} ok, start func: {start_time}, end func: {end_time}')
                    return result
                except Exception as error:
                    print(f'{func.__name__} error: {type(error).__name__}. Inputs: {args}, {kwargs}')
                    return None
            else:
                try:
                    start_time = time()
                    result = func(*args, **kwargs)
                    end_time = time()
                    with open(filename, 'a') as file:
                        file.write(f'{func.__name__} ok, start func: {start_time}, end func: {end_time}\n')
                        return result
                except Exception as error:
                    with open(filename, 'a') as file:
                        file.write(f'{func.__name__} error: {type(error).__name__}. Inputs: {args}, {kwargs}\n')
                        return None
        return wrapper
    return decorator
