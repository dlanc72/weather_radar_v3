#!/usr/bin/python
# -*- coding:utf-8 -*-

# I am far too lazy to actually write my own cowsay generator, so I'm just gonna use an API for now
import logging
from random import random

from src.cowsay import CowSay
from waveshare_epd import epd7in5b_V3

logging.basicConfig(
    filename="cowsay.log",
    filemode="a",
    format="%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s",
    datefmt="%H:%M:%S",
    level=logging.DEBUG,
)


try:
    logging.info("Cowsay")

    cowsay = CowSay()

    black_white, red_white = cowsay.build_images()

    epd = epd7in5b_V3.EPD()
    # images
    blackimage = epd.getbuffer(black_white)
    redimage = epd.getbuffer(red_white)

    logging.info("init and Clear")
    epd.init()
    if random() < 0.2:
        epd.Clear()

    logging.info("Displaying")
    epd.display(blackimage, redimage)

    logging.info("Go to Sleep for 10 minutes...")
    epd.sleep()

except IOError as e:
    logging.info(e)

except KeyboardInterrupt:
    logging.info("ctrl + c:")
    epd7in5b_V3.epdconfig.module_exit()
    exit()
