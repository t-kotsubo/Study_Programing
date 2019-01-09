import logging
from logging import getLogger
import pprint

name = "Takayuki"
list = {1:"Takayuki", 2:"Hiroshi", 3:"Kenta"}

logger = getLogger("test")
print(dir(logging))
print(dir(logger))
print(logger.name)

def print_name():
    logger.info(len(name))
    print(len(list))

print_name()
