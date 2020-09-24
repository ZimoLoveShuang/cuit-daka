import math
import json
import random
import base64


# 判断是否是json字符串
def isJson(s):
    try:
        jsonObj = json.loads(s)
    except:
        return False
    else:
        return True


# 解密
def decode(s):
    t = int(s[0:10])
    n = list(s[10:])
    a = 0
    o = 0
    while o < math.floor(t / 100) + 1:
        n.pop(100 * o + 1 - a)
        a += 1
        o += 1
    return base64.b64decode(''.join(n)).decode()


# 加密
def encode(n):
    if not isJson(n):
        n = json.dumps(n)
    return o(n) + i(n)


def o(e):
    t = str(int(len(e)))
    n = 10 - len(t)
    while n > 0:
        t = '0' + t
        n -= 1
    return t


def i(e, charset='utf-8'):
    t = list(str(base64.b64encode(e.encode(charset)), charset))
    n = 0
    while n < math.floor(len(e) / 100 + 1):
        t.insert(100 * n + 1, str(math.floor(10 * random.random())))
        n += 1
    return ''.join(t)
