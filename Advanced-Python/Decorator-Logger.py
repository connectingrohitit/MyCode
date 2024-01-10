import datetime
def logged(function):
    def wrapper(*args, **kwargs):
        value = function(*args, **kwargs)
        with open('logfile.txt', 'a+') as log:
            f_name = function.__name__
            log_message = f"{datetime.datetime.now().strftime('%d_%m_%y-%H_%M_%S')} -- Function {f_name} returned value {value}. \n"
            log.write(log_message)
            print(log_message)
        return value
    return wrapper


@logged
def add_num(a, b):
    return a + b


add_num(10, 20)
