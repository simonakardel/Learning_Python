import datetime

# Decorator exercise
def log_calls(func):
    def wrapper(*args):
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        result = func(*args)
        with open('log.txt', 'a') as f:
            f.write(f'{timestamp} {func.__name__} called with args {args} with result {result}\n')
        print(f'called at {timestamp} with result {result}')
        return result
    return wrapper


@log_calls
def add(*args):
    return sum(args)

add(3, 5, 4, 9)

@log_calls
def printer(text):
    return text

printer('hey')