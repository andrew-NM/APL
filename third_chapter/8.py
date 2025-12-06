def log_call(func):
    def wrapper(*args, **kwargs):
       print("blablablablabla")
       func()
       print("blablablablbla")
    return wrapper
