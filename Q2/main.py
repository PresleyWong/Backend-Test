import hashlib
import string
import random
import time
from typing import Union
from fastapi import FastAPI

app = FastAPI()


def random_string_generator(number_of_character=20):
    output = ""
    character_options = [string.ascii_letters, string.digits, string.punctuation]
    for i in range(number_of_character):
        selected_option = random.choice(character_options)
        selected_character = random.choice(selected_option)
        output += selected_character
    return output


@app.get("/")
def get_sha256_hash():
    start_time = time.time()
    text = random_string_generator()
    hash = hashlib.sha256(text.encode('UTF-8')).hexdigest()
    time.sleep(1)
    end_time = time.time()
    return {"hash": hash, "time_elapsed": end_time-start_time}
