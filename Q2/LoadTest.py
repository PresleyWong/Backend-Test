import requests
import time
import aiohttp
import asyncio


async def load_test(i):
    async with aiohttp.ClientSession() as session:
        print(f"#{i+1} call endpoint ")
        async with session.get('http://127.0.0.1:8000/get-hash-odd-number-v2') as response:
            data = await response.json()
            print(f"#{i+1} response: {data}")


async def main(iteration):
    tasks_list = []
    for i in range(iteration):
        task = asyncio.create_task(load_test(i))
        tasks_list.append(task)
        await asyncio.sleep(1)

    for task in tasks_list:
        await task


if __name__ == "__main__":
    iteration = input("Enter number of test:")
    if iteration.isdigit():
        asyncio.run(main(int(iteration)))
    else:
        print("Please enter a valid integer value.")
