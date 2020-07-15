#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@File:         base.py
@Author:       yili
@Email:        yili@panyi.ai
@Date:         2020/7/15 上午11:35
@Description: 
"""
from typing import Optional, Awaitable

from tornado.web import RequestHandler


class Base(RequestHandler):
    def data_received(self, chunk: bytes) -> Optional[Awaitable[None]]:
        pass
