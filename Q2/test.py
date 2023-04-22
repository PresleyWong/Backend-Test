import requests
import time

if __name__ == "__main__":
    for n in range(20):
        response = requests.get('http://127.0.0.1:8000/get-hash-odd-number')
        print(response.json())
        time.sleep(1)
