# # import requests
# # import redis
# # import json
# # from fastapi import FastAPI
# # from flask import Flask

# # rd = redis.Redis(host="localhost", port=6379, db=0)

# # app = FastAPI()

# # @app.get("/")
# # def read_root():
# #   return "Hello World"


# # @app.get("/fish")
# # def red():
# #   r = requests.get(f"https://api.coindesk.com/v1/bpi/currentprice.json")
# #   return "hey there"
# # # def read_fish(species: str):
# # #   cache = rd.get(species)
# # #   if cache:
# # #     print("cache hit")
# # #     return json.loads(cache)
# # #   else:
# # #     print("cache miss")
# # #     r = requests.get(f"https://api.coindesk.com/v1/bpi/currentprice.json")
# # #     rd.set(species, r.text)
# # #     rd.expire(species, 5)a
# # #     return r.json()


# import asyncio
# import time

# async def task1():
#     print("Task 1 starting")
#     await asyncio.sleep(2)  # Simulate a task
#     print("Task 1 finished")
#     return "Result of Task 1"

# async def task2(result_from_task1):
#     print(f"Task 2 starting with result: {result_from_task1}")
#     await asyncio.sleep(1)
#     print("Task 2 finished")

# async def task3():
#     await asyncio.sleep(2)
#     print("Task 3 doing something else...") 

# async def main():
#     st = time.time()
#     result1 = await task1()
#     # await task2(result1)
#     # await task3()  # Can run concurrently with task2 
#     print(result1)
#     et = time.time()
#     print("------------",et-st)

# # async def main():
# #     task1_handle = asyncio.create_task(task1())
# #     task2_handle = asyncio.create_task(task2(await task1_handle))  # task2 starts now!
# #     task3_handle = asyncio.create_task(task3())

# #     st = time.time()
# #     await task1_handle  # Ensure we get the result of task1
# #     await task2_handle
# #     await task3_handle
# #     et = time.time()
# #     print("------------",et-st) 


# asyncio.run(main())

import asyncio
import time

async def task1():
    print("Task 1 starting")
    await asyncio.sleep(4)  # Simulate a task
    print("Task 1 finished")
    return "Result of Task 1"

async def fetch_data(url):
    print(f"Fetching from: {url}")
    await asyncio.sleep(4)  # Simulate network delay
    return f"Data from: {url}"

async def main():
    st = time.time()
    fetch1 = asyncio.create_task(fetch_data("https://www.example.com"))
    fetch2 = asyncio.create_task(fetch_data("https://www.python.org"))
    fetch3 = asyncio.create_task(fetch_data("https://www.example.com"))
    fetch4 = asyncio.create_task(fetch_data("https://www.python.org")) 
    fetch5 = asyncio.create_task(fetch_data(await fetch_data("----------------")))
    fetch6 = asyncio.create_task(fetch_data("https://www.python.org")) 
    fetch7 = asyncio.create_task(fetch_data("https://www.example.com"))
    fetch8 = asyncio.create_task(fetch_data("https://www.python.org"))  
    # result1 = await task1()  # Await for task1 to complete
    # print(result1)
    # Concurrent network requests while main is paused
    # fetch1 = asyncio.create_task(fetch_data("https://www.example.com"))
    # fetch2 = asyncio.create_task(fetch_data("https://www.python.org")) 
    results = await asyncio.gather(fetch1, fetch2,fetch3,fetch4,fetch5,fetch6,fetch7,fetch8)
    for result in results:
        print(result)
    et=time.time()
    print(et-st)


  
asyncio.run(main())
  