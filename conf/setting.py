#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@File:         setting.py
@Author:       yili
@Email:        yili@panyi.ai
@Date:         2020/7/15 上午11:21
@Description: 
"""
import os


_cur_path = os.path.dirname(__file__)
root_path = os.path.dirname(_cur_path)

static_path = os.path.join(root_path, 'static')
template_path = os.path.join(root_path, 'template')


settings = {
    'debug': True,
    'xsrf_cookies': False,
    'cookie_secret': 'M93qJZBsRmyfe9RhD7/9W/SXZW+2eU6kq0lFrbLA8II=',
    'static_path': static_path,
    'template_path': template_path
}
