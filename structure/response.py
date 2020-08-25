#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@File:         response.py
@Author:       yili
@Email:        yili@panyi.ai
@Date:         2020/8/25 上午9:07
@Description: 
"""
import json


class Response:
    __slots__ = ['_data', '_code', '_msg']

    def __init__(self):
        self._data = ''
        self._code = ''
        self._msg = ''

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, v):
        if not isinstance(v, int):
            raise ValueError('`code` must be a integer.')

        self._code = v

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, v):
        if not hasattr(v, '__str__'):
            raise ValueError(f'{v} cannot be serialized.')

        self._data = v

    @property
    def msg(self):
        return self._msg

    @msg.setter
    def msg(self, v):
        if not isinstance(v, str):
            raise ValueError('`msg` must be a string.')

        self._msg = v

    @property
    def serial(self):
        return json.dumps({'code': self.code, 'data': self.data, 'msg': self.msg})
