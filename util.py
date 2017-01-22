#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
import logging.config

def file_relative_path(path):
    base = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(base, path)

class LoggingManager():

    def __init__(self, default_path='logging.json', default_level=logging.INFO, env_key='LOG_CFG'):
        self.setup_logging(default_path, default_level, env_key)

    def setup_logging(self, default_path, default_level, env_key):
        """Setup logging configuration
        """
        path = default_path
        value = os.getenv(env_key, None)
        if value:
            path = value
        if os.path.exists(path):
            with open(path, 'rt') as f:
                config = json.load(f)
            self.ensure_log_dir(config)
            logging.config.dictConfig(config)
        else:
            logging.basicConfig(level=default_level)

    def ensure_log_dir(self, config):
        handlers = config["handlers"]
        for key, handler in handlers.iteritems():
            if handler.has_key("filename"):
                dirpath = os.path.dirname(handler["filename"])
                if not os.path.exists(dirpath):
                    os.makedirs(dirpath)

