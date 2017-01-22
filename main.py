#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import logging
import time

import util

util.LoggingManager(util.file_relative_path("logging.json"))
logger = logging.getLogger(__name__)

def main():
    while True:
        logging.info("test")
        time.sleep(10)

if __name__ == '__main__':
    main()
