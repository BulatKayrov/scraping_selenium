import os
from pyvirtualdisplay import Display


def create_folder(_func=None, *, dir_name: str = None):
    def _decorator(func):
        def wrapper(*args, **kwargs):
            base_dir = os.path.dirname(os.path.abspath(__file__))
            dir_name_ = dir_name if dir_name is not None else 'default_name'
            template = os.path.join(base_dir, dir_name_)

            if not os.path.exists(template):
                os.mkdir(template)

            return func(*args, **kwargs)

        return wrapper

    if _func is None:
        return _decorator
    return _decorator(_func)


def hidden_chrome(func):
    def wrapper(*args, **kwargs):
        with Display() as disp:
            response = func(*args, **kwargs)
        return response
    return wrapper
