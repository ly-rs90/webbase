#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@File:         route.py
@Author:       yili
@Email:        yili@panyi.ai
@Date:         2020/7/15 上午11:20
@Description: 
"""
from tornado.web import StaticFileHandler
from handlers.index import Index
from conf.setting import static_path


handlers = [
    (r'/', Index),
    (r'/(.*)', StaticFileHandler, {'path': static_path})
]
