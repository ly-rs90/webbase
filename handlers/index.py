#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@File:         index.py
@Author:       yili
@Email:        yili@panyi.ai
@Date:         2020/7/15 上午11:34
@Description: 
"""
from .base import Base


class Index(Base):
    def get(self):
        self.render('index.html')
