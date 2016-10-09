# encoding:utf-8

import requests
import traceback


def get_token():
    try:
        data = {'grant_type': 'client_credential',
                'appid': 'wxffc2efc83cd3cac8',
                'secret': '6619da74b175a079677e505cbb6fe9dc'}
        res = requests.get('https://api.weixin.qq.com/cgi-bin/token', params=data)
        result = res.json()
        if result.get('errcode', ''):
            print 'error message:%s' % result['errmsg']
            return ''
        elif result.get('access_token', ''):
            return result['access_token']
        else:
            return ''
    except:
        traceback.print_exc()
        return ''


def init_menu():
    menu_json = '''
        {
             "button":[
             {
                   "name":"学号",
                   "sub_button":[
                   {
                       "type":"click",
                       "name":"徐永亮",
                       "key":"xuyl"
                    },
                    {
                       "type":"click",
                       "name":"徐越",
                       "key":"xuy"
                    },
                    {
                       "type":"click",
                       "name":"张珂",
                       "key":"zhangk"
                    }]
               },
              {
                   "name":"菜单",
                   "sub_button":[
                   {
                       "type":"view",
                       "name":"搜索",
                       "url":"http://www.soso.com/"
                    },
                    {
                       "type":"view",
                       "name":"视频",
                       "url":"http://v.qq.com/"
                    },

                    {
                       "type":"click",
                       "name":"说明",
                       "key":"info"
                    },
                    {
                       "type":"click",
                       "name":"NBA对战视频",
                       "key":"match"
                    }]
               }]
         }
    '''
    token = get_token()
    #  token = 'tokennMosXgd90FL8m_uc1gEIRc2T8jCfYEq5Fvb08_lXKLePli35CkDl2gqUGroRFUFyebvFEl86xQDzDYiPWA3lsTi49cf0rnRELkWxuulZ1TCXR9b7HypzwFW0WF_gk36zXEEaAGACJJ'
    if token:
        url = 'https://api.weixin.qq.com/cgi-bin/menu/create?access_token=%s' % token
        res = requests.post(url, data=menu_json).json()
        if str(res['errcode']) == '0':
            print 'change menu success'
        else:
            print 'change menu fail'
        print 'token : %s' % token


if __name__ == '__main__':
    init_menu()
