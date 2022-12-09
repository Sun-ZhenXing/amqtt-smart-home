import asyncio
import logging

import config
from amqtt.broker import Broker

try:
    uvloop = __import__('uvloop')
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
except ImportError:
    pass


async def broker_coro():
    broker = Broker(config.broker_config)
    await broker.start()


if __name__ == '__main__':
    formatter = '[%(asctime)s] :: %(levelname)s :: %(name)s :: %(message)s'
    logging.basicConfig(level=logging.INFO, format=formatter)
    asyncio.get_event_loop().run_until_complete(broker_coro())
    asyncio.get_event_loop().run_forever()
