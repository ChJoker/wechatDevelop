#!/usr/bin/python
# encoding:utf-8

from handler.weixin_vaild import WeixinVaild

url_map = [
    (r"/weixin", WeixinVaild)
]
