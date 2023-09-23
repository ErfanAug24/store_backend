import string
import random
import os
from dotenv import load_dotenv
import time
from functools import wraps
from flask import request
load_dotenv()


def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_letters
    digits = string.digits
    safe_digit = ''.join(random.choice(digits) for i in range(length))
    safe_string = ''.join(random.choice(letters) for i in range(length))
    safe_link = ''.join(random.choice(safe_digit) +
                        random.choice(safe_string) for i in range(length))
    return safe_link


def Permission_Required():
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            auth = request.args
            secret_Key = get_random_string(5)
            if auth.get("passkey") == secret_Key:
                return func(*args, **kwargs)
            return {"Authentication": "Authentication Faild , please pass 'passkey' argument in header request."}, 403
        return inner
    return wrapper


    # while True:
base_api_secret_key = get_random_string(
    int(os.getenv("API_LOCKER_LENGHT")))
# time.sleep(10)


# berlan bazar bozorg
