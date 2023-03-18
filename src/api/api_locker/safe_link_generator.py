import string
import random
import os
from dotenv import load_dotenv
import time
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


while True:

    base_api_secret_key = get_random_string(
        int(os.getenv("API_LOCKER_LENGHT")))
    print(base_api_secret_key)
    time.sleep(10)
