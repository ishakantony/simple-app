import time
import logging
import random

logging.basicConfig(
    format='[%(levelname)s] [%(asctime)s] %(message)s', level=logging.INFO)

endpoints = ['http://api-gateway.com/api/v1/products',
             'http://api-gateway.com/api/v1/schedule?region=US', 'http://api-getway.com/api/v1/order']

endpointevents = ['resulted in 200', 'resulted in 400',
                  'timed out after 60s', 'resulted in 500']

users = ['Alex', 'Amy', 'Brad', 'Charlie']

userevents = ['has logged in!', 'has logged out!', 'was denied login - too many attempts',
              'had made unsual number of requests for the past 30 seconds']

httpmethods = ['GET', 'POST', 'PUT', 'DELETE']


def getrandommessage():
    i = random.randint(0, 1)
    if i == 0:
        return f'{random.choice(users)} {random.choice(userevents)}'
    else:
        return f'{random.choice(httpmethods)} {random.choice(endpoints)} {random.choice(endpointevents)}'


while True:
    i = random.randint(0, 10)
    if i < 3:
        logging.info(getrandommessage())
    elif i >= 3 and i < 7:
        logging.warning(getrandommessage())
    else:
        logging.error(getrandommessage())
    time.sleep(0.3)
