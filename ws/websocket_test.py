import threading
import time

import websockets
import asyncio

async def message_handle(websocket):
    async for message in websocket:
        print(f'server receive: {message}')
        await websocket.send(message)

async def sever_start():
    async with websockets.serve(message_handle, "localhost", 8765) as ws_server:
        await asyncio.Future()  # run forever

async def client_ping(ws):
    while True:
        await ws.send('PING')
        await asyncio.sleep(1)

async def client_read(ws):
    while True:
        rec = await ws.recv()
        print(f'client receive: {rec}')

async def client_start():
    async with websockets.connect("ws://localhost:8765") as websocket:
        asyncio.create_task(client_read(websocket))
        asyncio.create_task(client_ping(websocket))
        await asyncio.Future()

def run_loop_inside_thread(loop):
    loop.run_forever()

async def just_wait(i:int):
    print('start')
    await asyncio.sleep(i)
    print('end')

if __name__ == '__main__':
    # asyncio.run(client_start())
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.create_task(sever_start())
    time.sleep(1)
    loop.create_task(client_start())
    loop.run_forever()
