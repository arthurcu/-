#
# @Time     : 2022/07/17 17:26
# @Author   : Dragon.G
# @File     : getdata.py
import requests
from headers import Headers


def get_data(username, password):
    url1 = 'https://webvpn.cczu.edu.cn/http/webvpn4578b329feda6a5f6cc5a9222350e3b0/sso/login?service=http%3A%2F%2Fs.cczu.edu.cn%2F'
    url2 = 'https://webvpn.cczu.edu.cn/http/webvpndc2d086cb5b297c15e661687e73c1549/web_cas/web_cas_login_jwgl.aspx'
    url3 = 'https://webvpn.cczu.edu.cn/http/webvpndc2d086cb5b297c15e661687e73c1549/View/indexTablejw.aspx'
    url4 = 'https://webvpn.cczu.edu.cn/http/webvpndc2d086cb5b297c15e661687e73c1549/web_cjgl/cx_cj_xh.aspx'
    headers = Headers.headers
    session = requests.Session()
    try:
        html = session.get(url1).text
    except:
        return 'No network'

    lt = get_lt(html)
    execution = get_execution(html)

    data = {
        'username': username,
        'password': password,
        'lt': lt,
        'execution': execution,
        '_eventId': 'submit',
        'useVCode': 'false',
        'sessionVcode': '',
        'errorCount': ''
    }
    try:
        resp1 = session.post(url=url1, headers=headers, data=data)
        if resp1.status_code != 200:
            return resp1
    except:
        return 'No network'
    resp2 = session.get(url=url2, headers=headers)
    resp3 = session.get(url=url3, headers=headers)
    resp4 = session.get(url=url4, headers=headers)
    return resp4


def get_lt(html):
    s = '"lt" value="'
    a = html.find(s)
    b = html.find('"/>', a + len(s))
    lt = html[a + len(s):b]
    return lt


def get_execution(html):
    s = 'execution" value="'
    a = html.find(s)
    b = html.find('"/>', a + len(s))
    execution = html[a + len(s):b]
    return execution


'''get_data('20416301', '270528')'''

'''get_data('20416330', '186937')'''


def judge_data(data):
    if data == 'No network':
        return -1, '没有网络,请在有网的环境下重试'
    elif data.status_code == 200:
        return 1, ''
    else:
        return 0, '账号或密码错误，请重新输入'


