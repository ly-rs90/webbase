#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@File:         run.py
@Author:       yili
@Email:        yili@panyi.ai
@Date:         2020/7/15 上午11:18
@Description: 
"""
import logging
import os

from tornado.options import define, options
from tornado.ioloop import IOLoop
from tornado.web import Application
from conf.setting import settings
from conf.route import handlers


define('port', default=9803, type=int, help='listening port')


class App(Application):
    def __init__(self):
        Application.__init__(self, handlers=handlers, **settings)


if __name__ == '__main__':
    log_file_prefix = os.path.abspath(os.path.join(os.path.dirname(__file__), f'logs/log@{options.port}.txt'))
    options.log_file_prefix = log_file_prefix
    options.log_file_max_size = 10 * 1024 * 1024
    options.logging = 'INFO'
    options.log_to_stderr = True
    options.parse_command_line()
    app = App()

    try:
        app.listen(options.port)
        logging.info(f'serve running on http://localhost:{options.port}')
        IOLoop.current().start()
    except KeyboardInterrupt:
        IOLoop.current().stop()
        logging.info('end.')
    except Exception as e:
        logging.error(e)
