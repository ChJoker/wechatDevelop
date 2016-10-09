# encoding:utf-8

import requests

request_url = 'http://www.tuling123.com/openapi/api'
request_robot_key = '901678d7f4e9402fa506a731d9790ad0'

# 调用图灵机器人的sdk
def get_turling_conversation(bag):
    assert isinstance(bag, dict)
    bag['key'] = request_robot_key
    res = requests.post(request_url, bag)
    return res.json()

if __name__ == '__main__':
    bag = {'info': '你是谁', 'userid': '123'}
    res = get_turling_conversation(bag)
    print res.content
