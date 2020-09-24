import json
import random
import encrypt
import requests

###################配置部分####################
# 账号，默认是学号
account = ''
# 密码，默认是身份证后六位
passWord = ''
# server酱key，不填就不会发通知，官方地址https://sc.ftqq.com/
key = ''
# 位置相关，可以使用location_helper.py的输出（默认是你的当前位置，但是ip定位略有偏差），或者你自己去百度或者高德地图获取合法的位置，但是事实上这个也不检查
location = '四川省成都市双流区西航港街道成都信息工程大学行政办公楼成都信息工程大学(航空港校区)'
locationProvince = '四川省'
locationCity = '成都市'
locationCountry = '双流区'
#######################################


# 全局session
session = requests.session()


# 登陆
def login():
    url = 'https://yxxt.cuit.edu.cn/api/blade-workbench/nobody/weixin/login'
    data = {
        'account': account,
        'passWord': passWord,
        'modelName': 'SERVICE_CENTER-https://yxxt.cuit.edu.cn/font/antiepidemicClockIn/#/login',
        'willBind': 0
    }

    data = {
        'data': encrypt.encode(data)
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Authorization': 'Basic c2FiZXI6c2FiZXJfc2VjcmV0',
        'Connection': 'keep-alive',
        'Content-Length': str(len(data)),
        'Content-Type': 'application/json;charset=UTF-8',
        'Host': 'yxxt.cuit.edu.cn',
        'Origin': 'https://yxxt.cuit.edu.cn',
        'Referer': 'https://yxxt.cuit.edu.cn/?modelName=SERVICE_CENTER-https%3A%2F%2Fyxxt.cuit.edu.cn%2Ffont%2FantiepidemicClockIn%2F%23%2Flogin',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1 Edg/85.0.4183.102'
    }
    res = session.post(url=url, headers=headers, data=json.dumps(data))
    msg = res.json()['msg']
    if msg != '操作成功':
        print('登陆失败')
        exit(-1)
    result = res.json()['result']
    return json.loads(encrypt.decode(result))['data']


# 打卡
def clockIn(info):
    url = 'https://yxxt.cuit.edu.cn/api/blade-workbench/studentClock/saveClockInfo'
    data = {
        'temperature': '%.1f' % (36 + random.random()),
        'location': '四川省成都市双流区西航港街道成都信息工程大学行政办公楼成都信息工程大学(航空港校区)',
        'locationProvince': '四川省',
        'locationCity': '成都市',
        'locationCountry': '双流区',
        'user_info_id': info['account'],
        'user_info_name': info['nick_name']
    }

    data = {
        'data': encrypt.encode(data)
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Authorization': 'Basic c2FiZXI6c2FiZXJfc2VjcmV0',
        'Blade-Auth': 'bearer ' + info['access_token'],
        'Connection': 'keep-alive',
        'Content-Length': str(len(data)),
        'Content-Type': 'application/json;charset=UTF-8',
        'Host': 'yxxt.cuit.edu.cn',
        'Origin': 'https://yxxt.cuit.edu.cn',
        'Referer': 'https://yxxt.cuit.edu.cn/font/antiepidemicClockIn/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1 Edg/85.0.4183.102'
    }
    res = session.post(url=url, headers=headers, data=json.dumps(data))
    msg = res.json()['msg']
    if msg != '操作成功':
        print('打卡失败')
        exit(-1)
    result = res.json()['result']
    return encrypt.decode(result)


# 微信消息通知
def sendMessage(msg):
    url = 'https://sc.ftqq.com/' + key + '.send?text=' + msg;
    requests.get(url)


# 腾讯云启动函数
def main_handler(event, context):
    try:
        info = login()
        result = clockIn(info)
        if result == r'"保存成功"':
            if len(key) > 0:
                sendMessage('自动打卡成功')
        else:
            print('自动打卡失败')
            exit(-1)
    except Exception as e:
        raise e
    else:
        return 'success'


if __name__ == '__main__':
    print(main_handler({}, {}))
