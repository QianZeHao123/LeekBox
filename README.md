# 韭菜盒子
### 一、介绍
* 1.基于ESP32+MQTT+MicroPython+树莓派实现的证券信息展板。
* 2.数据来源：新浪财经公开爬虫接口。
* 3.服务器端(Linux|Raspbian)：每8s从网上获取交易信息并处理这些数据，同时作为MQTT服务器和Publisher。
* ESP32：MQTT的Subscriber，实时显示信息，并作出震动/发声反馈。
### 二、基本功能
* 实时获取交易信息：当前股价、昨日收盘价、今日开盘价、总市值、成交量、换手率等。
* 对获取信息进行处理：计算收益率、当日总涨幅/跌幅。
* 异常数据警报：若(当前股价-股票买入价)/股票买入价 < a(预设-5%，可更改)时，ESP32在显示当前股票信息时，驱动内部电机震动做出提醒。
* 背景色设定规则：(当前股价-今日开盘价)>=0时，为深红色，否则为深绿色。
### 三、部署（2个设备，ESP32的开发板，电脑/树莓派当服务器）
#### （一）服务端
* 1.基本软件下载(python3, mqtt软件, git等)
```
sudo apt update
sudo apt upgrade # 更新到最新系统
sudo apt install vim python3 python3-pip mosquitto mosquitto-clients
```
* 2.服务器安装Python脚本依赖
```
pip3 install paho-mqtt requests -i https://pypi.tuna.tsinghua.edu.cn/simple/
```
* 3.mosquitto配置
```
service mosquitto status # 查看mosquitto是否在运行
mosquitto_passwd -c /etc/mosquitto/passwd 用户名 # 创建用户档案，再输入两次密码
vim /etc/mosquitto/mosquitto.conf # 进入配置文档
    # 添加以下两条内容
    # 设定账号密码档案
    password_file /etc/mosquitto/passwd
    # 允许匿名登入
    allow_anonymous true
service mosquitto restart # 重启mosquitto
```
* 4.运行程序
```
python3 Server.py        # 切换到Server.py所在目录
```
#### （二）ESP32
* 1.micropython固件下载，去M5Stack官网下载 https://m5stack.com/（不用考虑屏幕驱动问题）
* 2.https://flow.m5stack.com/ 使用Web IDE可以导入LeekBox.m5f文件直接运行。
### 注意事项
* mosquitto_passwd -c /etc/mosquitto/passwd 用户名这条指令需要在root模式下执行。
* Server.py中StockName和StockCodeIndexS两个列表可以自由添加股票名称和代码，上下必须一一对应。
* ESP32中MQTT活跃时间设置为4096，不要设置得过大，否则会被拒绝连接。
### 更新迭代
* 没有用ESP32直接HTTP获取股票信息就是出于性能考虑，才加上MQTT服务器，后期要更加充分利用服务端的计算性能，专注于后端算法编写。
* 增加ESP图形支持，使ESP32可以绘制K线图。
