import asyncio
import logging

try:
    uvloop = __import__('uvloop')
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
except ImportError:
    pass

import config
from amqtt.client import ClientException, MQTTClient
from amqtt.mqtt.constants import QOS_1, QOS_2


async def client_coro():
    cli = MQTTClient()
    await cli.connect(
        config.mqtt_server,
    )
    await cli.subscribe([
        ('test/topic', QOS_1),
        ('test/topic', QOS_2),
    ])
    while True:
        try:
            message = await cli.deliver_message()
            packet = message.publish_packet
            print(packet.variable_header.topic_name,
                  packet.payload.data.decode('utf-8'))
        except ClientException as ce:
            print(ce)


if __name__ == '__main__':
    formatter = "[%(asctime)s] %(name)s {%(filename)s:%(lineno)d} %(levelname)s - %(message)s"
    logging.basicConfig(level=logging.DEBUG, format=formatter)
    asyncio.get_event_loop().run_until_complete(client_coro())
