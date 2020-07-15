#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@File:         run.py
@Author:       yili
@Email:        yili@panyi.ai
@Date:         2020/7/15 上午11:18
@Description: 
"""
from tornado.options import define, options
from tornado.ioloop import IOLoop
from tornado.web import Application
from conf.setting import settings
from conf.route import handlers


define('port', default=9801, type=int, help='listening port')


class App(Application):
    def __init__(self):
        Application.__init__(self, handlers=handlers, **settings)


if __name__ == '__main__':
    options.parse_command_line()
    app = App()

    try:
        app.listen(options.port)
        print(f'running on http://localhost:{options.port}')
        IOLoop.current().start()
    except KeyboardInterrupt:
        IOLoop.current().stop()
        print('end.')
    except Exception as e:
        print(e)
