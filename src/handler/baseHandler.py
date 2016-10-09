#!/usr/bin/python
# encoding:utf-8

from tornado.web import RequestHandler
from tornado.gen import coroutine, Task


class BaseHandler(RequestHandler):

    # 集成tornado 的RequestHandle 对get post 请求统一处理以及将方法变成异步

    @coroutine
    def get(self):
        yield Task(self.run)
        self.do_response()

    @coroutine
    def post(self):
        yield Task(self.run)
        self.do_response()

    def do_response(self):
        self.write(self.result)

    @coroutine
    def run(self):
        self.do_action()

    def do_action(self):
        pass
