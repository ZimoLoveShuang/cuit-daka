# 请求头转字典
def dictheaders(header_raw):
    return dict(line.split(": ", 1) for line in header_raw.split("\n") if line != '')


s = '''
Accept: application/json, text/plain, */*
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
Authorization: Basic c2FiZXI6c2FiZXJfc2VjcmV0
Connection: keep-alive
Content-Length: 423
Content-Type: application/json;charset=UTF-8
Host: yxxt.cuit.edu.cn
Origin: https://yxxt.cuit.edu.cn
Referer: https://yxxt.cuit.edu.cn/font/antiepidemicClockIn/
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1 Edg/85.0.4183.102
'''
print(dictheaders(s))
