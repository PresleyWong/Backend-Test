import uvicorn
import hashlib
import string
import random
import time
from fastapi import FastAPI
from threading import Thread

app = FastAPI()


def random_string_generator(number_of_character=20):
    output = ""
    character_options = [string.ascii_letters, string.digits, string.punctuation]
    for i in range(number_of_character):
        selected_option = random.choice(character_options)
        selected_character = random.choice(selected_option)
        output += selected_character
    return output


@app.get("/get-random-hash")
async def get_sha256_hash():
    start_time = time.time()
    text = random_string_generator()
    hash = hashlib.sha256(text.encode('UTF-8')).hexdigest()
    time.sleep(1)
    end_time = time.time()
    return {"hash": hash, "time_elapsed": end_time - start_time}


@app.get("/get-hash-odd-number")
async def get_hash_odd_number():
    time_limit = 30
    start_time = time.time()
    found_flag = False
    while not found_flag:
        if (time.time() - start_time) > time_limit:
            return {"hash": "timeout", "time_elapsed": time.time() - start_time}

        response = await get_sha256_hash()
        last_character = response["hash"][-1]

        if last_character.isdigit() and int(last_character) % 2 != 0:
            found_flag = True
        else:
            continue

    end_time = time.time()
    return {"hash": response["hash"], "time_elapsed": end_time - start_time}



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
