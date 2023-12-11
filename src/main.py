import asyncio
import pygame
from pong import Pong


async def main():
    pong = Pong()
    while pong.running:
        pong.mainloop()
        await asyncio.sleep(0)
    pong.cleanup()

if __name__ == "__main__":
    asyncio.run(main())
