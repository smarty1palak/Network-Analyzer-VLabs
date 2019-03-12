import asyncio
import requests
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


async def main():
    loop = asyncio.get_event_loop()
    futures = [
        loop.run_in_executor(
            None, 
            requests.get, 
            'http://cse01-iiith.vlabs.ac.in/exp5/binarySearchTree.html'
        )
        for i in range(200)
    ]
    x=0
    c=0
    for response in await asyncio.gather(*futures):
        x=x+response.elapsed.total_seconds()
        c=c+1
    print(x/c)
    


loop = asyncio.get_event_loop()
loop.run_until_complete(main())