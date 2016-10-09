# encoding:utf-8

import requests

match_request_url = 'http://op.juhe.cn/onebox/basketball/nba'
team_request_url = 'http://op.juhe.cn/onebox/basketball/team'
request_robot_key = 'fb57754428a7650f64e175b5c1aaa3d4'

# 调用聚合网站的sdk

def get_basket_match():
    bag = {'key': request_robot_key}
    res = requests.post(match_request_url, bag)
    result = res.json()
    ret = []
    if int(result['error_code']) == 0:
        head = {}
        result = result['result']
        head['title'] = result['title']
        head['url'] = 'http://sports.qq.com/'
        head['picurl'] = 'http://mat1.gtimg.com/sports/index2015/images/logo_lianhe.jpg'
        ret.append(head)
        for l in result['list']:
            down_new = {}
            team = l['tr'][0]
            down_new['title'] = '%s %s vs %s' % (l['title'], team['player1'], team['player2'])
            down_new['url'] = team['link1url']
            down_new['picurl'] = team['player1logo']
            ret.append(down_new)
    return ret



def get_team_match(team_name):
    bag = {'key': request_robot_key, 'team': team_name}
    res = requests.post(team_request_url, bag)
    result = res.json()
    # print result
    ret = []
    if int(result['error_code']) == 0:
        for l in result['result']['list']:
            down_new = {}
            team = l
            down_new['title'] = '%s %s vs %s' % (team['m_time'], team['player1'], team['player2'])
            down_new['url'] = team['link1url']
            down_new['picurl'] = team['player1logo']
            ret.append(down_new)
    return ret


if __name__ == '__main__':
    # print get_basket_match()
    print get_team_match('凯尔特人')