import threading

import websockets
import asyncio

async def message_handle(websocket):
    async for message in websocket:
        await websocket.send(message)

async def sever_start():
    async with websockets.serve(message_handle, "localhost", 8765) as ws_server:
        await asyncio.Future()  # run forever

async def client_start():
    async with websockets.connect("ws://localhost:8765") as websocket:
        await websocket.send("Hello world!")
        s = await websocket.recv()
        print(s)


if __name__ == '__main__':
    asyncio.run(client_start())