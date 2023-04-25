import requests
import time


def load_test(n=20):
    for _ in range(n):
        response = requests.get('http://127.0.0.1:8000/get-hash-odd-number')
        print(response.json())
        time.sleep(1)


if __name__ == "__main__":
    iteration = input("Enter number of test:")
    load_test(int(iteration))

