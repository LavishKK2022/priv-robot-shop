import json
import pika
import os

class Publisher:
    HOST = os.getenv('AMQP_HOST', 'rabbitmq')
    VIRTUAL_HOST = '/'
    EXCHANGE='robot-shop'
    TYPE='direct'
    ROUTING_KEY = 'orders'


