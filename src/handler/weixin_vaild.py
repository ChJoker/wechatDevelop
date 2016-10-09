#!/usr/bin/python
# encoding:utf-8


from wechat_sdk import WechatConf, WechatBasic
from baseHandler import BaseHandler
from helper.process import ProcessBody


# 集成baseHandle ,实现do_action方法
class WeixinVaild(BaseHandler):
    def do_action(self):
        # 创建wechat sdk 把消息给封装起来,方便调用验证,以及消息提取和消息回复
        conf = WechatConf(
            token='xuyung',
            appid='wxffc2efc83cd3cac8',
            appsecret='6619da74b175a079677e505cbb6fe9dc',
            encrypt_mode='normal'
        )
        wechat = WechatBasic(conf=conf)
        signature = self.get_argument('signature', '')
        if signature:
            timestamp = self.get_argument('timestamp', '')
            nonce = self.get_argument('nonce', '')
            if wechat.check_signature(signature, timestamp, nonce):
                if self.get_argument('echostr', ''):
                    self.result = self.get_argument('echostr', '')
                    return
                else:
                    wechat.parse_data(self.request.body)
                    process = ProcessBody(wechat)
                    self.result = process.get_result()
            else:
                self.result = 'error'

        else:
            wechat.parse_data(self.request.body)
            process = ProcessBody(wechat)
            self.result = process.get_result()
