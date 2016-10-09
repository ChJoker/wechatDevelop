#!/usr/bin/python
# encoding:utf-8
from wechat_sdk.messages import *
from helper import tuling, juhe


# 作为中间件对应不同的动作返回不同的结果
class ProcessBody(object):
    def __init__(self, wechat):
        self.wechat = wechat

    def get_result(self):
        if isinstance(self.wechat.message, TextMessage):
            return self._process_tesxMessage()
        elif isinstance(self.wechat.message, EventMessage):
            return self._process_eventMessage()
        else:
            return self.wechat.response_text(content='功能未开发')

    def _process_tesxMessage(self):
        get_team_match = juhe.get_team_match(self.wechat.message.content)
        if get_team_match:
            return self.wechat.response_news(get_team_match)
        bag = {'info': self.wechat.message.content, 'userid': self.wechat.message.source}
        res = tuling.get_turling_conversation(bag)
        return self.wechat.response_text(content=res.get('text'))

    def _process_eventMessage(self):
        message = self.wechat.message
        if message.type == 'click':
            if message.key == 'xuyl':
                return self.wechat.response_text(content='13020031128,2013级计算机三班,徐永亮')
            elif message.key == 'xuy':
                return self.wechat.response_text(content='13020031129,2013级计算机三班,徐越')
            elif message.key == 'zhangk':
                return self.wechat.response_text(content='13020031158,2013级计算机三班,张珂')
            elif message.key == 'info':
                return self.wechat.response_text(content='''
                    公众号说明:
                    1.输入消息时候,如果是NBA球队名字则会返回该球队比赛消息。
                    2.否则则是公众和你聊天啦:)
                ''')
            else:
                return self.wechat.response_news(juhe.get_basket_match())
        else:
            return self.wechat.response_text(content='功能未开发')
