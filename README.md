# cuit-daka
智慧成信自动防疫打卡py脚本

# 使用

1. clone此仓库
    ```shell script
    git clone https://github.com/ZimoLoveShuang/cuit-daka.git
    ```
2. 配置`index.py`中的`account`，`passWord`，`key`
    - `key`是`server酱`的`key`，获取`key`参考[server酱官方说明](http://sc.ftqq.com/3.version)
    - `account` 是账号，默认是学号
    - `passWord` 是密码，默认是身份证后六位
    - 位置相关可根据自己的情况选择性配置
3. 登陆腾讯云，并打开云函数控制台，[直接戳这里，快人一步](https://console.cloud.tencent.com/scf/index?rid=1)
4. 新建云函数，运行环境选择`python3.6`，创建方式选择空白函数，然后下一步
5. 提交方法选择上传文件夹，选择你刚刚克隆下来的文件夹，然后点击下面的高级设置，设置超时时间为`60秒`
6. 点击保存并测试，如果没有意外，你应该可以收到一条微信通知
7. 配置触发器，进行定时打卡，下面的cron表达式代表每天早上八点执行，更多用法请参考官方文档
    ```shell script
    0 0 8 * * * *
    ```
8. enjoy it!!!

# 设计思路

1. 模拟登陆
2. 提交打卡信息
3. 推送微信通知

# 项目说明

1. `index.py` 完成模拟登陆流程和打卡流程，通过抓包完成
2. `encrypt.py` 处理智慧成信app与服务器交互过程中的加密解密过程，通过分析源代码完成
3. `headers_helper.py` 将原始请求头转换为字典
4. `location_helper.py` 帮助生成位置信息的脚本，通过使用百度和高德地图api完成
5. `requirements.txt` py依赖库以及版本说明文件，通过`pip freeze > requirements.txt`命令生成

